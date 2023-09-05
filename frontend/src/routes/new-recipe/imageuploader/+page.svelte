<script>
	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	import { slide } from 'svelte/transition';
	import { userIdentity } from '$store/stores';
	import { PUBLIC_BACKEND_USERS, PUBLIC_BACKEND_UPLOADS } from '$env/static/public';
	import Categories from '$lib/icons/Categories.svelte';
	import BooksmarksIcon from '$lib/icons/BooksmarksIcon.svelte';
	import PieChart from '$lib/icons/PieChart.svelte';
	import profileDefault from '$lib/images/profileDefault.jpg';
	import NavMenu from '$lib/components/NavMenu.svelte';
	export let data;

	let firstName: string;
	let lastName: string;
	let userID: string;
	let userName: string;
	let userEmail: string;
	let userDescription: string;
	let userImage: string;
	let fileInput: HTMLInputElement;
	let profilePic: Blob | undefined;

	async function getProfileImage(photo_id: string): Promise<void> {
		try {
			const response = await fetch(`${PUBLIC_BACKEND_UPLOADS}/files/${photo_id}`, {
				method: 'GET',
				headers: {
					'Content-Type': 'image/jpg'
				}
				// mode: 'no-cors'
			});
			if (!response.ok) {
				throw new Error('Failed to fetch user profile image');
			}
			const data = await response.blob();
			profilePic = data;
		} catch (error) {
			console.error('Failed to get profile image:', error);
		}
	}

	async function updateUserImageId(photo_ID: string): Promise<void> {
		try {
			const putResponse = await fetch(`${PUBLIC_BACKEND_USERS}/api/user/${userID}`, {
				method: 'PUT',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify({
					photo_id: photo_ID
				})
			});

			if (!putResponse.ok) {
				throw new Error('Failed to update user imageId');
			}

			console.log("we're done loading the image, so refresh your screen!");
		} catch (error) {
			console.error('Failed to update user imageId:', error);
		}
	}

	const handleFileUpload = async (): Promise<void> => {
		try {
			const file = fileInput.files?.[0];
			if (file) {
				const formData = new FormData();
				formData.append('photo', file);
				const response = await fetch(`${PUBLIC_BACKEND_UPLOADS}/upload-photo`, {
					method: 'POST',
					body: formData
				});

				if (response.ok) {
					const data = await response.json();
					const photoId = data.file_id;
					userIdentity.update((user) => {
						return { ...user, photo_id: photoId };
					});
					console.log(userIdentity);
					localStorage.setItem('userIdentity', JSON.stringify(userIdentity));
					await updateUserImageId(photoId);
					console.log('Image successfully updated!');
					window.location.assign('/profile');
				} else {
					console.error('Failed to upload photo');
				}
			}
		} catch (error) {
			console.error('Error occurred during file upload:', error);
		}
	};

	onMount(async () => {
		// console.log(data.user)
		fileInput = document.getElementById('profileImageInput') as HTMLInputElement;
		firstName = data.user.first_name;
		lastName = data.user.last_name;
		userID = data.user._id;
		userName = data.user.username;
		userEmail = data.user.email;
		userDescription = data.user.description;
		userImage = data.user.photo_id;
		getProfileImage(userImage);
	});
</script>

<script>
	//@ts-nocheck
	import { authHandlers, authStore } from '$lib/stores/authStore';
	import AuthReset from '$lib/components/AuthReset.svelte';
	import {
		PUBLIC_CLUSTER_PASSWORD,
		PUBLIC_CLUSTER_IMAGES,
		PUBLIC_CLUSTER_USERS
	} from '$env/static/public';
	import { Dropdown, DropdownItem, DropdownDivider, DropdownHeader } from 'flowbite-svelte';

	let email;
	let image;
	let userid;
	let authored_recipes;
	let showDelete = false;

	authStore.subscribe((curr) => {
		email = curr?.currentUser?.email;
		console.log(curr.currentUser);
		userid = curr?.currentUser?.uid;
	});

	async function getUser() {
		const response = await fetch(`${PUBLIC_CLUSTER_USERS}/api/user/${userid}`);
		const data = await response.json();
		authored_recipes = data.authored_recipes;
		return data;
	}
	async function getRecipe(recipeid) {
		const response = await fetch(`${PUBLIC_CLUSTER_PASSWORD}/api/recipe/${recipeid}`);
		const data = await response.json();
		return data;
	}

	async function deleteRecipe(recipeid) {
		const response = await fetch(`${PUBLIC_CLUSTER_PASSWORD}/api/recipe/${recipeid}`, {
			method: 'DELETE',
			headers: {
				'Content-Type': 'application/json'
			}
		});
	}
	async function deleteAuthoredRecipe(recipeid) {
		console.log(authored_recipes, 'before');
		authored_recipes = authored_recipes.filter((item) => item !== recipeid);
		console.log(authored_recipes, 'after');
		const response = await fetch(`${PUBLIC_CLUSTER_USERS}/api/user/${userid}`, {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				authored_recipes
			})
		});
		await getUser().then((window.location.href = '/privatedashboard'));
	}

	async function getRecipeImage(photo_id) {
		try {
			const response = await fetch(`${PUBLIC_CLUSTER_IMAGES}/files/${photo_id}`, {
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
			image = data;
			console.log('data', data);
			return image;
		} catch (error) {
			console.error('Failed to get profile image:', error);
		}
	}
</script>

<div
	class="mx-auto w-11/12 py-7 px-7 h-full bg-[url('$lib/icons/kitchen.jpg')] overflow-hidden bg-no-repeat bg-cover text-gray-300"
>
	This is my favorite recipes page
</div>

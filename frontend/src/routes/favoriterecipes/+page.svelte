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
	import Notification from '$lib/components/Notification.svelte';

	export let data;

	let email;
	let image;
	let userid;
	let favorited_recipes;
	let showDelete = false;
	let isNotificationVisible = false;
	let Recipes = [];

	authStore.subscribe((curr) => {
		email = curr?.currentUser?.email;
		console.log(curr.currentUser);
		userid = curr?.currentUser?.uid;
	});

	async function getUser() {
		const response = await fetch(`${PUBLIC_CLUSTER_USERS}/api/user/${userid}`);
		const data = await response.json();
		favorited_recipes = data.favorites;
		Recipes = await Promise.all(favorited_recipes.map((recipeId) => getFavoritedRecipes(recipeId)));
		return data;
	}
	async function getFavoritedRecipes(recipeid) {
		const response = await fetch(`${PUBLIC_CLUSTER_PASSWORD}/api/recipe/${recipeid}`);
		const data = await response.json();
		return data;
	}

	async function deleteFavoritedRecipe(recipeid) {
		let favorites = favorited_recipes.filter((item) => item !== recipeid);

		let user = await getUser();
		user.favorites = favorites;
		await fetch(`${PUBLIC_CLUSTER_USERS}/api/user/${userid}`, {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(user)
		}).then((window.location.href = '/favoriterecipes'));
		isNotificationVisible = true;

		// Automatically hide the notification after a few seconds
		setTimeout(() => {
			isNotificationVisible = false;
		}, 3000); // Adjust the duration (in milliseconds) as needed
	}

	async function alphabetsort() {
		console.log('before sorting', Recipes);
		let sortedRecipes = [...Recipes];
		sortedRecipes.sort((a, b) => {
			const titleA = a.title.toUpperCase();
			const titleB = b.title.toUpperCase();

			if (titleA < titleB) {
				return -1;
			} else if (titleA > titleB) {
				return 1;
			} else {
				return 0;
			}
		});
		Recipes = sortedRecipes;
		console.log('after sorting', Recipes);
	}

	function defaultSort() {
		Recipes = defaultRecipes;
		console.log(Recipes);
	}

	let defaultRecipes = [];

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

{#if isNotificationVisible}
	<Notification message="Favorite deleted!" />
{/if}

<div
	class="mx-auto w-11/12 py-7 px-7 h-full bg-[url('$lib/icons/kitchen.jpg')] overflow-hidden bg-no-repeat bg-cover text-gray-300"
>
	Favorites Page
	{#if $authStore.currentUser}
		<div class="flex flex-row justify-between w-full max-w-[675px] px-20">
			<h1 class="border-2 border-black bg-gray-900 bg-opacity-90 py-2 px-2 rounded-md">
				Current User: {email}
			</h1>
		</div>

		<div>
			<div class="flex flex-row justify-between px-1 py-2">
				<div class="text-sm font-bold font-serif">FAVORITE RECIPES</div>
				<div class="font-serif text-sm font-bold">SORT</div>
				<Dropdown class="bg-gray-800 rounded-md text-gray-300">
					<DropdownItem
						><button type="button" class="text-gray-300 text-xs" on:click={defaultSort}
							>DEFAULT</button
						></DropdownItem
					>
					<DropdownItem
						><button type="button" class="text-gray-300 text-xs" on:click={alphabetsort}
							>ALPHABETICAL</button
						></DropdownItem
					>
				</Dropdown>
			</div>
			{#await getUser()}
				Loading...
			{:then user}
				{#each user.favorites as recipe}
					{#await getFavoritedRecipes(recipe)}
						Loading...
					{:then recipedata}
						{@const imageId = recipedata.images[0].photo_id}
						<div
							class="rounded-md bg-gray-800 w-full max-w-[675px] mb-2 py-3 px-3 border-slate-900 border-2 shadow-inner bg-opacity-80"
						>
							<div class="flex flex-row w-full">
								<div class="flex flex-col justify-between w-full">
									<a
										class="mt-1 text-gray-300 flex justify-between w-full min-w-[500px]"
										href={`/${recipedata._id}`}
									>
										<div class="flex items-center justify-start w-1/2 capitalize text-xl ml-2">
											{recipedata.title}
										</div>
										{#await getRecipeImage(imageId)}
											loading ...
										{:then imageUrl}
											<img
												class="w-auto max-h-[200px] object-cover py-3 rounded-md"
												src={URL.createObjectURL(imageUrl)}
												alt=""
											/>
										{/await}
									</a>
									<div class="flex flex-row justify-between">
										<button
											type="button"
											on:click={() => {
												showDelete = true;
											}}
											class="text-red-900 text-sm font-bold border rounded-md border-black py-1 px-1 bg-gray-900 w-[65px]"
											>DELETE</button
										>
										{#if showDelete}
											<button
												type="button"
												class="text-gray-300 text-xs border-2 border-black"
												on:click={() => deleteFavoritedRecipe(recipedata._id)}>ARE YOU SURE?</button
											>
										{/if}
									</div>
								</div>
							</div>
						</div>
					{/await}
				{/each}
			{/await}

			<div class="flex justify-center w-full max-w-[675px] py-5">
				<button
					class="border-2 border-black bg-red-900 py-2 px-4 rounded-md bg-opacity-90"
					on:click={authHandlers.logout}>Logout</button
				>
			</div>
		</div>
	{:else}
		<div>Loading....</div>
	{/if}
</div>

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
	import { onMount } from 'svelte';

	// export let data;

	let email;
	let image;
	let userid;
	let favorited_recipes;
	let showDelete = false;
	let isNotificationVisible = false;
	let Recipes = [];
	let defaultRecipes = [];

	authStore.subscribe((curr) => {
		email = curr?.currentUser?.email;
		console.log(curr.currentUser);
		userid = curr?.currentUser?.uid;
	});

	async function getUser() {
		const response = await fetch(`${PUBLIC_CLUSTER_USERS}/api/user/${userid}`);
		const data = await response.json();
		favorited_recipes = data.favorites;
		defaultRecipes = await Promise.all(
			favorited_recipes.map((recipeId) => getFavoritedRecipes(recipeId))
		);
		Recipes = [...defaultRecipes]; // Initialize Recipes with a copy of defaultRecipes
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
		Recipes = [...defaultRecipes];
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
	onMount(async () => {
		getUser();
	});
</script>

<div class="min-h-screen bg-gradient-to-br from-neutral-50 to-neutral-100">
	{#if isNotificationVisible}
		<Notification message="Recipe removed from favorites!" />
	{/if}

	{#if $authStore.currentUser}
		<!-- Header Section -->
		<section class="section-padding bg-white border-b border-neutral-200">
			<div class="container-max">
				<div class="text-center mb-8">
					<h1 class="text-4xl md:text-5xl font-serif font-bold text-neutral-800 mb-6">
						My Favorite Recipes
					</h1>
					<p class="text-xl text-neutral-600">
						Your personal collection of beloved recipes
					</p>
				</div>

				<!-- User Info -->
				<div class="flex items-center justify-center mb-8">
					<div class="bg-primary-50 border border-primary-200 rounded-lg px-6 py-3">
						<span class="text-primary-800 font-medium">Signed in as: {email}</span>
					</div>
				</div>

				<!-- Sort Controls -->
				<div class="flex flex-col sm:flex-row items-center justify-between gap-4 mb-8">
					<div class="text-sm text-neutral-500">
						{Recipes.length} favorite recipes
					</div>
					<div class="flex items-center gap-4">
						<span class="text-sm font-medium text-neutral-700">Sort by:</span>
						<Dropdown class="bg-white border border-neutral-200 rounded-lg shadow-lg">
							<DropdownItem>
								<button class="text-neutral-700 text-sm px-4 py-2 hover:bg-neutral-50 w-full text-left" on:click={defaultSort}>
									Default
								</button>
							</DropdownItem>
							<DropdownItem>
								<button class="text-neutral-700 text-sm px-4 py-2 hover:bg-neutral-50 w-full text-left" on:click={alphabetsort}>
									Alphabetical
								</button>
							</DropdownItem>
						</Dropdown>
					</div>
				</div>
			</div>
		</section>

		<!-- Favorites Grid -->
		<section class="section-padding">
			<div class="container-max">
				{#if Recipes && Recipes.length > 0}
					<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
						{#each Recipes as recipe}
							{#await getFavoritedRecipes(recipe._id)}
								<div class="card p-6 flex items-center justify-center h-80">
									<div class="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
								</div>
							{:then recipedata}
								{@const imageId = recipedata.images[0].photo_id}
								<div class="card overflow-hidden group hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2">
									<!-- Recipe Image -->
									<div class="relative overflow-hidden h-48">
										{#await getRecipeImage(imageId)}
											<div class="w-full h-full bg-neutral-100 flex items-center justify-center">
												<div class="animate-spin rounded-full h-6 w-6 border-b-2 border-primary-600"></div>
											</div>
										{:then imageUrl}
											<img
												class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
												src={URL.createObjectURL(imageUrl)}
												alt={recipedata.title}
											/>
										{/await}
										<div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
									</div>

									<!-- Recipe Content -->
									<div class="p-6">
										<h3 class="text-xl font-serif font-semibold text-neutral-800 mb-3 line-clamp-2 group-hover:text-primary-600 transition-colors duration-200">
											{recipedata.title}
										</h3>
										
										<!-- Recipe Meta -->
										<div class="flex items-center justify-between mb-4 text-xs text-neutral-500">
											<div class="flex items-center gap-2">
												<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
													<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
												</svg>
												<span>{recipedata.cooking_time || 'N/A'}</span>
											</div>
											<div class="flex items-center gap-2">
												<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
													<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
												</svg>
												<span>{recipedata.serving_size || 'N/A'}</span>
											</div>
										</div>

										<!-- Action Buttons -->
										<div class="flex gap-3">
											<a href={`/${recipedata._id}`} class="flex-1">
												<button class="w-full btn-primary text-sm py-2.5">
													View Recipe
												</button>
											</a>
											<button
												type="button"
												class="p-2.5 text-red-600 hover:bg-red-50 rounded-lg transition-colors duration-200 border border-red-200"
												on:click={() => deleteFavoritedRecipe(recipedata._id)}
											>
												<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
													<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
												</svg>
											</button>
										</div>
									</div>
								</div>
							{/await}
						{/each}
					</div>
				{:else}
					<div class="text-center py-16">
						<div class="w-24 h-24 bg-neutral-100 rounded-full flex items-center justify-center mx-auto mb-6">
							<svg class="w-12 h-12 text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
							</svg>
						</div>
						<h3 class="text-2xl font-serif font-semibold text-neutral-800 mb-2">No favorites yet</h3>
						<p class="text-neutral-600 mb-6">Start exploring recipes and add them to your favorites!</p>
						<a href="/recipe-list" class="btn-primary">
							Browse Recipes
						</a>
					</div>
				{/if}

				<!-- Logout Button -->
				<div class="flex justify-center mt-12">
					<button
						class="btn-secondary flex items-center gap-2"
						on:click={authHandlers.logout}
					>
						<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
						</svg>
						Sign Out
					</button>
				</div>
			</div>
		</section>
	{:else}
		<div class="min-h-screen flex items-center justify-center">
			<div class="text-center">
				<div class="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600 mx-auto mb-4"></div>
				<p class="text-neutral-600">Loading...</p>
			</div>
		</div>
	{/if}
</div>

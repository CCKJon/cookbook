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
	import { list } from 'postcss';
	import { onMount } from 'svelte';
	import { Card, Button, Toggle } from 'flowbite-svelte';
	import { ArrowRightOutline } from 'flowbite-svelte-icons';

	let email;
	let image;
	let userid;
	let authored_recipes;
	let showDelete = false;
	let Recipes = [];
	let defaultRecipes = [];
	let hCard = false;

	authStore.subscribe((curr) => {
		email = curr?.currentUser?.email;
		console.log(curr.currentUser);
		userid = curr?.currentUser?.uid;
	});

	async function getUser() {
		const response = await fetch(`${PUBLIC_CLUSTER_USERS}/api/user/${userid}`);
		const data = await response.json();
		authored_recipes = data.authored_recipes;
		defaultRecipes = await Promise.all(authored_recipes.map((recipeId) => getRecipe(recipeId)));
		Recipes = [...defaultRecipes]; // Initialize Recipes with a copy of defaultRecipes
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

	function alphabetsort() {
		console.log('this is before', Recipes);
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
		console.log('this is after', Recipes);
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
			// console.log('data', data);
			return image;
		} catch (error) {
			console.error('Failed to get profile image:', error);
		}
	}
	onMount(async () => {
		getUser();
	});
</script>

<div
	class="mx-auto w-11/12 h-full px-7 bg-[url('$lib/icons/dashboard.jpg')] bg-no-repeat bg-cover text-gray-300 flex flex-col gap-10 items-center py-5"
>
	<div
		class="mx-auto font-serif font-bold text-3xl border-2 border-black bg-gray-900 rounded-md py-3 px-5 bg-opacity-80 w-full max-w-[550px] flex flex-row justify-center"
	>
		Welcome to your dashboard!
	</div>

	{#if $authStore.currentUser}
		<div class="flex flex-row justify-between w-full max-w-[675px] px-20">
			<h1 class="border-2 border-black bg-gray-900 bg-opacity-90 py-2 px-2 rounded-md">
				Current User: {email}
			</h1>
			<a
				class="border-2 border-black bg-pink-700 bg-opacity-80 font-serif py-2 px-2 rounded-md"
				href="/favoriterecipes"
			>
				<button type="button">Favorites</button>
			</a>
		</div>

		<div>
			<div class="flex flex-row justify-between px-1 py-2">
				<div class="text-sm font-bold font-serif">AUTHORED RECIPES</div>
				<div class="font-serif text-sm font-bold">SORT</div>
				<Dropdown class="bg-gray-800 rounded-md text-gray-300">
					<DropdownItem
						><button class="text-gray-300 text-xs" on:click={defaultSort}>DEFAULT</button
						></DropdownItem
					>
					<DropdownItem
						><button class="text-gray-300 text-xs" on:click={alphabetsort}>ALPHABETICAL</button
						></DropdownItem
					>
				</Dropdown>
			</div>
			<div class="w-full flex flex-wrap gap-10">
				{#if Recipes && Recipes.length > 0}
					{#each Recipes as recipe}
						{#await getRecipe(recipe._id)}
							Loading...
						{:then recipedata}
							{@const imageId = recipedata.images[0].photo_id}
							{#await getRecipeImage(imageId)}
								loading ...
							{:then imageUrl}
								<div class="dark">
									<Card img={URL.createObjectURL(imageUrl)} class="mb-4">
										<a href={`/${recipe._id}`}>
											<h5
												class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white"
											>
												{recipedata.title}
											</h5>
										</a>
										<p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
											{recipedata.description}
										</p>
										<div class="flex flex-row justify-between">
											<a href={`/${recipe._id}`}>
												<Button type="button">
													Update <ArrowRightOutline class="w-3.5 h-3.5 ml-2 text-white" />
												</Button>
											</a>
											<Button
												on:click={() => {
													showDelete = true;
												}}
											>
												Delete
											</Button>
										</div>
										{#if showDelete}
											<div class="flex flex-row justify-end py-2">
												<Button
													type="button"
													on:click={deleteAuthoredRecipe(recipedata._id)}
													on:click={deleteRecipe(recipedata._id)}>ARE YOU SURE?</Button
												>
											</div>
										{/if}
									</Card>
								</div>
							{/await}
						{/await}
					{/each}
				{:else}
					<div class="text-center py-16 w-full">
						<div class="w-24 h-24 bg-neutral-100 dark:bg-neutral-700 rounded-full flex items-center justify-center mx-auto mb-6">
							<svg class="w-12 h-12 text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
							</svg>
						</div>
						<h3 class="text-2xl font-serif font-semibold text-neutral-800 dark:text-neutral-100 mb-2">No recipes yet</h3>
						<p class="text-neutral-600 dark:text-neutral-300 mb-6">Start creating your first recipe!</p>
						<a href="/new-recipe" class="btn-primary">
							Create Your First Recipe
						</a>
					</div>
				{/if}
			</div>

			<div class="flex flex-row py-10">
				<AuthReset />
			</div>
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

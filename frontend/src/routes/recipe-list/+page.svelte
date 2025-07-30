<script>
	// @ts-nocheck

	import { onMount } from 'svelte';
	// @ts-ignore
	import { PUBLIC_CLUSTER_PASSWORD, PUBLIC_CLUSTER_IMAGES } from '$env/static/public';
	import { Spinner } from 'flowbite-svelte';
	import { Dropdown, DropdownItem, DropdownDivider, DropdownHeader } from 'flowbite-svelte';
	import { Card, Button, Toggle } from 'flowbite-svelte';
	import { ArrowRightOutline } from 'flowbite-svelte-icons';
	import { DarkMode } from 'flowbite-svelte';
	import { lazyLoad } from '$lib/services/lazyLoad.js';
	export let data;
	let image;
	let Recipes = data.items;
	let vCard = false;

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

	function alphabetsort() {
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
	}

	function defaultSort() {
		Recipes = defaultRecipes;
	}

	let defaultRecipes = [];

	onMount(() => {
		// searchableRecipes = Recipes;
		defaultRecipes = Recipes;
		console.log(Recipes);
		console.log(Recipes[0].images[0].photo_id);
	});
</script>

<div class="min-h-screen bg-gradient-to-br from-neutral-50 to-neutral-100 dark:from-neutral-900 dark:to-neutral-800">
	<!-- Header Section -->
	<section class="section-padding bg-white dark:bg-neutral-800 border-b border-neutral-200 dark:border-neutral-700">
		<div class="container-max">
			<div class="text-center mb-12">
				<h1 class="text-4xl md:text-5xl font-serif font-bold text-neutral-800 dark:text-neutral-100 mb-6">
					Recipe Collection
				</h1>
				<p class="text-xl text-neutral-600 dark:text-neutral-300 max-w-2xl mx-auto">
					Discover delicious recipes that have been carefully curated and tested for the perfect culinary experience
				</p>
			</div>

			<!-- Sort Controls -->
			<div class="flex flex-col sm:flex-row items-center justify-between gap-4 mb-8">
				<div class="text-sm text-neutral-500 dark:text-neutral-400">
					{Recipes.length} recipes available
				</div>
				<div class="flex items-center gap-4">
					<span class="text-sm font-medium text-neutral-700 dark:text-neutral-300">Sort by:</span>
					<Dropdown class="bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded-lg shadow-lg">
						<DropdownItem>
							<button class="text-neutral-700 dark:text-neutral-300 text-sm px-4 py-2 hover:bg-neutral-50 dark:hover:bg-neutral-700 w-full text-left" on:click={defaultSort}>
								Default
							</button>
						</DropdownItem>
						<DropdownItem>
							<button class="text-neutral-700 dark:text-neutral-300 text-sm px-4 py-2 hover:bg-neutral-50 dark:hover:bg-neutral-700 w-full text-left" on:click={alphabetsort}>
								Alphabetical
							</button>
						</DropdownItem>
					</Dropdown>
				</div>
			</div>
		</div>
	</section>

	<!-- Recipes Grid -->
	<section class="section-padding">
		<div class="container-max">
			<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
				{#each Recipes as recipe}
					{@const imageId = recipe.images[0].photo_id}
					{#await getRecipeImage(imageId)}
						<div class="card p-6 flex items-center justify-center h-80">
							<Spinner color="primary" size="8" />
						</div>
					{:then imageUrl}
						<div class="card overflow-hidden group hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-2">
							<!-- Recipe Image -->
							<div class="relative overflow-hidden h-48">
								<img 
									src={URL.createObjectURL(imageUrl)} 
									alt={recipe.title}
									class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
								/>
								<div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
							</div>

							<!-- Recipe Content -->
							<div class="p-6">
								<h3 class="text-xl font-serif font-semibold text-neutral-800 dark:text-neutral-100 mb-3 line-clamp-2 group-hover:text-primary-600 dark:group-hover:text-walnut-400 transition-colors duration-200">
									{recipe.title}
								</h3>
								<p class="text-neutral-600 dark:text-neutral-300 text-sm mb-4 line-clamp-3 leading-relaxed">
									{recipe.description}
								</p>
								
								<!-- Recipe Meta -->
								<div class="flex items-center justify-between mb-4 text-xs text-neutral-500 dark:text-neutral-400">
									<div class="flex items-center gap-2">
										<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
										</svg>
										<span>{recipe.cooking_time || 'N/A'}</span>
									</div>
									<div class="flex items-center gap-2">
										<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
										</svg>
										<span>{recipe.serving_size || 'N/A'}</span>
									</div>
								</div>

								<!-- View Recipe Button -->
								<a href={`/${recipe._id}`} class="block w-full">
									<button class="w-full btn-primary text-sm py-2.5">
										View Recipe
										<ArrowRightOutline class="w-4 h-4 ml-2 inline" />
									</button>
								</a>
							</div>
						</div>
					{/await}
				{/each}
			</div>

			<!-- Empty State -->
			{#if Recipes.length === 0}
				<div class="text-center py-16">
					<div class="w-24 h-24 bg-neutral-100 rounded-full flex items-center justify-center mx-auto mb-6">
						<svg class="w-12 h-12 text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
						</svg>
					</div>
					<h3 class="text-2xl font-serif font-semibold text-neutral-800 mb-2">No recipes found</h3>
					<p class="text-neutral-600 mb-6">Be the first to add a recipe to our collection!</p>
					<a href="/new-recipe" class="btn-primary">
						Add Your First Recipe
					</a>
				</div>
			{/if}
		</div>
	</section>
</div>

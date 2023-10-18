<script>
	// @ts-nocheck

	import { onMount } from 'svelte';
	// @ts-ignore
	import { PUBLIC_CLUSTER_PASSWORD, PUBLIC_CLUSTER_IMAGES } from '$env/static/public';
	import { Spinner } from 'flowbite-svelte';
	import { Dropdown, DropdownItem, DropdownDivider, DropdownHeader } from 'flowbite-svelte';
	import { Card, Button, Toggle } from 'flowbite-svelte';
	import { ArrowRightOutline } from 'flowbite-svelte-icons';

	// import { goto } from '$app/navigation';
	// import Fuse from 'fuse.js';
	// @ts-ignore
	export let data;
	let image;
	let Recipes = data.items;
	let vCard = false;
	// let showSearchbar = false;
	// let dueRecipes: any[] = [];
	// let searchPattern: any;
	// let fuse: string | Fuse<unknown>;
	// let searchresults: any[] = [];
	// let searchableRecipes: never[] = [];
	// const searchOptions = {
	// 	includeScore: true,
	// 	threshold: 0.5,
	// 	keys: ['title', 'description']
	// };

	// function search(Recipes: any[] | readonly unknown[]) {
	// 	fuse = new Fuse(Recipes, searchOptions);
	// }

	// $: searchPattern && searchRecipes();

	// const searchRecipes = () => {
	// 	search(searchableRecipes);
	// 	if (fuse) {
	// 		if (searchPattern) {
	// 			const searchResult = fuse.search(searchPattern);
	// 			const filteredRecipes = searchResult.map((obj: { item: any }) => obj.item);
	// 			searchresults = filteredRecipes;
	// 		} else {
	// 			searchresults = [];
	// 		}
	// 	}
	// };

	// function alphabetsort() {
	// 	let sortedRecipes = [...Recipes];
	// 	sortedRecipes.sort((a, b) => {
	// 		const titleA = a.title.toUpperCase();
	// 		const titleB = b.title.toUpperCase();

	// 		if (titleA < titleB) {
	// 			return -1;
	// 		} else if (titleA > titleB) {
	// 			return 1;
	// 		} else {
	// 			return 0;
	// 		}
	// 	});
	// 	Recipes = sortedRecipes;
	// }
	// function defaultSort() {
	// 	Recipes = defaultRecipes;
	// }

	// let defaultRecipes = [];
	// @ts-ignore
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

<div
	class="mx-auto w-11/12 py-7 px-7 h-full bg-[url('$lib/icons/recipe.jpg')] bg-no-repeat bg-cover overflow-auto"
>
	<div
		class="mx-auto grid grid-cols-1 content-start gap-1 place-items-center overflow-y-auto h-full overflow-hidden mb-5 text-gray-300 font-serif"
	>
		<div class="text-3xl mb-5">List of Recipes</div>
		<div class="flex flex-row justify-between w-1/2">
			<div class="text-gray-200 text-xs mb-2 mt-12">LIST OF RECIPES</div>
			<button class="text-gray-200 text-xs mb-2 mt-12">SORT</button>
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
		{#each Recipes as recipe}
			{@const imageId = recipe.images[0].photo_id}
			<div
				class="rounded-md bg-gray-800 w-1/2 mb-2 py-3 px-3 border-slate-900 border-2 shadow-inner bg-opacity-60"
			>
				<div class="flex flex-row gap-3">
					<a class="mt-1 text-gray-300 flex justify-between w-full" href={`/${recipe._id}`}>
						<div class="flex items-center justify-start w-1/2 capitalize text-xl ml-2">
							{recipe.title}
						</div>
						{#await getRecipeImage(imageId)}
							<Spinner color="red" />
						{:then imageUrl}
							<img
								class="w-auto max-h-[200px] object-cover"
								src={URL.createObjectURL(imageUrl)}
								alt=""
							/>
						{/await}
					</a>
				</div>
			</div>
		{/each}
		<div>
			<Card img="/images/image-1.webp" reverse={vCard} class="mb-4">
				<h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
					Noteworthy technology acquisitions 2021
				</h5>
				<p class="mb-3 font-normal text-gray-700 dark:text-gray-400 leading-tight">
					Here are the biggest enterprise technology acquisitions of 2021 so far, in reverse
					chronological order.
				</p>
				<Button>
					Read more <ArrowRightOutline class="w-3.5 h-3.5 ml-2 text-white" />
				</Button>
			</Card>
		</div>
	</div>
</div>

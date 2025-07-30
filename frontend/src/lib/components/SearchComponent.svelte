<script>
	// @ts-nocheck
	import { onMount } from 'svelte';
	import { PUBLIC_CLUSTER_PASSWORD } from '$env/static/public';
	import { Dropdown, DropdownItem } from 'flowbite-svelte';
	import Fuse from 'fuse.js';

	let fuse;
	let searchResults;
	let searchableResults;
	let showSearchbar = false;
	let searchPattern;
	const searchOptions = {
		includeScore: true,
		threshold: 0.1,
		keys: ['title', 'description']
	};

	async function getRecipes() {
		const response = await fetch(`${PUBLIC_CLUSTER_PASSWORD}/api/recipe`);
		const data = await response.json();
		return data;
	}

	function search(searchableResults) {
		fuse = new Fuse(searchableResults, searchOptions);
	}

	function gotoSlug(_id) {
		window.location.href = `/${_id}`;
	}

	$: searchPattern && searchRecipes();

	const searchRecipes = () => {
		search(searchableResults);
		if (fuse) {
			if (searchPattern) {
				const searchResult = fuse.search(searchPattern);
				const filteredsearchableResults = searchResult.map((obj) => obj.item);
				searchResults = filteredsearchableResults;
			} else {
				searchResults = [];
			}
		}
	};

	const closeDialog = () => {
		searchResults = null;
	};

	onMount(async () => {
		searchableResults = await getRecipes();
		console.log('These are my search results', searchableResults);
		document.addEventListener('click', (event) => {
			if (!event.target.closest('.dialog-content')) {
				closeDialog();
			}
		});
	});
</script>

<div class="relative w-full max-w-md">
	<!-- Search Input -->
	<div class="relative">
		<div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
			<svg class="h-5 w-5 text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
				<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
			</svg>
		</div>
		<input
			class="input-field pl-10 pr-4 py-3 w-full bg-white dark:bg-neutral-800 border border-neutral-300 dark:border-neutral-600 rounded-lg focus:ring-2 focus:ring-primary-500 dark:focus:ring-walnut-500 focus:border-transparent transition-all duration-200 text-neutral-900 dark:text-neutral-100"
			type="text"
			bind:value={searchPattern}
			on:input={searchRecipes}
			placeholder="Search recipes..."
		/>
	</div>

	<!-- Search Results -->
	{#if searchResults && searchResults.length > 0}
		<div class="absolute z-50 w-full mt-2 bg-white dark:bg-neutral-800 rounded-lg shadow-xl border border-neutral-200 dark:border-neutral-700 max-h-96 overflow-y-auto">
			<div class="py-2">
				{#each searchResults as result}
					<a 
						href={`/${result._id}`}
						class="block px-4 py-3 hover:bg-neutral-50 dark:hover:bg-neutral-700 transition-colors duration-200 border-b border-neutral-100 dark:border-neutral-700 last:border-b-0"
					>
						<div class="font-medium text-neutral-800 dark:text-neutral-100 mb-1">{result.title}</div>
						<div class="text-sm text-neutral-600 dark:text-neutral-300 line-clamp-2">{result.description}</div>
					</a>
				{/each}
			</div>
		</div>
	{:else if searchPattern && searchResults && searchResults.length === 0}
		<div class="absolute z-50 w-full mt-2 bg-white dark:bg-neutral-800 rounded-lg shadow-xl border border-neutral-200 dark:border-neutral-700">
			<div class="px-4 py-6 text-center">
				<svg class="w-8 h-8 text-neutral-400 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 12h6m-6-4h6m2 5.291A7.962 7.962 0 0112 15c-2.34 0-4.47-.881-6.08-2.33"></path>
				</svg>
				<div class="text-neutral-600 dark:text-neutral-300">No recipes found</div>
				<div class="text-sm text-neutral-500 dark:text-neutral-400">Try a different search term</div>
			</div>
		</div>
	{/if}
</div>

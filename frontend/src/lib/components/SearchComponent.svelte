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

<input
	class="text-black py-0"
	type="text"
	bind:value={searchPattern}
	on:input={searchRecipes}
	name=""
/>
<div class="relative">
	{#if searchResults}
		<dialog
			class="absolute left-0 rounded-md text-gray-200 w-52 min-h-20 max-h-56 overflow-hidden bg-gray-900 border-2 border-red-900 overflow-y-auto px-2 py-2 mt-2"
			open
		>
			{#each searchResults as result}
				<div class="border rounded-md py-1 px-1 border-gray-500 mt-1 mb-1 hover:bg-red-800/60">
					<button type="button" on:click={() => gotoSlug(result._id)}>{result.title}</button>
				</div>
			{/each}
		</dialog>
	{/if}
</div>

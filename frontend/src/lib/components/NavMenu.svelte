<script>
	import logo from '$lib/icons/logo.png';
	import SearchComponent from './SearchComponent.svelte';
	import { isLoggedIn } from '$lib/stores/authStore';
	let displaySearch = false;

	function displaySearchComponent() {
		displaySearch = !displaySearch;
	}

	// $: {
	// 	if ($isLoggedIn) {
	// 		console.log(true);
	// 	} else {
	// 		console.log(false);
	// 	}
	// }
</script>

<div class="px-5 py-2 flex flex-row items-center justify-between bg-[#0F0F0F] w-11/12 mx-auto">
	<a href="/"><img class="h-16 w-auto" src={logo} alt="logo" /></a>
	<div class="flex gap-5">
		{#if $isLoggedIn}
			<a class="text-gray-300 font-serif" href="/privatedashboard">Account</a>
		{:else}
			<a class="text-gray-300 font-serif" href="/login">Login</a>
		{/if}
		<a class="text-gray-300 font-serif" href="/recipe-list">Recipes</a>
		<a class="text-gray-300 font-serif" href="/new-recipe">Submit</a>
		<button on:click={() => displaySearchComponent()} type="button" class="text-gray-300 font-serif"
			>Search</button
		>
		{#if displaySearch}
			<div class="text-white">
				<SearchComponent />
			</div>
		{/if}
	</div>
</div>

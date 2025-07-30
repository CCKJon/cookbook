<script>
	import logo from '$lib/icons/logo.png';
	import SearchComponent from './SearchComponent.svelte';
	import { isLoggedIn } from '$lib/stores/authStore';
	import LoginModal from './LoginModal.svelte';
	import { Button, Modal, Label, Input, Checkbox } from 'flowbite-svelte';
	let formModal = false;
	import { auth } from '$lib/firebase/firebase.client';
	import Auth from './Auth.svelte';
	import { authHandlers, authStore } from '$lib/stores/authStore';

	import Modals from './Modals.svelte';
	let displaySearch = false;
	let modal = false;

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

<nav class="bg-white/95 backdrop-blur-md border-b border-neutral-200 sticky top-0 z-50 shadow-sm">
	<div class="container-max px-4 sm:px-6 lg:px-8">
		<div class="flex items-center justify-between h-16">
			<!-- Logo -->
			<a href="/" class="flex items-center space-x-3 group">
				<img class="h-10 w-auto transition-transform duration-200 group-hover:scale-105" src={logo} alt="Jonny's Cookbook" />
				<span class="text-xl font-serif font-semibold text-neutral-800 group-hover:text-primary-600 transition-colors duration-200">
					Jonny's Cookbook
				</span>
			</a>

			<!-- Navigation Links -->
			<div class="hidden md:flex items-center space-x-8">
				<a 
					href="/recipe-list" 
					class="text-neutral-600 hover:text-primary-600 font-medium transition-colors duration-200 relative group"
				>
					Recipes
					<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-primary-600 transition-all duration-200 group-hover:w-full"></span>
				</a>
				<a 
					href="/new-recipe" 
					class="text-neutral-600 hover:text-primary-600 font-medium transition-colors duration-200 relative group"
				>
					Submit Recipe
					<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-primary-600 transition-all duration-200 group-hover:w-full"></span>
				</a>
				<button 
					on:click={() => displaySearchComponent()} 
					type="button" 
					class="text-neutral-600 hover:text-primary-600 font-medium transition-colors duration-200 relative group"
				>
					Search
					<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-primary-600 transition-all duration-200 group-hover:w-full"></span>
				</button>
			</div>

			<!-- Auth Section -->
			<div class="flex items-center space-x-4">
				{#if $isLoggedIn}
					<a 
						href="/privatedashboard" 
						class="text-neutral-600 hover:text-primary-600 font-medium transition-colors duration-200"
					>
						Account
					</a>
					<a 
						href="/favoriterecipes" 
						class="text-neutral-600 hover:text-primary-600 font-medium transition-colors duration-200"
					>
						Favorites
					</a>
				{:else}
					<button 
						class="btn-primary" 
						type="button" 
						on:click={() => (formModal = true)}
					>
						Sign In
					</button>

					<Modal bind:open={formModal} size="xs" autoclose={false} class="w-full">
						<Auth bind:formModal />
					</Modal>
				{/if}
			</div>
		</div>

		<!-- Search Component -->
		{#if displaySearch}
			<div class="py-4 border-t border-neutral-200 animate-slide-up">
				<SearchComponent />
			</div>
		{/if}
	</div>
</nav>

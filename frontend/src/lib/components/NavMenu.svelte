<script>
	import logo from '$lib/icons/logo.png';
	import SearchComponent from './SearchComponent.svelte';
	import { Button, Modal, Label, Input, Checkbox } from 'flowbite-svelte';
	let formModal = false;
	import Auth from './Auth.svelte';
	let displaySearch = false;
	let modal = false;
	let mobileMenuOpen = false;

	function displaySearchComponent() {
		displaySearch = !displaySearch;
	}

	function toggleMobileMenu() {
		mobileMenuOpen = !mobileMenuOpen;
	}

	// $: {
	// 	if ($isLoggedIn) {
	// 		console.log(true);
	// 	} else {
	// 		console.log(false);
	// 	}
	// }
</script>

<nav class="bg-white/95 dark:bg-neutral-800/95 backdrop-blur-md border-b border-neutral-200 dark:border-neutral-700 sticky top-0 z-50 shadow-sm">
	<div class="container-max px-4 sm:px-6 lg:px-8">
		<div class="flex items-center justify-between h-16">
			<!-- Logo -->
			<a href="/" class="flex items-center space-x-3 group">
				<img class="h-10 w-auto transition-transform duration-200 group-hover:scale-105" src={logo} alt="Jonny's Cookbook" />
				<span class="text-xl font-serif font-semibold text-neutral-800 dark:text-neutral-100 group-hover:text-primary-600 dark:group-hover:text-walnut-400 transition-colors duration-200">
					Jonny's Cookbook
				</span>
			</a>

			<!-- Navigation Links - Hidden on mobile since we have bottom nav -->
			<div class="hidden md:flex items-center space-x-8">
				<a 
					href="/recipes" 
					class="text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-walnut-400 font-medium transition-colors duration-200 relative group"
				>
					Recipes
					<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-primary-600 dark:bg-walnut-500 transition-all duration-200 group-hover:w-full"></span>
				</a>
				<a 
					href="/new-recipe" 
					class="text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-walnut-400 font-medium transition-colors duration-200 relative group"
				>
					Submit Recipe
					<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-primary-600 dark:bg-walnut-500 transition-all duration-200 group-hover:w-full"></span>
				</a>
				<a 
					href="/ask-ai-chef" 
					class="text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-walnut-400 font-medium transition-colors duration-200 relative group"
				>
					AI Chef
					<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-primary-600 dark:bg-walnut-500 transition-all duration-200 group-hover:w-full"></span>
				</a>
				<button 
					on:click={() => displaySearchComponent()} 
					type="button" 
					class="text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-walnut-400 font-medium transition-colors duration-200 relative group"
				>
					Search
					<span class="absolute -bottom-1 left-0 w-0 h-0.5 bg-primary-600 dark:bg-walnut-500 transition-all duration-200 group-hover:w-full"></span>
				</button>
			</div>

			<!-- Auth Section -->
			<div class="flex items-center space-x-4">
				<!-- Mobile Menu Button -->
				<button 
					class="md:hidden p-2 rounded-lg text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-walnut-400 hover:bg-neutral-50 dark:hover:bg-neutral-700/50 transition-colors duration-200"
					on:click={toggleMobileMenu}
					type="button"
				>
					{#if mobileMenuOpen}
						<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
						</svg>
					{:else}
						<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
						</svg>
					{/if}
				</button>
				<button 
					class="btn-primary" 
					type="button" 
					on:click={() => (formModal = true)}
				>
					Sign In (Demo)
				</button>
			</div>
		</div>

		<!-- Mobile Navigation Menu -->
		{#if mobileMenuOpen}
		<div class="md:hidden py-4 border-t border-neutral-200 dark:border-neutral-700 animate-slide-down">
			<div class="flex flex-col space-y-3">
				<a 
					href="/recipes" 
					class="text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-walnut-400 font-medium transition-colors duration-200 px-3 py-2 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-700/50"
				>
					📖 Recipes
				</a>
				<a 
					href="/new-recipe" 
					class="text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-walnut-400 font-medium transition-colors duration-200 px-3 py-2 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-700/50"
				>
					➕ Submit Recipe
				</a>
				<a 
					href="/favoriterecipes" 
					class="text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-walnut-400 font-medium transition-colors duration-200 px-3 py-2 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-700/50"
				>
					❤️ Favorites
				</a>
				<a 
					href="/privatedashboard" 
					class="text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-walnut-400 font-medium transition-colors duration-200 px-3 py-2 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-700/50"
				>
					📊 Dashboard
				</a>
				<button 
					on:click={() => displaySearchComponent()} 
					type="button" 
					class="text-left text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-walnut-400 font-medium transition-colors duration-200 px-3 py-2 rounded-lg hover:bg-neutral-50 dark:hover:bg-neutral-700/50"
				>
					🔍 Search
				</button>
			</div>
		</div>
		{/if}

		<!-- Search Component -->
		{#if displaySearch}
			<div class="py-4 border-t border-neutral-200 dark:border-neutral-700 animate-slide-up">
				<SearchComponent />
			</div>
		{/if}
	</div>
</nav>

<!-- Modal outside of navigation to ensure proper z-index -->
<Modal bind:open={formModal} size="md" autoclose={false} class="w-full max-w-md mx-auto" style="z-index: 99999;">
	<Auth bind:formModal />
</Modal>

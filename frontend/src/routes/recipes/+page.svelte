<script>
	// @ts-nocheck
	import { onMount } from 'svelte';
	import { Spinner } from 'flowbite-svelte';
	import { Dropdown, DropdownItem } from 'flowbite-svelte';
	
	import { ArrowRightOutline } from 'flowbite-svelte-icons';
	import SearchComponent from '$lib/components/SearchComponent.svelte';
	
	// Sample recipe data - in a real app, this would come from your backend
	let recipes = [
		{
			id: 1,
			title: "Classic Margherita Pizza",
			description: "A traditional Italian pizza with fresh mozzarella, basil, and tomato sauce",
			cookingTime: "25 min",
			servingSize: "4 people",
			difficulty: "Easy",
			category: "Italian",
			image: "https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?w=400&h=300&fit=crop"
		},
		{
			id: 2,
			title: "Chocolate Chip Cookies",
			description: "Soft and chewy cookies with chocolate chips, perfect for any occasion",
			cookingTime: "15 min",
			servingSize: "24 cookies",
			difficulty: "Easy",
			category: "Dessert",
			image: "https://images.unsplash.com/photo-1499636136210-6f4ee915583e?w=400&h=300&fit=crop"
		},
		{
			id: 3,
			title: "Grilled Salmon",
			description: "Fresh salmon fillet grilled to perfection with herbs and lemon",
			cookingTime: "20 min",
			servingSize: "2 people",
			difficulty: "Medium",
			category: "Seafood",
			image: "https://images.unsplash.com/photo-1467003909585-2f8a72700288?w=400&h=300&fit=crop"
		},
		{
			id: 4,
			title: "Beef Tacos",
			description: "Spicy ground beef tacos with fresh vegetables and homemade salsa",
			cookingTime: "30 min",
			servingSize: "6 people",
			difficulty: "Easy",
			category: "Mexican",
			image: "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=400&h=300&fit=crop"
		},
		{
			id: 5,
			title: "Caesar Salad",
			description: "Crisp romaine lettuce with Caesar dressing, croutons, and parmesan cheese",
			cookingTime: "10 min",
			servingSize: "4 people",
			difficulty: "Easy",
			category: "Salad",
			image: "https://images.unsplash.com/photo-1546793665-c74683f339c1?w=400&h=300&fit=crop"
		},
		{
			id: 6,
			title: "Chicken Curry",
			description: "Aromatic Indian curry with tender chicken and fragrant spices",
			cookingTime: "45 min",
			servingSize: "4 people",
			difficulty: "Medium",
			category: "Indian",
			image: "https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?w=400&h=300&fit=crop"
		}
	];

	let filteredRecipes = [...recipes];
	let searchTerm = '';
	let selectedCategory = 'All';
	let selectedDifficulty = 'All';
	let sortBy = 'name';
	let loading = false;

	const categories = ['All', 'Italian', 'Dessert', 'Seafood', 'Mexican', 'Salad', 'Indian'];
	const difficulties = ['All', 'Easy', 'Medium', 'Hard'];

	function filterRecipes() {
		filteredRecipes = recipes.filter(recipe => {
			const matchesSearch = recipe.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
								 recipe.description.toLowerCase().includes(searchTerm.toLowerCase());
			const matchesCategory = selectedCategory === 'All' || recipe.category === selectedCategory;
			const matchesDifficulty = selectedDifficulty === 'All' || recipe.difficulty === selectedDifficulty;
			
			return matchesSearch && matchesCategory && matchesDifficulty;
		});

		// Sort recipes
		filteredRecipes.sort((a, b) => {
			switch (sortBy) {
				case 'name':
					return a.title.localeCompare(b.title);
				case 'time':
					return parseInt(a.cookingTime) - parseInt(b.cookingTime);
				case 'difficulty':
					const difficultyOrder = { 'Easy': 1, 'Medium': 2, 'Hard': 3 };
					return (difficultyOrder[a.difficulty] || 0) - (difficultyOrder[b.difficulty] || 0);
				default:
					return 0;
			}
		});
	}

	function handleSearch(event) {
		searchTerm = event.detail;
		filterRecipes();
	}

	function handleCategoryChange(event) {
		selectedCategory = event.target.value;
		filterRecipes();
	}

	function handleDifficultyChange(event) {
		selectedDifficulty = event.target.value;
		filterRecipes();
	}

	function handleSortChange(event) {
		sortBy = event.target.value;
		filterRecipes();
	}

	onMount(() => {
		filterRecipes();
	});
</script>

<div class="min-h-screen bg-gradient-to-br from-neutral-50 to-neutral-100 dark:from-neutral-900 dark:to-neutral-800">
	<!-- Header Section -->
	<section class="section-padding bg-white dark:bg-neutral-800 border-b border-neutral-200 dark:border-neutral-700">
		<div class="container-max">
			<div class="text-center mb-12">
				<h1 class="text-4xl md:text-5xl font-serif font-bold text-neutral-800 dark:text-neutral-100 mb-6">
					Our Recipe Collection
				</h1>
				<p class="text-xl text-neutral-600 dark:text-neutral-300 max-w-2xl mx-auto">
					Discover delicious recipes from around the world, carefully curated for every skill level and taste preference
				</p>
			</div>

			<!-- Search and Filters -->
			<div class="space-y-6">
				<!-- Search Bar -->
				<div class="max-w-2xl mx-auto">
					<SearchComponent on:search={handleSearch} placeholder="Search recipes by name or ingredients..." />
				</div>

				<!-- Filter Controls -->
				<div class="flex flex-col sm:flex-row items-center justify-between gap-4">
					<div class="text-sm text-neutral-500 dark:text-neutral-400">
						{filteredRecipes.length} of {recipes.length} recipes
					</div>
					
					<div class="flex flex-wrap items-center gap-4">
						<!-- Category Filter -->
						<select 
							bind:value={selectedCategory}
							on:change={handleCategoryChange}
							class="px-4 py-2 border border-neutral-200 dark:border-neutral-700 rounded-lg bg-white dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 text-sm focus:ring-2 focus:ring-primary-500 focus:border-transparent"
						>
							{#each categories as category}
								<option value={category}>{category}</option>
							{/each}
						</select>

						<!-- Difficulty Filter -->
						<select 
							bind:value={selectedDifficulty}
							on:change={handleDifficultyChange}
							class="px-4 py-2 border border-neutral-200 dark:border-neutral-700 rounded-lg bg-white dark:bg-neutral-800 text-neutral-700 dark:text-neutral-300 text-sm focus:ring-2 focus:ring-primary-500 focus:border-transparent"
						>
							{#each difficulties as difficulty}
								<option value={difficulty}>{difficulty}</option>
							{/each}
						</select>

						<!-- Sort Dropdown -->
						<Dropdown class="bg-white dark:bg-neutral-800 border border-neutral-200 dark:border-neutral-700 rounded-lg shadow-lg">
							<DropdownItem>
								<button class="text-neutral-700 dark:text-neutral-300 text-sm px-4 py-2 hover:bg-neutral-50 dark:hover:bg-neutral-700 w-full text-left" on:click={() => { sortBy = 'name'; filterRecipes(); }}>
									Sort by Name
								</button>
							</DropdownItem>
							<DropdownItem>
								<button class="text-neutral-700 dark:text-neutral-300 text-sm px-4 py-2 hover:bg-neutral-50 dark:hover:bg-neutral-700 w-full text-left" on:click={() => { sortBy = 'time'; filterRecipes(); }}>
									Sort by Cooking Time
								</button>
							</DropdownItem>
							<DropdownItem>
								<button class="text-neutral-700 dark:text-neutral-300 text-sm px-4 py-2 hover:bg-neutral-50 dark:hover:bg-neutral-700 w-full text-left" on:click={() => { sortBy = 'difficulty'; filterRecipes(); }}>
									Sort by Difficulty
								</button>
							</DropdownItem>
						</Dropdown>
					</div>
				</div>
			</div>
		</div>
	</section>

	<!-- Recipes Grid -->
	<section class="section-padding">
		<div class="container-max">
			{#if loading}
				<div class="flex justify-center items-center py-16">
					<Spinner color="primary" size="8" />
				</div>
			{:else if filteredRecipes.length > 0}
				<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
					{#each filteredRecipes as recipe}
						<div class="bg-white dark:bg-[#1a0f0a] rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 border border-neutral-100 dark:border-[#0d0805] overflow-hidden group hover:shadow-2xl transform hover:-translate-y-2">
							<!-- Recipe Image -->
							<div class="relative overflow-hidden h-48">
								<img 
									src={recipe.image} 
									alt={recipe.title}
									class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
								/>
								<div class="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
								
								<!-- Category Badge -->
								<div class="absolute top-4 left-4">
									<span class="px-3 py-1 bg-primary-600 text-white text-xs font-semibold rounded-full">
										{recipe.category}
									</span>
								</div>
								
								<!-- Difficulty Badge -->
								<div class="absolute top-4 right-4">
									<span class="px-3 py-1 bg-white/90 text-neutral-800 text-xs font-semibold rounded-full">
										{recipe.difficulty}
									</span>
								</div>
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
										<span>{recipe.cookingTime}</span>
									</div>
									<div class="flex items-center gap-2">
										<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
											<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
										</svg>
										<span>{recipe.servingSize}</span>
									</div>
								</div>

								<!-- View Recipe Button -->
								<a href={`/recipes/${recipe.id}`} class="block w-full">
									<button class="w-full btn-primary text-sm py-2.5">
										View Recipe
										<ArrowRightOutline class="w-4 h-4 ml-2 inline" />
									</button>
								</a>
							</div>
						</div>
					{/each}
				</div>
			{:else}
				<!-- Empty State -->
				<div class="text-center py-16">
					<div class="w-24 h-24 bg-neutral-100 dark:bg-neutral-700 rounded-full flex items-center justify-center mx-auto mb-6">
						<svg class="w-12 h-12 text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
						</svg>
					</div>
					<h3 class="text-2xl font-serif font-semibold text-neutral-800 dark:text-neutral-100 mb-2">No recipes found</h3>
					<p class="text-neutral-600 dark:text-neutral-300 mb-6">Try adjusting your search criteria or browse all recipes</p>
					<button 
						class="btn-primary"
						on:click={() => {
							searchTerm = '';
							selectedCategory = 'All';
							selectedDifficulty = 'All';
							filterRecipes();
						}}
					>
						Clear Filters
					</button>
				</div>
			{/if}
		</div>
	</section>
</div>

<style>
	.section-padding {
		padding: 4rem 0;
	}
	
	.container-max {
		max-width: 1200px;
		margin: 0 auto;
		padding: 0 1rem;
	}
	
	.card {
		background: white;
		border-radius: 1rem;
		box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
		transition: all 0.3s ease;
	}
	
	.dark .card {
		background: #374151;
		box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
	}
	
	.btn-primary {
		background: #dc2626;
		color: white;
		font-weight: 600;
		border-radius: 0.5rem;
		transition: all 0.3s ease;
	}
	
	.btn-primary:hover {
		background: #b91c1c;
		transform: translateY(-1px);
	}
	
	.dark .btn-primary {
		background: #92400e;
	}
	
	.dark .btn-primary:hover {
		background: #78350f;
	}
	
	.line-clamp-2 {
		display: -webkit-box;
		-webkit-line-clamp: 2;
		-webkit-box-orient: vertical;
		overflow: hidden;
	}
	
	.line-clamp-3 {
		display: -webkit-box;
		-webkit-line-clamp: 3;
		-webkit-box-orient: vertical;
		overflow: hidden;
	}
</style> 
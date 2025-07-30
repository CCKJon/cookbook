<script>
	import NewRecipe from '$lib/components/NewRecipe.svelte';
</script>

<div class="min-h-screen bg-gradient-to-br from-neutral-50 to-neutral-100 dark:from-neutral-900 dark:to-neutral-800">
	<!-- Header Section -->
	<section class="section-padding bg-white dark:bg-neutral-800 border-b border-neutral-200 dark:border-neutral-700">
		<div class="container-max">
			<div class="text-center">
				<h1 class="text-4xl md:text-5xl font-serif font-bold text-neutral-800 dark:text-neutral-100 mb-6">
					Share Your Recipe
				</h1>
				<p class="text-xl text-neutral-600 dark:text-neutral-300 max-w-2xl mx-auto">
					Contribute to our community by sharing your favorite recipes with fellow food enthusiasts
				</p>
			</div>
		</div>
	</section>

	<!-- Recipe Form -->
	<section class="section-padding">
		<div class="container-max">
			<NewRecipe />
		</div>
	</section>
</div>

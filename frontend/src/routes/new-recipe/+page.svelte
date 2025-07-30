<script>
	import NewRecipe from '$lib/components/NewRecipe.svelte';
</script>

<div class="min-h-screen bg-gradient-to-br from-neutral-50 to-neutral-100">
	<!-- Header Section -->
	<section class="section-padding bg-white border-b border-neutral-200">
		<div class="container-max">
			<div class="text-center">
				<h1 class="text-4xl md:text-5xl font-serif font-bold text-neutral-800 mb-6">
					Share Your Recipe
				</h1>
				<p class="text-xl text-neutral-600 max-w-2xl mx-auto">
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

<script>
	import kitchen from '$lib/icons/kitchen.jpg';
</script>

<!-- Hero Section -->
<section class="relative min-h-screen flex items-center justify-center overflow-hidden">
	<!-- Background Image with Overlay -->
	<div class="absolute inset-0 z-0">
		<img 
			src={kitchen} 
			alt="Kitchen background" 
			class="w-full h-full object-cover"
		/>
		<div class="absolute inset-0 bg-black/40"></div>
	</div>

	<!-- Hero Content -->
	<div class="relative z-10 text-center text-white px-4 sm:px-6 lg:px-8 animate-fade-in">
		<div class="max-w-4xl mx-auto">
			<!-- Subtitle -->
			<div class="text-lg font-medium text-primary-200 dark:text-walnut-200 mb-4 tracking-wider uppercase">
				Welcome to
			</div>
			
			<!-- Main Title -->
			<h1 class="text-5xl md:text-7xl lg:text-8xl font-serif font-bold mb-6 leading-tight">
				Jonny's
				<br />
				<span class="text-primary-300 dark:text-walnut-300">Cookbook</span>
			</h1>
			
			<!-- Description -->
			<p class="text-xl md:text-2xl text-neutral-200 mb-12 max-w-2xl mx-auto leading-relaxed">
				A curated collection of my personal favorite recipes, crafted with passion and shared with love
			</p>
			
			<!-- CTA Button -->
			<div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
				<a 
					href="/recipe-list" 
					class="btn-primary text-lg px-8 py-4 bg-primary-600 hover:bg-primary-700 dark:bg-walnut-700 dark:hover:bg-walnut-800 text-white font-semibold rounded-lg transition-all duration-300 shadow-2xl hover:shadow-primary-500/25 dark:hover:shadow-walnut-500/25 transform hover:-translate-y-1"
				>
					Explore Recipes
				</a>
				<a 
					href="/new-recipe" 
					class="btn-secondary text-lg px-8 py-4 bg-white/10 hover:bg-white/20 text-white font-semibold rounded-lg transition-all duration-300 border border-white/30 backdrop-blur-sm"
				>
					Share Your Recipe
				</a>
			</div>
		</div>
	</div>

	<!-- Scroll Indicator -->
	<div class="absolute bottom-8 left-1/2 transform -translate-x-1/2 animate-float">
		<div class="w-6 h-10 border-2 border-white/50 rounded-full flex justify-center">
			<div class="w-1 h-3 bg-white/70 rounded-full mt-2 animate-bounce"></div>
		</div>
	</div>
</section>

<!-- Features Section -->
<section class="section-padding bg-white dark:bg-neutral-800">
	<div class="container-max">
		<div class="text-center mb-16">
			<h2 class="text-4xl md:text-5xl font-serif font-bold text-neutral-800 dark:text-neutral-100 mb-6">
				Why Choose Jonny's Cookbook?
			</h2>
			<p class="text-xl text-neutral-600 dark:text-neutral-300 max-w-3xl mx-auto">
				Discover handpicked recipes that have been tested, refined, and perfected for the ultimate culinary experience
			</p>
		</div>

		<div class="grid md:grid-cols-3 gap-8">
			<!-- Feature 1 -->
			<div class="card p-8 text-center group">
				<div class="w-16 h-16 bg-primary-100 dark:bg-walnut-100 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:bg-primary-200 dark:group-hover:bg-walnut-200 transition-colors duration-300">
					<svg class="w-8 h-8 text-primary-600 dark:text-walnut-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
					</svg>
				</div>
				<h3 class="text-2xl font-serif font-semibold text-neutral-800 dark:text-neutral-100 mb-4">Tested & Trusted</h3>
				<p class="text-neutral-600 dark:text-neutral-300 leading-relaxed">
					Every recipe has been personally tested and refined to ensure perfect results every time
				</p>
			</div>

			<!-- Feature 2 -->
			<div class="card p-8 text-center group">
				<div class="w-16 h-16 bg-accent-100 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:bg-accent-200 transition-colors duration-300">
					<svg class="w-8 h-8 text-accent-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.746 0 3.332.477 4.5 1.253v13C19.832 18.477 18.246 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
					</svg>
				</div>
				<h3 class="text-2xl font-serif font-semibold text-neutral-800 dark:text-neutral-100 mb-4">Detailed Instructions</h3>
				<p class="text-neutral-600 dark:text-neutral-300 leading-relaxed">
					Step-by-step instructions with helpful tips and techniques to guide you through each recipe
				</p>
			</div>

			<!-- Feature 3 -->
			<div class="card p-8 text-center group">
				<div class="w-16 h-16 bg-success-100 rounded-full flex items-center justify-center mx-auto mb-6 group-hover:bg-success-200 transition-colors duration-300">
					<svg class="w-8 h-8 text-success-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
					</svg>
				</div>
				<h3 class="text-2xl font-serif font-semibold text-neutral-800 dark:text-neutral-100 mb-4">Community Driven</h3>
				<p class="text-neutral-600 dark:text-neutral-300 leading-relaxed">
					Join our community of food lovers and share your own favorite recipes with others
				</p>
			</div>
		</div>
	</div>
</section>

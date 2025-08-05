<script>
	import { page } from '$app/stores';
	import { isLoggedIn } from '$lib/stores/authStore';
	
	// Navigation items
	const navItems = [
		{ href: '/', label: 'Home', icon: '🏠' },
		{ href: '/recipes', label: 'Recipes', icon: '📖' },
		{ href: '/new-recipe', label: 'Submit', icon: '➕' },
		{ href: '/favoriterecipes', label: 'Favorites', icon: '❤️' },
		{ href: '/privatedashboard', label: 'Dashboard', icon: '📊' }
	];
</script>

<!-- Bottom Navigation - Only show on mobile -->
<nav class="md:hidden fixed bottom-0 left-0 right-0 bg-white/95 dark:bg-neutral-800/95 backdrop-blur-md border-t border-neutral-200 dark:border-neutral-700 z-50 shadow-lg">
	<div class="flex items-center justify-around px-2 py-2">
		{#each navItems as item}
			<a 
				href={item.href}
				class="flex flex-col items-center justify-center px-3 py-2 rounded-lg transition-all duration-200 group {($page.url.pathname === item.href || ($page.url.pathname.startsWith(item.href) && item.href !== '/')) ? 'text-primary-600 dark:text-walnut-400 bg-primary-50 dark:bg-walnut-900/20' : 'text-neutral-600 dark:text-neutral-300 hover:text-primary-600 dark:hover:text-walnut-400 hover:bg-neutral-50 dark:hover:bg-neutral-700/50'}"
			>
				<span class="text-xl mb-1">{item.icon}</span>
				<span class="text-xs font-medium">{item.label}</span>
			</a>
		{/each}
	</div>
</nav>

<!-- Add bottom padding to main content to account for bottom nav on mobile -->
<div class="md:hidden h-20"></div> 
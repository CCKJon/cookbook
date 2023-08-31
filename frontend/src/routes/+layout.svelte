<script>
	import '../app.postcss';
	import NavMenu from '$lib/components/NavMenu.svelte';
</script>

<div class="app min-h-screen bg-yellow-600 rounded-xl">
	<main class="h-screen">
		<NavMenu />
		<slot />
	</main>
</div>

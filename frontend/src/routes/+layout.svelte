<script>
	import '../app.postcss';
	import NavMenu from '$lib/components/NavMenu.svelte';
</script>

<div class="bg-red-800 min-h-screen overflow-hidden">
	<main class="h-screen">
		<NavMenu />
		<slot />
	</main>
</div>

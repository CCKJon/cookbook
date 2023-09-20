<script>
	//@ts-nocheck
	import '../app.postcss';
	import NavMenu from '$lib/components/NavMenu.svelte';
	import { onMount } from 'svelte';
	import { auth } from '$lib/firebase/firebase.client';
	import { authStore } from '$lib/stores/authStore';
	import { browser } from '$app/environment';

	onMount(() => {
		console.log(auth);
		const unsubscribe = auth.onAuthStateChanged((user) => {
			// console.log(user);
			authStore.update((curr) => {
				console.log(curr.currentUser);
				return { ...curr, isLoading: false, currentUser: user };
			});

			if (
				browser &&
				!$authStore?.currentUser &&
				!$authStore.isLoading &&
				window.location.pathname !== '/'
			) {
				window.location.href = '/';
			}
		});
		return unsubscribe;
	});
</script>

<div class="bg-red-800 min-h-screen overflow-hidden">
	<main class="h-screen">
		<NavMenu />
		<slot />
	</main>
</div>

<script>
	//@ts-nocheck
	import '../app.postcss';
	import NavMenu from '$lib/components/NavMenu.svelte';
	import { onMount } from 'svelte';
	import { auth } from '$lib/firebase/firebase.client';
	import { authStore, isLoggedIn } from '$lib/stores/authStore';
	import { browser } from '$app/environment';

	$: {
		if ($isLoggedIn) {
			console.log(true);
		} else {
			console.log(false);
		}
	}

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

<div class="min-h-screen bg-gradient-to-br from-neutral-50 to-neutral-100">
	<main class="min-h-screen">
		<NavMenu />
		<slot />
	</main>
</div>

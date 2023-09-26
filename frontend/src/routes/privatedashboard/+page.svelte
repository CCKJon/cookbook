<script>
	//@ts-nocheck
	import { authHandlers, authStore } from '$lib/stores/authStore';
	import AuthReset from '$lib/components/AuthReset.svelte';

	let email;
	let userid;

	authStore.subscribe((curr) => {
		email = curr?.currentUser?.email;
		console.log(curr.currentUser);
		userid = curr?.currentUser?.uid;
	});
</script>

<div>This is where my submitted recipes will go</div>

<a href="/favoriterecipes">This is where the link to a favorites page will go</a>

{#if $authStore.currentUser}
	<div>
		<h1>Current User: {email}</h1>

		<!-- {#each }
			<div></div>





		{/} -->

		<AuthReset />
		<button on:click={authHandlers.logout}>Logout</button>
	</div>
{:else}
	<div>Loading....</div>
{/if}

<style>
	div {
		flex: 1;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	h1 {
		text-align: center;
	}
</style>

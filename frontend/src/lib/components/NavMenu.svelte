<script>
	import logo from '$lib/icons/logo.png';
	import SearchComponent from './SearchComponent.svelte';
	import { isLoggedIn } from '$lib/stores/authStore';
	import LoginModal from './LoginModal.svelte';
	import { Button, Modal, Label, Input, Checkbox } from 'flowbite-svelte';
	let formModal = false;
	import { auth } from '$lib/firebase/firebase.client';
	import Auth from './Auth.svelte';
	import { authHandlers, authStore } from '$lib/stores/authStore';

	import Modals from './Modals.svelte';
	let displaySearch = false;
	let modal = false;

	function displaySearchComponent() {
		displaySearch = !displaySearch;
	}

	// $: {
	// 	if ($isLoggedIn) {
	// 		console.log(true);
	// 	} else {
	// 		console.log(false);
	// 	}
	// }
</script>

<div class="px-5 py-2 flex flex-row items-center justify-between bg-[#0F0F0F] w-11/12 mx-auto">
	<a href="/"><img class="h-16 w-auto" src={logo} alt="logo" /></a>
	<div class="flex gap-5">
		{#if $isLoggedIn}
			<a class="text-gray-300 font-serif" href="/privatedashboard">Account</a>
		{:else}
			<button class="text-gray-300 font-serif" type="button" on:click={() => (formModal = true)}
				>Login</button
			>

			<Modal bind:open={formModal} size="xs" autoclose={false} class="w-full">
				<form class="flex flex-col space-y-6" action="#">
					<h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">
						Sign in to our platform
					</h3>
					<Label class="space-y-2">
						<span>Email</span>
						<Input type="email" name="email" placeholder="name@company.com" required />
					</Label>
					<Label class="space-y-2">
						<span>Your password</span>
						<Input type="password" name="password" placeholder="•••••" required />
					</Label>
					<div class="flex items-start">
						<Checkbox>Remember me</Checkbox>
						<a
							href="/"
							class="ml-auto text-sm text-primary-700 hover:underline dark:text-primary-500"
						>
							Lost password?
						</a>
					</div>
					<Button type="submit" class="w-full1">Login to your account</Button>
					<div class="text-sm font-medium text-gray-500 dark:text-gray-300">
						Not registered? <a
							href="/"
							class="text-primary-700 hover:underline dark:text-primary-500"
						>
							Create account
						</a>
					</div>
				</form>
			</Modal>
			<!-- <a class="text-gray-300 font-serif" href="/login">Login</a> -->
		{/if}
		<!-- {#if modal}
			<LoginModal />
		{/if} -->
		<a class="text-gray-300 font-serif" href="/recipe-list">Recipes</a>
		<a class="text-gray-300 font-serif" href="/new-recipe">Submit</a>
		<button on:click={() => displaySearchComponent()} type="button" class="text-gray-300 font-serif"
			>Search</button
		>
		{#if displaySearch}
			<div class="text-white">
				<SearchComponent />
			</div>
		{/if}
	</div>
</div>

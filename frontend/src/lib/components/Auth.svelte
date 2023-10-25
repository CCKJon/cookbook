<script>
	import { authHandlers, authStore } from '$lib/stores/authStore';
	import { Button, Modal, Label, Input, Checkbox } from 'flowbite-svelte';

	let register = false;
	let email = '';
	let password = '';
	let confirmPassword = '';
	export let formModal = true;

	async function handleSubmit() {
		if (!email || !password || (register && !confirmPassword)) {
			return;
		}
		if (register && password === confirmPassword) {
			try {
				await authHandlers.signup(email, password);
			} catch (err) {
				console.log(err);
			}
		} else {
			try {
				await authHandlers.login(email, password);
			} catch (err) {
				console.log(err);
			}
		}
		if ($authStore.currentUser) {
			window.location.href = '/privatedashboard';
		}
	}
</script>

<!-- The modal for login should be placed into here -->
<h1>{register ? 'Register' : 'Log in'}</h1>
<form class="flex flex-col space-y-6" action="#">
	<h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Sign in to our platform</h3>
	<Label class="space-y-2">
		<span>Email</span>
		<Input bind:value={email} type="email" name="email" placeholder="name@company.com" required />
	</Label>
	<Label class="space-y-2">
		<span>Your password</span>
		<Input bind:value={password} type="password" name="password" placeholder="•••••" required />
	</Label>
	{#if register}
		<Label>
			<Input bind:value={confirmPassword} type="password" placeholder="Confirm Password" />
		</Label>
	{/if}
	<div class="flex items-start">
		<Checkbox>Remember me</Checkbox>
		<!-- svelte-ignore a11y-no-static-element-interactions -->
		<a
			on:click={() => {
				formModal = false;
			}}
			href="/forgotPassword"
			class="ml-auto text-sm text-primary-700 hover:underline dark:text-primary-500"
		>
			<p>Forgot Password?</p>
		</a>
	</div>
	<Button on:click={handleSubmit} type="submit" class="w-full1">Login to your account</Button>
	{#if register}
		<!-- svelte-ignore a11y-no-static-element-interactions -->
		<div
			class="text-sm font-medium text-gray-500 dark:text-gray-300"
			on:click={() => {
				register = false;
			}}
			on:keydown={() => {}}
		>
			Already have an account? <p class="text-primary-700 hover:underline dark:text-primary-500">
				Log in
			</p>
		</div>
	{:else}
		<!-- svelte-ignore a11y-no-static-element-interactions -->
		<div
			class="text-sm font-medium text-gray-500 dark:text-gray-300"
			on:click={() => {
				register = true;
			}}
			on:keydown={() => {}}
		>
			Not registered?
			<p class="text-primary-700 hover:underline dark:text-primary-500">Create account</p>
		</div>
		<!-- svelte-ignore a11y-no-static-element-interactions -->
	{/if}
</form>

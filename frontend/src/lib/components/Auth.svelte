<script>
	import { Button, Modal, Label, Input, Checkbox } from 'flowbite-svelte';
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	let register = false;
	let email = '';
	let password = '';
	let confirmPassword = '';
	let rememberMe = false;
	let isLoading = false;
	let errorMessage = '';
	let successMessage = '';
	
	export let formModal = true;

	// Reset form when modal opens/closes
	$: if (!formModal) {
		resetForm();
	}

	function resetForm() {
		email = '';
		password = '';
		confirmPassword = '';
		rememberMe = false;
		errorMessage = '';
		successMessage = '';
		register = false;
	}

	function validateForm() {
		errorMessage = '';
		
		if (!email || !email.trim()) {
			errorMessage = 'Email is required';
			return false;
		}
		
		if (!email.includes('@') || !email.includes('.')) {
			errorMessage = 'Please enter a valid email address';
			return false;
		}
		
		if (!password || password.length < 6) {
			errorMessage = 'Password must be at least 6 characters long';
			return false;
		}
		
		if (register && password !== confirmPassword) {
			errorMessage = 'Passwords do not match';
			return false;
		}
		
		return true;
	}

	async function handleSubmit() {
		if (!validateForm()) {
			return;
		}

		isLoading = true;
		errorMessage = '';
		successMessage = '';

		// Simulate API call delay
		await new Promise(resolve => setTimeout(resolve, 1500));

		try {
			if (register) {
				// Simulate successful registration
				successMessage = 'Account created successfully! This is a demo - no actual account was created.';
				// Don't close modal immediately for registration - let user see success message
			} else {
				// Simulate successful login
				successMessage = 'Login successful! This is a demo - no actual login occurred.';
				// Close modal after successful login
				setTimeout(() => {
					formModal = false;
					resetForm();
				}, 2000);
			}
		} catch (err) {
			console.error('Demo error:', err);
			errorMessage = 'This is a demo - no actual authentication is happening.';
		} finally {
			isLoading = false;
		}
	}

	function toggleMode() {
		register = !register;
		errorMessage = '';
		successMessage = '';
		password = '';
		confirmPassword = '';
	}

	function handleForgotPassword() {
		if (!email) {
			errorMessage = 'Please enter your email address first';
			return;
		}
		
		// Simulate password reset
		successMessage = 'Password reset email sent! (This is a demo - no email was actually sent)';
	}
</script>

<div class="p-6">
	<!-- Header -->
	<div class="text-center mb-6">
		<h2 class="text-2xl font-bold text-gray-900 dark:text-white mb-2">
			{register ? 'Create Account' : 'Welcome Back'}
		</h2>
		<p class="text-gray-600 dark:text-gray-400">
			{register ? 'Join Jonny\'s Cookbook to save and share your favorite recipes' : 'Sign in to access your recipes and favorites'}
		</p>
		<!-- Demo notice -->
		<div class="mt-2 p-2 bg-blue-50 border border-blue-200 text-blue-700 rounded-lg text-xs">
			<strong>Demo Mode:</strong> This is a cosmetic interface. No actual authentication will occur.
		</div>
	</div>

	<!-- Error/Success Messages -->
	{#if errorMessage}
		<div class="mb-4 p-3 bg-red-50 border border-red-200 text-red-700 rounded-lg text-sm">
			{errorMessage}
		</div>
	{/if}
	
	{#if successMessage}
		<div class="mb-4 p-3 bg-green-50 border border-green-200 text-green-700 rounded-lg text-sm">
			{successMessage}
		</div>
	{/if}

	<!-- Form -->
	<form class="space-y-4" on:submit|preventDefault={handleSubmit}>
		<Label class="space-y-2">
			<span class="text-sm font-medium text-gray-700 dark:text-gray-300">Email address</span>
			<Input 
				bind:value={email} 
				type="email" 
				name="email" 
				placeholder="Enter your email" 
				required 
				disabled={isLoading}
				class="w-full"
			/>
		</Label>
		
		<Label class="space-y-2">
			<span class="text-sm font-medium text-gray-700 dark:text-gray-300">Password</span>
			<Input 
				bind:value={password} 
				type="password" 
				name="password" 
				placeholder="Enter your password" 
				required 
				disabled={isLoading}
				class="w-full"
			/>
		</Label>
		
		{#if register}
			<Label class="space-y-2">
				<span class="text-sm font-medium text-gray-700 dark:text-gray-300">Confirm Password</span>
				<Input 
					bind:value={confirmPassword} 
					type="password" 
					name="confirmPassword" 
					placeholder="Confirm your password" 
					required 
					disabled={isLoading}
					class="w-full"
				/>
			</Label>
		{/if}
		
		<div class="flex items-center justify-between">
			<Checkbox bind:checked={rememberMe} disabled={isLoading}>
				Remember me
			</Checkbox>
			{#if !register}
				<button 
					type="button"
					on:click={handleForgotPassword}
					disabled={isLoading}
					class="text-sm text-primary-600 hover:text-primary-500 dark:text-primary-400 dark:hover:text-primary-300 font-medium"
				>
					Forgot password?
				</button>
			{/if}
		</div>
		
		<Button 
			type="submit" 
			class="w-full" 
			disabled={isLoading}
			color="primary"
		>
			{#if isLoading}
				<div class="flex items-center justify-center">
					<div class="animate-spin rounded-full h-4 w-4 border-b-2 border-white mr-2"></div>
					{register ? 'Creating Account...' : 'Signing In...'}
				</div>
			{:else}
				{register ? 'Create Account' : 'Sign In'}
			{/if}
		</Button>
	</form>
	
	<!-- Toggle Mode -->
	<div class="mt-6 text-center">
		<p class="text-sm text-gray-600 dark:text-gray-400">
			{register ? 'Already have an account?' : "Don't have an account?"}
			<button 
				type="button"
				on:click={toggleMode}
				disabled={isLoading}
				class="ml-1 text-primary-600 hover:text-primary-500 dark:text-primary-400 dark:hover:text-primary-300 font-medium"
			>
				{register ? 'Sign in' : 'Create account'}
			</button>
		</p>
	</div>
	
	<!-- Terms for Registration -->
	{#if register}
		<div class="mt-4 text-xs text-gray-500 dark:text-gray-400 text-center">
			By creating an account, you agree to our 
			<a href="/terms" class="text-primary-600 hover:text-primary-500">Terms of Service</a> 
			and 
			<a href="/privacy" class="text-primary-600 hover:text-primary-500">Privacy Policy</a>
		</div>
	{/if}
</div>

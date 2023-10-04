<script>
	import { authHandlers } from '$lib/stores/authStore';

	let action = '';
	let newEmail = '';
	let newPass = '';

	async function handleSubmit() {
		if (!action) {
			return;
		}
		if (action === 'updatePass') {
			console.log("i'm trying to update my password", newPass);
			return await authHandlers.updatePassword(newPass);
		}

		if (action === 'updateEmail') {
			console.log("I'm trying to update my email", newEmail);
			return await authHandlers.updateEmail(newEmail);
		}
	}
</script>

<div class="flex flex-row justify-between w-full max-w-[675px] px-5">
	<div class="rounded-md border-2 bg-blue-900 bg-opacity-90 border-black py-2 px-2">
		<button
			on:click={() => {
				action = 'updateEmail';
			}}>Update Email</button
		>
	</div>
	<div class="rounded-md border-2 bg-blue-900 bg-opacity-90 border-black py-2 px-2">
		<button
			on:click={() => {
				action = 'updatePass';
			}}>Reset Password</button
		>
	</div>

	{#if action === 'updatePass'}
		<form>
			<label>
				<input bind:value={newPass} type="password" placeholder="New Password" />
			</label>
			<button on:click={handleSubmit}>Submit</button>
		</form>
	{/if}

	{#if action === 'updateEmail'}
		<!-- <form>
			<label>
				<input bind:value={newEmail} type="email" placeholder="New Email" />
			</label>
			<button on:click={handleSubmit}>Submit</button>
		</form> -->
		<form on:submit={handleSubmit} class="flex flex-col gap-1" action="">
			<input bind:value={newEmail} autocomplete="on" type="email" id="email" placeholder="Email" />

			<button
				class="bg-gray-200 hover:bg-gray-200/50 border rounded-md border-gray-600"
				type="submit">Submit</button
			>
		</form>
	{/if}
</div>

<script>
	//@ts-nocheck
	import { authHandlers, authStore } from '$lib/stores/authStore';

	let email;
</script>

<div
	class="mx-auto w-11/12 py-7 px-7 h-full bg-[url('$lib/icons/kitchen.jpg')] overflow-hidden bg-no-repeat bg-cover"
>
	<div class="w-full flex flex-row justify-center gap-5 py-80">
		<input
			class="placeholder:text-gray-400 rounded-md px-2"
			type="email"
			placeholder="youremail@email.com"
			bind:value={email}
		/>
		<button
			class="px-2 py-1 rounded-md bg-white hover:bg-slate-300"
			type="button"
			on:click={() => {
				authHandlers.resetPassword(email);
			}}
			on:keydown={() => {}}
		>
			<p>Reset Password</p>
		</button>
	</div>
</div>

<script lang="ts">
	export let showModal: boolean;

	let dialog: HTMLDialogElement;

	$: if (dialog && showModal) dialog.showModal();
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
<dialog
	class="rounded-md py-1 border-2 border-yellow-300 bg-gray-900 bg-[url('$lib/icons/updateRecipe.jpg')] bg-no-repeat bg-cover"
	bind:this={dialog}
	on:close={() => (showModal = false)}
	on:click|self={() => dialog.close()}
>
	<div class="flex justify-end pt-10 pr-10">
		<button
			class="border border-black bg-blue-900 bg-opacity-90 py-1 px-1 rounded-md font-serif text-gray-300"
			autofocus
			on:click={() => dialog.close()}>Close Modal</button
		>
	</div>
	<!-- svelte-ignore a11y-no-static-element-interactions -->
	<div class="" on:click|stopPropagation>
		<slot />
		<!-- svelte-ignore a11y-autofocus -->
	</div>
</dialog>

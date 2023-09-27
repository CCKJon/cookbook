<script>
	// @ts-nocheck

	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	export let data;
	import { PUBLIC_CLUSTER_PASSWORD, PUBLIC_CLUSTER_IMAGES } from '$env/static/public';
	import { Spinner } from 'flowbite-svelte';

	let recipe;
	let title = '';
	let description = '';
	let id = data.id;
	let updatedTitle = '';
	let image;
	let serving_size = '';
	let difficulty = '';
	let cooking_time = '';

	async function getRecipe() {
		const response = await fetch(`${PUBLIC_CLUSTER_PASSWORD}/api/recipe/${id}`);
		const data = await response.json();
		return data;
	}

	async function getRecipeImage(photo_id) {
		try {
			const response = await fetch(`${PUBLIC_CLUSTER_IMAGES}/files/${photo_id}`, {
				method: 'GET',
				headers: {
					'Content-Type': 'image/jpg'
				}
				// mode: 'no-cors'
			});
			if (!response.ok) {
				throw new Error('Failed to fetch user profile image');
			}
			const dat = await response.blob();
			image = dat;
			console.log('data', dat);
			return image;
		} catch (error) {
			console.error('Failed to get profile image:', error);
		}
	}

	onMount(async () => {
		recipe = await getRecipe();
		console.log(recipe);
		// title = recipe.title;
		// description = recipe.description;
		// due_date = recipe.due_date;
	});
</script>

<div
	class="mx-auto w-11/12 py-7 px-7 h-full bg-[url('$lib/icons/recipe.jpg')] bg-no-repeat bg-cover overflow-auto font-serif"
>
	{#if recipe}
		<h1 class="mx-auto grid place-items-center text-3xl text-gray-300 capitalize font-serif my-3">
			{recipe.title}
		</h1>
		<hr class="w-60 grid place-items-center mx-auto mb-3" />
		<div class="my-5">
			<div class="grid place-items-center text-center mx-auto text-xl text-cyan-400">
				{recipe.description}
			</div>
		</div>
		{@const imageId = recipe.images[0].photo_id}
		{#await getRecipeImage(imageId)}
			<Spinner color="red" />
		{:then imageUrl}
			<div class="w-full flex items-center justify-center my-5">
				<img
					class="w-auto max-h-[450px] object-cover rounded-md border-2 border-gray-800"
					src={URL.createObjectURL(imageUrl)}
					alt=""
				/>
			</div>
		{/await}

		<div class=" w-96 mx auto text-center mx-auto grid place-items-center rounded-lg text-white">
			<!-- <form class="mb-3 grid place-items-center text-rose-default" on:submit={updateTodo}>
			<div class="text- text-center text-md mb-2">New Title:</div>
			<input
				required
				class="mb-1 rounded-xl text-black border-4 border-pink-400 placeholder:text-slate-300 w-52"
				type="text"
				placeholder={title}
				bind:value={title}
			/>

			<div class="text- text-center text-md mb-2">New description:</div>
			<input
				class="mb-1 rounded-xl text-black border-4 border-pink-400 placeholder:text-slate-300 w-52"
				type="text"
				placeholder={description}
				bind:value={description}
			/>
			<button
				class="py-1 px-1 mt-3 mb-20 text-center grid place-items-center w-44 mx-auto rounded-md text-white border-indigo-800 border-2 hover:bg-slate-600 font-bold"
				type="submit">Update Recipe</button
			>
		</form> -->
		</div>
		<div class="flex justify-center">
			<div class="flex flex-row justify-between w-full max-w-[675px] py-5">
				<div
					class="text-gray-300 text-lg font-serif w-full flex items-center justify-between px-2 py-5 border bg-gray-700 bg-opacity-40 border-black rounded-md"
				>
					<div class="hover:bg-red-800/60 px-2 rounded-md">
						{#if recipe.serving_size}
							Serving size: {recipe.serving_size}
						{:else}
							Serving size: N/A
						{/if}
					</div>

					<div class="hover:bg-red-800/60 px-2 rounded-md">
						{#if recipe.cooking_time}
							Cook time: {recipe.cooking_time}
						{:else}
							Cook time: N/A
						{/if}
					</div>
					<div class="hover:bg-red-800/60 px-2 rounded-md">
						{#if recipe.difficulty}
							Difficulty: {recipe.difficulty}
						{:else}
							Difficulty: N/A
						{/if}
					</div>
				</div>
			</div>
		</div>
		<div class="flex justify-center">
			<div class="flex flex-row justify-between w-full max-w-[675px]">
				<div class="border bg-gray-700 bg-opacity-40 rounded-md max-h-full p-5 border-black">
					<div class="my-2 text-center text-xl text-gray-300">Ingredients</div>
					<hr class="w-60 grid place-items-center mx-auto my-5" />
					{#each recipe.ingredients as ingredient}
						<div
							class="text-gray-300 text-lg font-serif w-full flex items-center justify-between hover:bg-red-800/60 px-2"
						>
							<div>
								{ingredient.name}
							</div>
							<div>
								{ingredient.amount}
							</div>
						</div>
					{/each}
				</div>
				<div class="border bg-gray-700 bg-opacity-40 rounded-md max-h-full p-5 border-black">
					<div class="my-2 text-center text-xl text-gray-300">Instructions</div>
					<hr class="w-60 grid place-items-center mx-auto my-5" />
					{#each recipe.steps as step}
						<div
							class="text-gray-300 text-lg font-serif w-full flex items-center justify-between my-1 hover:bg-red-800/60 px-2"
						>
							<div>{step.step_number}.</div>
							<div>{step.description}</div>
						</div>
					{/each}
				</div>
			</div>
		</div>
	{/if}
</div>

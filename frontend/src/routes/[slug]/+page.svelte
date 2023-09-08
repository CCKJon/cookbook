<script>
	// @ts-nocheck

	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	export let data;
	import { PUBLIC_CLUSTER_PASSWORD, PUBLIC_CLUSTER_IMAGES } from '$env/static/public';

	let recipe;
	let title = '';
	let description = '';
	let id = data.id;
	let updatedTitle = '';

	async function getRecipe() {
		const response = await fetch(`${PUBLIC_CLUSTER_PASSWORD}/api/recipe/${id}`);
		const data = await response.json();
		return data;
	}

	// async function deleteRecipe() {
	// 	const response = await fetch(`https://todo-test-api-jelz.onrender.com/api/todo/${id}`, {
	// 		method: 'DELETE',
	// 		headers: {
	// 			'Content-Type': 'application/json'
	// 		}
	// 	})
	// 		.then((response) => {
	// 			// @ts-ignore
	// 			window.location = '/';
	// 		})
	// 		.catch((error) => {
	// 			// Handle error
	// 		});
	// }

	// function updateRecipe() {
	// 	fetch(`https://todo-test-api-jelz.onrender.com/api/todo/${id}`, {
	// 		method: 'PUT',
	// 		headers: {
	// 			'Content-Type': 'application/json'
	// 		},
	// 		body: JSON.stringify({
	// 			category,
	// 			title,
	// 			description,
	// 			due_date: due_date ? new Date(due_date).toISOString().split('T')[0].toString() : 'null'
	// 		})
	// 	})
	// 		.then((_res) => {
	// 			goto('/');
	// 		})
	// 		.catch((_err) => {
	// 			_err = !_err;
	// 		});
	// }

	onMount(async () => {
		recipe = await getRecipe();
		console.log(recipe);
		// title = recipe.title;
		// description = recipe.description;
		// due_date = recipe.due_date;
	});
</script>

{#if recipe}
	<h1 class="grid place-items-center text-2xl font-bold text-white mb-3 mt-24">{recipe.title}</h1>
	<hr class="w-60 grid place-items-center mx-auto mb-3" />
	<div class="mb-24">
		<div class="grid place-items-center text-center mx-auto text-cyan-400">
			{recipe.description}
		</div>
	</div>

	<div class="mb-10 w-96 mx auto text-center mx-auto grid place-items-center rounded-lg text-white">
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
{/if}

<script>
	import { goto } from '$app/navigation';

	let title;
	let description;
	let category;
	let ingredients = [];
	let steps = [];
	let images = [];

	function showAndHideModal() {
		showModal = true; // Show the modal

		setTimeout(() => {
			showModal = false; // Hide the modal after the delay
			goto('/'); // Redirect to the desired location
		}, 3000); // Specify the delay in milliseconds (e.g., 3000ms = 3 seconds)
	}

	function handleSubmit(event) {
		event.preventDefault();
		const options = { timeZone: 'America/Chicago', dateStyle: 'short' };
		const currentTime = new Date();
		const create_date = currentTime.toLocaleString('en-US', options).split('T')[0];
		const newRecipe = {
			category,
			title,
			description,
			create_date: create_date,
			ingredients,
			steps,
			images
		};

		// fetch('https://recipe-test-api-jelz.onrender.com/api/recipe/', {
		// 	method: 'POST',
		// 	headers: {
		// 		'Content-Type': 'application/json'
		// 	},
		// 	body: JSON.stringify(newRecipe)
		// })
		// 	.then(() => {
		// 		goto('/');
		// 	})
		// 	.catch(() => {
		// 		return {
		// 			status: 301,
		// 			error: new Error('Could not create a new recipe')
		// 		};
		// 	});
		console.log(newRecipe);
	}

	function addIngredient() {
		ingredients.push({}); // Add an empty ingredient to the array
		ingredients = ingredients;
	}
	function addSteps() {
		steps.push({}); // Add an empty steps to the array
		steps = steps;
	}
</script>

<div
	class="mx-auto w-11/12 py-7 px-7 h-full bg-[url('$lib/icons/recipe.jpg')] bg-no-repeat bg-cover overflow-auto"
>
	<form
		class="mx-auto text-center grid place-items-center mb-10 text-black font-serif text-xl"
		on:submit={handleSubmit}
	>
		<div class="text-lg font-bold text-center font-serif text-gray-300 mb-2 mt-2">Title:</div>
		<input
			class="bg-gray-300 border-2 border-red-800 rounded-sm text-black font-serif w-1/6 mb-5"
			bind:value={title}
			type="text"
			required
		/>

		<div class="text-lg font-bold font-serif text-center text-gray-300 mb-2 mt-2">Description:</div>
		<textarea
			class="border-2 bg-gray-300 border-gray-800 rounded-sm text-black w-1/3 font-serif mb-5"
			bind:value={description}
		/>

		<div class="text-lg font-serif font-bold text-center text-gray-300 mb-2 mt-2">Ingredients</div>
		<button
			class="border-2 bg-yellow-500 hover:opacity-80 mb-3 font-serif text-md border-gray-800 rounded-sm w-40 text-gray-300 text-center py-1 px-1 font-bold"
			on:click={addIngredient}>+ingredient</button
		>
		{#each ingredients as ingredient, index}
			<div class="flex justify-between gap-5 py-2">
				<input
					class="border-2 bg-gray-300 font-serif border-gray-800 text-gray-900 rounded-sm w-52"
					type="text"
					placeholder="Name"
					bind:value={ingredients[index].name}
				/>

				<input
					class="border-2 bg-gray-300 font-serif border-gray-800 rounded-sm text-gray-900 w-52"
					type="text"
					placeholder="Amount"
					bind:value={ingredients[index].amount}
				/>
			</div>
		{/each}

		<div class="text-lg font-bold font-serif text-center text-gray-300 mb-2 mt-5">Instructions</div>
		<button
			class="border-2 bg-yellow-500 hover:opacity-80 text-md mb-3 border-gray-800 rounded-sm font-serif text-gray-300 w-40 text-center py-1 px-1 font-bold"
			on:click={addSteps}>+steps</button
		>
		{#each steps as step, index}
			<div class="flex items-start justify-between gap-5 py-2">
				<input
					class="font-serif border-2 bg-gray-300 border-gray-800 rounded-sm w-20"
					type="number"
					min="1"
					max="100"
					required
					placeholder="Step number"
					bind:value={steps[index].step_number}
				/>

				<textarea
					class="font-serif border-2 bg-gray-300 border-gray-800 rounded-sm w-96"
					placeholder="Instructions"
					required
					bind:value={steps[index].description}
				/>
			</div>
		{/each}

		<button
			class="text-gray-300 bg-red-800 font-serif text-lg border-red-900 border-2 mt-10 rounded-sm py-1 px-1 font-bold hover:opacity-80 mx-auto text-center"
			on:click={() => {
				showAndHideModal();
			}}
			type="submit">Submit Recipe</button
		>
	</form>
</div>

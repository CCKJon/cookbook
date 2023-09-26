<script>
	//@ts-nocheck
	import { goto } from '$app/navigation';
	import { PUBLIC_CLUSTER_PASSWORD, PUBLIC_CLUSTER_IMAGES } from '$env/static/public';
	import { onMount } from 'svelte';
	import Modal from './Modal.svelte';
	import { authStore } from '$lib/stores/authStore';

	let title;
	let description;
	let serving_size;
	let cooking_time;
	let difficulty;
	let category;
	let ingredients = [];
	let steps = [];
	let images = [];
	let author;
	let fileInput;
	let showModal = false;

	authStore.subscribe((curr) => {
		author = curr?.currentUser?.uid;
	});

	function showAndHideModal() {
		showModal = true; // Show the modal

		// goto('/'); // Redirect to the desired location
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
			images,
			serving_size,
			cooking_time,
			difficulty,
			author: author != null ? author : 'EZonoo2pWjhfhkgDaHsfUdZvwsJ2'
		};

		fetch(`${PUBLIC_CLUSTER_PASSWORD}/api/recipe`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(newRecipe)
		})
			.then(async (res) => {
				res = await res.json();
				console.log('this is the recipe id', res._id);
				const recipe_id = res._id;


				const response = await fetch(`http://127.0.0.1:8001/api/user/${author}`);
				const author_data = await response.json();
				// console.log('this is my author data', author_data);
				let authored_recipes = author_data.authored_recipes;
				// console.log('this is authored recipes', authored_recipes);
				authored_recipes.push(recipe_id); // Push the new recipe_id to the array

				await fetch(`http://127.0.0.1:8001/api/user/${author}`, {
					method: 'PUT',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({
						authored_recipes: authored_recipes // Assign the updated array back to authored_recipes
					})
				});

				.then((_res) => {
					goto('/');
				})
				.catch((_err) => {
					_err = !_err;
				});

			})
			.catch(() => {
				return {
					status: 301,
					error: new Error('Could not create a new recipe')
				};
			});
		console.log(newRecipe);
	}

	const handleFileUpload = async () => {
		try {
			const file = fileInput.files?.[0];
			if (file) {
				const formData = new FormData();
				formData.append('photo', file);
				const response = await fetch(`${PUBLIC_CLUSTER_IMAGES}/upload-photo`, {
					method: 'POST',
					body: formData
				});

				if (response.ok) {
					const data = await response.json();
					const photoId = data.file_id;
					images.push({ photo_id: photoId });
					console.log('image upload', images);
					console.log('Image successfully updated!');
				} else {
					console.error('Failed to upload photo');
				}
			}
		} catch (error) {
			console.error('Error occurred during file upload:', error);
		}
	};

	function addIngredient() {
		ingredients.push({}); // Add an empty ingredient to the array
		ingredients = ingredients;
	}
	function removeIngredient() {
		ingredients.pop(); // Add an empty ingredient to the array
		ingredients = ingredients;
	}
	function addSteps() {
		steps.push({}); // Add an empty steps to the array
		steps = steps;
	}
	function subtractStep() {
		steps.pop(); // Add an empty steps to the array
		steps = steps;
	}

	onMount(() => {
		console.log(author);
	});
</script>

<div
	class="mx-auto w-11/12 py-7 px-7 h-full bg-[url('$lib/icons/recipe.jpg')] bg-no-repeat bg-cover overflow-auto"
>
	<form
		class="mx-auto text-center grid place-items-center py-36 text-black font-serif text-xl"
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
		<div class="flex flex-row justify between">
			<div class="text-lg font-bold font-serif text-center text-gray-300 mb-2 mt-2 px-2">
				Serving Size
			</div>
			<select
				class="border-2 bg-gray-300 border-gray-800 rounded-sm text-black font-serif mb-5"
				bind:value={serving_size}
			>
				<option value="1 person">1 person</option>
				<option value="2 people">2 people</option>
				<option value="3 people">3 people</option>
				<option value="4 people">4 people</option>
				<option value="5 people">5 people</option>
				<option value="6 people">6 people</option>
				<option value="7 people">7 people</option>
				<option value="8 people">8 people</option>
				<option value="9 people">9 people</option>
				<option value="10 people">10 people</option>
				<option value="11 people">11 people</option>
				<option value="12 people">12 people</option>
				<option value="13 people">13 people</option>
				<option value="14 people">14 people</option>
				<option value="15 people">15 people</option>
			</select>
			<div class="text-lg font-bold font-serif text-center text-gray-300 mb-2 mt-2 px-2">
				Cooking time
			</div>
			<input
				class="border-2 bg-gray-300 border-gray-800 rounded-sm text-black font-serif mb-5"
				placeholder="e.g., 2 hours 30 minutes"
				bind:value={cooking_time}
			/>
			<div class="text-lg font-bold font-serif text-center text-gray-300 mb-2 mt-2 px-2">
				Difficulty
			</div>
			<select
				class="border-2 bg-gray-300 border-gray-800 rounded-sm text-black font-serif mb-5"
				bind:value={difficulty}
			>
				<option value="easy">Easy</option>
				<option value="medium">Medium</option>
				<option value="hard">Hard</option>
			</select>
		</div>

		<div class="text-lg font-serif font-bold text-center text-gray-300 mb-2 mt-2">Ingredients</div>
		<button
			type="button"
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
				<button
					type="button"
					class="border-2 bg-yellow-500 hover:opacity-80 mb-3 font-serif text-md border-gray-800 rounded-sm w-40 text-gray-300 text-center py-1 px-1 font-bold"
					on:click={removeIngredient}>-ingredient</button
				>
			</div>
		{/each}

		<div class="text-lg font-bold font-serif text-center text-gray-300 mb-2 mt-5">Instructions</div>
		<button
			type="button"
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
				<button
					type="button"
					class="border-2 bg-yellow-500 hover:opacity-80 text-md mb-3 border-gray-800 rounded-sm font-serif text-gray-300 w-40 text-center py-1 px-1 font-bold"
					on:click={subtractStep}>-step</button
				>
			</div>
		{/each}

		<div class="text-gray-300 w-full my-10">
			<input class=" ml-40" type="file" on:change={handleFileUpload} bind:this={fileInput} />
		</div>

		<button
			class="text-gray-300 bg-red-800 font-serif text-lg border-red-900 border-2 my-5 rounded-sm py-1 px-1 font-bold hover:opacity-80 mx-auto text-center"
			on:click={() => {
				showAndHideModal();
			}}
			type="submit">Submit Recipe</button
		>
	</form>
</div>

<!-- svelte-ignore missing-declaration -->
<Modal bind:showModal>
	<h2 class="font-bold text-3xl text-center grid place-items-center mx-auto" slot="header">
		New Recipe has successfully been created!
	</h2>

	<ol class="definition-list text-lg font-bold text-gray-800">
		<li class="mb-2 mt-2">
			Your new recipe been created! You will now be redirected back to the home page.
		</li>
		<li class="mb-5">Please click on the new to-do to edit or delete your new to-do.</li>
	</ol>
</Modal>

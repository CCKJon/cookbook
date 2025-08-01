<script>
	//@ts-nocheck
	import { goto } from '$app/navigation';
	import {
		PUBLIC_CLUSTER_PASSWORD,
		PUBLIC_CLUSTER_IMAGES,
		PUBLIC_CLUSTER_USERS
	} from '$env/static/public';
	import { onMount } from 'svelte';
	import Modal from './Modals.svelte';
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

				const response = await fetch(`${PUBLIC_CLUSTER_USERS}/api/user/${author}`);
				const author_data = await response.json();
				let authored_recipes = author_data.authored_recipes;
				authored_recipes.push(recipe_id);

				await fetch(`${PUBLIC_CLUSTER_USERS}/api/user/${author}`, {
					method: 'PUT',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({
						authored_recipes: authored_recipes
					})
				})
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
		ingredients.push({});
		ingredients = ingredients;
	}
	function removeIngredient() {
		ingredients.pop();
		ingredients = ingredients;
	}
	function addSteps() {
		steps.push({});
		steps = steps;
	}
	function subtractStep() {
		steps.pop();
		steps = steps;
	}

	onMount(() => {
		console.log(author);
	});
</script>

<div class="max-w-4xl mx-auto">
	<form on:submit={handleSubmit} class="space-y-8">
		<!-- Basic Information -->
		<div class="bg-white dark:bg-[#1a0f0a] rounded-xl shadow-lg border border-neutral-100 dark:border-[#0d0805] p-8">
			<h2 class="text-2xl font-serif font-bold text-neutral-800 dark:text-neutral-100 mb-6 flex items-center gap-3">
				<svg class="w-6 h-6 text-primary-600 dark:text-walnut-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
				</svg>
				Basic Information
			</h2>
			
			<div class="grid md:grid-cols-2 gap-6">
				<div>
					<label for="title" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-2">Recipe Title *</label>
					<input
						id="title"
						class="input-field"
						bind:value={title}
						type="text"
						required
						placeholder="Enter recipe title"
					/>
				</div>

				<div>
					<label for="category" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-2">Category</label>
					<select id="category" class="input-field" bind:value={category}>
						<option value="">Select category</option>
						<option value="breakfast">Breakfast</option>
						<option value="lunch">Lunch</option>
						<option value="dinner">Dinner</option>
						<option value="dessert">Dessert</option>
						<option value="snack">Snack</option>
						<option value="beverage">Beverage</option>
					</select>
				</div>
			</div>

			<div class="mt-6">
				<label for="description" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-2">Description</label>
				<textarea
					id="description"
					class="input-field"
					bind:value={description}
					rows="3"
					placeholder="Describe your recipe..."
				></textarea>
			</div>
		</div>

		<!-- Recipe Details -->
		<div class="bg-white dark:bg-[#0f0805] rounded-xl shadow-lg border border-neutral-100 dark:border-[#080403] p-8">
			<h2 class="text-2xl font-serif font-bold text-neutral-800 dark:text-neutral-100 mb-6 flex items-center gap-3">
				<svg class="w-6 h-6 text-primary-600 dark:text-walnut-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
				</svg>
				Recipe Details
			</h2>
			
			<div class="grid md:grid-cols-3 gap-6">
				<div>
					<label for="serving_size" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-2">Serving Size</label>
					<select id="serving_size" class="input-field" bind:value={serving_size}>
						<option value="">Select serving size</option>
						{#each Array(15) as _, i}
							<option value="{i + 1} person{(i + 1) > 1 ? 's' : ''}">{i + 1} person{(i + 1) > 1 ? 's' : ''}</option>
						{/each}
					</select>
				</div>

				<div>
					<label for="cooking_time" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-2">Cooking Time</label>
					<input
						id="cooking_time"
						class="input-field"
						placeholder="e.g., 2 hours 30 minutes"
						bind:value={cooking_time}
					/>
				</div>

				<div>
					<label for="difficulty" class="block text-sm font-medium text-neutral-700 dark:text-neutral-300 mb-2">Difficulty</label>
					<select id="difficulty" class="input-field" bind:value={difficulty}>
						<option value="">Select difficulty</option>
						<option value="easy">Easy</option>
						<option value="medium">Medium</option>
						<option value="hard">Hard</option>
					</select>
				</div>
			</div>
		</div>

		<!-- Ingredients -->
		<div class="bg-white dark:bg-[#1a0f0a] rounded-xl shadow-lg border border-neutral-100 dark:border-[#0d0805] p-8">
			<div class="flex items-center justify-between mb-6">
				<h2 class="text-2xl font-serif font-bold text-neutral-800 dark:text-neutral-100 flex items-center gap-3">
					<svg class="w-6 h-6 text-primary-600 dark:text-walnut-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
					</svg>
					Ingredients
				</h2>
				<button
					type="button"
					class="btn-secondary flex items-center gap-2"
					on:click={addIngredient}
				>
					<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
					</svg>
					Add Ingredient
				</button>
			</div>

			<div class="space-y-4">
				{#each ingredients as ingredient, index}
					<div class="flex gap-4 items-center">
						<div class="flex-1">
							<input
								class="input-field"
								type="text"
								placeholder="Ingredient name"
								bind:value={ingredients[index].name}
							/>
						</div>
						<div class="flex-1">
							<input
								class="input-field"
								type="text"
								placeholder="Amount"
								bind:value={ingredients[index].amount}
							/>
						</div>
						<button
							type="button"
							class="p-3 text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition-colors duration-200"
							on:click={removeIngredient}
						>
							<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
							</svg>
						</button>
					</div>
				{/each}
			</div>
		</div>

		<!-- Instructions -->
		<div class="bg-white dark:bg-[#0f0805] rounded-xl shadow-lg border border-neutral-100 dark:border-[#080403] p-8">
			<div class="flex items-center justify-between mb-6">
				<h2 class="text-2xl font-serif font-bold text-neutral-800 dark:text-neutral-100 flex items-center gap-3">
					<svg class="w-6 h-6 text-primary-600 dark:text-walnut-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
					</svg>
					Instructions
				</h2>
				<button
					type="button"
					class="btn-secondary flex items-center gap-2"
					on:click={addSteps}
				>
					<svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
					</svg>
					Add Step
				</button>
			</div>

			<div class="space-y-4">
				{#each steps as step, index}
					<div class="flex gap-4 items-start">
						<div class="flex-shrink-0">
							<input
								class="input-field w-20"
								type="number"
								min="1"
								max="100"
								required
								placeholder="Step"
								bind:value={steps[index].step_number}
							/>
						</div>
						<div class="flex-1">
							<textarea
								class="input-field"
								placeholder="Describe this step..."
								required
								rows="2"
								bind:value={steps[index].description}
							></textarea>
						</div>
						<button
							type="button"
							class="p-3 text-red-600 dark:text-red-400 hover:bg-red-50 dark:hover:bg-red-900/20 rounded-lg transition-colors duration-200"
							on:click={subtractStep}
						>
							<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
							</svg>
						</button>
					</div>
				{/each}
			</div>
		</div>

		<!-- Image Upload -->
		<div class="bg-white dark:bg-[#1a0f0a] rounded-xl shadow-lg border border-neutral-100 dark:border-[#0d0805] p-8">
			<h2 class="text-2xl font-serif font-bold text-neutral-800 dark:text-neutral-100 mb-6 flex items-center gap-3">
				<svg class="w-6 h-6 text-primary-600 dark:text-walnut-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path>
				</svg>
				Recipe Image
			</h2>
			
			<div class="border-2 border-dashed border-neutral-300 dark:border-neutral-600 rounded-lg p-8 text-center">
				<svg class="w-12 h-12 text-neutral-400 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
				</svg>
				<div class="text-neutral-600 dark:text-neutral-300 mb-4">
					<label for="file-upload" class="cursor-pointer">
						<span class="font-medium text-primary-600 dark:text-walnut-400 hover:text-primary-500 dark:hover:text-walnut-300">Click to upload</span>
						<span class="text-neutral-500 dark:text-neutral-400"> or drag and drop</span>
					</label>
				</div>
				<p class="text-sm text-neutral-500 dark:text-neutral-400">PNG, JPG, GIF up to 10MB</p>
				<input
					id="file-upload"
					class="hidden"
					type="file"
					accept="image/*"
					on:change={handleFileUpload}
					bind:this={fileInput}
				/>
			</div>
		</div>

		<!-- Submit Button -->
		<div class="flex justify-center">
			<button
				class="btn-primary text-lg px-12 py-4"
				type="submit"
				on:click={() => { showAndHideModal(); }}
			>
				<svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
					<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6"></path>
				</svg>
				Submit Recipe
			</button>
		</div>
	</form>
</div>

<!-- Success Modal -->
<Modal bind:showModal>
	<div class="text-center p-6">
		<div class="w-16 h-16 bg-success-100 rounded-full flex items-center justify-center mx-auto mb-4">
			<svg class="w-8 h-8 text-success-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
				<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
			</svg>
		</div>
		<h2 class="text-2xl font-serif font-bold text-neutral-800 mb-4">
			Recipe Created Successfully!
		</h2>
		<p class="text-neutral-600 mb-6">
			Your recipe has been added to our collection. You'll be redirected to the home page shortly.
		</p>
		<button class="btn-primary" on:click={() => goto('/')}>
			Go to Home
		</button>
	</div>
</Modal>

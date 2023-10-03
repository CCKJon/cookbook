<script>
	// @ts-nocheck

	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	export let data;
	import {
		PUBLIC_CLUSTER_PASSWORD,
		PUBLIC_CLUSTER_IMAGES,
		PUBLIC_CLUSTER_REVIEWS
	} from '$env/static/public';
	import { Spinner } from 'flowbite-svelte';
	import { authStore } from '$lib/stores/authStore';
	import Modal from '$lib/components/Modal.svelte';
	import UpdateRecipe from '$lib/components/UpdateRecipe.svelte';

	let recipe;
	let title = '';
	let description = '';
	let id = data.id;
	let updatedTitle = '';
	let image;
	let reviews;
	let serving_size = '';
	let difficulty = '';
	let cooking_time = '';
	let currentUserID;
	let showUpdateModal = false;
	let review = {};

	authStore.subscribe((curr) => {
		currentUserID = curr?.currentUser?.uid;
		// console.log(currentUserID, 'this is my currentuserid');
	});

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
			// console.log('data', dat);
			return image;
		} catch (error) {
			console.error('Failed to get profile image:', error);
		}
	}

	async function getReview(reviewId) {
		try {
			const response = await fetch(`${PUBLIC_CLUSTER_REVIEWS}/api/review/${reviewId}`, {
				method: 'GET'
			});
			if (!response.ok) {
				throw new Error('Failed to fetch reviews');
			}
			const review = await response.json();
			return review;
		} catch (error) {
			console.error('Failed to get review:', error);
		}
	}

	let recipe_id;

	async function submitReview() {
		review.author = currentUserID;
		review.create_date = new Date();
		review.recipe_id = recipe._id;
		try {
			let response = await fetch(`${PUBLIC_CLUSTER_REVIEWS}/api/review/`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json'
				},

				body: JSON.stringify(review)
			});
			if (!response.ok) {
				throw new Error('Failed to post review');
			} else {
				response = await response.json();
				// console.log(response._id, 'this is my response');
				recipe_id = response._id;
				addRecipeReview();
			}
		} catch (error) {
			console.error('Failed to post review:', error);
		}
	}

	async function addRecipeReview() {
		recipe.review_ids.push(recipe_id);
		console.log(recipe, 'this is addrecipereview recipe ');
		try {
			fetch(`${PUBLIC_CLUSTER_PASSWORD}/api/recipe/${recipe._id}`, {
				method: 'PUT',
				headers: {
					'Content-Type': 'application/json'
				},
				body: JSON.stringify(recipe)
			});
		} catch (error) {
			console.error('Failed to add review to recipe', error);
		}
	}

	onMount(async () => {
		recipe = await getRecipe();
		// console.log(recipe, 'this is my recipe');
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
		{#if recipe.author == currentUserID}
			<button
				on:click={() => {
					showUpdateModal = !showUpdateModal;
				}}
				class="text-gray-300"
				type="button">UPDATE</button
			>
			<Modal bind:showModal={showUpdateModal}>
				<UpdateRecipe {recipe} />
			</Modal>
		{/if}
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
		<div class="flex justify-center">
			<div class="text-gray-300 w-full max-w-[675px]">
				<p class="font-bold text-lg">Submit a review</p>

				<form action="submit" on:submit={submitReview}>
					<label for="title" class="block text-gray-300 mt-4">Title:</label>
					<input
						type="text"
						id="title"
						name="title"
						class="w-full py-2 px-3 rounded-md border border-gray-400 focus:outline-none focus:border-indigo-500"
						required
						bind:value={review.title}
					/>

					<label for="rating" class="block text-gray-300 mt-4">Rating:</label>
					<input
						type="number"
						id="rating"
						name="rating"
						class="w-full py-2 px-3 rounded-md border border-gray-400 focus:outline-none focus:border-indigo-500"
						min="1"
						max="5"
						required
						bind:value={review.rating}
					/>

					<label for="review" class="block text-gray-300 mt-4">Review:</label>
					<textarea
						id="review"
						name="review"
						class="w-full py-2 px-3 rounded-md border border-gray-400 focus:outline-none focus:border-indigo-500"
						rows="4"
						required
						bind:value={review.review}
					/>

					<button
						type="submit"
						class="mt-4 bg-indigo-500 text-white py-2 px-4 rounded-md hover:bg-indigo-600 focus:outline-none"
						>Submit Review</button
					>
				</form>
			</div>
		</div>
		<div class="">
			<div class="flex justify-between py-5 mt-10 px-40 text-gray-300 max-w-[675px] w-full">
				<div class=" w-full max-w-[675px] font-bold text-lg">REVIEWS</div>
				<div>SORT</div>
			</div>
		</div>

		<div class="flex justify-center">
			<div
				class="border-2 border-black px-5 py-5 w-full max-w-[675px] rounded-md bg-gray-900 bg-opacity-90"
			>
				{#each recipe.review_ids as reviewid}
					<div>
						{#await getReview(reviewid)}
							<Spinner color="red" />
						{:then review}
							<div class="flex justify-center py-2">
								<div
									class="w-full max-w-[675px] py-2 px-2 border border-red-900 rounded-md text-gray-300 bg-gray-700 bg-opacity-20"
								>
									<div>Title: {review.title}</div>
									<div>Rating: {review.rating} / 5</div>
									<div>Review: {review.review}</div>
								</div>
							</div>
						{/await}
					</div>
				{/each}
			</div>
		</div>
	{/if}
</div>

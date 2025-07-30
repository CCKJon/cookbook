<script>
	// @ts-nocheck

	import { goto } from '$app/navigation';
	import { onMount } from 'svelte';
	export let data;
	import {
		PUBLIC_CLUSTER_PASSWORD,
		PUBLIC_CLUSTER_IMAGES,
		PUBLIC_CLUSTER_REVIEWS,
		PUBLIC_CLUSTER_USERS
	} from '$env/static/public';
	import { Spinner } from 'flowbite-svelte';
	import { authStore } from '$lib/stores/authStore';
	import Modal from '$lib/components/Modals.svelte';
	import UpdateRecipe from '$lib/components/UpdateRecipe.svelte';
	import Notification from '$lib/components/Notification.svelte';

	let recipe;
	let favorite;
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
	let isNotificationVisible = false;

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

	async function addFavoriteRecipe() {
		const res = await fetch(`${PUBLIC_CLUSTER_USERS}/api/user/${currentUserID}`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json'
			}
		});
		const response_data = await res.json();
		let newuserdata = response_data;
		newuserdata.favorites.push(recipe._id);

		await fetch(`${PUBLIC_CLUSTER_USERS}/api/user/${currentUserID}`, {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(newuserdata)
		});
		isNotificationVisible = true;

		// Automatically hide the notification after a few seconds
		setTimeout(() => {
			isNotificationVisible = false;
		}, 3000); // Adjust the duration (in milliseconds) as needed
	}

	onMount(async () => {
		recipe = await getRecipe();
		console.log(recipe, 'this is my favorites recipe');
		// title = recipe.title;
		// description = recipe.description;
		// due_date = recipe.due_date;
	});
</script>

<div class="min-h-screen bg-gradient-to-br from-neutral-50 to-neutral-100 dark:from-neutral-900 dark:to-neutral-800">
	{#if isNotificationVisible}
		<Notification message="Recipe added to favorites!" />
	{/if}

	{#if recipe}
		<!-- Hero Section -->
		<section class="relative bg-white dark:bg-neutral-800 border-b border-neutral-200 dark:border-neutral-700">
			<div class="container-max px-4 sm:px-6 lg:px-8 py-12">
				<div class="grid lg:grid-cols-2 gap-12 items-center">
					<!-- Recipe Image -->
					<div class="relative">
						{#await getRecipeImage(recipe.images[0].photo_id)}
							<div class="aspect-[4/3] bg-neutral-100 dark:bg-neutral-700 rounded-2xl flex items-center justify-center">
								<Spinner color="primary" size="8" />
							</div>
						{:then imageUrl}
							<div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-2xl">
								<img
									class="w-full h-full object-cover"
									src={URL.createObjectURL(imageUrl)}
									alt={recipe.title}
								/>
							</div>
						{/await}
					</div>

					<!-- Recipe Header -->
					<div class="space-y-6">
						<h1 class="text-4xl md:text-5xl font-serif font-bold text-neutral-800 dark:text-neutral-100 leading-tight">
							{recipe.title}
						</h1>
						
						<p class="text-xl text-neutral-600 dark:text-neutral-300 leading-relaxed">
							{recipe.description}
						</p>

						<!-- Recipe Meta -->
						<div class="grid grid-cols-3 gap-4 py-6">
							<div class="text-center p-4 bg-neutral-50 dark:bg-neutral-700 rounded-xl">
								<div class="text-2xl font-bold text-primary-600 dark:text-walnut-400 mb-1">
									{recipe.serving_size || 'N/A'}
								</div>
								<div class="text-sm text-neutral-600 dark:text-neutral-300">Servings</div>
							</div>
							<div class="text-center p-4 bg-neutral-50 dark:bg-neutral-700 rounded-xl">
								<div class="text-2xl font-bold text-primary-600 dark:text-walnut-400 mb-1">
									{recipe.cooking_time || 'N/A'}
								</div>
								<div class="text-sm text-neutral-600 dark:text-neutral-300">Cook Time</div>
							</div>
							<div class="text-center p-4 bg-neutral-50 dark:bg-neutral-700 rounded-xl">
								<div class="text-2xl font-bold text-primary-600 dark:text-walnut-400 mb-1">
									{recipe.difficulty || 'N/A'}
								</div>
								<div class="text-sm text-neutral-600 dark:text-neutral-300">Difficulty</div>
							</div>
						</div>

						<!-- Action Buttons -->
						<div class="flex flex-col sm:flex-row gap-4">
							{#if $authStore.currentUser}
								<button
									class="btn-primary flex items-center justify-center gap-2"
									type="button"
									on:click={addFavoriteRecipe}
								>
									<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
									</svg>
									Add to Favorites
								</button>
							{/if}

							{#if recipe.author == currentUserID}
								<button
									on:click={() => { showUpdateModal = !showUpdateModal; }}
									class="btn-secondary flex items-center justify-center gap-2"
									type="button"
								>
									<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
										<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>
									</svg>
									Edit Recipe
								</button>
							{/if}
						</div>
					</div>
				</div>
			</div>
		</section>

		<!-- Recipe Content -->
		<section class="section-padding">
			<div class="container-max">
				<div class="grid lg:grid-cols-2 gap-12">
					<!-- Ingredients -->
					<div class="card p-8">
						<h2 class="text-3xl font-serif font-bold text-neutral-800 mb-8 flex items-center gap-3">
							<svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
							</svg>
							Ingredients
						</h2>
						<div class="space-y-4">
							{#each recipe.ingredients as ingredient}
								<div class="flex items-center justify-between p-4 bg-neutral-50 rounded-lg hover:bg-neutral-100 transition-colors duration-200">
									<span class="font-medium text-neutral-800">{ingredient.name}</span>
									<span class="text-neutral-600">{ingredient.amount}</span>
								</div>
							{/each}
						</div>
					</div>

					<!-- Instructions -->
					<div class="card p-8">
						<h2 class="text-3xl font-serif font-bold text-neutral-800 mb-8 flex items-center gap-3">
							<svg class="w-8 h-8 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
							</svg>
							Instructions
						</h2>
						<div class="space-y-6">
							{#each recipe.steps as step}
								<div class="flex gap-4">
									<div class="flex-shrink-0 w-8 h-8 bg-primary-600 text-white rounded-full flex items-center justify-center font-bold text-sm">
										{step.step_number}
									</div>
									<div class="flex-1 pt-1">
										<p class="text-neutral-700 leading-relaxed">{step.description}</p>
									</div>
								</div>
							{/each}
						</div>
					</div>
				</div>
			</div>
		</section>

		<!-- Reviews Section -->
		<section class="section-padding bg-white border-t border-neutral-200">
			<div class="container-max">
				<h2 class="text-3xl font-serif font-bold text-neutral-800 mb-8 text-center">
					Reviews & Ratings
				</h2>

				<!-- Review Form -->
				{#if $authStore.currentUser}
					<div class="card p-8 mb-12 max-w-2xl mx-auto">
						<h3 class="text-2xl font-serif font-semibold text-neutral-800 mb-6">Share Your Experience</h3>
						
						<form on:submit={submitReview} class="space-y-6">
							<div>
								<label for="title" class="block text-sm font-medium text-neutral-700 mb-2">Review Title</label>
								<input
									type="text"
									id="title"
									bind:value={review.title}
									class="input-field"
									required
									placeholder="Give your review a title"
								/>
							</div>

							<div>
								<label for="rating" class="block text-sm font-medium text-neutral-700 mb-2">Rating</label>
								<input
									type="number"
									id="rating"
									bind:value={review.rating}
									class="input-field"
									min="1"
									max="5"
									required
									placeholder="Rate from 1-5"
								/>
							</div>

							<div>
								<label for="review" class="block text-sm font-medium text-neutral-700 mb-2">Your Review</label>
								<textarea
									id="review"
									bind:value={review.review}
									class="input-field"
									rows="4"
									required
									placeholder="Share your thoughts about this recipe..."
								></textarea>
							</div>

							<button type="submit" class="btn-primary w-full">
								Submit Review
							</button>
						</form>
					</div>
				{/if}

				<!-- Reviews List -->
				<div class="space-y-6">
					{#if recipe.review_ids && recipe.review_ids.length > 0}
						{#each recipe.review_ids as reviewid}
							<div>
								{#await getReview(reviewid)}
									<div class="card p-6 flex items-center justify-center">
										<Spinner color="primary" size="6" />
									</div>
								{:then review}
									<div class="card p-6">
										<div class="flex items-start justify-between mb-4">
											<div>
												<h4 class="text-lg font-semibold text-neutral-800 mb-1">{review.title}</h4>
												<div class="flex items-center gap-2">
													<div class="flex items-center">
														{#each Array(5) as _, i}
															<svg class="w-4 h-4 {i < review.rating ? 'text-yellow-400' : 'text-neutral-300'}" fill="currentColor" viewBox="0 0 20 20">
																<path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
															</svg>
														{/each}
													</div>
													<span class="text-sm text-neutral-600">{review.rating}/5</span>
												</div>
											</div>
											<span class="text-sm text-neutral-500">
												{new Date(review.create_date).toLocaleDateString()}
											</span>
										</div>
										<p class="text-neutral-700 leading-relaxed">{review.review}</p>
									</div>
								{/await}
							</div>
						{/each}
					{:else}
						<div class="text-center py-12">
							<div class="w-16 h-16 bg-neutral-100 rounded-full flex items-center justify-center mx-auto mb-4">
								<svg class="w-8 h-8 text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
									<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path>
								</svg>
							</div>
							<h3 class="text-xl font-semibold text-neutral-800 mb-2">No reviews yet</h3>
							<p class="text-neutral-600">Be the first to share your experience with this recipe!</p>
						</div>
					{/if}
				</div>
			</div>
		</section>

		<!-- Update Modal -->
		{#if showUpdateModal}
			<Modal bind:showModal={showUpdateModal}>
				<UpdateRecipe {recipe} />
			</Modal>
		{/if}
	{/if}
</div>

<script>
	//@ts-nocheck
	import { authHandlers, authStore } from '$lib/stores/authStore';
	import AuthReset from '$lib/components/AuthReset.svelte';
	import {
		PUBLIC_CLUSTER_PASSWORD,
		PUBLIC_CLUSTER_IMAGES,
		PUBLIC_CLUSTER_USERS
	} from '$env/static/public';
	import { Dropdown, DropdownItem, DropdownDivider, DropdownHeader } from 'flowbite-svelte';

	let email;
	let image;
	let userid;
	let authored_recipes;
	let showDelete = false;

	authStore.subscribe((curr) => {
		email = curr?.currentUser?.email;
		console.log(curr.currentUser);
		userid = curr?.currentUser?.uid;
	});

	async function getUser() {
		const response = await fetch(`${PUBLIC_CLUSTER_USERS}/api/user/${userid}`);
		const data = await response.json();
		authored_recipes = data.authored_recipes;
		return data;
	}
	async function getRecipe(recipeid) {
		const response = await fetch(`${PUBLIC_CLUSTER_PASSWORD}/api/recipe/${recipeid}`);
		const data = await response.json();
		return data;
	}

	async function deleteRecipe(recipeid) {
		const response = await fetch(`${PUBLIC_CLUSTER_PASSWORD}/api/recipe/${recipeid}`, {
			method: 'DELETE',
			headers: {
				'Content-Type': 'application/json'
			}
		});
	}
	async function deleteAuthoredRecipe(recipeid) {
		console.log(authored_recipes, 'before');
		authored_recipes = authored_recipes.filter((item) => item !== recipeid);
		console.log(authored_recipes, 'after');
		const response = await fetch(`${PUBLIC_CLUSTER_USERS}/api/user/${userid}`, {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				authored_recipes
			})
		});
		await getUser().then((window.location.href = '/privatedashboard'));
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
			const data = await response.blob();
			image = data;
			console.log('data', data);
			return image;
		} catch (error) {
			console.error('Failed to get profile image:', error);
		}
	}
</script>

<div
	class="mx-auto w-11/12 py-7 px-7 h-full bg-[url('$lib/icons/kitchen.jpg')] overflow-hidden bg-no-repeat bg-cover text-gray-300"
>
	This is my favorite recipes page
	{#if $authStore.currentUser}
		<div class="flex flex-row justify-between w-full max-w-[675px] px-20">
			<h1 class="border-2 border-black bg-gray-900 bg-opacity-90 py-2 px-2 rounded-md">
				Current User: {email}
			</h1>
		</div>

		<div>
			<div class="flex flex-row justify-between px-1 py-2">
				<div class="text-sm font-bold font-serif">AUTHORED RECIPES</div>
				<div class="font-serif text-sm font-bold">SORT</div>
			</div>
			{#await getUser()}
				Loading...
			{:then user}
				<!-- {console.log(user, 'this is user')} -->

				{#each user.authored_recipes as recipe}
					{#await getRecipe(recipe)}
						Loading...
					{:then recipedata}
						{@const imageId = recipedata.images[0].photo_id}
						<div
							class="rounded-md bg-gray-800 w-full max-w-[675px] mb-2 py-3 px-3 border-slate-900 border-2 shadow-inner bg-opacity-80"
						>
							<div class="flex flex-row w-full">
								<div class="flex flex-col justify-between w-full">
									<a
										class="mt-1 text-gray-300 flex justify-between w-full min-w-[500px]"
										href={`/${recipedata._id}`}
									>
										<div class="flex items-center justify-start w-1/2 capitalize text-xl ml-2">
											{recipedata.title}
										</div>
										{#await getRecipeImage(imageId)}
											loading ...
										{:then imageUrl}
											<img
												class="w-auto max-h-[200px] object-cover py-3 rounded-md"
												src={URL.createObjectURL(imageUrl)}
												alt=""
											/>
										{/await}
									</a>
									<div class="flex flex-row justify-start">
										<div>
											<button
												type="button"
												on:click={() => {
													showDelete = true;
												}}
												class="text-red-900 text-sm font-bold border rounded-md border-black py-1 px-1 bg-gray-900 w-[65px]"
												>DELETE</button
											>
										</div>
									</div>
									{#if showDelete}
										<button
											type="button"
											class="text-gray-300 text-xs"
											on:click={deleteAuthoredRecipe(recipedata._id)}
											on:click={deleteRecipe(recipedata._id)}>ARE YOU SURE?</button
										>
									{/if}
								</div>
							</div>
						</div>
					{/await}
				{/each}
			{/await}

			<div class="flex justify-center w-full max-w-[675px] py-5">
				<button
					class="border-2 border-black bg-red-900 py-2 px-4 rounded-md bg-opacity-90"
					on:click={authHandlers.logout}>Logout</button
				>
			</div>
		</div>
	{:else}
		<div>Loading....</div>
	{/if}
</div>

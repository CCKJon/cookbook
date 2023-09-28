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
	class="mx-auto w-11/12 h-full py-7 px-7 bg-[url('$lib/icons/dashboard.jpg')] bg-no-repeat bg-cover text-gray-300 flex flex-col gap-10 items-center justify-center"
>
	<div class="h-1">This is where my submitted recipes will go</div>

	<a href="/favoriterecipes">This is where the link to a favorites page will go</a>

	{#if $authStore.currentUser}
		<h1>Current User: {email}</h1>
		<div>
			{#await getUser()}
				Loading...
			{:then user}
				<!-- {console.log(user, 'this is user')} -->
				{#each user.authored_recipes as recipe}
					<div>{recipe}</div>
					{#await getRecipe(recipe)}
						Loading...
					{:then recipedata}
						{@const imageId = recipedata.images[0].photo_id}
						<div
							class="rounded-md bg-gray-800 w-1/2 mb-2 py-3 px-3 border-slate-900 border-2 shadow-inner bg-opacity-60"
						>
							<div class="flex flex-row gap-3">
								<div class="flex flex-row justify-between">
									<a href={`/${recipedata._id}`}>Update</a>
									<button
										type="button"
										on:click={() => {
											showDelete = true;
										}}
										class="text-gray-200 text-xs">DELETE</button
									>
									{#if showDelete}
										<button
											type="button"
											class="text-gray-300 text-xs"
											on:click={deleteAuthoredRecipe(recipedata._id)}
											on:click={deleteRecipe(recipedata._id)}>ARE YOU SURE?</button
										>
									{/if}
								</div>
								<a
									class="mt-1 text-gray-300 flex justify-between w-full"
									href={`/${recipedata._id}`}
								>
									<div class="flex items-center justify-start w-1/2 capitalize text-xl ml-2">
										{recipedata.title}
									</div>
									{#await getRecipeImage(imageId)}
										loading ...
									{:then imageUrl}
										<img
											class="w-auto max-h-[200px] object-cover"
											src={URL.createObjectURL(imageUrl)}
											alt=""
										/>
									{/await}
								</a>
							</div>
						</div>
					{/await}
				{/each}
			{/await}
			<AuthReset />
			<button on:click={authHandlers.logout}>Logout</button>
		</div>
	{:else}
		<div>Loading....</div>
	{/if}
</div>

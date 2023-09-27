<script>
	//@ts-nocheck
	import { authHandlers, authStore } from '$lib/stores/authStore';
	import AuthReset from '$lib/components/AuthReset.svelte';

	let email;
	let userid;

	authStore.subscribe((curr) => {
		email = curr?.currentUser?.email;
		console.log(curr.currentUser);
		userid = curr?.currentUser?.uid;
	});

	async function getUser() {
		const response = await fetch(`http://127.0.0.1:8002/api/user/${userid}`);
		const data = await response.json();
		return data;
	}
	async function getRecipe(recipeid) {
		const response = await fetch(`http://127.0.0.1:8000/api/user/${recipeid}`);
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
			const data = await response.blob();
			image = data;
			console.log('data', data);
			return image;
		} catch (error) {
			console.error('Failed to get profile image:', error);
		}
	}
</script>

<div>This is where my submitted recipes will go</div>

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
							<a class="mt-1 text-gray-300 flex justify-between w-full" href={`/${recipedata._id}`}>
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

<style>
	div {
		flex: 1;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	h1 {
		text-align: center;
	}
</style>

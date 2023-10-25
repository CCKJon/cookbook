import { PUBLIC_CLUSTER_PASSWORD } from '$env/static/public';

async function getRecipes() {
	const response = await fetch(`${PUBLIC_CLUSTER_PASSWORD}/api/recipe`);
	const data = await response.json();
	return data;
}

// let recipes = await getRecipes();

export async function load() {
	return {
		items: await getRecipes()
	};
}

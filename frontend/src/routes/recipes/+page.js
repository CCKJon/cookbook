// This file can be used to load data from your backend API
// For now, we're using static data in the component

/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) {
	// In a real application, you would fetch data from your backend here
	// Example:
	// const response = await fetch('/api/recipes');
	// const recipes = await response.json();
	
	// For now, return empty data since we're using static data in the component
	return {
		recipes: []
	};
} 
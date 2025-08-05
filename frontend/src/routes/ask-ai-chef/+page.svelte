<script>
	import { onMount } from 'svelte';
	import { Button, Textarea, Card, Badge } from 'flowbite-svelte';

	let userPrompt = '';
	let aiResponse = '';
	let isLoading = false;
	let conversationHistory = [];

	// Placeholder AI responses for demonstration
	const placeholderResponses = [
		"I'd be happy to help you with that recipe! Here's a delicious variation that incorporates your ingredients...",
		"Based on your preferences, I'd recommend trying this cooking technique...",
		"That's a great question about cooking! Let me share some tips and a recipe that might work well for you...",
		"I can suggest several ways to modify that recipe to suit your dietary needs...",
		"Here's a step-by-step guide to help you master that cooking technique..."
	];

	function handleSubmit() {
		if (!userPrompt.trim()) return;
		
		isLoading = true;
		
		// Simulate AI processing delay
		setTimeout(() => {
			const randomResponse = placeholderResponses[Math.floor(Math.random() * placeholderResponses.length)];
			aiResponse = randomResponse;
			
			// Add to conversation history
			conversationHistory = [
				...conversationHistory,
				{ type: 'user', content: userPrompt },
				{ type: 'ai', content: aiResponse }
			];
			
			userPrompt = '';
			isLoading = false;
		}, 1500);
	}

	function clearConversation() {
		conversationHistory = [];
		aiResponse = '';
	}

	// Example prompts for inspiration
	const examplePrompts = [
		"How do I make fluffy pancakes from scratch?",
		"What can I cook with chicken, rice, and vegetables?",
		"Help me modify this recipe to be gluten-free",
		"What's the best way to cook salmon?",
		"How do I make homemade pasta sauce?"
	];
</script>

<div class="min-h-screen bg-gradient-to-br from-neutral-50 to-neutral-100 dark:from-neutral-900 dark:to-neutral-800">
	<!-- Header Section -->
	<section class="bg-white dark:bg-neutral-800 border-b border-neutral-200 dark:border-neutral-700">
		<div class="container-max px-4 sm:px-6 lg:px-8 py-12">
			<div class="text-center max-w-4xl mx-auto">
				<div class="flex justify-center mb-6">
					<div class="p-4 bg-primary-100 dark:bg-walnut-800 rounded-full">
						<svg class="w-12 h-12 text-primary-600 dark:text-walnut-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
							<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
						</svg>
					</div>
				</div>
				
				<h1 class="text-4xl md:text-5xl font-serif font-bold text-neutral-800 dark:text-neutral-100 mb-6">
					AI Chef Assistant
				</h1>
				
				<p class="text-xl text-neutral-600 dark:text-neutral-300 mb-8 leading-relaxed">
					Your personal AI cooking companion! Ask me anything about recipes, cooking techniques, 
					ingredient substitutions, or get personalized meal suggestions.
				</p>

				<!-- Feature Cards -->
				<div class="grid md:grid-cols-3 gap-6 mt-12">
					<Card class="text-center border-0 shadow-lg bg-gradient-to-br from-primary-50 to-primary-100 dark:from-walnut-900 dark:to-walnut-800">
						<div class="flex justify-center mb-4">
							<svg class="w-8 h-8 text-primary-600 dark:text-walnut-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path>
							</svg>
						</div>
						<h3 class="text-lg font-semibold text-neutral-800 dark:text-neutral-100 mb-2">
							Recipe Inspiration
						</h3>
						<p class="text-sm text-neutral-600 dark:text-neutral-300">
							Get creative recipe ideas based on ingredients you have or dietary preferences
						</p>
					</Card>

					<Card class="text-center border-0 shadow-lg bg-gradient-to-br from-primary-50 to-primary-100 dark:from-walnut-900 dark:to-walnut-800">
						<div class="flex justify-center mb-4">
							<svg class="w-8 h-8 text-primary-600 dark:text-walnut-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path>
							</svg>
						</div>
						<h3 class="text-lg font-semibold text-neutral-800 dark:text-neutral-100 mb-2">
							Cooking Guidance
						</h3>
						<p class="text-sm text-neutral-600 dark:text-neutral-300">
							Step-by-step instructions and cooking tips for any dish
						</p>
					</Card>

					<Card class="text-center border-0 shadow-lg bg-gradient-to-br from-primary-50 to-primary-100 dark:from-walnut-900 dark:to-walnut-800">
						<div class="flex justify-center mb-4">
							<svg class="w-8 h-8 text-primary-600 dark:text-walnut-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
								<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
							</svg>
						</div>
						<h3 class="text-lg font-semibold text-neutral-800 dark:text-neutral-100 mb-2">
							Smart Substitutions
						</h3>
						<p class="text-sm text-neutral-600 dark:text-neutral-300">
							Find perfect ingredient alternatives for dietary restrictions
						</p>
					</Card>
				</div>
			</div>
		</div>
	</section>

	<!-- Chat Interface Section -->
	<section class="section-padding">
		<div class="container-max">
			<div class="max-w-4xl mx-auto">
				<!-- Example Prompts -->
				<div class="mb-8">
					<h3 class="text-lg font-semibold text-neutral-800 dark:text-neutral-100 mb-4">
						Try asking me about:
					</h3>
					<div class="flex flex-wrap gap-2">
						{#each examplePrompts as prompt}
							<Badge 
								color="primary" 
								class="cursor-pointer hover:bg-primary-700 dark:hover:bg-walnut-600 transition-colors"
								on:click={() => userPrompt = prompt}
							>
								{prompt}
							</Badge>
						{/each}
					</div>
				</div>

				<!-- Chat Interface -->
				<div class="bg-white dark:bg-neutral-800 rounded-2xl shadow-xl border border-neutral-200 dark:border-neutral-700 overflow-hidden">
					<!-- Chat Header -->
					<div class="bg-primary-600 dark:bg-walnut-700 px-6 py-4">
						<div class="flex items-center gap-3">
							<div class="w-3 h-3 bg-green-400 rounded-full animate-pulse"></div>
							<h2 class="text-white font-semibold">AI Chef Assistant</h2>
							<span class="text-primary-200 dark:text-walnut-300 text-sm">Ready to help</span>
						</div>
					</div>

					<!-- Chat Messages -->
					<div class="h-96 overflow-y-auto p-6 space-y-4">
						{#if conversationHistory.length === 0}
							<div class="text-center text-neutral-500 dark:text-neutral-400 py-8">
								<svg class="w-12 h-12 mx-auto mb-4 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
									<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z"></path>
								</svg>
								<p>Start a conversation with your AI Chef!</p>
								<p class="text-sm mt-2">Ask about recipes, cooking tips, or ingredient substitutions</p>
							</div>
						{:else}
							{#each conversationHistory as message}
								<div class="flex {message.type === 'user' ? 'justify-end' : 'justify-start'}">
									<div class="max-w-xs lg:max-w-md px-4 py-3 rounded-2xl {
										message.type === 'user' 
											? 'bg-primary-600 text-white' 
											: 'bg-neutral-100 dark:bg-neutral-700 text-neutral-800 dark:text-neutral-100'
									}">
										<p class="text-sm leading-relaxed">{message.content}</p>
									</div>
								</div>
							{/each}
						{/if}

						{#if isLoading}
							<div class="flex justify-start">
								<div class="max-w-xs lg:max-w-md px-4 py-3 rounded-2xl bg-neutral-100 dark:bg-neutral-700">
									<div class="flex items-center gap-2">
										<div class="w-2 h-2 bg-neutral-400 rounded-full animate-bounce"></div>
										<div class="w-2 h-2 bg-neutral-400 rounded-full animate-bounce" style="animation-delay: 0.1s"></div>
										<div class="w-2 h-2 bg-neutral-400 rounded-full animate-bounce" style="animation-delay: 0.2s"></div>
									</div>
								</div>
							</div>
						{/if}
					</div>

					<!-- Input Area -->
					<div class="border-t border-neutral-200 dark:border-neutral-700 p-4">
						<form on:submit|preventDefault={handleSubmit} class="flex gap-3">
							<Textarea
								bind:value={userPrompt}
								placeholder="Ask me anything about cooking, recipes, or ingredients..."
								class="flex-1 resize-none"
								rows="2"
								disabled={isLoading}
							/>
							<Button 
								type="submit" 
								color="primary" 
								disabled={!userPrompt.trim() || isLoading}
								class="self-end"
							>
								{#if isLoading}
									<div class="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
								{:else}
									Send
								{/if}
							</Button>
						</form>
						
						{#if conversationHistory.length > 0}
							<div class="mt-3 flex justify-end">
								<Button 
									color="light" 
									size="xs" 
									on:click={clearConversation}
								>
									Clear Conversation
								</Button>
							</div>
						{/if}
					</div>
				</div>

				<!-- Information Section -->
				<div class="mt-8 bg-gradient-to-r from-primary-50 to-walnut-50 dark:from-walnut-900 dark:to-primary-900 rounded-xl p-6">
					<h3 class="text-lg font-semibold text-neutral-800 dark:text-neutral-100 mb-3">
						About AI Chef
					</h3>
					<p class="text-neutral-600 dark:text-neutral-300 text-sm leading-relaxed">
						This AI assistant is designed to help you with all aspects of cooking. It can provide recipe suggestions, 
						cooking techniques, ingredient substitutions, and answer your culinary questions. The AI is trained on 
						thousands of recipes and cooking knowledge to provide accurate and helpful responses.
					</p>
					<div class="mt-4 flex flex-wrap gap-2">
						<Badge color="primary">Recipe Suggestions</Badge>
						<Badge color="primary">Cooking Tips</Badge>
						<Badge color="primary">Ingredient Substitutions</Badge>
						<Badge color="primary">Dietary Modifications</Badge>
						<Badge color="primary">Technique Guidance</Badge>
					</div>
				</div>
			</div>
		</div>
	</section>
</div>

<style>
	.container-max {
		max-width: 1200px;
		margin: 0 auto;
	}
	
	.section-padding {
		padding: 4rem 0;
	}
	
	/* Custom scrollbar for chat */
	.overflow-y-auto::-webkit-scrollbar {
		width: 6px;
	}
	
	.overflow-y-auto::-webkit-scrollbar-track {
		background: transparent;
	}
	
	.overflow-y-auto::-webkit-scrollbar-thumb {
		background: #d1d5db;
		border-radius: 3px;
	}
	
	.overflow-y-auto::-webkit-scrollbar-thumb:hover {
		background: #9ca3af;
	}
	
	.dark .overflow-y-auto::-webkit-scrollbar-thumb {
		background: #4b5563;
	}
	
	.dark .overflow-y-auto::-webkit-scrollbar-thumb:hover {
		background: #6b7280;
	}
</style> 
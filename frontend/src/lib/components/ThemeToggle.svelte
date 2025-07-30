<script>
    import { currentTheme, toggleTheme } from '$lib/stores/themeStore';
</script>

<!-- Theme Toggle Button -->
<button
    on:click={toggleTheme}
    class="fixed bottom-6 right-6 z-50 p-3 rounded-full shadow-lg transition-all duration-300 hover:scale-110 group"
    class:bg-walnut-700={$currentTheme === 'dark'}
    class:bg-primary-600={$currentTheme === 'light'}
    class:text-neutral-100={$currentTheme === 'dark'}
    class:text-white={$currentTheme === 'light'}
    class:hover:bg-walnut-800={$currentTheme === 'dark'}
    class:hover:bg-primary-700={$currentTheme === 'light'}
    title="Toggle theme"
>
    <!-- Sun icon for dark theme (click to switch to light) -->
    {#if $currentTheme === 'dark'}
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path>
        </svg>
    {:else}
        <!-- Moon icon for light theme (click to switch to dark) -->
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>
        </svg>
    {/if}
</button>

<style>
    /* Add a subtle pulse animation */
    button {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% {
            opacity: 1;
        }
        50% {
            opacity: 0.8;
        }
    }
</style> 
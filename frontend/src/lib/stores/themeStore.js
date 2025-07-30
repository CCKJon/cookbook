import { writable } from 'svelte/store';

// Create a writable store for the theme
export const currentTheme = writable('dark'); // Default to dark theme

// Theme toggle function
export function toggleTheme() {
    currentTheme.update(theme => {
        const newTheme = theme === 'dark' ? 'light' : 'dark';
        // Store the theme preference in localStorage
        if (typeof window !== 'undefined') {
            localStorage.setItem('theme', newTheme);
        }
        return newTheme;
    });
}

// Initialize theme from localStorage
export function initializeTheme() {
    if (typeof window !== 'undefined') {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme) {
            currentTheme.set(savedTheme);
        }
    }
} 
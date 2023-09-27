//@ts-nocheck
import {
	PUBLIC_CLUSTER_PASSWORD,
	PUBLIC_CLUSTER_IMAGES,
	PUBLIC_CLUSTER_USERS
} from '$env/static/public';
import { writable, derived } from 'svelte/store';
import { auth } from '$lib/firebase/firebase.client';
import {
	signInWithEmailAndPassword,
	updateEmail,
	updatePassword,
	signOut,
	createUserWithEmailAndPassword,
	sendPasswordResetEmail,
	sendEmailVerification
	// updateCurrentUser
} from 'firebase/auth';

export const authStore = writable({
	isLoading: true,
	currentUser: null
});

export const authHandlers = {
	login: async (email, password) => {
		await signInWithEmailAndPassword(auth, email, password);
	},
	signup: async (email, password) => {
		const newUserCredential = await createUserWithEmailAndPassword(auth, email, password);
		console.log('this is the new user credential', newUserCredential);

		const newUser = {
			username: email,
			firebase_reference_id: newUserCredential.user.uid,
			authored_recipes: [],
			favorites: [],
			profile_photo: '',
			profile_description: ''
		};

		fetch(`${PUBLIC_CLUSTER_USERS}/api/user`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify(newUser)
		}).catch(() => {
			return {
				status: 301,
				error: new Error('Could not create a new todo')
			};
		});

		await sendEmailVerification(newUserCredential.user);
	},
	logout: async () => {
		await signOut(auth);
	},
	resetPassword: async (email) => {
		if (!email) {
			return;
		}
		await sendPasswordResetEmail(auth, email);
	},
	updateEmail: async (email) => {
		console.log('before updating email in authstore', auth.currentUser, email);
		// auth.currentUser.emailVerified = true; // on the good account, it still shows up as false?
		// console.log('this is my current user', auth.currentUser);
		await updateEmail(auth.currentUser, email).then(() => {
			authStore.update((curr) => {
				return {
					...curr,
					currentUser: {
						...curr.currentUser,
						email: email
					}
				};
			});
		});
	},
	updatePassword: async (password) => {
		await updatePassword(auth.currentUser, password);
	}
};

export const isLoggedIn = derived(authStore, ($authStore) => {
	if ($authStore.currentUser != null) {
		return true;
	} else {
		return false;
	}
});

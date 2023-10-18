<!-- Notification.svelte -->
<script>
	export let message;
</script>

<div class="notification">{message}</div>

<style>
	.notification {
		position: fixed;
		bottom: 20px;
		right: 20px;
		background-color: #333;
		color: white;
		padding: 10px 20px;
		border-radius: 5px;
	}
</style>

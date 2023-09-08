<script>
	import logo from '$lib/icons/logo.png';
</script>

<div class="px-5 py-2 flex flex-row items-center justify-between bg-[#0F0F0F] w-11/12 mx-auto">
	<a href="/"><img class="h-16 w-auto" src={logo} alt="logo" /></a>
	<div class="flex gap-5">
		<a class="text-gray-300 font-serif" href="/login">Login</a>
		<a class="text-gray-300 font-serif" href="/recipe-list">Recipes</a>
		<a class="text-gray-300 font-serif" href="/new-recipe">Submit</a>
		<div class="text-gray-300 font-serif">Search</div>
	</div>
</div>

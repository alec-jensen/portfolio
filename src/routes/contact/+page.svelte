<script>
	import KBNav from '$lib/KBNav.svelte';
</script>

<KBNav />

<svelte:head>
	<title>Contact</title>
	<meta name="description" content="Contact Alec Jensen" />
</svelte:head>

<div class="text-column">
	<h1><rainbow>Contact</rainbow> me</h1>

	<a href="mailto:alec@alecj.tk" target="_blank">Email</a>
	<a href="https://github.com/alec-jensen" target="_blank">GitHub</a>
	<a href="https://discord.com/users/766373301169160242" target="_blank">Discord</a>
	<a href="https://youtube.com/@alec.j" target="_blank">YouTube</a>
</div>

<style>
	a {
		text-align: center;
		font-size: 1.5rem;
		color: white;
		text-decoration: none;
		padding: 0.5em 2em;
		background-color: var(--color-theme-2);
		transition: background-color 0.2s ease-in-out;
		border-radius: 10px;
		margin: 0.4em;
	}

	a:hover {
		background-color: var(--color-theme-1);
		transition: background-color 0.2s ease-in-out;
	}
</style>

<script>
	let tool_width = 80;
	let tool_height = 80;
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<h1>Hi, I'm <name>Alec Jensen</name></h1>
	<h2>fullstack developer</h2>
	<h3>c++/python/java/js/ts</h3>

	<!-- <h2>
	<a href="/about">About me</a>
	</h2> -->
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	name {
		background: radial-gradient(circle at 24.01% 70.97%, #3d60c0, transparent 76%),radial-gradient(circle at 86.98% 7.01%, #2ce5d6, transparent 93%),radial-gradient(circle at 41.98% 69.97%, #5e3541, transparent 36%),radial-gradient(circle at 16.98% 38.04%, #7de590, transparent 6%),radial-gradient(circle at 84.01% 88.99%, #112322, transparent 23%),radial-gradient(circle at 50% 50%, #eeb4c5, #eeb4c5 100%);
		background-clip: text;
		-webkit-background-clip: text;
		color: transparent;
		-webkit-text-fill-color: transparent;
	}

	h1 {
		width: 100%;
		font-size: 80px;
	}

	h2 {
		font-size: 30px;
	}

	h3 {
		font-weight: 200;
	}
</style>

<script>
	import { page } from '$app/stores';
	import logo from '$lib/images/svelte-logo.svg';
	import github from '$lib/images/github.svg';
</script>

<link
	rel="stylesheet"
	href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200"
/>

<header>
	<nav>
		<!-- <div class="corner">
		<a href="https://kit.svelte.dev">
			<img src={logo} alt="SvelteKit" />
		</a>
	</div> -->
		<ul>
			<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/"><span class="material-symbols-outlined">home</span></a>
			</li>
			<li aria-current={$page.url.pathname === '/about' ? 'page' : undefined}>
				<a href="/about"><span class="material-symbols-outlined">person</span></a>
			</li>
			<li aria-current={$page.url.pathname === '/projects' ? 'page' : undefined}>
				<a href="/projects"><span class="material-symbols-outlined">code</span></a>
			</li>
			<li aria-current={$page.url.pathname === '/contact' ? 'page' : undefined}>
				<a href="/contact"><span class="material-symbols-outlined">mail</span></a>
			</li>
		</ul>
		<!-- <div class="corner">
		<a href="https://github.com/sveltejs/kit">
			<img src={github} alt="GitHub" />
		</a>
	</div> -->
	</nav>
</header>

<style>
	header {
		display: flex;
		justify-content: center;
	}

	nav .corner {
		width: 3em;
		height: 3em;
	}

	nav .corner a {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		height: 100%;
	}

	nav .corner img {
		width: 2.5em;
		height: 2.5em;
		object-fit: contain;
	}

	nav {
		display: flex;
		justify-content: center;
		--background: rgba(255, 255, 255, 0.068);
		backdrop-filter: blur(10px) brightness(60%);
		background: var(--background);
		background-size: contain;
		position: fixed;
		top: 0;
		z-index: 9999999999;
		border-bottom: 0.5px solid rgb(75, 75, 75);
		border-left: 0.5px solid rgb(75, 75, 75);
		border-right: 0.5px solid rgb(75, 75, 75);
		border-bottom-left-radius: 10px;
		border-bottom-right-radius: 10px;
	}

	ul {
		position: relative;
		padding: 0;
		margin: 0;
		height: 3em;
		width: 100%;
		display: flex;
		justify-content: center;
		align-items: center;
		list-style: none;
	}

	li {
		position: relative;
		height: 100%;
		padding: 0 2rem;
		border-radius: 10px;
	}

	li:hover {
		background: var(--color-bg-2);
	}

	li[aria-current='page'] a {
		color: var(--color-theme-1);
	}

	nav a {
		display: flex;
		height: 100%;
		align-items: center;
		padding: 0 0rem;
		color: var(--color-text);
		font-weight: 700;
		font-size: 0.8rem;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: color 0.2s linear;
	}

	a:hover {
		color: var(--color-theme-1);
	}

	@media (max-width: 720px) {
		nav {
			border-bottom-left-radius: 0;
			border-bottom-right-radius: 0;
			border-top-right-radius: 10px;
			border-top-left-radius: 10px;

			top: unset;
			bottom: 0;

			border-top: 0.5px solid rgb(75, 75, 75);
			border-left: 0.5px solid rgb(75, 75, 75);
			border-right: 0.5px solid rgb(75, 75, 75);
		}

		li:hover {
			background: unset;
		}
	}
</style>

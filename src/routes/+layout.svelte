<script>
	import Header from './Header.svelte';
	import './styles.css';
	import { onNavigate } from '$app/navigation';
	import { goto } from '$app/navigation';

	onNavigate((navigation) => {
		if (!document.startViewTransition) return;

		return new Promise((resolve) => {
			document.startViewTransition(async () => {
				resolve();
				await navigation.complete;
			});
		});
	});

	function handleKeydown(event) {
		if (event.shiftKey || event.ctrlKey || event.altKey || event.metaKey) {
			return;
		}

		if (event.key === 'h') {
			goto('/');
		} else if (event.key === 'a') {
			goto('/about');
		} else if (event.key === 'p') {
			goto('/projects');
		} else if (event.key === 'c') {
			goto('/contact');
		}
	}
</script>

<svelte:window on:keydown={handleKeydown} />

<div class="app">
	<Header />

	<main>
		<slot />
	</main>

	<footer>
		<p>&copy; Alec Jensen 2023-{new Date().getFullYear()}</p>
		<div class="footer-links">
			<a href="/terms">Terms</a> • <a href="/privacy">Privacy</a> • <a href="/security">Security</a>
		• <a href="/legal">Legal</a> • <a href="https://status.alecj.com">Status</a>
		</div>
	</footer>
</div>

<style>
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
		width: 100%;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		box-sizing: border-box;
		align-items: center;
		justify-content: center;
		margin: auto;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 6px;
	}

	footer p {
		font-family: var(--font-mono);
	}

	.footer-links {
		font-size: 0.9em;
		text-align: center;
		color: lightgray;
	}

	@media (min-width: 480px) {
		footer {
			padding: 6px 0;
		}
	}

	@media (max-width: 720px) {
		footer {
			margin-bottom: 3em;
		}
	}
</style>

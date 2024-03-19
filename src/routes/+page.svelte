<script>
	import { onMount } from 'svelte';
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';

	let descriptions = [
		'fullstack developer',
		'videographer',
		'photographer',
		'backend developer',
		'frontend developer'
	];

	let description = descriptions[Math.floor(Math.random() * descriptions.length)];

	let prev = '';

	let rendered_description = '';

	/** shut up vscode
	 * @param {number} min
	 * @param {number} max
	 */
	function randRange(min, max) {
		return Math.floor(Math.random() * (max - min + 1) + min);
	}

	// im sorry to anyone who has to read this

	onMount(() => {
		// typewriter effect

		function typewriter() {
			while (prev == description) {
				description = descriptions[Math.floor(Math.random() * descriptions.length)];
			}

			prev = description;

			let i = 0;
			function _typeWriter() {
				if (i < description.length) {
					rendered_description = description.substring(0, i + 1);
					i++;
					setTimeout(_typeWriter, randRange(30, 70));
				} else {
					setTimeout(run, 3000);
				}
			}

			_typeWriter();
		}

		function run() {
			function _delete() {
				if (rendered_description.length > 0) {
					rendered_description = rendered_description.substring(0, rendered_description.length - 1);
					setTimeout(_delete, randRange(30, 70));
				} else {
					typewriter();
				}
			}

			_delete();
		}

		run();
	});

	function handleKeydown(event) {
		console.log(event.key);
		if (event.key === 'a') {
			goto('/about');
		} else if (event.key === 'p') {
			goto('/projects');
		} else if (event.key === 'c') {
			goto('/contact');
		}
	}
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Alec Jensen portfolio" />
</svelte:head>

<section>
	<h1>Hi, I'm <br><name>Alec Jensen</name></h1>
	<div class="skills">
		<h2 class="code">{rendered_description}<span class="blinking-cursor">_</span></h2>
	</div>
	<h3 class="code">python/java/js</h3>

	<ul>
		<li>
			<a href="/about"><u>a</u>bout</a>
		</li>
		<li class="seperator">
			<p>-</p>
		</li>
		<li>
			<a href="/projects"><u>p</u>rojects</a>
		</li>
		<li class="seperator">
			<p>-</p>
		</li>
		<li>
			<a href="/contact"><u>c</u>ontact</a>
		</li>
	</ul>
</section>

<svelte:window on:keydown={handleKeydown} />

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	name {
		background: radial-gradient(circle at 24.01% 70.97%, #3d60c0, transparent 76%),
			radial-gradient(circle at 86.98% 7.01%, #2ce5d6, transparent 93%),
			radial-gradient(circle at 41.98% 69.97%, #5e3541, transparent 36%),
			radial-gradient(circle at 16.98% 38.04%, #7de590, transparent 6%),
			radial-gradient(circle at 84.01% 88.99%, #112322, transparent 23%),
			radial-gradient(circle at 50% 50%, #eeb4c5, #eeb4c5 100%);
		background-clip: text;
		-webkit-background-clip: text;
		color: transparent;
		-webkit-text-fill-color: transparent;
	}

	h1 {
		width: 100%;
		font-size: 80px;
		margin: unset;
	}

	h2 {
		font-size: 30px;
		min-height: 36px;
	}

	h3 {
		font-weight: 200;
	}

	a {
		text-align: center;
		font-size: 1.5rem;
		color: var(--color-theme-1);
		text-shadow: 0 0 0.5em var(--color-theme-1);
		text-decoration: none;
		transition: all 0.2s ease-in-out;
		border-radius: 10px;
	}

	a:hover {
		text-shadow: none;
		text-decoration: underline;
	}

	ul {
		display: flex;
		flex-direction: row;
		justify-content: center;
		align-items: center;
		list-style: none;
		padding: 0;
	}

	li {
		margin: 0.5em;
	}

	.seperator {
		position: relative;
		top: 0.1em;
	}

	@media (max-width: 768px) {
		h1 {
			font-size: 60px;
		}

		h2 {
			font-size: 20px;
			min-height: 30px;
		}

		h3 {
			font-size: 15px;
		}
	}

	.code {
		font-family: var(--font-mono);
	}

	.skills {
		padding: none;
		background: var(--color-bg-2);
		border: 1px solid var(--color-border);
		border-radius: 10px;
	}

	.skills h2 {
		padding: 0.25em 0.5em;
		margin: 0 0 0 0;
	}

	.blinking-cursor {
		margin-left: 0.1em;
		font-weight: 100;
		font-size: 30px;
		color: #2e3d48;
		-webkit-animation: 1s blink step-end infinite;
		-moz-animation: 1s blink step-end infinite;
		-ms-animation: 1s blink step-end infinite;
		-o-animation: 1s blink step-end infinite;
		animation: 1s blink step-end infinite;
	}

	@keyframes blink {
		from,
		to {
			color: transparent;
		}
		50% {
			color: var(--color-text);
		}
	}

	@-moz-keyframes blink {
		from,
		to {
			color: transparent;
		}
		50% {
			color: var(--color-text);
		}
	}

	@-webkit-keyframes blink {
		from,
		to {
			color: transparent;
		}
		50% {
			color: var(--color-text);
		}
	}

	@-ms-keyframes blink {
		from,
		to {
			color: transparent;
		}
		50% {
			color: var(--color-text);
		}
	}

	@-o-keyframes blink {
		from,
		to {
			color: transparent;
		}
		50% {
			color: var(--color-text);
		}
	}
</style>

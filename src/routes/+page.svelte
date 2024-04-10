<script>
	import { onMount } from 'svelte';
	import KBNav from '$lib/KBNav.svelte';

	let descriptions = [
		'fullstack developer',
		'videographer',
		'photographer',
		'backend developer',
		'frontend developer',
		'ml/dl developer',
		'game developer',
		'violist',
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
</script>

<KBNav />

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Alec Jensen portfolio" />
</svelte:head>

<section>
	<h1>Hi, I'm <br /><rainbow>Alec Jensen</rainbow></h1>
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

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	rainbow {
		font-size: 100px;
		font-weight: bold;
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
		text-align: center;
	}

	.blinking-cursor {
		margin-left: 0.1em;
		font-weight: 100;
		font-size: 30px;
		color: white;
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

<script>
	import { onMount } from 'svelte';

	onMount(() => {
		'use strict';

		// define variables
		var items = document.querySelectorAll('.timeline li');

		// check if an element is in viewport
		// http://stackoverflow.com/questions/123999/how-to-tell-if-a-dom-element-is-visible-in-the-current-viewport
		function isElementInViewport(el) {
			var rect = el.getBoundingClientRect();
			return (
				rect.top >= 0 &&
				rect.left >= 0 &&
				rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
				rect.right <= (window.innerWidth || document.documentElement.clientWidth)
			);
		}

		function callbackFunc() {
			for (var i = 0; i < items.length; i++) {
				if (isElementInViewport(items[i])) {
					items[i].classList.add('in-view');
				}
			}
		}

		// listen for events
		window.addEventListener('load', callbackFunc);
		window.addEventListener('resize', callbackFunc);
		window.addEventListener('scroll', callbackFunc);
	});
</script>

<svelte:head>
	<title>About</title>
	<meta name="description" content="Information about me" />
</svelte:head>

<div class="text-column">
	<h1>About me</h1>

	<p>
		I am Alec Jensen, a software developer from the United States. I have been programming since
		2018, starting with C on an Arduino Uno. I have since learned C++, Python, Java, JavaScript,
		TypeScript, Svelte and SvelteKit.
	</p>

	<!-- <pre>npm create svelte@latest</pre> -->

	<p>
		I enjoy making cool projects using the technologies I have learned, and learning new ones to do
		even more cool stuff!
	</p>

	<p>
		Outside of programming, I enjoy playing the viola, flying my drone, and making youtube videos. I
		also enjoy playing video games, my favorite being Minecraft. I am in the computer science club
		and roboboat club at my school.
	</p>
</div>

<!--<p style="color: gray;"><em>(scroll down)</em></p>-->

<style>
	p {
		font-size: 18px;
		text-align: center;
	}

	@media (min-width: 768px) {
		.text-column {
			padding-top: 24vh;
			padding-bottom: 14vh;
		}
	}

	@media (max-width: 768px) {
		.text-column {
			padding-top: 10vh;
			padding-bottom: 10vh;
		}
	}
</style>

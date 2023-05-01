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

<p style="color: gray;"><em>(scroll down)</em></p>

<section class="timeline">
	<ul>
		<li>
			<div>
				<time>2018</time> Started learning C on an Arduino Uno
			</div>
		</li>
		<li>
			<div>
				<time>2020</time> I learned Python and discord.py to start making Discord bots
			</div>
		</li>
		<li>
			<div>
				<time>2021</time> Learned Java and the Spigot API so I could make Minecraft plugins
			</div>
		</li>
		<li>
			<div>
				<time>2022</time> Joined robotics club at school and learned C++ to program the robot
			</div>
		</li>
		<li>
			<div>
				<time>2023</time> Participated in my first Hackathon at school and placed 4th overall
			</div>
		</li>
		<li>
			<div>
				<time>2023</time> Got into web dev and learned HTML, CSS, JavaScript, and TypeScript (Svelte
				& SvelteKit)
			</div>
		</li>
	</ul>
</section>

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

	.timeline ul li {
		list-style-type: none;
		position: relative;
		width: 6px;
		margin: 0 auto;
		padding-top: 50px;
		background: #fff;
		color: rgb(247, 243, 243);
	}

	.timeline ul li::after {
		content: '';
		position: absolute;
		left: 50%;
		bottom: 0;
		transform: translateX(-50%);
		width: 30px;
		height: 30px;
		border-radius: 50%;
		background: inherit;
		z-index: 1;
	}

	.timeline ul li div {
		position: relative;
		bottom: 0;
		width: 400px;
		padding: 15px;
		background: rgb(46, 45, 45);
	}

	.timeline ul li div::before {
		content: '';
		position: absolute;
		bottom: 7px;
		width: 0;
		height: 0;
		border-style: solid;
	}

	.timeline ul li:nth-child(odd) div {
		left: 45px;
	}

	.timeline ul li:nth-child(odd) div::before {
		left: -15px;
		border-width: 8px 16px 8px 0;
		border-color: transparent rgb(46, 45, 45) transparent transparent;
	}

	.timeline ul li:nth-child(even) div {
		right: 470px;
	}

	.timeline ul li:nth-child(even) div::before {
		right: -15px;
		border-width: 8px 0 8px 16px;
		border-color: transparent transparent transparent rgb(46, 45, 45);
	}

	time {
		display: block;
		font-size: 1.2rem;
		font-weight: bold;
		margin-bottom: 8px;
	}

	.timeline ul li::after {
		transition: background 0.5s ease-in-out;
	}

	.timeline ul li div {
		visibility: hidden;
		opacity: 0;
		transition: all 400ms cubic-bezier(0.47, 1.64, 0.41, 0.8);
	}

	.timeline ul li:nth-child(odd) div {
		transform: translate3d(200px, 0, 0);
	}

	.timeline ul li:nth-child(even) div {
		transform: translate3d(-200px, 0, 0);
	}

	.timeline ul li.in-view div {
		transform: none;
		visibility: visible;
		opacity: 1;
	}

	@media screen and (max-width: 768px) {
		.timeline ul li {
			margin-left: 20px;
			margin-right: 0px;
		}
		.timeline ul li div {
			width: calc(70vw - 91px);
		}
		.timeline ul li:nth-child(even) div {
			left: 45px;
		}
		.timeline ul li:nth-child(even) div::before {
			left: -15px;
			border-width: 8px 16px 8px 0;
			border-color: transparent rgb(46, 45, 45) transparent transparent;
		}
	}

	.timeline-clippy ul li::after {
		width: 40px;
		height: 40px;
		border-radius: 0;
	}

	.timeline-rhombus ul li::after {
		clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
	}

	.timeline-rhombus ul li div::before {
		bottom: 12px;
	}

	.timeline-star ul li::after {
		clip-path: polygon(
			50% 0%,
			61% 35%,
			98% 35%,
			68% 57%,
			79% 91%,
			50% 70%,
			21% 91%,
			32% 57%,
			2% 35%,
			39% 35%
		);
	}

	.timeline-heptagon ul li::after {
		clip-path: polygon(50% 0%, 90% 20%, 100% 60%, 75% 100%, 25% 100%, 0% 60%, 10% 20%);
	}

	.timeline-infinite ul li::after {
		animation: scaleAnimation 2s infinite;
	}

	@keyframes scaleAnimation {
		0% {
			transform: translateX(-50%) scale(1);
		}
		50% {
			transform: translateX(-50%) scale(1.25);
		}
		100% {
			transform: translateX(-50%) scale(1);
		}
	}
</style>

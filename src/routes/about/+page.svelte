<svelte:head>
	<title>About</title>
	<meta name="description" content="Information about me" />
</svelte:head>

<div class="text-column">
	<h1>About me</h1>

	<p>
		I am Alec Jensen, a software developer from the United States. I have been programming since
		2018, starting with C on an Arduino Uno. I have since learned C++, Python, Java, JavaScript,
		Svelte and SvelteKit.
	</p>

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

<svelte:head>
	<title>About</title>
	<meta name="description" content="Information about me" />
</svelte:head>

<div class="text-column">
	<h1><rainbow>About</rainbow> me</h1>

	<p>
		I am Alec Jensen, a software developer from the United States. I have been programming since
		2018, starting with C on an Arduino Uno. I have since learned C++, Python, Java, JavaScript,
		Svelte/SvelteKit, and Astro.
	</p>

	<p>
		I enjoy making cool projects using the technologies I have learned, and learning new ones to do
		even more cool things!
	</p>

	<p>
		Outside of programming, I enjoy playing the viola, flying my drone, and making YouTube videos. I
		also enjoy playing video games, my favorite being Minecraft. I am in the computer science club
		and Roboboat club at my school.
	</p>

	<div class="abuseipdb">
		<a
			href="https://www.abuseipdb.com/user/75358"
			title="AbuseIPDB is an IP address blacklist for webmasters and sysadmins to report IP addresses engaging in abusive behavior on their networks"
		>
			<img
				src="https://www.abuseipdb.com/contributor/75358.svg"
				alt="AbuseIPDB Contributor Badge"
				style="width: 381px;border-radius: 5px; border-top: 5px solid #058403; border-right: 5px solid #111; border-bottom: 5px solid #111; border-left: 5px solid #058403; padding: 5px;background: #35c246 linear-gradient(rgba(255,255,255,0), rgba(255,255,255,.3) 50%, rgba(0,0,0,.2) 51%, rgba(0,0,0,0)); padding: 5px;"
			/>
		</a>
	</div>
</div>

<style>
	p {
		font-size: 1.2em;
		text-align: center;
		color: lightgray;
		line-height: 175%;
	}

	.abuseipdb {
		display: flex;
		justify-content: center;
		margin-top: 2em;
	}
</style>

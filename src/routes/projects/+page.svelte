<svelte:head>
	<title>About</title>
	<meta name="description" content="Information about me" />
</svelte:head>

<div class="page">
	<h1>My <rainbow>Projects</rainbow></h1>

	<div class="projects">
		<div class="project_card">
			<!-- <img class="project_card__image" src="/images/kidney-bot.png" alt="kidney-bot" /> -->

			<div class="project_card__header">
				<h2>kidney bot</h2>
				<p>
					kidney bot is an open source discord bot designed to help effectively moderate
					communities, while at the same time keeping privacy paramout.
				</p>

				<div class="project_card__links">
					<a href="https://kidneybot.alecj.tk" target="_blank">Website</a>
					<a href="https://github.com/alec-jensen/kidney-bot" target="_blank">Github</a>
				</div>
			</div>
		</div>

		<div class="project_card">
			<!-- <img class="project_card__image" src="/images/generalutils.png" alt="generalutils" /> -->

			<div class="project_card__header">
				<h2>GeneralUtils</h2>
				<p>
					GeneralUtils is a no-bs spigot plugin designed to replace Essentials, while doing exactly
					what is asked of it and nothing more.
				</p>

				<div class="project_card__links">
					<a href="https://github.com/alec-jensen/generalutils" target="_blank">Github</a>
				</div>
			</div>
		</div>

		<div class="project_card">
			<!-- <img class="project_card__image" src="/images/firescript.png" alt="firescript" /> -->

			<div class="project_card__header">
				<h2>firescript</h2>
				<p>
					firescript is a work in progress programming language that can be compiled natively or to JavaScript,
					designed for use in the web. It is strongly & statically typed, and the major philosophy
					is "simplicity through explicit design".
				</p>

				<div class="project_card__links">
					<a href="https://github.com/alec-jensen/firescript" target="_blank">Github</a>
				</div>
			</div>
		</div>

		<div class="project_card">
			<!-- <img class="project_card__image" src="" alt="" /> -->

			<div class="project_card__header">
				<h2>NoteAI</h2>
				<p>
					NoteAI is a tool designed to help students enforce what they have already learned, improving grades and helping them to learn more effectively.
				</p>

				<div class="project_card__links">
					<a href="https://github.com/alec-jensen/NoteAI" target="_blank">Github</a>
				</div>
			</div>
		</div>

		<div class="project_card">
			<!-- <img class="project_card__image" src="" alt="" /> -->

			<div class="project_card__header">
				<h2>EnhancedInput</h2>
				<p>
					EnhancedInput is a python library designed to make it easier to get input from the user, and to validate that input.
				</p>

				<div class="project_card__links">
					<a href="https://github.com/alec-jensen/EnhancedInput" target="_blank">Github</a>
				</div>
			</div>
		</div>

		<div class="project_card">
			<!-- <img class="project_card__image" src="" alt="" /> -->

			<div class="project_card__header">
				<h2>botnet</h2>
				<p>
					Simple botnet with 3 parts: server, client, and a web interface. The server is written in python, the client in Nim, and the web interface using Astro.
				</p>

				<div class="project_card__links">
					<a href="https://github.com/alec-jensen/botnet">GitHub</a>
				</div>
			</div>
		</div>

		<div class="project_card">
			<!-- <img class="project_card__image" src="" alt="" /> -->

			<div class="project_card__header">
				<h2>webserver</h2>
				<p>
					Webserver written in Python with support for writing HTML directly with Python.
				</p>

				<div class="project_card__links">
					<a href="https://github.com/alec-jensen/webserver">GitHub</a>
				</div>
			</div>
		</div>
	</div>
</div>

<style>
	h2 {
		font-size: 26px;
	}

	p {
		font-size: 16px;
		text-align: center;
	}

	.projects {
		display: flex;
		flex-wrap: wrap;
		justify-content: center;
		min-width: 90%;
	}

	.project_card {
		background-color: var(--color-bg-2);
		padding: 1em;
		border-radius: 10px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
		display: flex;
		flex-direction: column;
		overflow: hidden;
		align-items: center;
		width: 25vw;

		margin: 1em;
	}

	.project_card__header {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		text-align: center;

		max-width: 20vw;
		height: 100%;
	}

	.project_card__header h2 {
		margin: 0;
		font-weight: bold;
	}

	.project_card__header p {
		margin: 0;
		color: lightgray
	}

	.project_card__links {
		display: flex;
		justify-content: space-evenly;

		margin-top: 1em;
	}

	.project_card__links a {
		color: white;
		text-decoration: none;
		padding: 0.5em 2em;
		background-color: var(--color-theme-2);
		border-radius: 10px;
		transition: background-color 0.2s ease-in-out;
	}

	.project_card__links a:hover {
		background-color: var(--color-theme-1);
		transition: background-color 0.2s ease-in-out;
	}

	.project_card__image {
		max-height: 25vh;
		width: auto;
		border-radius: 10px;

		margin-bottom: 10px;
	}

	.page {
		padding-top: 5vh;
		height: 100%;
		width: 100%;
	}

	@media (max-width: 768px) {
		.page {
			padding-top: 10vh;
			padding-bottom: 10vh;
		}

		.project_card {
			width: 80vw;
		}

		.project_card__header {
			max-width: 80vw;
		}

		.project_card__image {
			max-width: 80vw;
		}
	}
</style>

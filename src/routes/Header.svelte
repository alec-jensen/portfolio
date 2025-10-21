<script>
	import { page } from '$app/stores';
</script>

<header>
	<nav>
		<ul>
			<li aria-current={$page.url.pathname === '/' ? 'page' : undefined}>
				<a href="/"
					><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"
						><title>Home</title><path
							d="M240-200h120v-240h240v240h120v-360L480-740 240-560v360Zm-80 80v-480l320-240 320 240v480H520v-240h-80v240H160Zm320-350Z"
						/></svg
					></a
				>
			</li>
			<li aria-current={$page.url.pathname === '/about' ? 'page' : undefined}>
				<a href="/about"
					><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"
						><title>About Me</title><path
							d="M480-480q-66 0-113-47t-47-113q0-66 47-113t113-47q66 0 113 47t47 113q0 66-47 113t-113 47ZM160-160v-112q0-34 17.5-62.5T224-378q62-31 126-46.5T480-440q66 0 130 15.5T736-378q29 15 46.5 43.5T800-272v112H160Zm80-80h480v-32q0-11-5.5-20T700-306q-54-27-109-40.5T480-360q-56 0-111 13.5T260-306q-9 5-14.5 14t-5.5 20v32Zm240-320q33 0 56.5-23.5T560-640q0-33-23.5-56.5T480-720q-33 0-56.5 23.5T400-640q0 33 23.5 56.5T480-560Zm0-80Zm0 400Z"
						/></svg
					></a
				>
			</li>
			<li aria-current={$page.url.pathname === '/projects' ? 'page' : undefined}>
				<a href="/projects"
					><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"
						><title>Projects</title><path
							d="M320-240 80-480l240-240 57 57-184 184 183 183-56 56Zm320 0-57-57 184-184-183-183 56-56 240 240-240 240Z"
						/></svg
					></a
				>
			</li>
			<li aria-current={$page.url.pathname === '/contact' ? 'page' : undefined}>
				<a href="/contact"
					><svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 -960 960 960" width="24"
						><title>Contact</title><path
							d="M160-160q-33 0-56.5-23.5T80-240v-480q0-33 23.5-56.5T160-800h640q33 0 56.5 23.5T880-720v480q0 33-23.5 56.5T800-160H160Zm320-280L160-640v400h640v-400L480-440Zm0-80 320-200H160l320 200ZM160-640v-80 480-400Z"
						/></svg
					></a
				>
			</li>
			<li>
				<a id="blog_link" href="https://blog.alecj.tk/" target="_blank">
					<svg
						xmlns="http://www.w3.org/2000/svg"
						height="24px"
						viewBox="0 -960 960 960"
						width="24px"
					>
						<title>Blog (opens in new tab)</title>
						<mask id="blog_link_mask" x="0" y="0" width="24" height="24">
							<rect x="0" y="-960" width="960" height="960" fill="white" />
							<rect x="550" y="-500" width="5000" height="5000" fill="black" />
						</mask>
						<path
							d="M240-280h280v-80H240v80Zm400 0h80v-400h-80v400ZM240-440h280v-80H240v80Zm0-160h280v-80H240v80Zm-80 480q-33 0-56.5-23.5T80-200v-560q0-33 23.5-56.5T160-840h640q33 0 56.5 23.5T880-760v560q0 33-23.5 56.5T800-120H160Zm0-80h640v-560H160v560Zm0 0v-560 560Z"
							mask="url(#blog_link_mask)"
						/>
					</svg>
				</a>
				<svg
					id="blog_open_in_new"
					xmlns="http://www.w3.org/2000/svg"
					height="16px"
					viewBox="0 -960 960 960"
					width="16px"
					fill="#e8eaed"
					><path
						d="M200-120q-33 0-56.5-23.5T120-200v-560q0-33 23.5-56.5T200-840h280v80H200v560h560v-280h80v280q0 33-23.5 56.5T760-120H200Zm188-212-56-56 372-372H560v-80h280v280h-80v-144L388-332Z"
					/></svg
				>
			</li>
		</ul>
	</nav>
</header>

<style>
	header {
		display: flex;
		justify-content: center;
	}

	nav .corner a {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		height: 100%;
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
		border-radius: 10px;
		transition: background 0.2s linear;
	}

	li:hover {
		background: var(--color-bg-2);
	}

	li[aria-current='page'] svg {
		fill: var(--color-theme-1);
	}

	nav a svg {
		display: flex;
		height: 100%;
		align-items: center;
		padding: 0 2rem;
		fill: rgb(255, 255, 255);
		font-weight: 700;
		font-size: 0.8rem;
		text-transform: uppercase;
		letter-spacing: 0.1em;
		text-decoration: none;
		transition: fill 0.2s linear;
	}

	#blog_open_in_new {
		position: absolute;
		left: 45px;
		top: 23px;
		transition: fill 0.2s linear;
	}

	@media (min-width: 720px) {
		nav li:hover svg {
			fill: var(--color-theme-1);
		}
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

			width: auto;
		}

		nav svg {
			padding: 0 1.4rem;
		}

		li:hover {
			background: unset;
		}

		#blog_open_in_new {
			left: 23px;
			top: 23px;
		}
	}
</style>

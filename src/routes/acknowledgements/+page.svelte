<svelte:head>
	<title>Acknowledgements</title>
	<meta name="description" content="Acknowledgements for Alec Jensen Development" />
</svelte:head>

<div class="text-column">
	<h1><rainbow>Acknowledgements</rainbow></h1>

	<div class="policy">
		<p>
			This page is dedicated to recognizing the open-source projects, critical infrastructure
			providers, design communities, and security researchers whose work makes Alec Jensen
			Development's services possible, stable, and secure. We are deeply grateful for the
			foundational contributions of the community.
		</p>

		<!-- Open Source -->
		<h2>Open Source Contributions</h2>
		<p>
			The majority of the code, tools, and libraries used across the websites and services
			(including <em>alecj.com</em>, <em>alecj.tk</em>, and <em>3ln.me</em>) are made available
			under open-source licenses. We gratefully rely on countless libraries, frameworks, and tools
			provided by the open-source community to build, secure, and deliver our applications.
		</p>
		<p>
			Specific license information and comprehensive lists of dependencies for individual projects
			can be found on the respective service's documentation or repository.
		</p>

		<!-- Infrastructure & Security -->
		<h2>Infrastructure & Security Dependencies</h2>
		<p>
			These critical services help us deliver content reliably and maintain a robust defense against
			malicious activity:
		</p>
		<ul>
			<li>
				<strong>Web Security & WAF:</strong> Services like CrowdSec for threat mitigation and abuse prevention.
			</li>
			<li>
				<strong>Analytics:</strong> Privacy-respecting analytics tools such as Swetrix, used solely for
				aggregated site performance measurement.
			</li>
		</ul>

		<!-- Assets & Design -->
		<h2>Assets & Design Inspiration</h2>
		<ul>
			<li>
				Icons and SVGs used across the Services are subject to their respective licenses (e.g.,
				open-source icon packs).
			</li>
			<li>
				The overall design, user experience patterns, and documentation structure are inspired by
				the collective knowledge of the broader web development community.
			</li>
		</ul>

		<!-- Security Researchers -->
		<h2>Security Researchers</h2>
		<p>
			We formally recognize and thank the security researchers who responsibly disclose
			vulnerabilities in accordance with our policy. These contributions are vital to maintaining
			the integrity of Alec Jensen Development's services.
		</p>
		<p>
			For information on our disclosure process and safe harbor guidelines, please consult the <a
				href="/security">Alec Jensen Development Security Policy</a
			>.
		</p>

		<p class="last-updated">Last updated: October 12, 2025</p>
	</div>
</div>

<style>
	.text-column {
		display: flex;
		flex-direction: column;
		align-items: center;
	}
	h1 {
		margin-top: 2em;
	}
	.policy {
		max-width: 800px;
		margin: 1rem auto;
		text-align: left;
	}
	.policy h2 {
		margin-top: 1.25rem;
		margin-bottom: 0.5rem;
		font-size: 1.4rem;
	}
	p {
		color: lightgray;
	}
	.policy ul {
		margin: 0.25rem 0 0.75rem 1.2rem;
		color: lightgray;
	}
	.policy a {
		color: var(--color-theme-1, #9ad);
		text-decoration: underline;
	}
	.last-updated {
		color: #aaa;
		font-size: 0.95em;
		margin-top: 1rem;
	}
</style>

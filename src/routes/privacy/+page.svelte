<svelte:head>
	<title>Privacy Policy</title>
	<meta name="description" content="Privacy Policy for Alec Jensen Development" />
</svelte:head>

<div class="text-column">
	<h1><rainbow>Alec Jensen Development</rainbow> Privacy Policy</h1>

	<div class="policy">
		<!-- Introduction and Scope -->
		<p>
			I respect your privacy and am committed to transparency regarding any information collected
			while operating my Services. This policy explains what data I collect, how I use it, and your
			choices.
		</p>
		<p>
			I do not conduct user profiling, behavioral advertising, or marketing based on activity on the
			Services. Analytics are limited to aggregated, privacy‑respecting, cookieless metrics for
			operational insights only.
		</p>
		<p>
			This policy applies to all websites, domains, services, and networks operated by Alec J.
			(collectively, the "Services"), including alecj.com, alecj.tk, and 3ln.me.
		</p>

		<h2>Controller and contact details</h2>
		<p>
			Controller: Alec J. (United States). For privacy questions or requests, please use the
			<a href="/contact">contact</a> page.
		</p>

		<h2>At a glance</h2>
		<ul>
			<li>
				What I collect: minimal security logs (e.g., IP address, headers, timestamps), aggregated,
				cookieless first‑party analytics, and any details you voluntarily send via the contact page.
			</li>
			<li>
				What I don't collect: advertising identifiers, third‑party tracking data, behavioral
				profiles, or data from data brokers.
			</li>
			<li>
				Where data lives: Services and self‑hosted analytics run on infrastructure located in the
				United States. All traffic is routed through a web application firewall (WAF) on a cloud
				VPS, where some security telemetry may be stored. Some application data is stored in cloud
				databases (for example, kidney bot data is stored in a MongoDB database).
			</li>
			<li>Why: keep the site secure and improve content/UX.</li>
			<li>
				How long: security logs are kept only as long as needed to protect the service; analytics
				are aggregated and retained for operational insights; contact emails are kept as long as
				needed to respond.
			</li>
			<li>
				Security: Security logs are separate from analytics. Detected malicious IPs may be
				automatically reported to reputable community threat‑intelligence lists to help protect the
				broader internet.
			</li>
			<li>
				See also: the <a href="/security">Security Policy</a> for testing guidelines and responsible
				disclosure.
			</li>
		</ul>

		<h2>What I Collect and Why</h2>
		<p>
			I specifically aim to collect zero Personally Identifiable Information (PII) for operational
			and analytical purposes. The data collected falls into two categories:
		</p>

		<h3>1. Non-PII Usage Data (Analytics)</h3>
		<ul>
			<li>
				To understand traffic patterns and improve the user experience across the Services, I use
				self-hosted, first‑party, privacy‑respecting, cookieless analytics running on my own
				infrastructure.
			</li>
			<li>
				This system records non-personal data points, such as:
				<ul>
					<li>Page views and session duration.</li>
					<li>The general geographic area (country/region).</li>
					<li>The type of device, browser, and operating system used.</li>
					<li>Referrer URLs.</li>
				</ul>
			</li>
			<li>
				Crucially, this system is configured to avoid cross-site tracking and does not use
				third-party trackers or advertising identifiers. It does not process IP addresses or device
				IDs to personally identify you, it does not set analytics cookies, and it is not used for
				profiling or marketing.
			</li>
		</ul>

		<h3>2. Security and Server Log Data</h3>
		<ul>
			<li>
				To protect the integrity and security of the network and to prevent malicious activity (like
				DoS attacks or unauthorized access), server logs and security systems (CrowdSec WAF)
				temporarily process basic network information. All inbound traffic is routed through a WAF
				running on a cloud VPS; certain security telemetry (for example, block lists and counters)
				may be stored on that VPS.
			</li>
			<li>
				This data includes IP addresses, request headers, and timestamps. IP addresses are processed
				strictly for security purposes such as detecting, preventing, and responding to abuse, spam,
				fraud, and service disruption (e.g., rate limiting and blocking malicious traffic).
			</li>
			<li>
				Security logs are kept separate from analytics. This security data is retained only for as
				long as necessary to maintain network safety and is not used for marketing or profiling.
			</li>
			<li>
				To help protect the broader community, IPs conclusively identified as malicious may be
				automatically reported to crowdsourced malicious IP databases/threat‑intel feeds (for
				example, abuse blacklists). Only indicators necessary for abuse mitigation are shared — not
				analytics or contact content.
			</li>
		</ul>

		<h3>Traffic routing and security infrastructure</h3>
		<p>
			To help protect the website, its content, and users, all incoming web traffic to the site is
			routed through a secure Virtual Private Server (VPS) operated via Oracle Cloud which functions
			as a Web Application Firewall (WAF). This means that HTTP/HTTPS requests pass first through
			this server, where certain security checks (for example, known attack patterns, bot traffic,
			and request anomalies) may be filtered before being forwarded to the origin server.
		</p>
		<p>
			For transport security and inspection, TLS may be terminated on this VPS — in other words,
			requests are decrypted on this VPS and then securely routed to their respective origin servers
			via a private VPN tunnel. End-to-end protections and least-privilege access controls are
			maintained on the internal network.
		</p>
		<p>
			This routing is done to improve the safety, availability, and integrity of the site and
			service. It is not used to sell, disclose, or otherwise share identifiable user data except as
			described elsewhere in this policy.
		</p>
		<p>
			Because this process involves handling minimal connection metadata (for example, IP address,
			request headers, and timestamps), such metadata may be temporarily processed by the VPS/WAF
			infrastructure. This information is handled the same way as Security and Server Log Data
			described above.
		</p>
		<p>
			Role of provider: The VPS/WAF provider (Oracle Cloud) acts as my processor under my
			instructions; I remain the data controller for this processing.
		</p>

		<h3>3. Contact Information</h3>
		<ul>
			<li>
				If you voluntarily email me or submit a contact form, I receive the information you provide
				(e.g., your name and email address) solely to respond to your inquiry.
			</li>
		</ul>

		<h3>4. Service Data (feature/bot content)</h3>
		<ul>
			<li>
				Some interactive features may store limited data required to operate the feature. This
				application data is kept in cloud databases. For example, kidney bot stores its data in a
				MongoDB database.
			</li>
			<li>
				kidney bot (Discord): When enabled by a server admin, the bot may submit message text to
				Google's Perspective API to score for potentially harmful content (e.g., toxicity). If a
				score exceeds a configured threshold, the bot may delete the message and optionally record
				an audit log. To operate moderation and audits, we may store Discord IDs (user, message,
				channel, server), timestamps, relevant category scores, and the moderation decision. We
				strive to minimize retention.
			</li>
			<li>
				This data is used only to provide the relevant feature and is not used for advertising or
				behavioral profiling.
			</li>
		</ul>

		<h2>What I do not do</h2>
		<ul>
			<li>No selling or sharing of personal information.</li>
			<li>No user profiling or behavioral advertising.</li>
			<li>No session replay, heatmaps, or fingerprinting.</li>
			<li>No third‑party analytics or cross‑site tracking.</li>
		</ul>

		<h2>Legal bases for processing</h2>
		<ul>
			<li>
				Security logging: Legitimate interests (IT/network security; prevention and detection of
				abuse and fraud).
			</li>
			<li>
				Analytics (self‑hosted, aggregated, cookieless): Legitimate interests (improving content,
				performance, and usability).
			</li>
			<li>
				Contact responses: Legitimate interests (responding to your inquiry) or contract if
				applicable.
			</li>
		</ul>
		<p>
			Where processing is based on legitimate interests, you may object to processing. If you wish
			to object to analytics or security logging, contact me and I’ll explain options and
			implications (note: basic logging is technically required to deliver the site and maintain
			security).
		</p>

		<h2>How I Use Data</h2>
		<ul>
			<li>
				To operate, maintain, and improve the functionality of the Services (using Non-PII Usage
				Data).
			</li>
			<li>To respond to your inquiries and provide user support.</li>
			<li>
				To maintain security and prevent abuse, fraud, and illegal activity (using Security and
				Server Log Data).
			</li>
		</ul>

		<h2>Data Sharing and Disclosure</h2>
		<p>
			I do not sell your personal information to any third parties. I also do not share data with
			any external partners for marketing or advertising purposes.
		</p>
		<p>
			Minimal data is shared with necessary service providers strictly to operate the Services,
			subject to appropriate contractual safeguards:
		</p>
		<ul>
			<li>Hosting and Infrastructure Providers: To keep the Services running.</li>
			<li>
				Cloud infrastructure provider (Oracle Cloud): Provides the VPS/WAF used to route and filter
				traffic; acts as my processor under instructions and may process minimal connection metadata
				for security.
			</li>
			<li>
				Security Services (e.g., CrowdSec): To identify and mitigate security threats on my network.
			</li>
			<li>
				Analytics (self‑hosted): Analytics run on my own infrastructure. No analytics data is shared
				with third parties, used for advertising, or combined with data from other websites.
			</li>
			<li>
				Cloud databases: To store application data required for features (for example, kidney bot
				data in a MongoDB database).
			</li>
			<li>
				AI moderation provider (Google Perspective API): When a Discord server enables AI filtering
				for kidney bot, message text may be sent to Perspective for scoring, subject to Google's
				terms and privacy notices. Only what is necessary for scoring is sent.
			</li>
		</ul>
		<p>
			These providers act as processors under my instructions where applicable. Subprocessors may
			change over time; material changes will be reflected in this policy.
		</p>
		<p>
			I may also disclose data if legally required to do so, or if I believe in good faith that such
			action is necessary to comply with legal obligations, protect the security of my networks, or
			protect my rights.
		</p>

		<h2>Data Retention</h2>
		<p>
			I keep data only as long as necessary for the purposes outlined above or to comply with legal
			obligations. Security and WAF telemetry are typically retained for up to 30–90 days unless
			required longer to investigate suspected abuse. Analytics are aggregated and retained for
			operational insights without personal identifiers. Contact messages are retained as long as
			needed to respond and maintain reasonable records.
		</p>

		<h2>Security incidents</h2>
		<p>
			If I become aware of a data incident that is likely to pose a risk to your rights or freedoms,
			I will notify affected users and/or regulators where required by law.
		</p>

		<h2>Your Choices and Rights</h2>
		<ul>
			<li>
				Since I do not collect PII for analytics or general site operation, there is no personal
				data to access, correct, or delete in those systems.
			</li>
			<li>
				If you have provided contact information (via email or form), you can contact me to request
				access to, correction of, or deletion of that information, where applicable and legally
				permissible.
			</li>
		</ul>

		<h2>Your rights (EU/UK GDPR)</h2>
		<ul>
			<li>Access: request a copy of personal data that relates to you.</li>
			<li>Rectification: request corrections to inaccurate data.</li>
			<li>Erasure: request deletion where applicable (for example, where no longer needed).</li>
			<li>Restriction: request processing to be limited in certain circumstances.</li>
			<li>
				Portability: receive certain data in a structured, commonly used, machine‑readable format.
			</li>
			<li>
				Object: object to processing based on legitimate interests (including analytics and security
				logging) where applicable.
			</li>
			<li>
				Complaint: lodge a complaint with a supervisory authority in your country of residence or
				work.
			</li>
		</ul>
		<p>
			To exercise any of these rights, please use the <a href="/contact">contact</a> page. Note that
			basic security logging may be technically necessary to deliver the site and maintain integrity.
		</p>

		<h2>Children's Privacy</h2>
		<p>
			The Services are not directed to children under the age of 13. I do not knowingly collect
			personal information from children under 13.
		</p>

		<h2>Cookies</h2>
		<p>
			The Services may set a small number of first-party cookies that are strictly necessary for
			basic site functionality (for example, to remember simple preferences or to manage session
			state). These cookies are not used for advertising, cross-site tracking, or profiling.
			Analytics are fully cookieless and set no analytics cookies.
		</p>
		<ul>
			<li>No third-party advertising cookies are used.</li>
			<li>
				Analytics are self‑hosted, first‑party, privacy‑respecting, and cookieless; they do not
				track you across other websites.
			</li>
			<li>You can control or delete cookies via your browser settings at any time.</li>
		</ul>
		<p>Analytics for this site operate entirely without cookies.</p>

		<h2>Do Not Track (DNT)</h2>
		<p>
			Browsers may send a Do Not Track (DNT) signal. This site does not track you for advertising
			and does not use third‑party trackers. Because there is no cross‑site tracking to disable, DNT
			does not change site behavior — but your preference is respected in spirit.
		</p>

		<h2>Global Privacy Control (GPC)</h2>
		<p>
			This site honors Global Privacy Control (GPC) signals as an opt‑out of selling or sharing
			personal information. I do not sell or share personal information; therefore, GPC does not
			change behavior, but it is recorded as your preference where applicable.
		</p>

		<h2>Changes to this Policy</h2>
		<p>
			I may update this policy from time to time. Material changes will be prominently reflected on
			this page. Your continued use of the Services after changes take effect constitutes acceptance
			of the updated Policy.
		</p>

		<h2>Contact Information</h2>
		<p>
			Questions about this policy or your data? Please <a href="/contact">contact me</a>.
		</p>
		<h2>Regional rights (CPRA/CCPA)</h2>
		<p>
			If you are a California resident, you may have rights under the CCPA/CPRA (e.g., to know,
			delete, correct, and to be free from discrimination). I do not sell or share personal
			information for cross‑context behavioral advertising. To exercise rights or ask questions,
			please contact me via the <a href="/contact">contact</a> page.
		</p>

		<h2>International transfers</h2>
		<p>
			My servers, VPS/WAF, and self‑hosted analytics are located in the United States. If you access
			the Services from outside the U.S., your connection will route to U.S. infrastructure to
			deliver and secure the site. Where I engage service providers to process personal data from
			the EU/UK, I rely on appropriate safeguards such as Standard Contractual Clauses, where
			applicable.
		</p>

		<p class="last-updated">Last updated: October 20, 2025</p>
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
	p {
		color: lightgray;
	}
	.policy h2 {
		margin-top: 1.25rem;
		margin-bottom: 0.5rem;
		font-size: 1.4rem;
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

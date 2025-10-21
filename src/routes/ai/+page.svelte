<section>
	<h1>AI Transparency</h1>
	<p>Last updated: October 20, 2025</p>

	<h2>What is kidney bot?</h2>
	<p>
		kidney bot is a Discord moderation bot. It can optionally use an AI model to evaluate messages
		for potentially harmful content and delete them when they cross a configured threshold.
	</p>

	<h2>Where it operates</h2>
	<p>
		kidney bot only operates in Discord servers where it has been invited and granted the necessary
		permissions by the server administrators. The AI features must be explicitly enabled by the
		server administrators. No data is transmitted to external servers without consent.
	</p>

	<h2>How the AI filtering works</h2>
	<ul>
		<li>
			Model: Google’s Perspective API may be used to score message text for toxicity and related
			categories.
		</li>
		<li>
			What may be sent to Perspective: the message text (and optional language hint) for scoring.
		</li>
		<li>
			Decision: if a score exceeds an admin‑configured threshold, the bot may delete the message and
			optionally log the event.
		</li>
	</ul>

	<h2>What we store</h2>
	<p>
		As noted in the Privacy Policy, kidney bot stores data in MongoDB. To operate moderation and
		provide audit logs, we may store minimal metadata such as:
	</p>
	<ul>
		<li>Discord IDs (user, message, channel, and server IDs), timestamps</li>
		<li>Category scores returned by Perspective (e.g., toxicity) and the delete/allow decision</li>
		<li>Configuration settings for a server (e.g., enabled categories and thresholds)</li>
	</ul>
	<p>We strive to minimize retention and avoid storing unnecessary personal data.</p>

	<h2>Retention and use</h2>
	<ul>
		<li>
			Logs are kept only as long as necessary for moderation, troubleshooting, and abuse prevention.
		</li>
		<li>Data is not sold or used for advertising or behavioral profiles.</li>
		<li>
			Submitted text is used solely for moderation scoring; we do not use it to train our own
			models.
		</li>
	</ul>

	<h2>Administration and controls</h2>
	<ul>
		<li>Server admins can enable/disable AI filtering, choose categories, and set thresholds.</li>
		<li>
			Admins may request deletion of bot logs for their server subject to verification and
			applicable limits.
		</li>
	</ul>

	<h2>Notes about third‑party services</h2>
	<p>
		When enabled, message text submitted for scoring is processed by Google’s Perspective API and is
		subject to Google’s applicable terms and privacy notices. We send only what’s needed for
		scoring.
	</p>

	<h2>Contact</h2>
	<p>Questions about kidney bot or AI filtering? Email ai@alecjensen.com.</p>
</section>

<style>
	section {
		max-width: 900px;
		margin: 0 auto;
	}
	h1,
	h2 {
		text-align: left;
	}
	p,
	li {
		line-height: 1.6;
	}
</style>

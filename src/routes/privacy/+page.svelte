<svelte:head>
	<title>Privacy Policy</title>
	<meta name="description" content="Privacy Policy for Alec Jensen Development" />
</svelte:head>

<div class="text-column">
    <h1><rainbow>Alec Jensen Development</rainbow> Privacy Policy</h1>

    <div class="policy">
        <!-- Introduction and Scope -->
        <p>
            I respect your privacy and am committed to transparency regarding any information collected while operating my Services. This policy explains what data I collect, how I use it, and your choices.
        </p>
        <p>
            This policy applies to all websites, domains, services, and networks operated by Alec J. (collectively, the "Services"), including <em>alecj.com</em>, <em>alecj.tk</em>, and <em>3ln.me</em>.
        </p>

        <h2>What I Collect and Why</h2>
        <p>
            I specifically aim to collect <em>zero Personally Identifiable Information (PII)</em> for operational and analytical purposes. The data collected falls into two categories:
        </p>

        <h3>1. Non-PII Usage Data (Analytics)</h3>
        <ul>
            <li>
                To understand traffic patterns and improve the user experience across the Services, I use <em>privacy-respecting analytics software (Swetrix)</em>.
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
                Crucially, this system <em>does not use cookies</em> and does not process IP addresses or device IDs to personally identify you.
            </li>
        </ul>

        <h3>2. Security and Server Log Data</h3>
        <ul>
            <li>
                To protect the integrity and security of the network and to prevent malicious activity (like DoS attacks or unauthorized access), <em>server logs and security systems (CrowdSec WAF)</em> temporarily process basic network information.
            </li>
            <li>
                This data includes IP addresses, request headers, and timestamps, which are processed strictly to identify and block security threats and abuse.
            </li>
            <li>
                This security data is retained only for the duration necessary to maintain network safety and is <em>not used for marketing or analytics purposes</em>.
            </li>
        </ul>

        <h3>3. Contact Information</h3>
        <ul>
            <li>If you voluntarily email me or submit a contact form, I receive the information you provide (e.g., your name and email address) solely to respond to your inquiry.</li>
        </ul>

        <h2>How I Use Data</h2>
        <ul>
            <li>To operate, maintain, and improve the functionality of the Services (using Non-PII Usage Data).</li>
            <li>To respond to your inquiries and provide user support.</li>
            <li>To maintain security and prevent abuse, fraud, and illegal activity (using Security and Server Log Data).</li>
        </ul>

        <h2>Data Sharing and Disclosure</h2>
        <p>
            I <em>do not sell your personal information</em> to any third parties. I also do not share data with any external partners for marketing or advertising purposes.
        </p>
        <p>
            Minimal data is shared with necessary service providers *strictly* to operate the Services, subject to appropriate contractual safeguards:
        </p>
        <ul>
            <li>
                <em>Hosting and Infrastructure Providers:</em> To keep the Services running.
            </li>
            <li>
                <em>Security Services (e.g., CrowdSec):</em> To identify and mitigate security threats on my network.
            </li>
            <li>
                <em>Analytics Provider (Swetrix):</em> This provider processes the non-PII usage data on my behalf, but does not use or sell this data for their own purposes.
            </li>
        </ul>
        <p>
            I may also disclose data if legally required to do so, or if I believe in good faith that such action is necessary to comply with legal obligations, protect the security of my networks, or protect my rights.
        </p>

        <h2>Data Retention</h2>
        <p>
            I keep data only as long as necessary for the purposes outlined above (e.g., security logs are purged regularly, and analytical data is kept in an aggregated, non-PII form) or to comply with legal obligations.
        </p>

        <h2>Your Choices and Rights</h2>
        <ul>
            <li>
                Since I do not collect PII for analytics or general site operation, there is no personal data to access, correct, or delete in those systems.
            </li>
            <li>
                If you have provided contact information (via email or form), you can contact me to request access to, correction of, or deletion of that information, where applicable and legally permissible.
            </li>
        </ul>

        <h2>Children's Privacy</h2>
        <p>The Services are not directed to children under the age of 13. I do not knowingly collect personal information from children under 13.</p>

        <h2>Changes to this Policy</h2>
        <p>
            I may update this policy from time to time. Material changes will be prominently reflected on this page. Your continued use of the Services after changes take effect constitutes acceptance of the updated Policy.
        </p>

        <h2>Contact Information</h2>
        <p>
            Questions about this policy or your data? Please <a href="/contact">contact me</a>.
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

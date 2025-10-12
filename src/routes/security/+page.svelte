<svelte:head>
	<title>Security Policy</title>
	<meta name="description" content="Alec Jensen Development Security Policy" />
</svelte:head>

<div class="text-column">
    <h1><rainbow>Alec Jensen Development</rainbow> Security Policy</h1>

    <p>
        Alec Jensen Development takes the security and integrity of its applications, networks, and user data extremely seriously. This policy governs how we protect our Services and outlines the requirements for security researchers engaging in good-faith testing.
    </p>

    <div class="policy">
        <!-- Scope -->
        <h2>Scope and Covered Assets</h2>
        <p>
            This policy applies to all public-facing services, applications, APIs, and network infrastructure directly owned and operated by Alec Jensen Development. Assets are considered <strong>In Scope</strong> if they handle user data, facilitate user interaction, or process financial transactions. This includes, but is not limited to, those hosted under the domains <em>alecj.com</em>, <em>alecj.tk</em>, and <em>3ln.me</em>.
        </p>
        <p>
            Any assets not explicitly listed, or that are third-party services integrated but not directly managed by Alec Jensen Development (e.g., social media pages, external payment processors), are considered <strong>Out of Scope</strong> unless otherwise directed.
        </p>

        <!-- Reporting -->
        <h2>Vulnerability Reporting Process</h2>
        <p>
            We appreciate the efforts of security researchers in improving the security of our Services. Please follow these guidelines for responsible disclosure:
        </p>
        <ul>
            <li>
                <strong>Method of Contact:</strong> Report the vulnerability using a contact method found on the <a href="/contact">Contact me</a> page. Please use encrypted communication if available.
            </li>
            <li>
                <strong>Required Details:</strong> Your report must be clear, detailed, and actionable, including:
                <ul>
                    <li>A concise description of the vulnerability.</li>
                    <li>Detailed, repeatable steps to reproduce the issue (including any necessary tools or scripts).</li>
                    <li>The potential security impact and severity.</li>
                    <li>Any relevant proof-of-concept code, screenshots, or network traffic logs.</li>
                </ul>
            </li>
            <li>
                <strong>Non-Disclosure:</strong> Researchers must keep all details of the vulnerability confidential. Please avoid sharing information publicly on blogs, forums, or social media until we have confirmed the issue is resolved.
            </li>
        </ul>

        <!-- Response Timelines -->
        <h2>Response and Remediation Timelines</h2>
        <p>
            We strive to respond promptly to all reports that comply with this policy:
        </p>
        <ul>
            <li><strong>Acknowledgement:</strong> Within 5 business days of receipt.</li>
            <li><strong>Triage & Assessment:</strong> Within 14 business days to confirm validity and severity.</li>
            <li><strong>Fix & Mitigation:</strong> Targeted within 90 days. Remediation time is dependent on the complexity and severity of the vulnerability.</li>
        </ul>

        <!-- Testing Guidelines -->
        <h2>Guidelines for Authorized Testing</h2>
        <p>
            To qualify for <em>Safe Harbor</em> (non-prosecution), all research activities must strictly adhere to the following rules:
        </p>
        <ul>
            <li>Only test against assets explicitly covered under the Scope section.</li>
            <li>Respect the integrity and availability of the Services. Do not conduct <em>Denial-of-Service (DoS), rate-limiting attacks</em>, or any test that could degrade or disrupt production services.</li>
            <li>Do not engage in testing that could violate user privacy, such as accessing, collecting, deleting, or altering data belonging to other users.</li>
            <li><em>Absolutely no social engineering, phishing, or physical security attacks</em> against any personnel or infrastructure.</li>
            <li>Limit testing to the minimum necessary to prove the vulnerability's existence.</li>
        </ul>

        <!-- Safe Harbor and Legal -->
        <h2>Safe Harbor</h2>
        <p>
            If you make a good faith effort to comply with this policy during your security research, we agree not to pursue legal action against you or ask law enforcement to investigate you. We consider activities conducted in accordance with this policy to be authorized.
        </p>
        
        <!-- Out of Scope -->
        <h2>General Exclusions (Out of Scope)</h2>
        <p>
            The following categories of vulnerabilities or testing activities are considered <strong>Out of Scope</strong> and typically do not qualify for recognition or remediation:
        </p>
        <ul>
            <li>Denial-of-Service (DoS) and volumetric attacks.</li>
            <li><strong>Theoretical or Best-Practice Recommendations</strong>: Best-practice or security-hardening recommendations (e.g., missing security headers, missing DNS records) without a proven, demonstrable security impact that leads to a direct exploit.</li>
            <li><strong>Client-Side Issues</strong>: Issues requiring unverifiable user-agents, rooted devices, or outdated browser versions to exploit.</li>
            <li>Vulnerabilities only exploitable through man-in-the-middle (MITM) attacks, unless the vulnerability allows a bypass of transport layer security (TLS).</li>
            <li><strong>Self-XSS</strong>: Cross-Site Scripting (XSS) that only affects the user and cannot be exploited by an attacker against other users.</li>
        </ul>

        <!-- Recognition -->
        <h2>Recognition</h2>
        <p>
            We are happy to credit researchers who responsibly report significant, valid, and previously unknown vulnerabilities. Recognition will be provided on our <a href="/acknowledgements">Acknowledgements</a> page, with the researcher's permission.
        </p>

        <p class="last-updated">Last updated: October 12, 2025</p>
    </div>
</div>

<style>
	p {
		text-align: left;
		color: lightgray;
		line-height: 175%;
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

	.policy ul {
		margin: 0.25rem 0 0.75rem 1.2rem;
		color: lightgray;
	}

	.policy a {
		color: var(--color-theme-1, #9ad);
		text-decoration: underline;
	}
</style>

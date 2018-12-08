# Google Gruyere Notes
https://google-gruyere.appspot.com

## Cross-Site Scripting (XSS)
* __Stored XSS__ - the attacker stores the attack in the application (e.g., in a snippet) and the victim triggers the attack by browsing to a page on the server that renders the attack, by not properly escaping or sanitizing the stored data
* __Reflected XSS__ - the attack is in the request itself (frequently the URL) and the vulnerability occurs when the server inserts the attack in the response verbatim or incorrectly escaped or sanitized. The victim triggers the attack by browsing to a malicious URL created by the attacker.

This webpage has a green button that says `Flag`. Clicking on it gives the message: `I'm sorry it doesn't look like you are the admin.`. We need to get admin privileges despite the login functionality not working.

In the `Logon` picoCTF challenge, there was a cookie named `admin` which was a boolean. We can try to create a cookie for this webpage, with the name of the cookie being `admin`, and the value being `true`. Once the cookie is created, clicking the `Flag` button displays the flag.

Flag: `picoCTF{n0l0g0n_n0_pr0bl3m_eb9bab29}`
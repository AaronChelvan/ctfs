The title of this challenge is a hint that we should have a look at the `robots.txt` file of this website. Navigating to `http://2018shell3.picoctf.com:10157/robots.txt`, we can see that the contents of the file is:
```
User-agent: *
Disallow: /143ce.html
```

When we navigate to the `/143ce.html` page, we can see the flag.

Flag: `picoCTF{th3_w0rld_1s_4_danger0us_pl4c3_3lli0t_143ce}`
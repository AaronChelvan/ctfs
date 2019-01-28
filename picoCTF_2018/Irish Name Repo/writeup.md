On the main page of this website, we see a grid of photos and a menu icon on the top left.
The menu has 3 options: `Close Menu`, `Support`, and `Admin Login`.

On the `Support` page, there are some questions that were asked by users. One of the questions is: `Hi. I tried adding my favorite Irish person, Conan O'Brien. But I keep getting something called a SQL Error`. This is a hint that this website uses an SQL database.

On the `Admin Login` page, we can try to login by exploiting an SQL injection vulnerability. Set the username as `admin` and the password as `' or 1=1 --`. We are redirected to a page that displays the flag.

Flag: `picoCTF{con4n_r3411y_1snt_1r1sh_c0d93e2f}`
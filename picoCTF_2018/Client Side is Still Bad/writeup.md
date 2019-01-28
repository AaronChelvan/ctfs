This website lets you input a password, and it will display an alert which states whether the password is correct or not. If we view the source for this page, we can see that there is some JavaScript being executed:
```
function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(split*7, split*8) == '}') {
      if (checkpass.substring(split*6, split*7) == '17e9') {
        if (checkpass.substring(split*5, split*6) == 'd_91') {
         if (checkpass.substring(split*4, split*5) == 's_ba') {
          if (checkpass.substring(split*3, split*4) == 'nt_i') {
            if (checkpass.substring(split*2, split*3) == 'clie') {
              if (checkpass.substring(split, split*2) == 'CTF{') {
                if (checkpass.substring(0,split) == 'pico') {
                  alert("You got the flag!")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }
}
```

By piecing the substrings in the if statements together, we can obtain the flag.

Flag: `picoCTF{client_is_bad_9117e9}`

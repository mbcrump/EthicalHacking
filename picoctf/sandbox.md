query 

```
        var str = "";
        for (i = 0; i < 9; i++) {  
            str = str + "\n"  + _0x4b5b("0x" + [i] );
        }
        
        
        var str = "";
        for (i = 0; i < 9; i++) {  
            console.log("\n"  + "_0x4b5b(\"0x" + [i] + "\) = " + _0x4b5b("0x" + [i] ));
        }
```

```text
_0x4b5b("0x0") = getElementById
VM770:3 
_0x4b5b("0x1) = value
VM770:3 
_0x4b5b("0x2) = substring
VM770:3 
_0x4b5b("0x3) = picoCTF{
VM770:3 
_0x4b5b("0x4) = not_this
VM770:3 
_0x4b5b("0x5) = 25df2}
VM770:3 
_0x4b5b("0x6) = _again_b
VM770:3 
_0x4b5b("0x7) = this
VM770:3 
_0x4b5b("0x8) = Password Verified
```
```javascript
    checkpass = document[getElementById]("pass")[value];
    split = 4;
    if (checkpass[substring](0, split * 2) == "picoCTF{") {
        if (checkpass[substring](7, 9) == "{n") {
            if (checkpass[substring](split * 2, split * 2 * 2) == not_this) {
                if (checkpass[substring](3, 6) == "oCT") {
                    if (checkpass[substring](split * 3 * 2, split * 4 * 2) == "25df2") {
                        if (checkpass["substring"](6, 11) == "F{not") {
                            if (checkpass[substring](split * 2 * 2, split * 3 * 2) == "_again_b") {
                                if (checkpass[substring](12, 16) == this) {
                                    alert("Password Verified");
                                }
                            }
                        }
                    }
                }
            }
        }
 ```

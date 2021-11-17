# loom
![version](https://img.shields.io/github/v/release/Nanobot567/loom?label=version)
![size](https://img.shields.io/github/repo-size/Nanobot567/loom?label=size)

The encryptor/decryptor

## So... what is it?
Loom is a file encryptor. Simple as that.

## How does it encrypt files?
Essentially, Loom searches through the file that you point it to. It gets the Unicode code point for each character, and converts it to a hex code on the fly. As soon as it's converted, an integer chosen by the user (called the loomcode) is converted to a hex code as well and is added to that same character. This process is repeated until the file ends, and as soon as it's done, Loom spits out a new file. 

## What kind of encryption is that?! You can crack it super easily!
Well, if the user chooses a REALLY simple loomcode for their encryption, then yeah, it's really easy to find the correct one. The thing is, though, there are thousands of numbers you can use as your loomcode. Sure, your hex values will be huge, but it would be a LOT harder to get the correct loomcode.

## Limitations?
Python hates hex codes. You can't go over 0x110000, you can't write some chr() values. It STINKS! I would do C++ or something else, but Python is the only language I'm really fluent in. So, as of now, brute-forcing is kind of a bust :(

## Why should I care?
You shouldn't. I just made this for fun.
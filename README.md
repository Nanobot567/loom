# loom
![version](https://img.shields.io/github/v/release/Nanobot567/loom?label=version)
![size](https://img.shields.io/github/repo-size/Nanobot567/loom?label=size)

The encryptor and decryptor.

## So... what is it?
Loom is a file encryptor. Simple as that.

## How does it encrypt files, and how easy is it to crack the loomcode?
Essentially, Loom searches through the file that you point it to. It gets the Unicode code point for each character, and converts it to a hex code on the fly. As soon as it's converted, an integer chosen by the user (called the loomcode) is converted to a hex code as well and is added to that same character. This process is repeated until the file ends, and as soon as it's done, Loom spits out a new file.

As for ease of cracking the encryption, it really depends on the loomcode the user chooses. If the user chooses a REALLY simple loomcode for their encryption, then it's really easy to find the correct one. The thing is, though, there are thousands of numbers you can use as your loomcode. Sure, your hex values will be huge, but it would be a LOT harder to get the correct loomcode.

## Limitations?
You can only write characters that are in Unicode, meaning you cannot write characters that have a hex value higher than 0x110000.

## Why should I care?
You shouldn't. I just made this for fun.
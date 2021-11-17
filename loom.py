from os import read

yn = ""

try:
    from alive_progress import alive_bar
except:
    print("\nWarning: alive_progress not installed! Would you like to install it using pip? [y/n]")
    while True:
        yn = input("> ")
        if yn == "y":
            try:
                from pip import _internal
            except:
                print("ERROR: pip is not installed!")
                quit()
            try:
                _internal.main(["install","alive-progress"])
                print("Please restart loom.")
                quit()
            except:
                print("ERROR: _internal not supported!")
                quit()
        elif yn == "n":
            quit()


inputstr = ""
loomcode = ""
final = ""
ans = ""
debug = False
ver = "1.0"


print(f"""
                                  
                                     
  ██  
  ██       
  ██   ██████    ██████   ██████ ████
  ██  ██    ██  ██    ██  ██   ██   ██
  ██  ██    ██  ██    ██  ██   ██   ██
  ██   ██████    ██████   ██   ██   ██

        encryption/decryption
                 {ver}



""")
while ans != "q":
    print("Encrypt, decrypt, help, or quit? [e/d/h/q]")
    ans = input("> ")

    final = ""
    if ans == "e":
        print("Would you like to use a file as input? [y/n]")
        usefile = input("> ")
        if usefile == "y":
            filething = input("Where is the file you would like to encrypt? ")
            rfile = open(filething,"r")
            fileout = input("What should the output file be called? ")
        else:
            inputstr = input("enter text to encode: ")
        loomcode = input("loomcode (integer): ")
        # loomcode = hex(int(loomcode))

        print("Encrypting...")
        char = 0
        if usefile == "y":
            readstuff = rfile.read()
            if debug:
                print(readstuff)
            try:
                with alive_bar(len(readstuff)) as bar:
                    for i in readstuff:
                        char += 1
                        # ri = hex(int(ord(i)))
                        ri = hex(int(ord(i))+int(loomcode))
                        if char == (len(readstuff)):
                            final += str(ri)
                        else:
                            final += str(ri)+","
                        if debug:
                            print(ri)
                        bar()
            except TypeError as err:
                print(f"\nERROR! ({err})")
        else:
            try:
                with alive_bar(len(inputstr)) as bar:
                    for i in inputstr:
                        char += 1
                        # ri = hex(int(ord(i)))
                        ri = hex(int(ord(i))+int(loomcode))
                        if char == len(inputstr):
                            final += str(ri)
                        else:
                            final += str(ri)+","
                        if debug:
                            print(ri)
                        bar()
            except TypeError as err:
                print(f"ERROR! ({err})")
        if debug:
            print(final)
        if usefile == "y":
            try:
                f = open(fileout+".loomed","w")
                f.write(final)
                f.close()
            except UnicodeEncodeError as err:
                print(f"\nERROR! ({err})")
        else:
            try:
                f = open("loom_out.loomed","w")
                f.write(final)
                f.close()
            except UnicodeEncodeError as err:
                print(f"\nERROR! ({err})")

        print("Finished!")
    elif ans == "d":
        print("Would you like to use a file as input? [y/n]")
        usefile = input("> ")
        if usefile == "y":
            filething = input("Where is the file you would like to decrypt? ")
            rfile = open(filething,"r")
            fileout = input("What should the output file be called? ")
        else:
            inputstr = input("Enter hex to decode (each hex code separated by a comma): ")

        loomcode = input("loomcode (integer): ")

        print("Decrypting...")

        if usefile == "y":
            istr = rfile.read().split(",")
        else:
            istr = inputstr.split(",")

        if debug:
            print(istr)

        try:
            with alive_bar(len(istr)) as bar:
                for i in istr:
                    # ir = chr(int(i, 0))
                    ir = chr(int(i, 0)-int(loomcode))
                    final += str(ir)
                    bar()
        except Exception as err:
            print(f"ERROR! ({err})")
        
        if debug:
            print(final)
        
        try:
            f = open(fileout,"w")
            f.write(final)
            f.close()
        except UnicodeEncodeError as err:
            print(f"ERROR! ({err})")

        print("Finished!")

    elif ans == "h":
        print("\n\nWelcome to Loom!")
        print("\n----What is Loom?----\n")
        print("Loom is a file encryptor. It uses an encryption method where hex codes are replaced with the characters in the file. Read the README.md for info on how it works.")
        print("\n----Commands----\n")
        print("There are 4 commands available:\n")
        print(" e (encrypt) - encrypt files or plaintext")
        print(" d (decrypt) - decrypt your already encrypted files or plaintext")
        print(" h (help) - tells about how to use loom")
        print(" q (quit) - get outta here!\n")
        
    elif ans == "q":
        break



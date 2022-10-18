yn = ""

try:
    from alive_progress import alive_bar
except Exception:
    print("\nWarning: alive_progress not installed! Would you like to install it using pip? [y/n]")
    while True:
        yn = input("> ")
        if yn == "y":
            try:
                from pip import _internal
            except Exception:
                print("ERROR: pip is not installed!")
                quit()

            _internal.main(["install","alive-progress"])
            print("Please restart loom.")
            quit()
        elif yn == "n":
            quit()


inputstr = ""
loomcode = ""
usefile = ""
mode = ""
final = ""
ans = ""
debug = False
ver = "2.0"


print(f"""
                                  
                                     
  ██  
  ██       
  ██   ██████    ██████   ██████ ████
  ██  ██    ██  ██    ██  ██   ██   ██
  ██  ██    ██  ██    ██  ██   ██   ██
  ██   ██████    ██████   ██   ██   ██

         encryption/compression
                  {ver}



""")
while ans != "q":
    ans = input("Encryption, help, or quit? [e/h/q] ")

    final = ""
    if ans == "e":
        while mode.lower() not in ["e","d"]:
            mode = input("Encrypt or decrypt? [e/d] ")
        while usefile.lower() not in ["y","n"]:
            usefile = input("Would you like to use a file as input? [y/n] ")
        
        if usefile.lower() == "y":
            filething = input("Where is the file you would like to encrypt? ")
            rfile = open(filething,"r", encoding="utf-8")
            fileout = input("What should the output file be called? ")
        else:
            inputstr = input("Enter text: ")
        loomcode = input("loomcode (integer): ")
        # loomcode = hex(int(loomcode))

        print("Please wait...")
        char = 0
        if usefile.lower() == "y":
            inputstr = rfile.read()

        if debug:
            print(inputstr)

        try:
            if mode == "e":
                with alive_bar(len(inputstr), bar="classic", spinner="classic") as bar:
                    for i in inputstr:
                        char += 1
                        # ri = hex(int(ord(i)))
                        ri = int(ord(i))+int(loomcode)
                        final += chr(ri)
                        if debug:
                            print(ri)
                        bar.text(i+" encrypted")
                        bar()
            else:
                with alive_bar(len(inputstr), bar="classic", spinner="classic") as bar:
                    for i in inputstr:
                        # ir = chr(int(i, 0))
                        ir = chr(int(ord(i))-int(loomcode))
                        final += str(ir)
                        bar.text(i+" decrypted")
                        bar()

        except TypeError as err:
            print(f"\nERROR! ({err})")
        except Exception as err:
            print(f"\nERROR! ({err})")

        if debug:
            print(final)

        if usefile == "y":
            try:
                f = open(fileout,"w", encoding="utf-8")
                f.write(final)
                f.close()
            except UnicodeEncodeError as err:
                print(f"\nERROR! ({err})")

        print("Finished!")
    # elif ans == "c":
    #     mode = input("Compress or decompress? [c/d] ")
    #     usefile = input("Would you like to use a file as input? [y/n] ")
    #     if usefile == "y":
    #         filething = input("Where is the file? ")
    #         rfile = open(filething,"r")
    #         fileout = input("What should the output file be called? ")
    #         inputstr = rfile.read()
    #     else:
    #         inputstr = input("Enter text to encode: ")

    #     origFileLen = len(inputstr)

    #     if mode == "c":
    #         with alive_bar(len(inputstr)) as bar:
    #             for i in range(int(len(inputstr))):
    #                 # ir = chr(int(i, 0))
    #                 final += compTable[hex(ord(inputstr[i])).split("0x")[1]]
    #                 bar()
            
    #         print(origFileLen / len(final))

    #     else:
    #         with alive_bar(len(inputstr)) as bar:
    #             for i in inputstr:
    #                 # ir = chr(int(i, 0))
    #                 final += chr(int(list(compTable.keys())[list(compTable.values()).index(i)], 16))
    #                 bar()
            
    #     if usefile == "y":
    #         try:
    #             f = open(fileout,"w")
    #             f.write(final)
    #             f.close()
    #         except UnicodeEncodeError as err:
    #             print(f"\nERROR! ({err})")
    #     else:
    #         print(final)
        

    elif ans == "h":
        print("\n\nWelcome to Loom!")
        print("\n----What is Loom?----\n")
        print("Loom is a file encryptor and compressor. It uses an encryption method where hex codes are replaced with the characters in the file. Read the README.md for info on how it works.")
        print("\n----Commands----\n")
        print("There are 3 commands available:\n")
        print(" e (encryption) - encrypt or decrypt files or plaintext")
        # print(" c (compression) - compresses or decompresses files or plaintext")
        print(" h (help) - tells about how to use loom")
        print(" q (quit) - get outta here!\n")
      
    elif ans == "q":
        break
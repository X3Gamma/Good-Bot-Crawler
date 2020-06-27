# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
import sys

# Note: Compatible with python2.5>

# Only edit this if you need to change the output file name
FILE = u"role.txt"

def main():
    sep = b"\xe2\x81\xa3"
    space = b"\xe2\x80\x82"
    try:
        role = raw_input("Role name: ")
    except NameError:
        role = input("Role name: ").encode()
    if len(role) > 32:
        print("Only role names lesser than 32 characters are supported.")
        exit(1)

    # Role max char is 32
    try:
        with open(FILE, "wb") as target:
            spacereq = 32-len(role)
            if spacereq % 2:
                val = space*int(spacereq/2)
                txt = sep +space+ val+role+val+sep
            else:
                val = space*int(spacereq/2)
                txt = sep+val+role+val+sep
            target.write(txt)
    except Exception as e:
        print("Could not open '{}'.\r\n"
              "Please ensure you have file access permissions.".format(FILE))

    print("Open '{}' for the role name. You can copy and paste directly into discord.\r\n"
          "Remember to set role color as #2F3136.".format(FILE))

if __name__ == "__main__":
    if sys.version_info[0] == 2 and sys.version_info[1] < 5:
        print("Sorry. Only python2.5> is supported.")
        exit(1)
    main()

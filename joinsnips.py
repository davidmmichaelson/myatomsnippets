# joinsnips.py # David Michaelson
import os
# script that joins all "snip_*" files into the TARGET_FILE, which
# Atom expects to be "snippets.cson"


TARGET_FILE = "snippets.cson" # output file

try:
    with open(TARGET_FILE, "w+") as join:
        print(f"Creating `{TARGET_FILE}`...\n") 
        for _, _, files in os.walk(os.getcwd()): # traverses all files in local dir
            for file in files:
                if file.split('_')[0] == 'snip': # and filters for 'snip_*'
                    with open(file) as f:
                        join.write(f.read() + '\n\n')
                        print(f"...Joined `{file}` to `{TARGET_FILE}`")
    print("\nJoining success!")
except Exception as err:
    raise err

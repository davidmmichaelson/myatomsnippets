import os

TARGET_FILE = "snippets.cson"

try:
    with open(TARGET_FILE, "w+") as join:
        print(f"Creating `{TARGET_FILE}`...\n") 
        for _, _, files in os.walk(os.getcwd()):
            for file in files:
                if file.split('_')[0] == 'snip':
                    with open(file) as f:
                        join.write(f.read() + '\n\n')
                        print(f"...Joined `{file}` to `{TARGET_FILE}`")
    print("\nJoining success!")
except Exception as err:
    raise err

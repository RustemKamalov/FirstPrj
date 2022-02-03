import os
import os.path

with open("test_w.txt", "w") as out:
    for current_dir, dirs, files in os.walk("main"):
        for file in files:
            if file.endswith(".py"):
                out.write(current_dir + "\n")
                break


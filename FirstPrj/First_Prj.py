import os
import os.path

with open("test_w.txt", "w") as out:
    for current_dir, dirs, files in os.walk("main"):
        for _ in os.listdir(current_dir):
            if _.endswith(".py"):
                out.write(current_dir + "\n")
                break


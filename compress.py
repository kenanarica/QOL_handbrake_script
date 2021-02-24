import os
import sys
import crayons
import subprocess
# List the things in the directory

# Check if there's a cmdline argument for directory provided 

if len(sys.argv) < 2: 
    print("No input directory provided!")
    exit()

# get the folder
input_path = sys.argv[1]

# If we can't find the folder in the directory
e = os.listdir()
if not input_path in e:
    print(crayons.red(f"[WARNING] No directory called: {input_path} found", True))
    exit()
else: 
    print(crayons.green(f"[✓] ", True) + f"Directory found!")



# make our own post-compressed folder, if it doesn't exist



if not os.path.isdir("post-compressed clips"): 
    print(crayons.magenta("[NOTICE] ", True) + f" No path for ./post-compressed clips/ found, creating it.")
    os.mkdir("post-compressed clips")

# I know this way of using the handbrake CLI is really janky. I might fix this later, I might not. 

compression_input_path = os.listdir(input_path)
input_path = ".\\" + input_path
os.chdir(input_path)

for uncompressed_video in compression_input_path:

        if uncompressed_video is "HandBrakeCLI.exe":
            continue

        if uncompressed_video is "compressed":
            continue
        
        print(crayons.blue(f".\\HandBrakeCLI.exe -i '{uncompressed_video}\' -o '{uncompressed_video}_compressed' -e x264 -q 30 -B 160", True))
        
        # os.system(f".\\HandBrakeCLI.exe -i '{uncompressed_video}\' -o '{uncompressed_video}_compressed' -e x264 -q 30 -B 160")
        subprocess.run([".\\HandBrakeCLI.exe", "-i", uncompressed_video, "-o", ".\\compressed\\" + uncompressed_video, "-e", "x264", "-q", "30", "-B", "160"])

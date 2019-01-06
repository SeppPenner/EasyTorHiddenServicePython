import os
import subprocess

os.chdir("./web")
subprocess.run(["python", "-m", "SimpleHTTPServer", "8000"])

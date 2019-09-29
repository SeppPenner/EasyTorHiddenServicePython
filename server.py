import os
import subprocess

os.chdir("./web")
subprocess.run(["python", "-m", "http.server", "8000"])

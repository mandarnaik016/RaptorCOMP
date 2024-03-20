import subprocess
import sys
import os
 
if len(sys.argv) != 2:
    print("Usage: python script.py <file_name>")
    sys.exit(1)
 
file_name = sys.argv[1]
 
# Command 1
command1 = [
    "nz.exe",
    "x",
    "-m256m",
    f"{file_name}.pcf.srep.nz"
]
 
# Command 2
command2 = [
    "srep.exe",
     f"{file_name}.pcf.srep"
]
 
# Command 3
command3 = [
    "precomp.exe",
    "-r",
    f"{file_name}.pcf"
]
 
# Command 4
command4 = [
    "7za.exe",
    "x",
    f"{file_name}.tar",
    f"-o{file_name}"
]
 
# Execute commands
try:
    subprocess.run(command1, check=True)
    subprocess.run(command2, check=True)
    subprocess.run(command3, check=True)
    subprocess.run(command4, check=True)
    print("Commands executed successfully.")
    os.remove(f"{file_name}.tar")
    os.remove(f"{file_name}.pcf")
    os.remove(f"{file_name}.pcf.srep")

except subprocess.CalledProcessError as e:
    print("Error executing command:", e)
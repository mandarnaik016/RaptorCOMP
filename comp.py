import subprocess
import sys
import os
 
if len(sys.argv) != 3:
    print("Usage: python script.py <file_path> <file_name>")
    sys.exit(1)
 
file_path = sys.argv[1]
file_name = sys.argv[2]
 
# Command 1
command1 = [
    "7za.exe",
    "a",
    "-ttar",
    f"{file_name}.tar",
    f"{file_path}\\*"
]
 
# Command 2
command2 = [
    "precomp.exe",
    "-cn",
    "-intense",
     f"{file_name}.tar"
]
 
# Command 3
command3 = [
    "srep.exe",
    "-m5",
    f"{file_name}.pcf"
]
 
# Command 4
command4 = [
    "nz.exe",
    "a",
    "-cc",
    "-m256m",
    f"{file_name}.pcf.srep.nz",
    f"{file_name}.pcf.srep"
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
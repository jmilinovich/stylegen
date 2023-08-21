import subprocess
import webbrowser
import os
import sys
import subprocess

# Check if the flag --prompts_only is present in the command-line arguments
if '--prompts_only' in sys.argv:
    print("Running gen_prompts.py...")
    result_gen_prompts = subprocess.run([sys.executable, 'gen_prompts.py'], stderr=subprocess.PIPE)
    
    if result_gen_prompts.returncode == 0:
        print("gen_prompts.py executed successfully!")
    else:
        print("Error in executing gen_prompts.py:")
        print(result_gen_prompts.stderr.decode())
        exit(1)
    exit(0) # Exit the script after running gen_prompts.py

def install_requirements():
    # Path to the requirements.txt file
    requirements_path = 'requirements.txt'

    # Run the pip install command
    subprocess.check_call(['pip', 'install', '-r', requirements_path])

# Call the function to install the dependencies
print("Installing dependencies...")
install_requirements()


# Get the current Python executable
python_executable = sys.executable

# Running GENERATOR.PY
print("Running GENERATOR.PY...")
result_gen = subprocess.run([python_executable, 'GENERATOR.PY'], stderr=subprocess.PIPE)

if result_gen.returncode == 0:
    print("GENERATOR.PY executed successfully!")
else:
    print("Error in executing MAIN.PY:")
    print(result_gen.stderr.decode())
    exit(1)

# Running PAGEMAKER.PY
print("Running PAGEMAKER.PY...")
result_pagemaker = subprocess.run([python_executable, 'PAGEMAKER.PY'], stderr=subprocess.PIPE)

if result_pagemaker.returncode == 0:
    print("PAGEMAKER.PY executed successfully!")
else:
    print("Error in executing PAGEMAKER.PY:")
    print(result_pagemaker.stderr.decode())
    exit(1)

print("Both scripts executed successfully!")

# Open the newly created index.html file in the default web browser
index_file_path = os.path.abspath('pages/index.html')
index_url = f'file://{index_file_path}'
print(f"Opening {index_url} in the default web browser...")
webbrowser.open(index_url)
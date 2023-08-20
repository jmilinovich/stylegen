import subprocess
import webbrowser

# Running MAIN.PY
print("Running MAIN.PY...")
result_main = subprocess.run(['python', 'MAIN.PY'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result_main.returncode == 0:
    print("MAIN.PY executed successfully!")
else:
    print("Error in executing MAIN.PY:")
    print(result_main.stderr.decode())
    exit(1)

# Running PAGEMAKER.PY
print("Running PAGEMAKER.PY...")
result_pagemaker = subprocess.run(['python', 'PAGEMAKER.PY'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

if result_pagemaker.returncode == 0:
    print("PAGEMAKER.PY executed successfully!")
else:
    print("Error in executing PAGEMAKER.PY:")
    print(result_pagemaker.stderr.decode())
    exit(1)

print("Both scripts executed successfully!")

# Open the newly created index.html file in the default web browser
index_file_path = 'pages/index.html'
print(f"Opening {index_file_path} in the default web browser...")
webbrowser.open(index_file_path, new=2)

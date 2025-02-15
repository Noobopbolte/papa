import subprocess
from keep_alive import keep_alive
keep_alive()

# List of scripts to run
scripts = ["evil.py", "group.py"]

# Start each script in a new process
processes = []
for script in scripts:
    try:
        process = subprocess.Popen(["python3", script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes.append(process)
        print(f"Started {script} (PID: {process.pid})")
    except Exception as e:
        print(f"Failed to start {script}: {e}")

# Wait for all processes to complete
for process in processes:
    process.wait()

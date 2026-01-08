import subprocess
import os
import shlex

def run_shell():
    print("Custom Python Shell (PW7) - Type 'exit' to quit")
    
    while True:
        try:
            # 1. User inputs command
            user_input = input("$ ").strip()
            
            if not user_input:
                continue
            if user_input.lower() == "exit":
                break

            # 2. Support Piping: ps aux | grep term
            if "|" in user_input:
                # Split the command into parts
                cmd_parts = user_input.split("|")
                # First process
                p1 = subprocess.Popen(shlex.split(cmd_parts[0]), stdout=subprocess.PIPE)
                # Second process (takes input from p1)
                p2 = subprocess.Popen(shlex.split(cmd_parts[1]), stdin=p1.stdout)
                p1.stdout.close()
                p2.communicate()

            # 3. Support Output Redirection: ls -la > out.txt
            elif ">" in user_input:
                cmd_str, file_name = user_input.split(">")
                with open(file_name.strip(), "w") as f:
                    subprocess.run(shlex.split(cmd_str), stdout=f)

            # 4. Support Input Redirection: bc < input.txt
            elif "<" in user_input:
                cmd_str, file_name = user_input.split("<")
                if os.path.exists(file_name.strip()):
                    with open(file_name.strip(), "r") as f:
                        subprocess.run(shlex.split(cmd_str), stdin=f)
                else:
                    print(f"Error: {file_name.strip()} not found.")

            # 5. Normal Command Execution: ls -la
            else:
                subprocess.run(shlex.split(user_input))

        except Exception as e:
            print(f"Shell Error: {e}")

if __name__ == "__main__":
    run_shell()

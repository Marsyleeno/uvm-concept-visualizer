import subprocess
import sys
import os
import webbrowser

def run_uvm_test():
    try:
        print("Compiling SystemVerilog files...")
        compile_cmd = ["vlog", "coffee_pkg.sv", "coffee_if.sv", "coffee_machine.sv", "top_tb.sv"]
        subprocess.run(compile_cmd, check=True)

        print("Starting UVM simulation...")
        run_cmd = ["vsim", "-c", "top_tb", "-do", "run -all; quit"]
        subprocess.run(run_cmd, check=True)

        print("Simulation finished successfully.")

        # --- Launch & Print Animated UVM Architecture Hyperlink ---
        html_file = "uvm_coffee_sim.html"
        html_path = os.path.abspath(html_file)
        
        if os.path.exists(html_path):
            # Format the path as a valid file URL (replacing backslashes with forward slashes)
            file_url = "file:///" + html_path.replace(os.sep, "/")
            
            print("\n" + "="*70)
            print("To view the Animated UVM Architecture, Ctrl + Click the link below:")
            print(file_url)
            print("="*70 + "\n")
            
            # Optional: Keep this line if you want it to also auto-open, 
            # or delete it if you ONLY want to use the printed hyperlink.
            webbrowser.open(file_url)
        else:
            print(f"Visualization skipped: Could not find {html_file} in the current directory.")
            
    except subprocess.CalledProcessError as e:
        print(f"Simulation failed with error code: {e.returncode}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Simulator command not found. Ensure your HDL simulator is in your system PATH.")
        sys.exit(1)

if __name__ == "__main__":
    run_uvm_test()
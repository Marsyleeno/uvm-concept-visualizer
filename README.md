# UVM Concept Visualizer: Coffee Machine Analogy

<div align="center">
  <img src="https://github.com/Marsyleeno/uvm-concept-visualizer/blob/main/uvm-visualizer.png"/>
</div>

This project is a Python-automated SystemVerilog verification environment that models the Universal Verification Methodology (UVM) using an intuitive coffee machine analogy. Designed to bridge the gap between command-line Hardware Description Language (HDL) execution and system-level comprehension, it pairs a functional UVM testbench with an interactive HTML/JS visualization of the verification architecture.

## Questa Simulation & Python Automation
The verification workflow is entirely automated via a custom Python script (`run_sim.py`). Executing this script invokes the Questa simulator (via `vlog` and `vsim` commands) to compile the SystemVerilog packages (`coffee_pkg.sv`, `top_tb.sv`, etc.) and run the testbench. The core output is the Questa terminal transcript, which provides a detailed, phase-by-phase log of the UVM execution. This transcript tracks the unique transaction ID in memory and outputs a timestamped table of the monitored data, logging variables such as `size`, `with_milk`, `with_foam`, and the final `coffee_type` evaluated by the Scoreboard.

## Core Architecture & Data Flow
The testbench models a transaction lifecycle (`coffee_tr`) representing a coffee order. The workflow adheres strictly to standard UVM hierarchy:
* **Sequencer & Driver (Agent):** Generates randomized order constraints and drives them to the hardware interface.
* **DUT (Design Under Test):** The conceptual coffee machine hardware that processes the interface signals to determine the output.
* **Monitor:** Observes the interface pins and reconstructs the transaction for analysis.
* **Scoreboard:** Compares the actual DUT output against the expected reference model to verify correctness.

## Interactive UI Visualization
Upon successful completion of the Questa simulation, the Python script dynamically resolves the local file path and provides a clickable terminal link to launch the frontend visualizer (`uvm_coffee_sim.html`). The UI utilizes a responsive Flexbox layout to map the software hierarchy (Test, Env, Agent, Scoreboard) alongside the Interface and Hardware. Dynamic, Manhattan-style SVG paths animate the transaction token's flow through the system, correlating directly with the data flow steps logged in the Questa transcript.

## Usage
1. Ensure Python and a Questa HDL simulator (e.g., Intel FPGA Starter Edition) are installed and accessible in your system PATH.
2. Clone this repository and open the directory in your terminal.
3. Execute `python run_sim.py` to compile the SV files and run the UVM test.
4. Review the generated UVM transcript for the Scoreboard results, then `Ctrl + Click` the generated file URL in the terminal to watch the animated architectural flow in your browser.

# SIR Model Simulation Using Python and Mathematica

This project integrates Python with the Wolfram Mathematica kernel to simulate an SIR (Susceptible, Infected, Recovered) model, commonly used in epidemiology to understand the dynamics of infectious disease spread within a population.

## Overview

The SIR model divides the population into three compartments: susceptible, infected, and recovered. This Python script calculates the model's dynamics using Mathematica's powerful differential equation solvers and plots the results using Python's matplotlib library. The integration is managed through the Wolfram Client Library for Python.

## Requirements

- **Wolfram Mathematica**: Ensure that Mathematica is installed on your system as it provides the computational backend.
- **Python 3.x**: Python scripting language.
- **Wolfram Client for Python**: Allows Python to run Mathematica code.
- **Matplotlib**: Python plotting library.

## Setup Instructions

### Step 1: Install Mathematica

Install Mathematica from [Wolfram's official website](https://www.wolfram.com/mathematica/). Follow the installation guide provided by Wolfram to complete the setup.

### Step 2: Install Python and Required Packages

If not already installed, download and install Python from [python.org](https://www.python.org/). Then, install the required Python packages using pip:

pip install matplotlib
pip install wolframclient

### Step 3: Configure the Mathematica Kernel Path

Locate your Mathematica installation path. The Mathematica kernel, `WolframKernel`, is typically found at:

- **Windows**: `C:\Program Files\Wolfram Research\Mathematica\<version>\WolframKernel`
- **macOS**: `/Applications/Mathematica.app/Contents/MacOS/WolframKernel`
- **Linux**: `/usr/local/Wolfram/Mathematica/<version>/Executables/WolframKernel`

Ensure this path is correctly set in your Python script:

kernel_path = "/Applications/Mathematica.app/Contents/MacOS/WolframKernel"  # Update this path accordingly

### Step 4: Running the Script

Once all configurations are complete, run the Python script. Ensure that the Mathematica kernel path is correctly set in the script as shown in the setup steps. The script will execute the model in Mathematica and plot the results using matplotlib.

## Usage

Run the script with the following command:

python <script_name>.py

Replace `<script_name>` with the name of your Python script. The script will simulate the SIR model dynamics over a specified time frame and display the population changes graphically.

## Troubleshooting

If you encounter issues related to the Mathematica kernel connection, verify the kernel path and check your Mathematica installation. For issues with Python packages, ensure that all packages are installed correctly using `pip` and Python is updated to the latest version.
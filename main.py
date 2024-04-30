"""
SIR Model Simulation Using Python and Mathematica

Project Overview:
-----------------
This project integrates Python with the Wolfram Mathematica kernel to simulate an SIR (Susceptible, Infected, Recovered) model. 
The SIR model is a simple epidemiological model used to describe the spread of a disease through a population divided into 
three compartments: susceptible, infected, and recovered.

The script leverages the computational power of Mathematica's NDSolveValue function to solve the differential equations 
representing the SIR model dynamics. Python is used to handle the input/output and to plot the results using matplotlib. 
This allows for a detailed visual analysis of how an infectious disease could potentially spread through a population 
over time under given initial conditions.

Specialized Commands:
---------------------
1. `WolframLanguageSession`: Establishes a session with the Mathematica kernel. This is necessary to execute Mathematica code from Python.
2. `NDSolveValue`: A Mathematica function used to solve differential equations numerically. It is crucial for obtaining the dynamics of the SIR model.
3. `matplotlib.pyplot`: Used in Python to plot the data obtained from the Mathematica computation, allowing for visual analysis.

Method/Steps:
-------------
To successfully run this simulation, follow these steps:
1. Ensure Mathematica and Python are installed on your machine along with the required libraries (wolframclient, matplotlib).
2. Configure the path to your Mathematica kernel in the script.
3. Run the Python script. The script will communicate with Mathematica to perform the simulation and then use Python to plot the results.

Representative Example:
-----------------------
The script sets initial conditions with 1,000,000 susceptible individuals, 100 infected, and 0 recovered. It simulates the 
disease spread over 100 days, assuming very low disease transmission and recovery rates. By adjusting these rates or initial 
conditions, the user can simulate different scenarios and analyze the impacts of various intervention strategies.

Usage Guidance:
---------------
- Inputs: Adjust `S0`, `G0`, `R0`, `beta`, and `gamma` in the script to change the initial conditions and model parameters.
- Returns: The script will output a plot showing the number of susceptible, infected, and recovered individuals over time.
- Limitations: The model assumes a closed population without births, deaths (unrelated to the disease), or disease-induced mortality.

Ensure the kernel_path variable is correctly set to the location of your Mathematica installation. Run the script using a Python 
interpreter to see the epidemic curve plotted.
"""

from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr
import matplotlib.pyplot as plt

def main():
    kernel_path = "/Applications/Mathematica.app/Contents/MacOS/WolframKernel"
    with WolframLanguageSession(kernel_path) as session:
        session.start()
        # Parameters
        # Transmission rate is 0.000001, this is supposed to be beta
        # Recovery rate is 0.1, this is supposed to be gamma
        
        # Mathematica code with correctly escaped braces
        mathematica_code = """
        Module[{solution},
            solution = NDSolveValue[
            {
                S'[t] == -0.000001 * S[t] * G[t],
                G'[t] == 0.000001 * S[t] * G[t] - 0.1 * G[t],
                R'[t] == 0.1 * G[t],
                S[0] == 1000000,
                G[0] == 100,
                R[0] == 0
            },
            {S, G, R}, {t, 0, 100}, MaxSteps -> 50000
        ];
        Table[{t, solution[[1]][t], solution[[2]][t], solution[[3]][t]}, {t, 0, 100, 0.1}]
        ]
        """

        results = session.evaluate(wlexpr(mathematica_code))

        # print(results)
    # Assuming `results` is a list of tuples (t, S, G, R)
    t_values = [res[0] for res in results]
    S_values = [res[1] for res in results]
    G_values = [res[2] for res in results]
    R_values = [res[3] for res in results]

    plt.figure(figsize=(10, 6))
    plt.plot(t_values, S_values, label='Susceptible')
    plt.plot(t_values, G_values, label='Infected')
    plt.plot(t_values, R_values, label='Recovered')
    plt.title('SIR Model Simulation Results')
    plt.xlabel('Time (days)')
    plt.ylabel('Population')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

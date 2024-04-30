from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wlexpr
import matplotlib.pyplot as plt

def main():
    kernel_path = "/Applications/Mathematica.app/Contents/MacOS/WolframKernel"
    with WolframLanguageSession(kernel_path) as session:
        session.start()
        # Parameters
        # Transmission rate is 0.000001
        # Recovery rate is 0.1
        
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

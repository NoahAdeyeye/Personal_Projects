import time
import numpy as np
import matplotlib.pyplot as plt
import ODESolver
from ODESolver import ForwardEuler
from ODESolver import RungeKutta4
from ODESolver import AdamsB

start_time = time.time()

class SIR:
    def __init__(self, nu, beta, S0, I0, R0):

        if isinstance(nu, (float, int)):
            self.nu = lambda t: nu
        elif callable(nu):
            self.nu = nu

        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta

        self.initial_conditions = [S0, I0, R0]

    def __call__(self, u, t):
        S, I, R = u

        return np.asarray([
            -self.beta(t)*S*I,
            self.beta(t)*S*I - self.nu(t)*I,
            self.nu(t)*I
        ])
if __name__ == "__main__":

    sir = SIR(0.1, 0.0005, 1500, 1, 0)
    solver = ForwardEuler(sir)
    solver.set_initial_conditions(sir.initial_conditions)
    time_steps = np.linspace(0, 60, 1001)
    u, t = solver.solve(time_steps)

    
    sir_true = SIR(0.1, 0.0005, 1500, 1, 0)
    solver_true = ForwardEuler(sir_true)
    solver_true.set_initial_conditions(sir_true.initial_conditions)
    time_steps_true = np.linspace(0, 60, 10001)
    u_true, t_true = solver_true.solve(time_steps_true)

    #Convergence rate
    errors = np.abs(u_true[::10] - u)
    dt_true = time_steps_true[1] - time_steps_true[0]
    dt_approx = time_steps[1] - time_steps[0]
    p = np.log(errors[:-1] / errors[1:]) / np.log(dt_approx / dt_true)


    
    plt.plot(t, u[:, 0], label="Susceptible")
    plt.plot(t, u[:, 1], label="Infected")
    plt.plot(t, u[:, 2], label="Recovered")
    plt.legend()
    
    print(f"Convergence rate: {p[-1][0]:.3f}")
    print("--- %s seconds ---" % (time.time() - start_time))
    plt.show()


    sir = SIR(0.1, 0.0001, 1500, 1, 0)
    solver = ForwardEuler(sir)
    solver.set_initial_conditions(sir.initial_conditions)

    time_steps = np.linspace(0, 60, 1001)
    u, t = solver.solve(time_steps)

    plt.plot(t, u[:, 0], label="Susceptible")
    plt.plot(t, u[:, 1], label="Infected")
    plt.plot(t, u[:, 2], label="Recovered")
    plt.legend()
    plt.show() 

import time
import numpy as np
import matplotlib.pyplot as plt
import ODESolver
from ODESolver import ForwardEuler
from ODESolver import RungeKutta4
from ODESolver import AdamsB

start_time = time.time()

class ProblemSIRV():
    def __init__(self, nu, beta, p, S0, I0, R0, V0, T):
        
        if isinstance(nu, (float, int)):
            self.nu = lambda t: nu
        elif callable(nu):
            self.nu = nu

        if isinstance(beta, (float, int)):
            self.beta = lambda t: beta
        elif callable(beta):
            self.beta = beta

        if isinstance(p, (float, int)):
            self.p = lambda t: p
        elif callable(p):
            self.p = p

        self.initial_conditions = [S0, I0, R0, V0]

    def __call__(self, u, t):
        S, I, R, V = u

        return np.asarray([
            -self.beta(t)*S*I - self.p(t)*S,
            self.beta(t)*S*I - self.nu(t)*I,
            self.nu(t)*I,
            self.p(t)*S
        ])

class SolverSIRV():
    def __init__(self, problem, dt):
        self.problem, self.dt = problem, dt
    def solve(self, method=ODESolver.ForwardEuler):
        self.solver = method(self.problem)
        ic = [self.problem.S0, self.problem.I0, self.problem.R0]
        self.solver.set_initial_condition(ic)
        n = int(round(self.problem.T/float(self.dt)))
        t = np.linspace(0, self.problem.T, n+1)
        u, self.t = self.solver.solve(t)
        self.S, self.I, self.R, self.V = u[:,0], u[:,1], u[:,2], u[:,3]
        
if __name__ == "__main__":
    
    max_infected_list = []
    
    def max_infected(u):
        return np.max(u[:, 1])
    
    problem = ProblemSIRV(p=lambda t: 0.1 if 6 <= t <= 6 + 5 else 0, beta=.0001,
    nu=0.1, S0=1500, I0=1, R0=0, V0=0, T=60)
    solver = AdamsB(problem)
    solver.set_initial_conditions(problem.initial_conditions)


    time_steps = np.linspace(0, 60, 1001)
    u, t = solver.solve(time_steps)
    max_infected_list.append(max_infected(u))
        
    plt.plot(t, u[:, 0], label="Susceptible")
    plt.plot(t, u[:, 1], label="Infected")
    plt.plot(t, u[:, 2], label="Recovered")
    plt.plot(t, u[:, 3], label="Vaccinated")
        
        
    plt.legend()
    print("--- %s seconds ---" % (time.time() - start_time))
    plt.show()


    plt.plot(range(1, 36), max_infected_list)
    plt.xlabel("Vaccination period (VT)")
    plt.ylabel("Maximum number of infected people")
    plt.show()

import numpy as np
import matplotlib.pyplot as plt

class ODESolver:

    def __init__(self, f):
        self.f = f

    def advance(self):
        raise NotImplementedError

    def set_initial_conditions(self, U0):
        if isinstance(U0, (int,float)):
            self.number_of_equations = 1
            U0 = float(U0)
        else:
            U0 = np.asarray(U0)
            self.number_of_equations = U0.size
            
        self.U0 = U0


    def solve(self, time_points):

        self.t = np.asarray(time_points)
        n = self.t.size
        self.u = np.zeros((n, self.number_of_equations))

        self.u[0, :] = self.U0

        for i in range(n - 1):
            self.i = i
            self.u[i + 1] = self.advance()

        return self.u[:i+2] , self.t[:i+2]
    
# First method, Leapfrog
class ForwardEuler(ODESolver):
    def advance(self):
        u, f, i, t = self.u, self.f, self.i, self.t
        dt = t[i +1] - t[i]
        return u[i, :] + dt * f(u[i, :], t[i])

# Second method, Runge kutta fourth order
class RungeKutta4(ODESolver):
    def advance(self):
        u, f, i, t = self.u, self.f, self.i, self.t
        dt = t[i +1] - t[i]
        k1 = f(u[i, :], t[i])
        k2 = f(u[i, :] + k1*dt/2, t[i] + dt/2)
        k3 = f(u[i, :] + k2*dt/2, t[i] + dt/2)
        k4 = f(u[i, :] + k3*dt, t[i] + dt)
        return u[i, :] + dt/6*(k1 + 2*k2 + 2*k3 + k4)

#Third method, Third-order Adams-Bashforth
class AdamsB(ODESolver):
    def advance(self):
        u, f, i, t = self.u, self.f, self.i, self.t
        dt = t[i +1] - t[i]
        f_1 = f(u[i,:],t[i])
        f_2 = f(f_1, t[i])
        return u[i,:] + dt * f_1 + ((dt**2)/2) * f_2




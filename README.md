# Generalised Runge-Kutta Method implementation:

A general runge kutta class implementation with function definitions to sovle implicitly or explicitly. Functionality is tested using the Dahliquist equation.

## Code Functions:

**assignemnt_re.py:** 
 - Defines the dahlquist problem by creating an object of the dahlquist class
 - Creates the RK method object (implcit or explicit) by supplying the Butcher table values and the dahlquist problem object to the Rk_general class.
 - Plots the results of solution and error over iterations

**Dahlquist.py:**
 - Class definition for instantiating dahlquist problem object

**RK_general.py:** 
- implements the implict and explcit solver functions (sol_imp() and sol_exp())
- Calls the Newton sovler to solve for slopes in implicit case
- evaluates the slopes in the explicit solver function for explicit case
- Integrates the equation over time, based on the slope evaluations

**newton.py:** 
- Implements a general newton method to solve iteratively for the slopes of the implicit RK method







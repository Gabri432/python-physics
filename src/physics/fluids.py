"""
MODULE NAME: fluids

DESCRIPTION: A collection of various Physics formulas related to Fluid Dynamics.

LINKS:
github - https://github.com/Gabri432/python-physics/blob/master/src/physics/fluids.py
"""

from physics import mathem

#Hagen-Poiseuille law, check for more information https://en.wikipedia.org/wiki/Hagen%E2%80%93Poiseuille_equation
def law_Hagen_Poiseuille(fluid_viscosity: float, pipe_length: float, flow_rate: float, pipeRadius: float) -> float:
	"""Calculates delta_p = ((8 * fluid_viscosity * pipe_length * flow_rate) / (greek_pi * (pipeRadius**4))), where greek_pi = 3.1416.

    Parameters:
    ----------
        - fluid_viscosity (Pascal*second), a float representing the fluid viscosity. 
        - pipe_length (meters), a float representing the length of the pipe.
		- flow_rate (cube meters per second) a float representing the flow rate.
		- pipe_radius (meters), a float representing the pipe radius.

    Returns:
    ---------
        A float representing the pressure difference as result of that fluid viscosity, pipe length, flow rate and pipe radius.
    
    """
	return ((8 * fluid_viscosity * pipe_length * flow_rate) / (mathem.greek_pi * pipeRadius**4)), "Pascal"

#Stokes law, check for more information https://en.wikipedia.org/wiki/Stokes%27_law
def law_Stokes(fluid_viscosity: float, radius: float, speed: float) -> float:
	"""Calculates F = 6 * greek_pi * fluid_viscosity * radius * speed, where greek_pi = 3.1416.

    Parameters:
    ----------
        - fluid_viscosity (Pascal*second), a float representing the fluid viscosity. 
        - radius (meters), a float representing the radius of the particle.
		- speed (meters per second), a float representing the speed of the particle.

    Returns:
    ---------
        A float representing the force as result of that mass and acceleration.
    
    """
	return 6 * mathem.greek_pi * fluid_viscosity * radius * speed, "N"
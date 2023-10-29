"""
MODULE NAME: fluids

DESCRIPTION: A collection of various Physics formulas related to Gravitational laws.

LINKS:
github - https://github.com/Gabri432/python-physics/blob/master/physics/fluids.py
"""

from physics import constants

#Potential Gravitational Energy, check for more information https://en.wikipedia.org/wiki/Gravitational_energy
def potential_grav_energy(mass: float, height: float) -> float:
	"""Calculates Potential Grav. Energy = mass * g * height, where g is 9.81.

    Parameters:
    ----------
        - mass (kilograms), a float representing the mass of the object. 
        - height (meters/s**2), a float representing the height.

    Returns:
    ---------
        A float representing the Potential Gravitational Energy as result of that mass and height.
    
    """
	return mass * constants.GRAVITY * height, "J"

#Universal Gravitational Law (Gravitational Attraction Law), check for more information https://en.wikipedia.org/wiki/Newton%27s_law_of_universal_gravitation
def grav_attraction(mass1: float, mass2: float, distance: float) -> float:
	"""Calculates F = (G * mass1* mass2) / (distance**2), where G = 6.67*10**-11.

    Parameters:
    ----------
        - mass1 (kilograms), a float representing the mass of the first object.
		- mass2 (kilograms), a float representing the mass of the second object. 
        - distance (meters), a float representing the distance between the two objects.

    Returns:
    ---------
        A float representing the Gravitational Attraction Force as result of that masses and distance.
    
    """
	return (constants.G * mass1 * mass2) / (distance**2), "N"

#Gravitational Field of an object, check for more information https://en.wikipedia.org/wiki/Gravity
def grav_field(mass: float, radius: float) -> float:
	"""Calculates Gravitational Field = (G * m) / distance**2.

    Parameters:
    ----------
        - mass (kilograms), a float representing the mass of the object. 
        - distance (meters), a float representing the distance between the two objects.

    Returns:
    ---------
        A float representing the Gravitational Field as result of that mass and radius.
    
    """
	return (constants.G * mass) / (radius**2), "m/s^2"

#Potential Gravitatonal Energy between two masses, check for more information https://en.wikipedia.org/wiki/Gravitational_energy
def potential_grav_energy_2(mass1: float, mass2: float, distance: float) -> float:
	"""Calculates PGE = -1 * ((G * mass1 * mass2) / (distance)), where G = 6.67*10**-11

    Parameters:
    ----------
        - mass1 (kilograms), a float representing the mass of the first object.
		- mass2 (kilograms), a float representing the mass of the second object. 
        - distance (meters), a float representing the distance between the two objects.


    Returns:
    ---------
        A float representing the Potential Gravitational Energy as result of that masses and distance.
    
    """
	return -1 * ((constants.G * mass1 * mass2) / (distance)), "J"

#Escape Speed, check for more information https://en.wikipedia.org/wiki/Escape_velocity
def escape_speed(mass: float, radius: float) -> float:
	"""Calculates v = ((2 * G * mass) / (radius))**(1/2).

    Parameters:
    ----------
        - mass (kilograms), a float representing the mass of the object. 
        - radius (meters), a float representing the radius of the planet.

    Returns:
    ---------
        A float representing the Escape Speed as result of that mass and radius.
    
    """
	return ((2 * constants.G * mass) / (radius))**(1/2), "m/s"
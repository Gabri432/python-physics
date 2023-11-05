"""
MODULE NAME: relativity

DESCRIPTION: A collection of various Physics formulas related to the Relativity field.

LINKS:
github - https://github.com/Gabri432/python-physics/blob/master/src/physics/relativity.py
"""

import math
from physics import constants

#Relativistic time (Time dilatation), check for more information https://en.wikipedia.org/wiki/Time_dilation
def relative_time(traveler_time: float, speed: float) -> float:
	"""Calculates relative_time = traveler_time * lorentz_factor(speed).

    Parameters:
    ----------
        - traveler_time (seconds), a float representing the time for the traveler. 
        - speed (meters per second), a float representing the speed of the traveler.

    Returns:
    ---------
        A float representing the moving observer time as result of that traveler time and speed.
    
    """
	return traveler_time * lorentz_factor(speed), "s"

#Lorentz factor, check for more information https://en.wikipedia.org/wiki/Lorentz_factor
def lorentz_factor(speed: float) -> float:
	"""Calculates y = 1 / [square_root( 1  - fraction)], where:\n
	   fraction = speed**2/light_speed**2

    Parameters:
    ----------
        - speed (meters per second), a float representing the speed of the traveler.

    Returns:
    ---------
        A float representing the value of the Lorentz factor as result of that speed.
    
    """
	return 1 / ((math.sqrt(1-((speed**2)/(constants.C**2)))))

#Relativistic distance (Compression of distances) in meters, check for more information https://en.wikipedia.org/wiki/Proper_length
def relative_distance(non_traveler_distance: float, speed: float) -> float:
	"""Calculates compressed_distance = non_traveler_distance / lorentz_factor(speed).

    Parameters:
    ----------
        - non_traveler_distance (meters), a float representing the distance for the non-traveler. 
        - speed (meters per second), a float representing the speed of the traveler.

    Returns:
    ---------
        A float representing the contractedDistance as result of that distance observed at rest and speed.
    
    """
	return non_traveler_distance / lorentz_factor(speed), "m"

#Relativistic Mass (Increment of Mass), check for more information https://en.wikipedia.org/wiki/Mass_in_special_relativity
def relative_mass(traveler_mass: float, speed: float) -> float:
	"""Calculates relative_mass = traveler_mass * lorentz_factor(speed).

    Parameters:
    ----------
        - traveler_mass (kilograms), a float representing the mass of the traveler. 
        - speed (meters per second), a float representing the speed of the traveler.

    Returns:
    ---------
        A float representing the relativistic mass as result of that traveler mass and speed.
    
    """
	return traveler_mass * lorentz_factor(speed), "kg"

#Relativistic Momentum (Increment of Momentum), check for more information https://en.wikipedia.org/wiki/Energy%E2%80%93momentum_relation
def relative_momentum(traveler_momentum: float, speed: float) -> float:
	"""Calculates relative_momentum = (traveler_momentum * speed) * lorentz_factor(speed).

    Parameters:
    ----------
        - traveler_momentum (kilograms * m/s), a float representing the mass of the traveler. 
        - speed (meters per second), a float representing the speed of the traveler.

    Returns:
    ---------
        A float representing the relativistic Momentum as result of that traveler momentum and speed.
    
    """
	return (traveler_momentum * speed) * lorentz_factor(speed), "kg*m/s"

#Photoelettric effect, check for more information https://en.wikipedia.org/wiki/Photoelectric_effect
def photo_elettric_effect(frequency: float) -> float:
	"""Calculates energy = Planck_constant * frequency.

    Parameters:
    ----------
        - frequency (kilograms), a float representing the frequency of the electromagnetic wave.

    Returns:
    ---------
        A float representing the energy needed to remove an electron from a material as result of that frequency.
    
    """
	return constants.PLANCK * frequency, "J"
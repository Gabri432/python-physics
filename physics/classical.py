"""
MODULE NAME: classical

DESCRIPTION: A collection of various Physics formulas related to Cinematics and Dynamics.

LINKS:
github - https://github.com/Gabri432/python-physics/blob/master/physics/classical.py
"""

def force(mass: float, acceleration: float) -> float:
    """Calculates F = mass*acceleration.

    Parameters:
    ----------
        - mass (kilograms), a float representing the mass of the object. 
        - acceleration (meters/s^2), a float representing the acceleration of the object.

    Returns:
    ---------
        A float representing the force as result of that mass and acceleration.
    
    """
    return mass*acceleration

def speed(distance: float, time: float) ->  float:
    """Calculates v = distance/time.

    Parameters:
    ----------
        - distance (meters), a float representing a distance. 
        - time (seconds), a float representing the time to cover such distance.

    Returns:
    ---------
        A float representing the speed as result of that distance and time.
    
    """
    return distance/time

def time(distance: float, speed: float) -> float:
    """Calculates t = distance/speed.

    Parameters:
    ----------
        - distance (meters), a float representing a distance. 
        - speed (meters/seconds), a float representing the speed of an object.

    Returns:
    ---------
        A float representing the time as result of that distance and speed.
    
    """
    return distance/speed
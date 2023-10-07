"""
MODULE NAME: classical

DESCRIPTION: A collection of various Physics formulas related to Cinematics and Dynamics.

LINKS:
github - https://github.com/Gabri432/python-physics/blob/master/physics/classical.py
"""

def force(mass, acceleration):
    """Calculates F = mass*acceleration.

    Parameters:
    ----------
        - mass, a float representing the mass of the object. 
        - acceleration, a float representing the acceleration of the object.

    Returns:
    ---------
        A float representing the force as result of that mass and acceleration.
    
    """
    return mass*acceleration
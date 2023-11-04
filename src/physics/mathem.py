"""
MODULE NAME: mathem

DESCRIPTION: A collection of some Math formulas and constants used in the library.

LINKS:
github - https://github.com/Gabri432/python-physics/blob/master/physics/mathem.py
"""
import math

greek_pi = 3.1416

radiant_to_deg = 57.2958

def sine_square(angle: float) -> float:
	"""Calculates sine**2(angle) = (1 - cosine(2*angle)) / 2.

    Parameters:
    ----------
        - angle (degrees)
	"""
	return (1 - math.cos(2*(angle/57.2958))) / 2

def cosine_square(angle: float) -> float: 
	"""Calculates cosine**2(angle) = 1 - sine**2(angle).

    Parameters:
    ----------
        - angle (degrees)
	"""
	return 1 - sine_square(angle)

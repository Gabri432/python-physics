"""
MODULE NAME: electromagnetism

DESCRIPTION: A collection of various Physics formulas related to Electromagnetism.

LINKS:
github - https://github.com/Gabri432/python-physics/blob/master/src/physics/electromagnetism.py
"""
import math
from physics import constants

#Coulomb law formula, check for more information https://en.wikipedia.org/wiki/Coulomb%27s_law
def law_Coulomb(charge1: float, charge2: float, distance: float) -> float: 
	"""Calculates electro_static_force = k * charge1 * charge2 / (distance**2), k is Coulumb constant.

    Parameters:
    ----------
        - charge1, charge2 (Coulomb), two floats representing the charges of the particles. 
        - distance (meters), a float representing the distance between the particles.

    Returns:
    ---------
        A float representing the Electrostatic force between the particles as result of that charges and distance.
    
    """
	return constants.COULOMB * (math.abs(charge1) * math.Abs(charge2)) / (distance * distance), "N"

#Gauss theorem, Flux of electric field, check for more information https://en.wikipedia.org/wiki/Gauss%27s_law
def gauss_flux(charge: float) -> float:
	"""Calculates electric_flux = charge / e0, where e0 is the Vacuum Permittivity.

    Parameters:
    ----------
        - charge (Coulomb), a float representing the charge of the particle.

    Returns:
    ---------
        A float representing the Electric Flux as result of that charge.
    
    """
	return charge / constants.VACUUM_PERMITTIVITY, "N*m^2/C"

#Electric Field, check for more information https://en.wikipedia.org/wiki/Electric_potential
#or https://phys.libretexts.org/Bookshelves/College_Physics/Book%3A_College_Physics_(OpenStax)/19%3A_Electric_Potential_and_Electric_Field/19.01%3A_Electric_Potential_Energy-_Potential_Difference
def electric_field(charge: float, radius: float) -> float:
	"""Calculates electric_field = k * charge1 * charge2 / (distance**2), k is Coulumb constant.

    Parameters:
    ----------
        - charge1, charge2 (Coulomb), two floats representing the charges of the particles. 
        - distance (meters), a float representing the distance between the particles.

    Returns:
    ---------
        A float representing the Electrostatic Force between the particles as result of that charges and distance.
    
    """
	return (charge) / (4 * 3.1416 * constants.VACUUM_PERMITTIVITY * radius * radius), "N/C"

#Electric Potential on electric Field formula from a point-like charge, check for more information https://en.wikipedia.org/wiki/Electric_potential
#or https://phys.libretexts.org/Bookshelves/College_Physics/Book%3A_College_Physics_(OpenStax)/19%3A_Electric_Potential_and_Electric_Field/19.01%3A_Electric_Potential_Energy-_Potential_Difference
def electric_potential(charge: float, distance: float) -> float:
	"""Calculates electro_potential = charge / (4 * greek_pi * e0 * distance), where greek_pi = 3.1416, e0 is the vacuum permittivity.

    Parameters:
    ----------
        - charge1, charge2 (Coulomb), two floats representing the charges of the particles. 
        - distance (meters), a float representing the distance at which the potential is evaluated.

    Returns:
    ---------
        A float representing the Electric Potential between the particles as result of that charges and distance.
    
    """
	return (charge) / (4 * 3.1416 * constants.VACUUM_PERMITTIVITY * distance), "V"

#Electric Potential Energy between two particles (do not confuse it with Voltage), check for more information https://en.wikipedia.org/wiki/Electric_potential_energy
#or https://phys.libretexts.org/Bookshelves/College_Physics/Book%3A_College_Physics_(OpenStax)/19%3A_Electric_Potential_and_Electric_Field/19.01%3A_Electric_Potential_Energy-_Potential_Difference
def electric_potent_energy_two(charge1: float, charge2: float, distance: float) -> float:
	"""Calculates electric_potential_energy_of_two_charges = [(charge1 * charge2) / (4 * greek_pi * e0)] * [(1 / distance)], where greek_pi = 3.1416, e0 is the vacuum permittivity.

    Parameters:
    ----------
        - charge1, charge2 (Coulomb), two floats representing the charges of the particles. 
        - distance1 (meters), a float representing the distance between the particles.

    Returns:
    ---------
        A float representing the Electric Potential Difference between the particles as result of that charges and distances.
    
    """
	return ((charge1 * charge2) / (4 * 3.1416 * constants.VACUUM_PERMITTIVITY)) * ((1 / distance)), "J"

#Electric Potential Difference, or Voltage, between two point from the charge position, check for more information https://en.wikipedia.org/wiki/Voltage
#or https://phys.libretexts.org/Bookshelves/College_Physics/Book%3A_College_Physics_(OpenStax)/19%3A_Electric_Potential_and_Electric_Field/19.01%3A_Electric_Potential_Energy-_Potential_Difference
def electric_potent_diff(charge: float, distance1: float, distance2: float) -> float:
	"""Calculates electric_potential_difference or voltage due to a charge = [charge / (4 * greek_pi * e0)] * [(1 / distance1) - (1 / distance2)], where greek_pi = 3.1416, e0 is the vacuum permittivity.

    Parameters:
    ----------
        - charge (Coulomb), a float representing the charge of the particle. 
        - distance1, distance2 (meters), two floats representing two distances between the particle and the two points.

    Returns:
    ---------
        A float representing the Voltage or Electrostatic Potential Difference between two points due to a charge between as result of that charge and distances.
    
    """
	return (charge / (4 * 3.1416 * constants.VACUUM_PERMITTIVITY)) * ((1 / distance1) - (1 / distance2)), "V"

#Voltage, or Electric Potential Difference, between two point from the charge position, check for more information https://en.wikipedia.org/wiki/Voltage
#or https://phys.libretexts.org/Bookshelves/College_Physics/Book%3A_College_Physics_(OpenStax)/19%3A_Electric_Potential_and_Electric_Field/19.01%3A_Electric_Potential_Energy-_Potential_Difference
def voltage(charge: float, distance1: float, distance2: float) -> float:
	"""Calculates electric_potential_difference or voltage due to a charge = [charge / (4 * greek_pi * e0)] * [(1 / distance1) - (1 / distance2)], where greek_pi = 3.1416, e0 is the vacuum permittivity.

    Parameters:
    ----------
        - charge (Coulomb), a float representing the charge of the particle. 
        - distance1, distance2 (meters), two floats representing two distances between the particle and the two points.

    Returns:
    ---------
        A float representing the Voltage or Electrostatic Potential Difference between two points due to a charge between as result of that charge and distances.
    
    """
	return electric_potent_diff(charge, distance1, distance2)

#Conductor capacitance, check for more information https://en.wikipedia.org/wiki/Capacitance
def self_capacitance(charge: float, potential: float) -> float:
	"""Calculates capacitance = charge / potential.

    Parameters:
    ----------
        - charge (Coulomb), a float representing the charge of a particle. 
        - potential (Volt), a float representing the potential of a particle.

    Returns:
    ---------
        A float representing the Capacitance as result of that charge and potential.
    
    """
	return charge / potential, "C/V"

#Sphere Conductor capacitance, check for more information https://en.wikipedia.org/wiki/Capacitance
def self_capacitance_sphere(radius: float) -> float:
	"""Calculates capacitance = 4 * greek_pi * e0 * radius, where greek_pi = 3.1416, e0 is the vacuum permittivity.

    Parameters:
    ----------
        - radius (meters), a float representing the sphere radius.

    Returns:
    ---------
        A float representing the Capacitance as result of that radius.
    
    """
	return 4 * 3.14159 * constants.VACUUM_PERMITTIVITY * radius, "C/V"

#Density of energy of Electric Field, check for more information https://en.wikipedia.org/wiki/Electric_potential_energy
def energy_dens_electric_field(electric_field: float) -> float:
	"""Calculates energy_density_electric_field = (1 / 2) * e0 * (electric_field**2), is the vacuum permittivity.

    Parameters:
    ----------
        - electric_field (Volt/meters), a float representing the electric field.

    Returns:
    ---------
        A float representing the Energy Density of an Electric Field as result of that electric field.
    
    """
	return (1 / 2) * constants.VACUUM_PERMITTIVITY * (electric_field * electric_field), "J/m^3"

#First Ohm law, check for more information https://en.wikipedia.org/wiki/Ohm%27s_law
def law_ohm1_voltage(resistance: float, current_intensity: float) -> float:
	"""Calculates voltage = resistance * current_intensity.

    Parameters:
    ----------
        - resistance (ohm), two floats representing the resistance of the conductor. 
        - current_intensity (Ampere), a float representing the current intensity of through the conductor.

    Returns:
    ---------
        A float representing the Voltage as result of that resistance and current intensity.
    
    """
	return resistance * current_intensity, "V"

#Second Ohm law, check for more information https://en.wikipedia.org/wiki/Ohm%27s_law
def law_ohm2_resistance(resistivity: float, length: float, area: float) -> float:
	"""Calculates electro_static_force = k * charge1 * charge2 / (distance**2), k is Coulumb constant.

    Parameters:
    ----------
        - resistivity (Ohm*meters), a float representing the electrical resistivity of the material. 
        - length (meters), a float representing the length of the conductor.
		- area (square meters), a float representing the the cross-sectional area of the conductor.

    Returns:
    ---------
        A float representing the Resistance of the conductor as result of that resistivity, length and area.
    
    """
	return resistivity * length / area, "Ohm"

#Drift Speed, check for more information https://en.wikipedia.org/wiki/Drift_velocity
def drift_speed(intensity: float, charge_carrier_density: float, area: float, charge: float) -> float: #(driftVelocity float64, measurementUnit string)
	"""Calculates drift_speed = intensity / (charge_carrier_density * area * charge).

    Parameters:
    ----------
        - intensity (Ampere), a float representing the current intensity through the material. 
		- charge_carrier_density (electron per cubic meters), a float representing the charge-carrier number density. 
        - area (square meters), a float representing the cross-sectional area of the wire.
		- charge (Coulomb), a float representing the charge of the particle

    Returns:
    ---------
        A float representing the Drift speed as result of that intensity, charge-carrier density, area, and charge.
    
    """
	return intensity / (charge_carrier_density * area * charge), "m/s"

#Energy Density of electric and magnetic fields, check for more information https://en.wikipedia.org/wiki/Energy_density
def energy_density(electric_field: float, magnetic_field: float) -> float:
	"""Calculates energy_density = [1/2]*[(1/p0)*(magnetic_field**2) + e0*(electric_field**2)], d0 is the dielectric constant, p0 is the vacuum permeability.

    Parameters:
    ----------
        - electric_field (N/C), a float representing the electric field. 
        - magnetic_field (Ampere/meters), a float representing the magnetic field.

    Returns:
    ---------
        A float representing the Energy Density of the electric and magnetic field between the particles as result of that charges and distance.
    
    """
	return (1/2)*((1/constants.VACUUM_PERMEABILITY)*(magnetic_field**2) + constants.DIELECTRIC*(electric_field**2)), "J/m^3"
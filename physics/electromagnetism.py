"""
MODULE NAME: electromagnetism

DESCRIPTION: A collection of various Physics formulas related to Electromagnetism.

LINKS:
github - https://github.com/Gabri432/python-physics/blob/master/physics/electromagnetism.py
"""
import math
import constants

#Coulomb law formula, check for more information https://en.wikipedia.org/wiki/Coulomb%27s_law
def LawCoulomb(charge1: float, charge2: float, distance: float) -> float: #(electroStaticForce float64, measurementUnit string) {
	return constants.COULOMB * (math.abs(charge1) * math.Abs(charge2)) / (distance * distance), "N"

#Gauss theorem, Flux of electric field, check for more information https://en.wikipedia.org/wiki/Gauss%27s_law
def GaussFlux(charge: float) -> float:
	return charge / constants.VACUUM_PERMITTIVITY, "N*m^2/C"

#Electric Field, check for more information https://en.wikipedia.org/wiki/Electric_potential
#or https://phys.libretexts.org/Bookshelves/College_Physics/Book%3A_College_Physics_(OpenStax)/19%3A_Electric_Potential_and_Electric_Field/19.01%3A_Electric_Potential_Energy-_Potential_Difference
def ElectricField(charge: float, radius: float) -> float:
	return (charge) / (4 * 3.1416 * constants.VACUUM_PERMITTIVITY * radius * radius), "N/C"

#Electric Potential on electric Field formula from a point-like charge, check for more information https://en.wikipedia.org/wiki/Electric_potential
#or https://phys.libretexts.org/Bookshelves/College_Physics/Book%3A_College_Physics_(OpenStax)/19%3A_Electric_Potential_and_Electric_Field/19.01%3A_Electric_Potential_Energy-_Potential_Difference
def ElectricPotential(charge: float, distance: float) -> float:
	return (charge) / (4 * 3.1416 * constants.VACUUM_PERMITTIVITY * distance), "V"

#Electric Potential Energy Difference (do not confuse it with Voltage), check for more information https://en.wikipedia.org/wiki/Electric_potential_energy
#or https://phys.libretexts.org/Bookshelves/College_Physics/Book%3A_College_Physics_(OpenStax)/19%3A_Electric_Potential_and_Electric_Field/19.01%3A_Electric_Potential_Energy-_Potential_Difference
def ElectricPotentEnergyDiff(charge1: float, charge2: float, distance1: float, distance2: float) -> float:
	return ((charge1 * charge2) / (4 * 3.1416 * constants.VACUUM_PERMITTIVITY)) * ((1 / distance1) - (1 / distance2)), "J"

#Electric Potential Difference, or Voltage, between two point from the charge position, check for more information https://en.wikipedia.org/wiki/Voltage
#or https://phys.libretexts.org/Bookshelves/College_Physics/Book%3A_College_Physics_(OpenStax)/19%3A_Electric_Potential_and_Electric_Field/19.01%3A_Electric_Potential_Energy-_Potential_Difference
def ElectricPotentDiff(charge: float, distance1: float, distance2: float) -> float:
	return (charge / (4 * 3.1416 * constants.VACUUM_PERMITTIVITY)) * ((1 / distance1) - (1 / distance2)), "V"

#Voltage, or Electric Potential Difference, between two point from the charge position, check for more information https://en.wikipedia.org/wiki/Voltage
#or https://phys.libretexts.org/Bookshelves/College_Physics/Book%3A_College_Physics_(OpenStax)/19%3A_Electric_Potential_and_Electric_Field/19.01%3A_Electric_Potential_Energy-_Potential_Difference
def Voltage(charge: float, distance1: float, distance2: float) -> float:
	return ElectricPotentDiff(charge, distance1, distance2)

#Conductor capacitance, check for more information https://en.wikipedia.org/wiki/Capacitance
def SelfCapacitance(charge: float, potential: float) -> float: #(coulombPotential float64, measurementUnit string) {
	return charge / potential, "C/V"

#Sphere Conductor capacitance, check for more information https://en.wikipedia.org/wiki/Capacitance
def SelfCapacitanceSphere(radius: float) -> float: #(coulombPotential float64, measurementUnit string) {
	return 4 * 3.14159 * constants.VACUUM_PERMITTIVITY * radius, "C/V"

#Density of energy of Electric Field, check for more information https://en.wikipedia.org/wiki/Electric_potential_energy
def EnergyDens(electricFieldModule: float) -> float:
	return (1 / 2) * constants.VACUUM_PERMITTIVITY * (electricFieldModule * electricFieldModule), "J/m^3"

#First Ohm law, check for more information https://en.wikipedia.org/wiki/Ohm%27s_law
def LawOhm1(resistance: float, currentIntensity: float) -> float: #(voltage float64, measurementUnit string)
	return resistance * currentIntensity, "V"

#Second Ohm law, check for more information https://en.wikipedia.org/wiki/Ohm%27s_law
def LawOhm2(resistivity: float, length: float, area: float) -> float: #(electricalResistance float64, measurementUnit string)
	return resistivity * length / area, "Ohm"

#Drift Speed, check for more information https://en.wikipedia.org/wiki/Drift_velocity
def DriftSpeed(intensity: float, chargeCarrierDensity: float, area: float, particleCharge: float) -> float: #(driftVelocity float64, measurementUnit string)
	return intensity / (chargeCarrierDensity * area * particleCharge), "m/s"

#Energy Density of electric and magnetic fields, check for more information https://en.wikipedia.org/wiki/Energy_density
def EnergyDensity(electricField: float, magneticField: float) -> float:
	return (1/2)*constants.DIELECTRIC*(electricField*electricField) + (1/(2*constants.VACUUM_PERMEABILITY))*(magneticField*magneticField), "J/m^3"
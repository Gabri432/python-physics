"""
MODULE NAME: constants

DESCRIPTION: A collection of various Physics constants, across different fields.

LINKS:
github - https://github.com/Gabri432/python-physics/blob/master/src/physics/constants.py
"""

#Earth Gravity constant in meters per square second
GRAVITY = 9.81

#Light speed on vacuum in meters per second.
LIGHT_SPEED = 299792452
C = LIGHT_SPEED

#Distance Moon-Earth in meters
LUNARDIST = 384_000_000

#Distance Moon-Earth in meters
LUNARDIST_MIN = 362_000_000

#Distance Moon-Earth in meters
LUNARDIST_MAX = 405_000_000

#Speed of sound on air in meters per sec.
SOUND = 340

#Astronomical Unit in meters
AU = 149_000_000_000

#Parsec in meters
PARSEC = 3.08e16

#Earth Mass in kilograms
EARTH_MASS = 5.98e24

#Sun Mass in kilograms
SUN_MASS = 1.98e30

#Moon Mass in kilograms
MOON_MASS = 7.342e22

#Earth Radius in meters
EARTH_RADIUS = 6378e3

#Sun Radius in meters
SUN_RADIUS = 69634e4

#Moon Radius in meters
MOON_RADIUS = 1731e3

#Universal Gravity Constant in [(Newton * meters^2) / (kilograms^2)]
G = 6.67e-11

#Light year in meters
LIGHT_YEAR = 9.46e15

#Hubble Constant in (km/s)/Mpc, Mpc is MegaParsec, for more info https:#en.wikipedia.org/wiki/Hubble%27s_law
HUBBLE = 69.8

#Proton Mass in kilograms
PROTON_MASS = 1.672e-27

#Electron Mass in kilograms
ELECTRON_MASS = 9.109e-31

#Neutron Mass in kilograms
NEUTRON_MASS = 1.674e-27

#Absolute Zero in Celsius Deg
ABS_ZERO = -273

#Avogadro Constant (with grams) in molecules per mole
AVOGADRO = 6.022e23

#Ideal Gasses Constant in [(Joule) / (Mole × Kelvin Degrees)]
R = 8.316

#Thermal Expansion Coefficient 1/273 <=> 0.036
THERM_EXPANSCOEFF = 1 / 273

#Planck Constant in [(meters^2 × kilograms) / (seconds)]
PLANCK = 6.6260693e-34

#Planck Mass in kilograms
PLANCK_MASS = 2.17645e-8

#Planck Time in seconds
PLANCK_TIME = 5.391e-44

#Stefan-Boltzmann Constant in [Watt/(meters^2 * Kelvin^4)]
STEFBOLTZ = 5.67e-8

#Coulomb constant in [Newton × (meters^2) / (Coulomb^2)]
COULOMB = 8.988e9

#Dielectric constant in vacuum in [Faraday/meters]
DIELECTRIC = 8.854e-12
E_0 = DIELECTRIC
VACUUM_PERMITTIVITY = DIELECTRIC

#Vacuum Permability in Henry units per meter, or Newtons per square Ampere
VACUUM_PERMEABILITY = 1.256637e-6

#Elementary Charge in Coulomb
ELEM_CHARGE = 1.602e-19

#Silver resistivity at 20 °C
SILVER_RESISTIVITY = 1.59e-8

#Copper resistivity at 20 °C
COPPER_RESISTIVITY = 1.68e-8

#Iron resistivity at 20 °C
IRON_RESISTIVITY = 9.7e-8

#Stainless Steel resistivity at 20 °C
STEEL_RESISTIVITY = 69.0e-8

#Proportionality constant in [Newton/(Amprere**2)]
PROPORTION_CONST = 2.7e-7

#Weber in [Maxwell]
WEBER = 10e8

#Tesla in [Gauss]
TESLA = 10e4

#Atomic Mass in kilograms
ATOM_MASS = 1.66053e-27

#Air Density in [kilograms/(meters**3)]
AIR_DENSITY = 1.29

#Water Density in [kilograms/(meters**3)]
WATER_DENSITY = 10e3

#Helium Mass
HELIUM_MASS = 5.006e-27

#Atmosphere in Pascal
ATM = 1.013e5

#Angstrom in meters
ANGSTROM = 10e-19

#Water viscosity at 0 Celsius deg, in [pascal*seconds]
WATER_VISCOSITY_DEG_0 = 1.8e-3

#Water viscosity at 20 Celsius deg, in [pascal*seconds]
WATER_VISCOSITY_DEG_20 = 10e-3

#Copper thermal conductivity at 0 °C in [Watt/(meters*Kelvin)]
COPPER_THERM_CONDUCTIVITY = 401

#Gold thermal conductivity at 0 °C in [Watt/(meters*Kelvin)]
GOLD_THERM_CONDUCTIVITY = 318

#Iron thermal conductivity at 0 °C in [Watt/(meters*Kelvin)]
IRON_THERM_CONDUCTIVITY = 83.5

#Dry Air thermal conductivity at 0 °C in [Watt/(meters*Kelvin)]
AIR_THERM_CONDUCTIVITY = 0.024
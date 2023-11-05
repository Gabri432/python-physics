"""
MODULE NAME: thermodynamics

DESCRIPTION: A collection of various Physics formulas related to Thermodynamics.

LINKS:
github - https://github.com/Gabri432/python-physics/blob/master/src/physics/thermodynamics.py
"""

#Gay-Lussac first law  (Volume variation), check for more information https://en.wikipedia.org/wiki/Ideal_gas_law#Combined_gas_law
def isobaric_process(volume: float, temperature: float) -> float:
	"""Calculates delta_volume = volume * (1 + a*temperature), where a = 1/273 (
thermal expansion coefficient).

    Parameters:
    ----------
        - volume (cube meters), a float representing the volume of a gas. 
        - temperature (Celsius Degrees), a float representing the temperature of that gas.

    Returns:
    ---------
        A float representing the Volume Variation (with constant pressure) as result of that volume and temperature.
    
    """
	return volume * (1 + (1/273)*(temperature)), "m^3"

#Gay-Lussac second law (Pressure Variation), check for more information https://en.wikipedia.org/wiki/Ideal_gas_law#Combined_gas_law
def isochoric_process(pressure: float, temperature: float) -> float:
	"""Calculates delta_pressure = pressure * (1 + (1/273)*(temperature)), where a = 1/273 (
thermal expansion coefficient).

    Parameters:
    ----------
        - volume (cube meters), a float representing the volume of a gas. 
        - temperature (Celsius Degrees), a float representing the temperature of that gas.

    Returns:
    ---------
        A float representing the Pressure Variation (with constant volume) as result of that pressure and temperature.
    
    """
	return pressure * (1 + (1/273)*(temperature)), "Pascal"

#Net Heat Energy Transfer, check for more information https://en.wikipedia.org/wiki/Rate_of_heat_flow
def net_heat_energy_transfer(thermal_conductivity_constant: float, area: float, heat_variation: float, time: float, width: float)-> float:
	"""Calculates Q = -1 * (thermal_conductivity_constant * area * heat_variation * time) / (width).

    Parameters:
    ----------
		- thermal conductivity constant (Watt/meters x Kelvin), a float representing a thermal conductivity constant.
		- area (square meters), a float representing an area.
		- heat variation (kelvin Degrees), a float representing the heat variation.
		- time (seconds), a float representing the time taken.
		- width (meters), a float representing the width of the material.

    Returns:
    ---------
        A float representing the Net Heat Energy Transfer as result of that Thermal Conductivity Constant, area, heat variation, time and width.
    
    """
	return -1 * (thermal_conductivity_constant * area * heat_variation * time) / (width), "J"

#Heat Flux, check for more information https://en.wikipedia.org/wiki/Thermal_conductivity
def heat_flux(thermal_conductivity_constant: float, starting_temperature: float, final_temperature: float, distance: float)-> float:
	"""Calculates Q = -1 * thermal_conductivity_constant * (finalTemperatureKelvin - startingTemperatureKelvin) / distance.

    Parameters:
    ----------
	    - thermal conductivity constant (Watt/meters x Kelvin), a float representing a thermal conductivity constant.
        - starting_temperature (kelvin Degrees), a float representing the starting temperature value.
		- final_temperature (kelvin Degrees), a float representing the final temperature value.
        - distance (meters), a float representing the distance.

    Returns:
    ---------
        A float representing the Heat Flux as result of that Thermal Conductivity Constant, starting and ending temperatures, distance.
    
    """
	return -1 * thermal_conductivity_constant * (final_temperature - starting_temperature) / distance, "W"

#Joule Heating, or Resistance, check for more information https://en.wikipedia.org/wiki/Joule_heating
def joule_heating(resistance: float, current_intensity: float) -> float: #(power float64, measurementUnit string) {
	"""Calculates Power = resistance * current_intensity**2.

    Parameters:
    ----------
        - resistance (ohm), a float representing the resistance. 
        - current_intensity (Ampere), a float representing the current intensity.

    Returns:
    ---------
        A float representing the force as result of that mass and acceleration.
    
    """
	return resistance * current_intensity**2, "W"

#Joule Heating, or Resistance, check for more information https://en.wikipedia.org/wiki/Joule_heating
def joule_heating_2(current_intensity: float, voltage_difference: float) -> float: #(power float64, measurementUnit string) {
	"""Calculates Power = current_intensity * voltage_difference.

    Parameters:
    ----------
        - current_intensity (Ampere), a float representing the current intensity.
        - voltage_difference (Voltage), a float representing the voltage difference.

    Returns:
    ---------
        A float representing the force as result of that mass and acceleration.
    
    """
	return current_intensity * voltage_difference, "W"


#Pressure is the normal force/area ratio, check for more information https://en.wikipedia.org/wiki/Pressure
def pressure(normal_force: float, area: float) -> float:
	"""Calculates pressure = normal_force / area.

    Parameters:
    ----------
        - normal_force (newton), a float representing the normal force. 
        - area (square meters), a float representing the area.

    Returns:
    ---------
        A float representing the Pressure as result of that normal force and area.
    
    """
	return normal_force / area, "Pascal"
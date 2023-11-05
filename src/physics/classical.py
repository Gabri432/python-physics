"""
MODULE NAME: classical

DESCRIPTION: A collection of various Physics formulas related to Cinematics and Dynamics.

LINKS:
github - https://github.com/Gabri432/python-physics/blob/master/src/physics/classical.py
"""

import math
from physics import constants
from physics import mathem


def force(mass: float, acceleration: float) -> float:
    """Calculates F = mass*acceleration.

    Parameters:
    ----------
        - mass (kilograms), a float representing the mass of the object. 
        - acceleration (meters/s**2), a float representing the acceleration of the object.

    Returns:
    ---------
        A float representing the force as result of that mass and acceleration.
    
    """
    return mass*acceleration, "N"

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
    return distance/time, "m/s"

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
    return distance/speed, "s"


def work(force: float, distance: float) -> float: 
    """Calculates W = force*distance.

    Parameters:
    ----------
        - force (newton), a float representing the value of a force. 
        - distance (meters), a float representing the distance the object has to travel.

    Returns:
    ---------
        A float representing the work as result of that force and distance.
    """
    return force*distance, "J"


def acceleration(force: float, mass: float) -> float:
    """Calculates a = force/mass.

    Parameters:
    ----------
        - force (newton), a float representing the value of a force. 
        - distance (meters), a float representing the distance the object wants to cover.

    Returns:
    ---------
        A float representing the acceleration as result of that force and mass.
    """
    return force / mass, "m/s**2"


def density(mass: float, volume: float) -> float:
    """Calculates d = mass/volume.

    Parameters:
    ----------
        - mass (kg), a float representing the mass of an object. 
        - volume (cube meteres), a float representing the volume of the object.

    Returns:
    ---------
        A float representing the density as result of that mass and volume.
    """
    return mass/volume, "kg/m^3"


def intensity(power: float, area: float) -> float:
    """Calculates i = power*area.

    Parameters:
    ----------
        - power (watt), a float representing the power. 
        - area (square meters), a float representing an area.

    Returns:
    ---------
        A float representing the intensity as result of that power and area.
    """
    return power / area, "W/m**2"


def potential_energy(mass: float, acceleration: float, distance: float) -> float:
    """Calculates PE = mass*acceleration*distance.

    Parameters:
    ----------
        - mass (kg), a float representing the mass of an object. 
        - acceleration (square meters), a float representing the acceleration of the object.
        - distance (meters), a float representing the distance the object has to cover.

    Returns:
    ---------
        A float representing the Potential Energy as result of that mass, acceleration and distance.
    """
    return mass * acceleration * distance, "J"


#Kinetic Energy is the product between half the mass and the square speed
def kinetic_ener(mass: float, speed: float) -> float:
    """Calculates K = (1/2)*mass*(speed**2).

    Parameters:
    ----------
        - mass (kg), a float representing the mass of an object. 
        - speed (meters per second), a float representing the speed of the object.

    Returns:
    ---------
        A float representing the Kinetic Energy as result of that mass and speed.
    """
    return (1 / 2) * mass * (speed * speed), "J"


#Mechanic Energy is the sum of Potential energy and kinetic energy, check for more information https://en.wikipedia.org/wiki/Mechanical_energy
def mechanical_ener(potential: float, kinetic: float) -> float:
    """Calculates M = PE + K.

    Parameters:
    ----------
        - PE (Joule), a float representing the Potential Energy. 
        - K (Joule), a float representing the Kinetic Energy.

    Returns:
    ---------
        A float representing the Mechanical Energy as result of that Potential and Kinetic Energies.
    """
    return potential + kinetic, "J"


#Momentum is the product between mass and speed
def momentum(mass: float, speed: float) -> float:
    """Calculates p = mass*speed.

    Parameters:
    ----------
        - mass (kg), a float representing the mass of an object. 
        - speed (meters per second), a float representing the speed of the object.

    Returns:
    ---------
        A float representing the momentum as result of that mass and speed.
    """
    return mass * speed, "kg*m/s"


#Power is the work/time ratio
def power(work: float, time: float) -> float:
    """Calculates P = work/time.

    Parameters:
    ----------
        - work (Joule), a float representing the work. 
        - time (seconds), a float representing the time.

    Returns:
    ---------
        A float representing the power as result of that work and time.
    """
    return work / time, "W"


#Potential Elastic Energy, check for more information https://en.wikipedia.org/wiki/Elastic_energy
def elastic_potential_energy(elastic_constant: float, distance: float) -> float:
    """Calculates PE = (1 / 2) * elastic_constant * (distance**2).

    Parameters:
    ----------
        - elastic_constant (newton per meters), a float representing the elastic constant. 
        - distance (meters), a float representing the distance the object wants to cover.

    Returns:
    ---------
        A float representing the Elastic Potential Energy as result of that elastic constant and distance.
    """
    return (1 / 2) * elastic_constant * (distance * distance), "J"


#Frequency is the speed/distance ratio
def Frequency(speed: float, distance: float) -> float:
    """Calculates f = speed/distance.

    Parameters:
    ----------
        - speed (meters per second), a float representing the speed of an object. 
        - distance (meters), a float representing the distance the object wants to cover.

    Returns:
    ---------
        A float representing the time as result of that speed and distance.
    """
    return speed / distance, "hertz"


#Doppler effect (when listener is getting closer to the sound source), check for more information https://en.wikipedia.org/wiki/Doppler_effect
def DopplerCloser(speed: float, frequency: float) -> float:
    """Calculates observed_f = (1 + (speed / 340)) * frequency (when listener is getting closer to the sound source).

    Parameters:
    ----------
        - speed (meters per second), a float representing the value of a force. 
        - frequence (hertz), a float representing the distance the object wants to cover.

    Returns:
    ---------
        A float representing the observed frequency as result of that speed and frequence.
    """
    return (1 + (speed / 340)) * frequency, "hertz"


#Doppler effect (when listener is getting far away from sound source), check for more information https://en.wikipedia.org/wiki/Doppler_effect
def DopplerFarer(speed: float, frequency: float) -> float:
    """Calculates observed_f = (1 - (speed / 340)) * frequency (when listener is getting far away from sound source).

    Parameters:
    ----------
        - speed (meters per second), a float representing the value of a force. 
        - frequence (hertz), a float representing the distance the object wants to cover.

    Returns:
    ---------
        A float representing the observed frequency as result of that speed and frequence.
    """
    return (1 - (speed / 340)) * frequency, "hertz"


#Angular Frequency is the radiant/time ratio
def angular_frequency(time: float) -> float:
    """Calculates angular_frequency = (2 * greek_pi) / time, where greek_pi = 3.1416.

    Parameters:
    ----------
        - force (newton), a float representing the value of a force. 
        - distance (meters), a float representing the distance the object wants to cover.

    Returns:
    ---------
        A float representing the Angular Frequency as result of that time.
    """
    return (2 * mathem.greek_pi) / time, "rad/s"

#Centripetal Force is the ratio between the mass and square speed product and the radius
def centripetal_force(mass: float, speed: float, radius: float) -> float:
    """Calculates centripetal_force = (mass * speed**2) / radius.

    Parameters:
    ----------
        - mass (kg), a float representing the mass of an object. 
        - speed (meters per second), a float representing the speed of the object.
        - radius (meters) a float representing the distance of the object from the center of rotation.

    Returns:
    ---------
        A float representing the Centripetal Force as result of that mass, speed and radius.
    """
    return (mass * speed * speed) / radius, "N"


#Centripetal Acceleration is the ratio between the square speed and the radius
def centripetal_accel(speed: float, radius: float) -> float:
    """Calculates centripetal_acceleration = (speed**2) / radius.

    Parameters:
    ----------
        - speed (meters per second), a float representing the speed of an object.
        - radius (meters) a float representing the distance of the object from the center of rotation.

    Returns:
    ---------
        A float representing the Centripetal Acceleration as result of that speed and radius.
    """
    return (speed * speed) / radius, "m/s**2"


#Pendulum Period, check for more information https://en.wikipedia.org/wiki/Pendulum
def pendulum_period(pendulum_length: float) -> float:
    """Calculates t = (2 * greek_pi) * math.sqrt(pendulum_length/g), where greek_pi = 3.1416, g = 9.81.

    Parameters:
    ----------
        - pendulum_length (meters), a float representing the length of the pendulum.

    Returns:
    ---------
        A float representing the time as result of that distance and speed.
    """
    return (2 * mathem.greek_pi) * math.sqrt(pendulum_length/constants.GRAVITY), "s"


#Maximum height of projectile, check for more info https://en.wikipedia.org/wiki/Projectile_motion
def projectile_max_height(initial_velocity: float, angle: float) -> float:
    """Calculates h = (initial_velocity**2 * sine**2(angle)) / (2 * g), where g = 9.81.

    Parameters:
    ----------
        - initial_velocity (meters per second), a float representing the initial velocity of the object. 
        - angle (degrees), a float representing the distance the angle at which it is thrown.

    Returns:
    ---------
        A float representing the Projectile Max Height as result of that initial velocity and angle.
    """
    return (initial_velocity * initial_velocity * mathem.sine_square(angle)) / (2 * constants.GRAVITY), "m"


#Horizontal range of projectile from ground, check for more info https://en.wikipedia.org/wiki/Range_of_a_projectile
def projectile_max_range(initial_velocity: float, angle: float) -> float:
    """Calculates d = (initial_velocity**2 * sine(2*angle)) / (2 * g), where g = 9.81.

    Parameters:
    ----------
       - initial_velocity (meters per second), a float representing the initial velocity of the object. 
       - angle (degrees), a float representing the distance the angle at which it is thrown.

    Returns:
    ---------
        A float representing the Projectile Max Range as result of that initial velocity and angle.
    """
    return (initial_velocity * initial_velocity * math.sin((2*angle)/57.2958)) / constants.GRAVITY, "m"


#Total time of flight of projectile, check for more info https://en.wikipedia.org/wiki/Projectile_motion
def projectile_flight_time(initial_velocity: float, angle: float) -> float:
    """Calculates t = (2 * initial_velocity * sine(angle)) / g, where g = 9.81.

    Parameters:
    ----------
       - initial_velocity (meters per second), a float representing the initial velocity of the object. 
       - angle (degrees), a float representing the distance the angle at which the object is thrown.

    Returns:
    ---------
        A float representing the Projectile Flight Time as result of initial velocity and angle.
    """
    return (2 * initial_velocity * math.sin(angle/57.2958)) / constants.GRAVITY, "s"


#Horizontal Position after t time from ground https://en.wikipedia.org/wiki/Range_of_a_projectile
def horizontal_position(velocity: float, time: float, angle: float) -> float:
    """Calculates projectile_horizontal_position_on_flight = velocity * time * cosine(angle).

    Parameters:
    ----------
        - velocity (newton), a float representing the value of a force. 
        - time (meters), a float representing the distance the object wants to cover.
        - angle (degrees), a float representing the distance the angle at which the object is thrown.

    Returns:
    ---------
        A float representing the Projectile Horizontal Position on flight (at that time) as result of that velocity and angle.
    """
    return velocity * time * math.cos(angle/57.2958), "m"


#Vertical Position after t time from ground https://en.wikipedia.org/wiki/Range_of_a_projectile
def vertical_position(velocity: float, time: float, angle: float) -> float:
    """Calculates projectile_vertical_position_on_flight = velocity * time * sine(angle) - (1/2) * g * t**2.

    Parameters:
    ----------
        - force (newton), a float representing the value of a force. 
        - distance (meters), a float representing the distance the object wants to cover.
        - angle (degrees), a float representing the distance the angle at which the object is thrown.

    Returns:
    ---------
        A float representing the Projectile Vertical Position on flight (at that time) as result of that velocity and angle.
    """
    return velocity*time*math.sin(angle/57.2958) - (1/2)*constants.GRAVITY*time*time, "m"

"""
Class for Body

The porpuse of this class is to ease calculations.
"""
from physics import classical, gravity
    
class Body:
    """
    A Body is any object defined by its name, mass and speed.

    The is expected to be not empty, and mass and radius to be positive float values.
    """

    def __init__(self, name: str, mass: float, speed: float):
        """
        Constructor of the Body class.

        Parameters:
        ----------
            - name: string representing the name of the body.
            - mass: float representing the mass of the body.
            - speed: float representing the speed of the body.
        """
        self.name = name
        self.mass = mass
        self.speed = speed 

    def __str__(self) -> str:
        return f"Name: {self.name}\nMass: {self.mass} kg\nSpeed: {self.speed} m/s."

    def force(self, acceleration: float) -> float:
        """Calculates the force generated by the mass and the acceleration of the body."""
        return classical.force(self.mass, acceleration)
    
    def density(self, volume: float) -> float:
        """Calculates the density of the body due to its mass and volume."""
        return classical.density(self.mass, volume)
    
    def momentum(self) -> float:
        """Calculates the momentum generated by the mass and speed of the body."""
        return classical.momentum(self.mass, self.speed)
    
    def acceleration(self, force: float) -> float:
        """Calculates the acceleration of the body given its mass and the applied force."""
        return classical.acceleration(self.mass, force)
    
    def projectile_max_range(self, angle: float) -> float:
        """Calculates the max horizontal distance covered by the body given its speed and the initial angle."""
        return classical.projectile_max_range(self.speed, angle)
    
    def projectile_flight_time(self, angle: float) -> float:
        """Calculates the flight time of the body given its speed and the initial angle."""
        return classical.projectile_flight_time(self.speed, angle)
    
    def projectile_max_height(self, angle: float) -> float:
        """Calculates the max vertical distance covered by the body given its speed and the initial angle."""
        return classical.projectile_max_height(self.speed, angle)
    
    def potential_grav_energy(self, height: float) -> float:
        """Calculates the potential gravitational energy of the body given its mass and height."""
        return gravity.potential_grav_energy(self.mass, height)
    
    def grav_field(self, radius: float) -> float:
        """Calculates the gravitational field of the body given its mass and radius."""
        return gravity.grav_field(self.mass, radius)

    def escape_speed(self, radius) -> float:
        """Calculates the escape speed of the body given given its mass and radius."""
        return gravity.escape_speed(self.mass, radius)

        

import math

# 1. SPEED
def speed(distance, time):
    return distance / time

# 2. VELOCITY
def velocity(displacement, time):
    return displacement / time

# 3. ACCELERATION
def acceleration(final_velocity, initial_velocity, time):
    return (final_velocity - initial_velocity) / time

# 4. FORCE (Newton's Second Law)
def force(mass, acceleration):
    return mass * acceleration

# 5. WEIGHT
def weight(mass, gravity=9.81):
    return mass * gravity

# 6. MOMENTUM
def momentum(mass, velocity):
    return mass * velocity

# 7. WORK DONE
def work_done(force, distance, angle=0):
    return force * distance * math.cos(math.radians(angle))

# 8. POWER
def power(work, time):
    return work / time

# 9. KINETIC ENERGY
def kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity**2

# 10. POTENTIAL ENERGY
def potential_energy(mass, gravity, height):
    return mass * gravity * height

# 11. DENSITY
def density(mass, volume):
    return mass / volume

# 12. PRESSURE
def pressure(force, area):
    return force / area

# 13. FREQUENCY
def frequency(number_of_cycles, time):
    return number_of_cycles / time

# 14. PERIOD
def period(frequency):
    return 1 / frequency

# 15. WAVE SPEED
def wave_speed(frequency, wavelength):
    return frequency * wavelength

# 16. ELECTRIC CHARGE
def electric_charge(current, time):
    return current * time

# 17. VOLTAGE
def voltage(current, resistance):
    return current * resistance

# 18. RESISTANCE
def resistance(voltage, current):
    return voltage / current

# 19. ELECTRICAL POWER
def electrical_power(voltage, current):
    return voltage * current

# 20. SPECIFIC HEAT CAPACITY
def specific_heat(heat_energy, mass, temperature_change):
    return heat_energy / (mass * temperature_change)

# 21. HEAT ENERGY
def heat_energy(mass, specific_heat, temperature_change):
    return mass * specific_heat * temperature_change

# 22. EFFICIENCY
def efficiency(useful_output, total_input):
    return (useful_output / total_input) * 100

# 23. STRESS
def stress(force, area):
    return force / area

# 24. STRAIN
def strain(change_in_length, original_length):
    return change_in_length / original_length

# 25. YOUNG'S MODULUS
def young_modulus(stress, strain):
    return stress / strain

# 26. SPRING FORCE (Hooke's Law)
def spring_force(spring_constant, extension):
    return spring_constant * extension

# 27. MOMENT OF FORCE
def moment(force, perpendicular_distance):
    return force * perpendicular_distance

# 28. VISCOUS FORCE (Newton's law of viscosity)
def viscous_force(viscosity, area, velocity_gradient):
    return viscosity * area * velocity_gradient

# 29. REACTION FORCE
def reaction_force(weight, other_vertical_forces=0):
    return weight + other_vertical_forces

# 30. GRAVITATIONAL POTENTIAL
def gravitational_force(mass1, mass2, distance):
    G = 6.67430e-11
    return G * mass1 * mass2 / distance**2


# EXAMPLE CALCULATIONS
print("Speed:", speed(100, 20), "m/s")
print("Force:", force(10, 5), "N")
print("Weight:", weight(50), "N")
print("Momentum:", momentum(10, 4), "kg m/s")
print("Work Done:", work_done(20, 5), "J")
print("Power:", power(100, 10), "W")
print("Kinetic Energy:", kinetic_energy(10, 5), "J")
print("Density:", density(20, 4), "kg/m³")
print("Pressure:", pressure(100, 5), "Pa")
print("Voltage:", voltage(2, 5), "V")
print("Resistance:", resistance(12, 3), "Ω")

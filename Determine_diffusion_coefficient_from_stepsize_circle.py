# Determine diffusion coefficient for a given stepsize
import random
import time
import math
time_interval = 0.0001  # seconds. i.e. 0.1 ms
simulation_timecourse = 1  # i.e. 1 s
step = float(input('''For what stepsize would you like the diffusion coefficient calculated? (unit = angstroms)
 The stepsize is the maximum distance travelled in 0.1 ms.
 Stepsize: '''))
repeats = 10000
# Initial coordinates:
x = 0
y = 0
###
start = time.time()
diffusion_coefficient_list = []
for n in range(repeats):
    for t in range(int(simulation_timecourse / time_interval)):
        degrees = random.randint(0, 90)
        radians = (degrees * math.pi) / 180
        dx = step * math.cos(radians)
        dy = step * math.sin(radians)
        x += random.choice([- dx, dx])
        y += random.choice([- dy, dy])
        #print (f'{x}, {y}') # Commented out the printing of the list
    # Calculate linear distance (modulus x) travelled in 1 s
    mod_x = (x ** 2 + y ** 2) ** 0.5
    #print(mod_x)
    diffusion_coefficient_single = (mod_x ** 2) / 4
    #print(diffusion_coefficient_single)
    diffusion_coefficient_list.append(diffusion_coefficient_single)
    x = 0
    y = 0
#print(diffusion_coefficient_list)
#print(diffusion_coefficient_single)
diffusion_coefficient_average = sum(diffusion_coefficient_list) / repeats
print(f'A stepsize of {step} angstroms results in a diffusion coeffient of {diffusion_coefficient_average}.')
end = time.time()
print(f"The time taken for the execution of this program was {end - start} seconds.")
input("Press any button to quit the program.")

# Calculate step size required to get diffusion coefficient
import random
import math
import time
time_interval = 0.0001  # seconds. i.e. 0.1 ms
simulation_timecourse = 1  # seconds i.e. 1 s
step = 0.0  # angstroms
aim = float(input('What diffusion coefficient would you like to aim for? (unit = a2/s): '))
# 2400000 is experimentally determined diffusion coefficient for VSG on live trypanosome surface
# 100000000 and 250000000 are experimentally determined diffusion coefficients on artificial membranes (0.01 - 0.025 um2/s)
# New value from Engstler is 1 um2/s which is 100000000 a2/s
success_count = 0 # counts how many time the simulated diffusion coefficient is within 5% of the "aim". Resets to 0 if subsequent iteration is >5% from "aim".
# Initial coordinates:
x = 0
y = 0
###
start = time.time() # I time how long the program takes to run.
multiplier = (aim / 2400000) ** 0.5 # This value affects the increase/decrease in stepsize during the trial and error process. If the "aim" is bigger the multiplier is larger.
req_success_count = 3 # This can be increased to make it more stringent but 3 gives reproducible results.
while success_count < req_success_count:
    repeats = 100 # This gives reproducible results. Can be increased to be more stringent but runs slower.
    diffusion_coefficient_list = [] # The calculated diffusion coeffient of each run is stored here.
    for repeat in range(repeats):
        for t in range(int(simulation_timecourse / time_interval)): # This for loop generates a random walk in which each 0.1ms, the x, y coordinates change in a positive or negative direction by a random value within +/- step.
            degrees = random.randint(0, 90)
            radians = (degrees * math.pi) / 180
            dx = step * math.cos(radians)
            dy = step * math.sin(radians)
            x += random.choice([- dx, dx])
            y += random.choice([- dy, dy])
            # print (f'{x}, {y}') # Commented out the printing of the list
        mod_x = (x ** 2 + y ** 2) ** 0.5 # Calculate linear distance (modulus x) travelled in 1 s
        # print(mod_x)
        diffusion_coefficient_single = (mod_x ** 2) / 4 # diffusion coefficient of a single random walk
        diffusion_coefficient_list.append(diffusion_coefficient_single) # stores the single diffusion coefficient in the list.
        x = 0 # reset x and y for the next random walk
        y = 0
        # print(mod_x)
        # print(diffusion_coefficient_list)
        # print(diffusion_coefficient_single)
    diffusion_coefficient_average = sum(diffusion_coefficient_list) / repeats # averages all diffusion coefficient values stored in the list.
    # print(diffusion_coefficient_average)
    difference_from_aim = aim - diffusion_coefficient_average # Calculate difference from aim. The step is then altered by the below if statements depending on how close the calculated diffusion coefficient is to the aim.
    if abs(difference_from_aim) <= aim / 20: # less than 5% difference
        success_count += 1 # If this reaches the req_success_count, the loop will break.
        print(f'{success_count} successful runs! {3 - success_count} more required to pass')
    else:
        success_count = 0
        #print('Unsuccessful stepsize, altering stepsize and repeating.')
        if abs(difference_from_aim) <= aim / 10: # less than 10% difference
            if difference_from_aim > 0:
                step += 0.025 * multiplier
            else:
                step -= 0.025 * multiplier
        if abs(difference_from_aim) <= aim / 5: #less than 20% difference
            if difference_from_aim > 0:
                step += 0.5 * multiplier
            else:
                step -= 0.5 * multiplier
        if abs(difference_from_aim) >= aim / 5: #more than 20% difference
            if difference_from_aim > 0:
                step += 1 * multiplier
            else:
                step -= 1 * multiplier

    print(step) #Allows to see how the stepsize is changing during the run. I would normally comment this out.
print(f'The step size that results in the correct diffusion coeffient is {abs(step)}.')
f = open('stepsize.txt', 'w+')
f.write(f'{step}')
f.close()
end = time.time()
print(f"The time taken for the execution of this program was {end - start} seconds.")
input("Press any button to quit the program. Your stepsize has been saved as 'stepsize.txt'.")

import csv
import math
import random
import time

# Parameters of the simulation
time_interval = 0.0001  # seconds. i.e. 0.1 ms
simulation_timecourse = 1  # seconds e.g. 1 s
step = float(input('What step size should be used? (unit = angstroms): '))

# Simulation on lattice 1
file = open("initial_lattice1_coords.csv", "r")
data = csv.reader(file, delimiter=",")

xvals = []
yvals = []
zvals = []

for x, y, z in data:
    xvals.append(float(x))
    yvals.append(float(y))
    zvals.append(int(z))

# Apply random walk to each molecule
# The rules just act as mirror boundaries at the moment. Need to add in the other plane onto which they are transported
start = time.time()
for t in range(int(simulation_timecourse / time_interval)):
    if t % 10000 == 0:
        print(str(t/10000) + " seconds have so far been modelled on lattice 1. Lattice 2 to do next.")
    # Every interval of time, apply a step in x and y, until the time course is finished
    for i in range(len(xvals)):
        degrees = random.randint(0, 90)
        radians = (degrees * math.pi) / 180
        dx = step * math.cos(radians)
        dy = step * math.sin(radians)
        randx = random.choice([- dx, dx])
        randy = random.choice([- dy, dy])
        x = xvals[i] + randx
        y = yvals[i] + randy
        z = zvals[i]

        # If not already in the FP, the move randomly and if it moves into FP, mark it.
        if z == 1 or z == 2:
            # If coordinate outside of trypanosome boundary:
            if x < 0:
                x = 0 - x
                if z == 1:
                    z += 1
                elif z == 2:
                    z -= 1

            if x > 227000:
                x = 227000 - (x - 227000)
                if z == 1:
                    z += 1
                elif z == 2:
                    z -= 1
            if x == 227000:
                xdiameter = 521.3 * 2
                if y > 521.3:
                    y = 0 - (y - xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1
                if y < -521.3:
                    y = 0 - (y + xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1

            if 0 <= x < 37500:
                posylimit = (2.9 * pow(10, -10) * pow(x, 3)) - (3 * pow(10, -5) * pow(x, 2)) + (1.175 * x) + 231.03
                negylimit = 0 - posylimit
                xdiameter = posylimit * 2
                if y > posylimit:
                    y = 0 - (y - xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1
                if y < negylimit:
                    y = 0 - (y + xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1

            if x >= 37500 and x <= 62500:
                posylimit = (0.0003 * x) + 17380.33
                negylimit = 0 - posylimit
                xdiameter = posylimit * 2
                if y > posylimit:
                    y = 0 - (y - xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1
                if y < negylimit:
                    y = 0 - (y + xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1

            if 62500 < x < 227000:
                posylimit = - (2 * pow(10, -7) * pow(x, 2)) - (0.0447 * x) + 20974
                negylimit = 0 - posylimit
                xdiameter = posylimit * 2
                if y > posylimit:
                    y = 0 - (y - xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1
                if y < negylimit:
                    y = 0 - (y + xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1

            # If coordinate moves into FP:
            if x >= 23200 and x <= 26800:
                dx = abs(x - 25000)
                dy = abs(y)
                dx2dy2 = (pow(dx, 2)) + (pow(dy, 2))
                d = math.sqrt(dx2dy2)
                if d < 1800 and z == 1:
                    z = 3

            xvals[i] = x
            yvals[i] = y
            zvals[i] = z

with open('final_lattice1_coords.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(zip(xvals, yvals, zvals))
print("Created file: final_lattice1_coords.csv")

# Simulation on lattice 2
file = open("initial_lattice2_coords.csv", "r")
data = csv.reader(file, delimiter=",")

xvals = []
yvals = []
zvals = []

for x, y, z in data:
    xvals.append(float(x))
    yvals.append(float(y))
    zvals.append(int(z))

# Apply random walk to each molecule
# The rules just act as mirror boundaries at the moment. Need to add in the other plane onto which they are transported
for t in range(int(simulation_timecourse / time_interval)):
    if t % 10000 == 0:
        print(str(t/10000) + " seconds have so far been modelled on lattice 2. Lattice 1 already complete.")
    # Every interval of time, apply a step in x and y, until the time course is finished
    for i in range(len(xvals)):
        randx = round(random.uniform(- step, step), 2)
        randy = round(random.uniform(- step, step), 2)
        x = xvals[i] + randx
        y = yvals[i] + randy
        z = zvals[i]

        # If not already in the FP, the move randomly and if it moves into FP, mark it.
        if z == 1 or z == 2:
            # If coordinate outside of trypanosome boundary:
            if x < 0:
                x = 0 - x
                if z == 1:
                    z += 1
                elif z == 2:
                    z -= 1

            if x > 227000:
                x = 227000 - (x - 227000)
                if z == 1:
                    z += 1
                elif z == 2:
                    z -= 1
            if x == 227000:
                xdiameter = 521.3 * 2
                if y > 521.3:
                    y = 0 - (y - xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1
                if y < -521.3:
                    y = 0 - (y + xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1

            if 0 <= x < 37500:
                posylimit = (2.9 * pow(10, -10) * pow(x, 3)) - (3 * pow(10, -5) * pow(x, 2)) + (1.175 * x) + 231.03
                negylimit = 0 - posylimit
                xdiameter = posylimit * 2
                if y > posylimit:
                    y = 0 - (y - xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1
                if y < negylimit:
                    y = 0 - (y + xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1

            if x >= 37500 and x <= 62500:
                posylimit = (0.0003 * x) + 17380.33
                negylimit = 0 - posylimit
                xdiameter = posylimit * 2
                if y > posylimit:
                    y = 0 - (y - xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1
                if y < negylimit:
                    y = 0 - (y + xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1

            if 62500 < x < 227000:
                posylimit = - (2 * pow(10, -7) * pow(x, 2)) - (0.0447 * x) + 20974
                negylimit = 0 - posylimit
                xdiameter = posylimit * 2
                if y > posylimit:
                    y = 0 - (y - xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1
                if y < negylimit:
                    y = 0 - (y + xdiameter)
                    if z == 1:
                        z += 1
                    elif z == 2:
                        z -= 1

            # If coordinate moves into FP:
            if x >= 23200 and x <= 26800:
                dx = abs(x - 25000)
                dy = abs(y)
                dx2dy2 = (pow(dx, 2)) + (pow(dy, 2))
                d = math.sqrt(dx2dy2)
                if d < 1800 and z == 1:
                    z = 3

            xvals[i] = x
            yvals[i] = y
            zvals[i] = z

with open('final_lattice2_coords.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(xvals, yvals, zvals))
print("Created file: final_lattice2_coords.csv")

end = time.time()
print(f"The time taken for the execution of this program was {end - start} seconds.")
import csv

# Extract lattice 1 values from final1:
file = open("final_lattice1_coords.csv", "r")
data = csv.reader(file, delimiter=",")

xvals = []
yvals = []
zvals = []

for x, y, z in data:
    xvals.append(float(x))
    yvals.append(float(y))
    zvals.append(int(z))

x_lattice1 = []
y_lattice1 = []
z_lattice1 = []

for i in range(len(zvals)):
    z = zvals[i]
    if z == 1:
        x_lattice1.append(xvals[i])
        y_lattice1.append(yvals[i])
        z_lattice1.append(zvals[i])

# Extract lattice 1 values from final2:
file = open("final_lattice2_coords.csv", "r")
data = csv.reader(file, delimiter=",")

xvals = []
yvals = []
zvals = []

for x, y, z in data:
    xvals.append(float(x))
    yvals.append(float(y))
    zvals.append(int(z))

for i in range(len(zvals)):
    z = zvals[i]
    if z == 1:
        x_lattice1.append(xvals[i])
        y_lattice1.append(yvals[i])
        z_lattice1.append(zvals[i])

print("The number of molecules on plane 1 is: " + str(len(x_lattice1)))

with open('final_combined_lattice1_coords.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(x_lattice1, y_lattice1, z_lattice1))

# Extract lattice 2 values from final1:
file = open("final_lattice1_coords.csv", "r")
data = csv.reader(file, delimiter=",")

xvals = []
yvals = []
zvals = []

for x, y, z in data:
    xvals.append(float(x))
    yvals.append(float(y))
    zvals.append(int(z))

x_lattice2 = []
y_lattice2 = []
z_lattice2 = []

for i in range(len(zvals)):
    z = zvals[i]
    if z == 2:
        x_lattice2.append(xvals[i])
        y_lattice2.append(yvals[i])
        z_lattice2.append(zvals[i])

# Extract lattice 2 values from final2:
file = open("final_lattice2_coords.csv", "r")
data = csv.reader(file, delimiter=",")

xvals = []
yvals = []
zvals = []

for x, y, z in data:
    xvals.append(float(x))
    yvals.append(float(y))
    zvals.append(int(z))

for i in range(len(zvals)):
    z = zvals[i]
    if z == 2:
        x_lattice2.append(xvals[i])
        y_lattice2.append(yvals[i])
        z_lattice2.append(zvals[i])

print("The number of molecules on plane 2 is: " + str(len(x_lattice2)))

with open('final_combined_lattice2_coords.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(x_lattice2, y_lattice2, z_lattice2))

# Extract lattice 3 values from final1:
file = open("final_lattice1_coords.csv", "r")
data = csv.reader(file, delimiter=",")

xvals = []
yvals = []
zvals = []

for x, y, z in data:
    xvals.append(float(x))
    yvals.append(float(y))
    zvals.append(int(z))

x_lattice3 = []
y_lattice3 = []
z_lattice3 = []

for i in range(len(zvals)):
    z = zvals[i]
    if z == 3:
        x_lattice3.append(xvals[i])
        y_lattice3.append(yvals[i])
        z_lattice3.append(zvals[i])

# Extract lattice 3 values from final2:
file = open("final_lattice2_coords.csv", "r")
data = csv.reader(file, delimiter=",")

xvals = []
yvals = []
zvals = []

for x, y, z in data:
    xvals.append(float(x))
    yvals.append(float(y))
    zvals.append(int(z))

for i in range(len(zvals)):
    z = zvals[i]
    if z == 3:
        x_lattice3.append(xvals[i])
        y_lattice3.append(yvals[i])
        z_lattice3.append(zvals[i])

print("The number of molecules in the FP: " + str(len(x_lattice3)))

with open('final_combined_lattice3_coords.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(x_lattice3, y_lattice3, z_lattice3))
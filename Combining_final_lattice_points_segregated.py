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

with open('final_lattice1_coords_from_1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(x_lattice1, y_lattice1, z_lattice1))
print("Created file: final_lattice1_coords_from_1.csv")

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

x_lattice1 = []
y_lattice1 = []
z_lattice1 = []

for i in range(len(zvals)):
    z = zvals[i]
    if z == 2:
        x_lattice1.append(xvals[i])
        y_lattice1.append(yvals[i])
        z_lattice1.append(zvals[i])

with open('final_lattice2_coords_from_1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(x_lattice1, y_lattice1, z_lattice1))
print("Created file: final_lattice2_coords_from_1.csv")

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

x_lattice2 = []
y_lattice2 = []
z_lattice2 = []

for i in range(len(zvals)):
    z = zvals[i]
    if z == 1:
        x_lattice2.append(xvals[i])
        y_lattice2.append(yvals[i])
        z_lattice2.append(zvals[i])

with open('final_lattice1_coords_from_2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(x_lattice2, y_lattice2, z_lattice2))
print("Created file: final_lattice1_coords_from_2.csv")

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

x_lattice2 = []
y_lattice2 = []
z_lattice2 = []

for i in range(len(zvals)):
    z = zvals[i]
    if z == 2:
        x_lattice2.append(xvals[i])
        y_lattice2.append(yvals[i])
        z_lattice2.append(zvals[i])

with open('final_lattice2_coords_from_2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(x_lattice2, y_lattice2, z_lattice2))
print("Created file: final_lattice2_coords_from_2.csv")
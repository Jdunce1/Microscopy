# Program to create an initial array of coordinates

import math
import csv
import shutil

# Choose whether you want trypanosome shape or flagellar pocket shape

location = input('''Do you want your molecules to be on the surface of the cell, or within the flagellar pocket?
Type S for surface or F for flagellar pocket. ''')
location = location.upper()
while location not in {"S", "F"}:
    print("Invalid choice")
    location = input('Please type S or F. ')
    location = location.upper()

### Ask if they want to flagellar pocket to have a mirror boundary or not.

sa_trypanosome = 10000000000 # angstroms squared i.e. 100 um2
sa_fp = 500000000 # angstroms squared i.e. 5 um2

if location == "S":
    sa = sa_trypanosome
if location == "F":
    sa = sa_fp

# Provide the number of molecules you wish you model
val_ok = False
while not val_ok:
    try:
        num_mol = int(input('What number of molecules do you wish to simulate the movement of? '))
        if num_mol > 0:  # if not a positive int print message and ask for input again
            val_ok = True
            if location == "S":
                print("You have chosen to simulate the movement of " + str(num_mol) + " molecules on the cell surface.")
            if location == "F":
                print("You have chosen to simulate the movement of " + str(num_mol) + " within the flagellar pocket.")
        else:
            print("That's not a positive number. Try again: ")
    except ValueError:
        print("Sorry, input must be a positive integer, try again")



#Create an appropriately sized lattice:
if location == "S":
    # Determine the spacing between the molecules

    hexagonal_area_per_molecule = sa / num_mol
    hexagon_edge_length = math.sqrt(hexagonal_area_per_molecule / ((3 * math.sqrt(3)) / 2))
    distance_between_hexagon_centres = math.sqrt((3 * pow(hexagon_edge_length, 2)))

    spacing = distance_between_hexagon_centres
    print("The initial spacing between each molecule is " + str(spacing) + " angstroms.")
    vertical_separation = math.sqrt((3 / 4) * (spacing * spacing))
    horizontal_separation = spacing / 2

    tryp_length = 227000  # angstroms
    tryp_width = 34798  # angstroms

    xcoords = []
    ycoords = []

    x = 0
    y = 0 - (tryp_width / 2) - 2 * vertical_separation

    while y <= tryp_width:
        x = 0
        y += 2 * vertical_separation
        while x <= tryp_length:
            x += horizontal_separation
            y += vertical_separation
            xcoords.append(x)
            ycoords.append(y)
            x += horizontal_separation
            y -= vertical_separation
            xcoords.append(x)
            ycoords.append(y)

    # Empty filtered lists
    xaccepted1 = []
    yaccepted1 = []
    xaccepted2 = []
    yaccepted2 = []
    xaccepted3 = []
    yaccepted3 = []
    xaccepted4 = []
    yaccepted4 = []
    zaccepted = []

    # Filtering coordinates on the basis of the geometric rules for a trypanosome (determined in excel sheet)
    # The trypanosome shape starts at x=0 and ends at x= its length (227000)
    for i in range(len(xcoords)):
        x = xcoords[i]
        y = ycoords[i]
        if x < 0 or x > tryp_length:
            continue
        else:
            xaccepted1.append(x)
            yaccepted1.append(y)

    # There cannot be any values of y other than 0 at x=0
    for i in range(len(xaccepted1)):
        x = xaccepted1[i]
        y = yaccepted1[i]
        if x == 0 and y != 0:
            continue
        else:
            xaccepted2.append(x)
            yaccepted2.append(y)

    # There cannot be any values of y greater than 521.3 or less than -521.3 at x = 227000

    for i in range(len(xaccepted2)):
        x = xaccepted2[i]
        y = yaccepted2[i]
        if x != 227000:
            xaccepted3.append(x)
            yaccepted3.append(y)
        else:
            if y <= 521.3 and y >= -521.3:
                xaccepted3.append(x)
                yaccepted3.append(y)

    # For x values between 0 and 37500 in xaccepted3
    for i in range(len(xaccepted3)):
        x = xaccepted3[i]
        y = yaccepted3[i]
        if x > 0 and x < 37500:
            posylimit = (2.9 * pow(10, -10) * pow(x, 3)) - (3 * pow(10, -5) * pow(x, 2)) + (1.175 * x) + 231.03
            negylimit = 0 - posylimit
            if y > negylimit and y < posylimit:
                xaccepted4.append(x)
                yaccepted4.append(y)
        else:
            continue

    # For x values between 37500 and 62500 in xaccepted3
    for i in range(len(xaccepted2)):
        x = xaccepted3[i]
        y = yaccepted3[i]
        if x >= 37500 and x <= 62500:
            posylimit = 17399
            negylimit = 0 - posylimit
            if y > negylimit and y < posylimit:
                xaccepted4.append(x)
                yaccepted4.append(y)
        else:
            continue

    # For x values between 62500 and 227000 in xaccepted3
    for i in range(len(xaccepted3)):
        x = xaccepted3[i]
        y = yaccepted3[i]
        if x > 62500 and x < 227000:
            posylimit = - (2 * pow(10, -7) * pow(x, 2)) - (0.0447 * x) + 20974
            negylimit = 0 - posylimit
            if y > negylimit and y < posylimit:
                xaccepted4.append(x)
                yaccepted4.append(y)
        else:
            continue

    print("The number of molecules on your modelled trypanosome surface is " + str(len(xaccepted4) * 2) + " with " + str(len(xaccepted4)) + " molecules on plane 1 and the same number on plane 2")

    for i in range(len(xaccepted4)):
        zaccepted.append(1)

    with open('initial_lattice1_coords.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(zip(xaccepted4, yaccepted4, zaccepted))


original = r'initial_lattice1_coords.csv'
target = r'initial_lattice2_coords.csv'

shutil.copyfile(original, target)

file = open("initial_lattice2_coords.csv", "r")
data = csv.reader(file, delimiter=",")
xvals2 = []
yvals2 = []
zvals2 = []

for x, y, z in data:
    xvals2.append(float(x))
    yvals2.append(float(y))
    zvals2.append(2)

with open('initial_lattice2_coords.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(zip(xvals2, yvals2, zvals2))

'''
if location == "F":
    # Many options here
    print("This part of the program has not been developed yet.")

'''



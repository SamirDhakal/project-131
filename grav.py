import csv

rows = []

with open("main.csv", "r") as f:
  csvreader = csv.reader(f)
  for row in csvreader: 
    rows.append(row)

headers = rows[0]
star_data_rows = rows[1:]
print(headers)
print(star_data_rows[0])
mass = []
radius = []
star_names = []
for star_data in star_data_rows:
  mass.append(star_data[3])
  radius.append(star_data[4])
  star_names.append(star_data[1])

def convert_to_si(radius,mass): 
  for i in range(0,len(radius)-1): 
    radius[i] = radius[i]*6.957e+8 
    mass[i] = mass[i]*1.989e+30 
    convert_to_si(radius,mass)

star_gravity = []
for index, name in enumerate(star_names):
  gravity = (float(mass[index])) / (float(radius[index])*float(radius[index]))
  star_gravity.append(gravity)

convert_to_si(radius, mass)
print(star_gravity)

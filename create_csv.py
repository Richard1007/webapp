import csv
f = open('house.csv','w')
writer = csv.writer(f)

row1= "description, host_name, price"
row2='Bedroom with private bath in Southwest Las Vegas, Lenore, $300'
row3='Furnished Las Vegas House with Pool, Richard, $500'
row4='Private Guest room near downtown, Marry, $250'
writer.writerow(row1)
writer.writerow(row2)
writer.writerow(row3)
writer.writerow(row4)

f.close()
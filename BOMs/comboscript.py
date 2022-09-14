import os
import glob
all_filenames = glob.glob("*Digikey*.csv")
f1 = open("MasterDigikeyList.csv", 'a')
for f in all_filenames:
    f2 = open(f, 'r')
    f1.write(f2.read())
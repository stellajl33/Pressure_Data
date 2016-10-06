import os

path = 'Q:/namerica/everett/allwkgrp/DHI/Sheffield/Beta2/Logs'

for filename in os.listdir(path):

    array = []

    with open(filename) as file:
        for line in file:
            if 'FAILURE!' in line:
                break
            elif 'Delta:' in line:
                        x = line[6::]
                        x = float(x)
                        array.append(x)

print max(array)

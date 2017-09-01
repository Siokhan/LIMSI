import csv
import sys
import numpy as np
framesNb = 756
videoLength = 33

learningVector = np.zeros(framesNb)

f = open('export.csv', 'rt')
try:
    reader = csv.reader(f)
    for row in reader:
        element = row[0].split('\t')
        if element[2] == 'i01l3-v3' and element[18] != '':
            dataToWrite = [int(float(element[4])*framesNb/videoLength),int(float(element[5])*framesNb/videoLength)]
            if element[18] == 'true':
                learningVector[int(float(element[4])*framesNb/videoLength):int(float(element[5])*framesNb/videoLength)] =1
            if element[18] == 'false':
                learningVector[int(float(element[4])*framesNb/videoLength):int(float(element[5])*framesNb/videoLength)] =-1                            
finally:
    f.close()
    print(learningVector)

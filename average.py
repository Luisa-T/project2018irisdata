# Luisa Timothy 01/04/2018
# Project 2018 The Iris Data set calculating the average

with open("irisdata.csv") as f:
  a = 0.0; b = 0.0; c = 0.0; d = 0.0; i = 0 # variables replacing the position in the dataset
  for line in f:
    line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3] # splitting data set up so that I can analyse it as columns
    a = a + float(line.split(',') [0]) # calculating together
    b = b + float(line.split(',') [1])
    c = c + float(line.split(',') [2])
    d = d + float(line.split(',') [3])
    i = i + 1 # counter for number of lines
  def average(x, y): # function for average, where x stands for the total of each column added together and y is the counter (i) for the number of rows
    return (round((x / y),4)) # rounding to the floating number
  print ("This is the average for the whole dataset", '{:8}{:8}{:8}{:8}'.format(str(average(a, i)), str(average(b, i)), str(average(c, i)), str(average(d, i))))
# Luisa Timothy 08-04-2018
# Iris data set calculating mean

with open("irisdata.csv") as f:
  a = 0.0; b = 0.0; c = 0.0; d = 0.0; i = 0 # variables replacing the position in the dataset
  for line in f:
    line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3] # splitting data set
    a = a + float(line.split(',') [0]) # calculating together
    b = b + float(line.split(',') [1])
    c = c + float(line.split(',') [2])
    d = d + float(line.split(',') [3])
    i = i + 1 # counter for number of lines
  def mean(iris): # defining the function mean for the iris dataset
    return float(sum(y) / max(len(i), 4) # should return a floating number summing up the dataset and divide it by the total of occurrences, stack overflow used for part of the function
#incomplete as of yet
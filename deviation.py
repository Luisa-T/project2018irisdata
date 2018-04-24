# Luisa Timothy 14-04-2018
# standard deviation

def average(x, y): # function for average
  return (round((x / y),4)) # rounding to the floating number, four numbers
def classcalculator(z): # function to calculate the calss
  with open("irisdata.csv") as f:
    a = 0.0; b = 0.0; c = 0.0; d = 0.0; i = 0 # variables replacing the position in the dataset
    for line in f:
      line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3] # splitting data set
      if line.find(z) != -1:
        a = a + float(line.split(',') [0]) # calculating together
        b = b + float(line.split(',') [1])
        c = c + float(line.split(',') [2])
        d = d + float(line.split(',') [3])
        i = i + 1 # counter for number of lines
  return (average(a, i), average(b, i), average(c, i), average(d, i), i) # this function calculates the average of each the columns in the dataset
def stdvar(z): # function to valcuate standard variation of each line
  with open("irisdata.csv") as f:
    a = 0.0; b = 0.0; c = 0.0; d = 0.0; i = 0 # variables replacing the position in the dataset
    list1 = classcalculator(z) # taking the values calculated in the class function
    avea = list1[0] # average calculated in function above given variables
    aveb = list1[1]
    avec = list1[2]
    aved = list1[3]
    i = list1[4]
    for line in f:
      line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3] # splitting data set
      if line.find(z) != -1:
        a = a + ((float(line.split(',')[0]) - avea)**2) # taking values in column one minus average squared
        b = b + ((float(line.split(',')[1]) - aveb)**2)
        c = c + ((float(line.split(',')[2]) - avec)**2)
        d = d + ((float(line.split(',')[3]) - aved)**2)
    return (round((a/(i-1))**0.5, 5), round((b/(i-1))**0.5, 5), round((c/(i-1))**0.5, 5), round((d/(i-1))**0.5, 5)) # returns standard deviation of each column rounding to 5 decimal points
print ("This is the standard deviation for iris setosa", stdvar('setosa')) # print standard deviation by class
print ("This is the standard deviation for iris versicolor", stdvar('versicolor'))
print ("This is the standard deviation for Iris virginica", stdvar('virginica'))
# the calculation for the standard variation follows the formula described on wikipedia, the way the calculation is written I have found and adapted from stack overflow (to use times 0.5 instead of sqrt)
#Luisa Timothy 22-04-2018
# output calculated with all functions displayed together in table form
def average(x, y): # function for average
  return (round((x / y),4)) # rounding to the floating number

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

def sorting(z): # function to sort the values in each column
  with open("irisdata.csv") as f:
    a = []; b = []; c = []; d = []; i = 0 # variables replacing the position in the dataset
    for line in f:
      line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3] # splitting data set
      if line.find(z) != -1:
        a.append(line.split(',')[0]) # appends the values to sort them
        b.append(line.split(',')[1])
        c.append(line.split(',')[2])
        d.append(line.split(',')[3])
        i = i + 1 # counter for number of lines
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    mina = a[0] # returns the minimum value for a meaning the one in position 0
    maxa = a[i-1] # returns the maximum which is position i-1
    mediana = a[int(i/2)] # prvides the median for a
    minb = b[0]
    maxb = b[i-1]
    medianb = b[int(i/2)]
    minc = c[0]
    maxc = c[i-1]
    medianc = c[int(i/2)]
    mind = d[0]
    maxd = d[i-1]
    mediand = d[int(i/2)]
  return (mina, maxa, mediana, minb, maxb, medianb, minc, maxc, medianc, mind, maxd, mediand)

print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Name", "Values", "Average", "Minimum", "Maximum", "Median", "Standard-Dev"))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("All", "1", str(classcalculator('ris')[0]), str(sorting('ris')[0]), str(sorting('ris')[1]), str(sorting('ris')[2]), str(stdvar('ris')[0])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("All", "2", str(classcalculator('ris')[1]), str(sorting('ris')[3]), str(sorting('ris')[4]), str(sorting('ris')[5]), str(stdvar('ris')[1])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("All", "3", str(classcalculator('ris')[2]), str(sorting('ris')[6]), str(sorting('ris')[7]), str(sorting('ris')[8]), str(stdvar('ris')[2])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("All", "4", str(classcalculator('ris')[3]), str(sorting('ris')[9]), str(sorting('ris')[10]), str(sorting('ris')[11]), str(stdvar('ris')[3])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Setosa", "1", str(classcalculator('setosa')[0]), str(sorting('setosa')[0]), str(sorting('setosa')[1]), str(sorting('setosa')[2]), str(stdvar('setosa')[0])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Setosa", "2", str(classcalculator('setosa')[1]), str(sorting('setosa')[3]), str(sorting('setosa')[4]), str(sorting('setosa')[5]), str(stdvar('setosa')[1])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Setosa", "3", str(classcalculator('setosa')[2]), str(sorting('setosa')[6]), str(sorting('setosa')[7]), str(sorting('setosa')[8]), str(stdvar('setosa')[2])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Setosa", "4", str(classcalculator('setosa')[3]), str(sorting('setosa')[9]), str(sorting('setosa')[10]), str(sorting('setosa')[11]), str(stdvar('setosa')[3])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Versicolor", "1", str(classcalculator('ersicolor')[0]), str(sorting('ersicolor')[0]), str(sorting('ersicolor')[1]), str(sorting('ersicolor')[2]), str(stdvar('ersicolor')[0])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Versicolor", "2", str(classcalculator('ersicolor')[1]), str(sorting('ersicolor')[3]), str(sorting('ersicolor')[4]), str(sorting('ersicolor')[5]), str(stdvar('ersicolor')[1])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Versicolor", "3", str(classcalculator('ersicolor')[2]), str(sorting('ersicolor')[6]), str(sorting('ersicolor')[7]), str(sorting('ersicolor')[8]), str(stdvar('ersicolor')[2])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Versicolor", "4", str(classcalculator('ersicolor')[3]), str(sorting('ersicolor')[9]), str(sorting('ersicolor')[10]), str(sorting('ersicolor')[11]), str(stdvar('ersicolor')[3])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Virginica", "1", str(classcalculator('irginica')[0]), str(sorting('irginica')[0]), str(sorting('irginica')[1]), str(sorting('irginica')[2]), str(stdvar('irginica')[0])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Virginica", "2", str(classcalculator('irginica')[1]), str(sorting('irginica')[3]), str(sorting('irginica')[4]), str(sorting('irginica')[5]), str(stdvar('irginica')[1])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Virginica", "3", str(classcalculator('irginica')[2]), str(sorting('irginica')[6]), str(sorting('irginica')[7]), str(sorting('irginica')[8]), str(stdvar('irginica')[2])))
print ('{:12}{:12}{:12}{:12}{:12}{:12}{:12}'.format("Virginica", "4", str(classcalculator('irginica')[3]), str(sorting('irginica')[9]), str(sorting('irginica')[10]), str(sorting('irginica')[11]), str(stdvar('irginica')[3])))
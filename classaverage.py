# Luisa Timothy 07-04-2018
# Calculating the average of each class in the dataset

with open("irisdata.csv") as f:
    a = 0.0; b = 0.0; c = 0.0; d = 0.0; i = 0 # variables replacing the position in the dataset
    def average(x, y): # function for average
      return (round((x / y),4)) # rounding to the floating number
    for line in f:
      line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3] # splitting data set
      if line.find('setosa') != -1:
        a = a + float(line.split(',') [0]) # calculating together
        b = b + float(line.split(',') [1])
        c = c + float(line.split(',') [2])
        d = d + float(line.split(',') [3])
        i = i + 1 # counter for number of lines
      elif line.find('versicolor') != -1:
        a = a + float(line.split(',') [0]) # calculating together
        b = b + float(line.split(',') [1])
        c = c + float(line.split(',') [2])
        d = d + float(line.split(',') [3])
        i = i + 1 # counter for number of lines
      else:
        a = a + float(line.split(',') [0]) # calculating together
        b = b + float(line.split(',') [1])
        c = c + float(line.split(',') [2])
        d = d + float(line.split(',') [3])
        i = i + 1 # counter for number of lines
    print ('{:8}{:8}{:8}{:8}'.format(str(average(a, i)), str(average(b, i)), str(average(c, i)), str(average(d, i))))
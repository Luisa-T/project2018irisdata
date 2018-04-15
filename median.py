# Luisa Timothy 14-04-2018
# median calculation of the iris dataset
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
  return (mina, maxa, mediana, '\n', minb, maxb, medianb, '\n', minc, maxc, medianc, '\n', mind, maxd, mediand)


print(sorting('ris')) # prints the minimum, maximum and median for the whole dataset by columns
print(sorting('setosa')) # prints minimum, maximum, and median for each column by flower class
print(sorting('versicolor'))
print(sorting('virginica'))
# Luisa Timothy 21/04/2018
# histogram for the Iris dataset

def sep(z, y): # function to separate the dataset and represent the data in a graphic fashion
  with open("irisdata.csv") as f: # opens the .csv file
    a = []; b = []; c = []; d = []; i = 0
    for line in f:
      line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3] # splitting data set
      if line.find(z) != -1:
        a.append(line.split(',')[0]) # appends the values to sort them
        b.append(line.split(',')[1])
        c.append(line.split(',')[2])
        d.append(line.split(',')[3])
        i = i + 1 # counter for number of lines
    if y == 1:
      return(a)
    elif y == 2:
      return(b)
    elif y == 3:
      return(c)
    elif y == 4:
      return(d)
import matplotlib.pyplot as pl # importing the plotting functionality to display the data in the above function in a graphic way
pl.hist(sep('ris', 1)) # picks the data according to a string and the position, I enter the flower name and the position and run the code instead of using ipython. I therefore only have to run the code which I find more convenient
pl.show() # shows a graphical representation of the data
# to run this code first run it for 'ris' 1-4 and then for 'setosa' 1-4, 'versicolor' 1-4, and 'virginica' 1-4
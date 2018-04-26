# Project 2018 Programming and Scripting Luisa Timothy.

# The Iris dataset and Python code to analyse it. 
Project task 2018 for the module Programming and Scripting, GMIT.
Contents:

1. A brief overview of the origin of the Iris Dataset
2. Why is it important for Data Analytics
3. Python code
4. Tables and graphics
5. Investigations conducted and findings
6. References

1. A brief overview of the origin of the Iris Dataset
The Iris Dataset was first discussed by Ronald Fisher, a British statistician and biologist[1]. He first published it in his article "The use of multiple measurements in taxonomic problems" in 1936[1]. It was collected by Edgar Anderson (therefore also sometimes called the Anderson's Iris dataset)[1]. 50 samples each were collected for the dataset from samples of Iris setosa, Iris virginica, and Iris versicolor[1].

The dataset contains four features for each sample:

- the length of the sepals
 in centimeters
- the width of the sepals
 in centimeters
- the length of the petals
 in centimeters
- the width of the petals in centimeters [1]


The class of iris could be considered a fifth feature within the dataset[1].
Based on the data, Fisher was able to distinguish between the class using a linear discriminant model[1] because it is not possible to separate the class  using a linear model[3].

2. Why is it important for Data Analytics

3. Python code
  
3.1 average.py calculates the average of each column and displays them in one row
  
3.2 classaverage.py is meant to calculate the average of each class of Irises
  
3.3 The file median.py calculates three values: a) the median, b) the minimum value, and c) the maximum value of each column as well as broken down to the flower classes.
  
3.4 The file deviation.py calculates the standard deviation of each column in the dataset and then also breaks it down by flower class.

3.5 The file output.py displays the full output of the above code in a table.
The column values stands for the four features:
1 stands for the sepal length
2 stands for the sepal width
3 stands for the petal length
4 stands for the petal width
3.6 histogram.py is the code used to get the graphic representations of the data
4. Tables and graphics

col1.png-col4.png are each column for the whole dataset
setosa1.png-setosa4.png is a graphic representation of each column for iris setosa
versicolor1.png-versicolor4.png is a graphic representation of each column for iris versicolor
virginica1.png-virginica4.png is a graphic representation of each column for iris virginica

5. Investigations conducted and findings

First I used the average.py to calculate the average for each column. I have rounded the values to four decimal points.
The average values for the whole dataset are the following: 5.8433 sepal length, 3.054 sepal width, 3.7587 petal length, and 1.1987 petal width.
Following up on that I used the classaverage.py code to calculate the average values for each flower type:
The average values for iris-setosa are 5.006 (sepal length)  3.418 (sepal width)  1.464  (petal length) 0.244 (petal width).
The average values for iris-versicolor are 5.936 (sepal length)  2.77 (sepal width)   4.26 (petal length)  1.326 (petal width).
The average values for iris-virginica are 6.588 (sepal length)  2.974 (sepal width)  5.552  (petal length) 2.026 (petal width).
Additionally, I used median.py to output the minimum, maximum and median values of the dataset. The results are as follows:
This is the minimum, maximum, and median of Iris setosa ('4.3', '5.8', '5.0', (sepal length), '2.3', '4.4', '3.4', (sepal width), '1.0', '1.9', '1.5', (petal length), '0.1', '0.6', '0.2' (petal width))
This is the minimum, maximum, and median of Iris versicolor ('4.9', '7.0', '5.9', (sepal length) '2.0', '3.4', '2.8', (sepal width), '3.0', '5.1', '4.4', (petal length), '1.0', '1.8', '1.3' (petal width))
This is the minimum, maximum, and median of Iris Virginica ('4.9', '7.9', '6.5', (sepal length), '2.2', '3.8', '3.0', (sepal width), '4.5', '6.9', '5.6', (petal length), '1.4', '2.5', '2.0' (petal width)).
Lastly, I used deviation.py to calculate the standard deviation of the dataset:
This is the standard deviation for iris setosa (0.35249, 0.38102, 0.17351, 0.10721)
This is the standard deviation for iris versicolor (0.51617, 0.3138, 0.46991, 0.19775)
This is the standard deviation for Iris virginica (0.63588, 0.3225, 0.55189, 0.27465)
While the average value for sepal length is calculated as 5.8433 we can see from the graph col1.png that there are two peeks, one around 5.0 but another one which is actually higher at 6.0-6.3. For the sepal width the average seems to be fairly accurate compared to col2.png. For petal length, comparing to col3.png the average seems even more scewed since most values are below the average value calculated and the same goes for petal width average compared to col4.png.
6. References


1. https://en.wikipedia.org/wiki/Iris_flower_data_set

2. http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html

3. https://archive.ics.uci.edu/ml/datasets/iris

4. Fisher,R.A. "The use of multiple measurements in taxonomic problems" Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to Mathematical Statistics" (John Wiley, NY, 1950). 

# AI Assignment 1
Assignment 1 (Bonus) for my Artificial Intelligence course

## Information
Name: Tretin Raney

700#: 700721956

## Assignment Information
There were 4 different exercises to finish in this assignment, each other requiring some sections to be finished. Here is a description of what was done in each section:

### Exercise 1
The first exercise was working on prediction of housing prices in California. I had to fill out some missing methods. The first one I had to finish was the "train_test_split" method call, where I had to set the test_size to 0.8. By setting it to 0.8, we are setting the training set size to 80% of the total set, which allows us to set the other 20% as the testing set. The next method I had to fill out was the .fit() function on my model, which allows me train my model. The last thing I had to fill out in Exercise 1 was the .predict() function, which goes through the last 20% of the set attempting to make predictions and comparing them to the actual values.

### Exercise 2
The second exercise was working on K-Means clustering. I also had to fill out some missing methods in this exercise. The first one I had to finish was the "n_clusters" attribute in the KMEANS() method call. Since the exercise wanted me to initialize it with 4 clusters, I had to set n_clusters to 4. After that, I had to add the .fit_predict() method to cluster the data in X to the 4 clusters I created previously.

### Exercise 3
The third exercise was working on Neural Networks with Kera. For the first attribute I had to finish, I had to set the input_shape attribute of the input layer of the Neural Network. Since we specified beforehand the num_features for this attribute, I just had to specify this within the input_shape attribute. After this, I had to set the learning_rate of the model.compile() method call. Since we normally use 0.001 as our learning rate in order to encourage more precise learning of the model.

### Exercise 4
The fourth and last exercise was implementing a better step function for the GridWorld environment. There was only one attribute I had to set within this one, which was placing a 1 in the max function for r. This caused the function call to look like:
'''
r = max(r - 1, 0)
'''
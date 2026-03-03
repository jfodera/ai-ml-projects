# Lect 2 Notes
- [Titanic mini-project](https://github.com/Uzmamushtaque/Projects-in-Machine-Learning-and-AI/blob/main/TitanicExample.ipynb) is set up extremley well. 
  - this is how we should set up our in class projects

## Review
- y-hat - models predicted value of the target value y 

## Going Over Titanic example
- Go over this before you start the homework 
- can drop a certain feature if there is not enough actual data
  - meaning there is a lot of NaN
- Good idea to visualize the data before as its important to understand correlation
  - because correlation is important to dependency on variables
- not all of these visualizations are required, but you need some and a blurb to justify what you are pulling from those charts 
- Sometimes we need to transform the data from how we receive it in its raw state
- need to convert categorical data types to numericals (transforming) 
- other times we need to do scaling to make sure the bias and variance is in the right spot 

## Introduction to tensors
- multidimensional numerical representation of data 
- recall: mutability; can change variable, immutable; cannot change variable 
- Binary scalar operations are available and faster so [use the shortcuts](https://colab.research.google.com/github/Uzmamushtaque/CSCI_4170_6170_Spring2026/blob/main/Lecture_02.ipynb#scrollTo=sNiy0EOh1AzG)

## What the [minimal preprocessing](https://colab.research.google.com/github/Uzmamushtaque/CSCI_4170_6170_Spring2026/blob/main/Lecture_02.ipynb#scrollTo=0aFfHGtZeyKb) should be 
- this should be only for the first couple of homework, will evolve over time. 

## Vectorization 
### What Logistic Regression is and how we will implement this on HW 1
- Maximum Likelihood Estimate (MLE) for Logistic regression 
  - Bernoli 
- Negative Log Likeliehood (NLL) 
- Obviously, the goal is to minimize the loss 
- Understand why we are using Cross entropy error instead of mean squared error 
  - cross entropy loss is both convex and differentiable which is good because that is what we want. 
    - **convex** - any local min is a global minimum 
- **Implement** - come up with optimal parameter model 
  - aka the optimal weights 
- See the graph, minimizing the loss function to find the weights 
  - aka cost function 
- **Gradient Descent** 
  - 1) Initialize parameters (w_1, w_2)
    - randomly generate them 
    - note we are trying to move closer to the bottom
  - 2) Compute A
    - typically referred to as *forward pass* 
  - 3) Then we compute the gradient of the loss with respect to the current weights
    - see formulas on notes sheet 
  - 4) Update Weights 
  - We keep running this until we are in a certain range of loss (close enough to the global min) 
  - we are also takling about the learning rate 
    - multiplying the gradient of the lost by some positive value 
      - once we have the direction to move the initial values, we need to define how *far* we move
      - the variable that determines that is the learning rate (is called a hyperparameter) 
    
## Activation Functions 
- there are multiple, right now we are only using sigmoid 
  - maps any real number to a value between zero and 1
- *Saturation* in a problem, can become an issue 

## Talking about paper 1
- Batch Gradient Descent
  - assumption is that it uses the entire data set to update
  - really slow 
- Mini-Batch Gradient Descent
  - Smaller batches, a little faster
- Stochastic Gradient Descent 
  - picking a random data point, to help move in the right direction. eventually converges 
  - from the paper, thing of the thetas and 'w's

- Reviewing the Challenges
  - choosing the learning rate can be difficult 
    - it can be variable 
  - Adagrad algorithm adapts the learning rate to parameters
  - Adadelta is a easier one to understand 
  - RMSprop - these are others
  - Adam - these are others
  - will revisit these for lab 1 

## To do 
- review **one hot encoding** 
  - helps to convert categorical data types to numerical data types 
- What does the [rank](https://colab.research.google.com/github/Uzmamushtaque/CSCI_4170_6170_Spring2026/blob/main/Lecture_02.ipynb#scrollTo=7U2InS2KsjwD&line=1&uniqifier=1) here represent? 
- Figure out what the [Broadcasting Mechanism](https://colab.research.google.com/github/Uzmamushtaque/CSCI_4170_6170_Spring2026/blob/main/Lecture_02.ipynb#scrollTo=eLW3ildFibT9) is 
  - what the mis match is? 
- Read the paper 1 for lecture 
  - don't get too bogged down in the features
    



# Lect 1 In-Class Notes

## Administrative stuff
- grade will be assessed on how well we can explain our performance. Not necc how good/bad it is. 
- Data for projects is located in lect-1.ipynb
  - along with resources for final projects 
- For homeworks, submit a .txt file with a link to your work as your submission 


## What is Machine Learning? 
- ML algorithm is the process that uncovers underlying relationship within the data
- Machine learning model is the result of a Machine Learning Algorithm. 
  - think of this model as a function with varying outputs given varying inputs
- Model is derived from historical data. 
  - when trained on differing data, the model itself will change

## ML Applications
- recognize objects from pictures
- predict location of robot 
- direct self-driving car. 

## Categorizing ML Models 
### Types of Learning 
- Supervised: Regression, Classification 
- Unsupervised: model is not trained on the y's 
- Reinforcement Learning
### Types of models
- Discriminative - learns the decision boundary in order to classify 
  - cannot generate
- Generative - Learns the distribution of data in order to correctly infer, and generate new date 


## Grouping ML Algorithms'
### 3 Main Ways
- first by their learning style 
- second is by *modeling paradigm*
  - what they assume about the data and what they choose to model 
    - *Note* - this is not by task or optimization method 
- third by grouping of algorithm by similarity in form or function 

## ML Algorithms Grouped by Style 
### Supervised Learning Algorithms 
- input data is called training data and each point has a known label or result 
  - like spam/not-spam for emails 
- model is culminated by forcing it to make predictions on training data and correcting when wrong 
  - training continues until model reaches desired accuracy on training data 
- Example problems: 
  - Classification 
  - Regression 
- Example Algorithms: 
  - **Logistic Regression** - returns the probability that an input x belongs to class 1
    - where linear regression typically outputs a continuous real-valued number but is helpful for creating a decsision boundary 
  - **Back Propagation Neural Network** - utilizes gradient descent over multiple layers to minimize prediction error 

### Unsupervised Leaerning ALgorithms 
- input data is not labeled and does not have a known result 
- Model is curated by analyzing and pulling out structures present in the input data 
  - could organize data by similarity 
  - to process data and reduce redundancy
  - or to extract general rules.
- Example problems: 
  - clustering 
  - dimensionality reduction
  - *association rule learning* - discovers interesting relationships, patterns, or correlations between variables in large datasets 
    - if X occurs, then Y tends to occur. 
- Example Algorithms 
  - *DBScan* - Density-Based Spacial Clustering of Applications with Noise
  - *K-Means* - partitions data into K clusters

### Semi-Supervised Learning 
- Input data is a mixture of labeled and unlabeled 
- typically a desired prediction problem but the model must learn the structures to organize the data as well as make predictions 
- Example Problems: 
  - classification
  - regression 
- Example Algorithms 
  - extensions to other flexible methods that make assumptions about how to model the unlabeled data


## Reinforcement Learning 
- Training ML models to make a sequence of decisions
- Agent learns to achieve goal in uncertain and potentially complex environment. 
- The AI faces a 'game-like' situation 
- trial and error based when model is solving problems 
- In order to train, the AI gets either rewards or penalties for the actions it performs 
  - the goal of the model is to maximize the reward 

## ML Algs Grouped by Modeling Paradigm
- Back to the discriminative and Generative models 
### Discriminative Models
- make predictions on unseen data by considering conditional probability 
- used to discriminate between various classes 
- In the form of P(y|x) 
- Meant to either model the conditional distribution (P(y|x)) or directly learn a decision boundary 
- Goal: predict y from x 
- Ex. Log regression, SVM (support vector machine), or neural network classifiers 
### Generative Models 
- models focus on the distribution of the dataset to make a call on how llikely a given sample is. 
- capture probability in the form of P(y,x) or P(x) if no lables 
- Model joint distribution p(x,y) often via p(x | y) * p(y) or model p(x) alone 
- Goal: learn how data is generated, so it can eventually do it itself 
  - Can classify using Bayes': 
  $$p(y \mid x)=\frac{p(x \mid y)\,p(y)}{p(x)}.$$
- Examples: Naive Byes, Gaussian Mixture Models, HMMs, VAEs, GANs, diffusion 
#### Problem formation 
- assumed labeled data spam or ham problem
- we want to determine probability of spam email (P(y=1|x))
- Discriminative way: model will assume some underlying functional form for P(y|x)
  - parameters of the model are then determined by using training data. 
- Generative Model: conditional probability P(y|x) is calculated by using the prior P(y) and likelihood P(x|y) from training data
  - this is applied to Bayes theorem to get final result 

## Machine Learning Algorithms Grouped by Similarity.

- 1.) **Regression Algorithms**
  - Most popular algorithms: 
    - Ordinary Least Squares Regression (OLSR) 
    - Linear Regression 
    - Logistic Regression 
    - Stepwise Regression 
- 2.) **Instance-based Algorithms** 
  - These learning models are decision problems with instances or examples of training data that are deemed important or required to the model 
  - Most popular algorithms: 
    - K-Nearest Neighbor (KNN) 
    - Self-Organizing Map (SOM) 
    - Support Vector Machines (SVM) 
- 3.) **Regularization Algorithms**
  - Extension made to another method (typically regression methods) that penalize models based on their complexity. 
  - This results in the favoring of the simpler models that are better at generalizing
  - the most popular algorithms are: 
    - Ridge Regression 
    - Least Absolute Shrinkage and Selection Operator (LASSO) 
    - Elastic Net
    - Least-Angle Regression (LARS) 
- 4.) **Decision Tree Algorithms**
  - These methods construct a model of decisions made based on actual values of attribtues in the data. 
  - Most popular algs: 
    - Classification and Regression Tree (CART) 
    - Conditional Decision Trees
- 5.) **Clustering Algorithms**
  - typically organized by modeling approches such as: 
    - *centroid-based* - utilizes a central data point
    - *Hierarchical* - not based off a center
  - popular algs: 
    - K-Means 
    - K-Medians 
- 6.) **Artificial Neural Network Algorithsm** 
  - Most popular algs
    - Perceptron 
    - Multilayer Perceptrons (MLP) 
    - Back-propagation 
    - Stochastic Gradient Descent
    - Hopfield Network
    - Radial Basis Function Network (RBFN) 
- 7.) **Deep Learning Algorithms**
  - A modern update to artificial neural networks that exploit abundant cheap computation
  - most popular algs: 
    - COnvolutional Neural Network (CNN) 
    - Recurrent Neural Network (RNN ) 
    - Long Short Term Memory Networks (LSTMs)
      - built to remember long and short well 
    - Stacked Auto-Encoders
    - Deep Boltzmann Machine (DBM) 
    - Deep Belief Networks (DBN) 

## THe Linear Model
- Here, we assume there exists and linear relationship between independent and dependent variables. We will discuss the linear model from the perspective of regression (numeric values mostly)
### Linear Regression 
- assume linear between x and y 
- therefore, y can be expressed as a weighted sum of the elements in x
- some noise is permissable 
- the independent variables upon which teh predictions are based on are called features (covariates) 
- data is indexed by i, such that each input can be broken down as such: $x^{(i)}$ = $[x_1^{(i)},x_2^{(i)}]$ and the corresponding labels as $y^{(i)}$
  - yhat is defined by this: $\hat{y}^{(i)} = w^\top x^{(i)} + b$
    - remember, b is the bias 

- **The Model**
  - the linearity assumptions states that the target variable can be expressed as a weighted sum of the features: 
    - Note: we are using price of a house as a taget, and area (in sqft) and age(in years) to predict it. 
  - $price = w_{area}.area + w_{age}.age +b$
  - The goal is to choose the weights w and the bias 'b' such that on average, the predictions made according to our model best fit the true prices observed in the data.  
  - Models whose output prediction is determined by the affine trasformation of input features are linear models.
    - In these scenarios, the affine transformation is specified by the chosen weights ans bias. 
    - an affine transformation is a linear transformation followed by a shift

## Loss Function 
- There is a target value and a predicted value in any ML problem 
  - predicted trying to be target
- Loss function is a way to quantify difference between the real and predicted value of the target
- usually positive num where smaller vals are better 
- most popular lost function in regression problems is the *squared error* 

- if the predicted value for an example i is $\hat{y}^{(i)}$
- corresponding actual label is: ${y}^{(i)}$
- then the squared error loss function is given by: $l^{i}(w,b)$ = $\frac{1}{2}(\hat{y}^{(i)} - y^{(i)})^{2}$
  - this is a function of weights and biases, for the given data example indexed by i 
  - note the first character is an l
  - the constant of 1/2 makes no real difference, but is notationally convenient, cancelling out with the exponent when we take the derivative of the loss. 
- Sicne training dataset is given to us and out of our control, the empirical error is only a function of the model parameters. 

## Cost Function 
- Can measure the quality of a model on entire dataset of n examples by either averaging or summing the losses on the training set. 
- This gives us the *cost function*: 
  - $L(w,b) = \frac{1}{n} \sum_{i=1}^{n} l_i(w,b)$
- When training the model, we wint to find the parameters (w* - optimal weight, and b* optimal bias) that minimize the total loss across all training examples; 
  - $w^∗$,$b^∗$ = $argmin_{w,b} \space L(w,b) $
    - argmin means the values of w,b that minimize the cost function
- We solve the optimization problem by: 
  - assuming bias b is part of w 
    - appending a column to the design matrix X consisting of all ones
  - From here, our problem boils down to minimizing $∥y−Xw∥^2$
  - taking the derivative of the loss with respect to W and setting it equal to zero yeilds the analytical (closed-form) solution: 
    - 'closed form' - no iteration, no approximation, no “keep computing until it converges.”
    - $\textbf{w}^* = (X^TX)^{-1} X^Ty$

## Linear Model Assumptions
- Linearity - relationship bet independent and dependent variables is linear
- Independence - observations are independent of each other
- Homoscedasticity: variance of the errors is constant across all levels of the independent variables
- Normality - Errors follow a normal distribution
- No Multicollinearity - independent variables are not highly correlated with eachother. 

### MLE (Maximum Likelihood Estimation)
- *likelihood function* - The likelihood function measures the probability of observing the given data under the assumed model.
  - think of the Likelihood Function as a "Summary of Success" for your model's current settings.
  - we want to maximize this 
- Most ML models are optimization problems focused on minimization of error. 
- MLE is a recipe for formulating the loss function that is to be minimized 
- MLE is meant to find parameter values within the training data that maximize the likelihood function

### Logistic Regression 
- Using linear regression to predict binary classification will result in a continuous outcome. 
- A problem with bounded target outcomes (specifically binary classification) will use logistic regression. 
- In Logistic Regression, the model doesn't output "0" or "1" directly. It outputs a continuous value between 0 and 1, which we interpret as the probability that the input $x_i$ belongs to the "positive" class ($y=1$).
- To do this, we use an activation on top of our linear model(from linear regression) 
  - usually the sigmoid function. 
  - 'activation' is simply a function applied to the output of a linear model. 
- The predicted outcome:
  - $\hat{y}$= $\sigma(\textbf{w}^Tx + b)$
  - where $\sigma(z) = \frac{1}{(1+e^{-z})}$
### Loss Function 
- Cannot use squared error loss function for logistic regression 
- So, the loss function for a single instance i is given by: 
  - $l^{i}(y^{(i)},\hat{y}^{(i)})$ = $-(y^{(i)}\space log\hat{y}^{(i)} + (1-y^{i}) log(1-\hat{y}^{(i)}))$
- The cost function for the entire data: 
  - $L(y,\hat{y}) = \frac{1}{n} \sum_{i=1}^{n} l^{i}(y^{(i)},\hat{y}^{(i)})$

### To formulate a loss function using MLE, you need two ingredients:

1. **The Model ():** Your guess for the outcome (the architecture).
2. **The Probability Distribution:** Your assumption about how the real data  varies around your guess  (the noise).

Here is how those two work together to "formulate" the loss:

#### 1. Defining  (The "Signal")

When you define , you are defining the **structure of your prediction**.

* In Linear Regression: 
* In Neural Networks: 

By defining , you are essentially saying: *"I believe the 'true' center of the data follows this mathematical pattern."*

#### 2. Defining the Distribution (The "Noise")

This is the part that actually turns  into a **Likelihood function**. You have to decide how  (the actual data) is distributed around your .

* **Assumption A:** "I think the data  varies around  like a bell curve." → **This leads to Mean Squared Error.**
* **Assumption B:** "I think  is a binary choice (0 or 1) with probability ." → **This leads to Cross-Entropy.**

## Gradient Descent
- in a ML Alg, goal is to minimize the cost function 
- This typically cannot be solved analytically. 
- In these cases, we iteratively reduce the error by updating the parameters in the direction that incrementally lowers the cost function. - **Gradient Descent**

- Instead of calculated the cost function of every iteration and updating from there (very expensive) we settle for sampling a random minibatch of examples every time we need to make an update. 
  - This is called **minibatch stochastic gradient descent**
### Steps
- Initialize the values of the model parameters, typically at random
- iteratively sample random minibatches from the data, updating the parameters i nthe direction of the negative gradient
### Mathematically 
- $(w,b) \leftarrow (w, b)- \frac{\eta}{B}\sum_{i\epsilon{B}}\partial_{(w,b)}l^{i}(y^{(i)},\hat{y}^{(i)})$
  - B is number of examples in each minibatch 
  - $\eta$ is learning rate
  - these two above are hyperparams and not typically learned through model training
- hyperparams are adjusted on a separate validation set
- after training for a predetermined number of iterations (or until stopping criteria is met), we record the estimated model parameters, denoted $\hat{w},\hat{b}$. 
  - we use hats because these are not going to be the exact minimizers of the loss funciton
- Once these params are learned, we can go and calculate the predicted value for each example 

## Why convex
- If the loss function L($\theta$) is convex in the parameters $\theta$: 
- *No spurious local minima* - any local minimum is a global minimum
  - ensures gradient-based solutions don't fall down the 'wrong path' 
- *Stronger Guarantees* - Many optimization algorithms have clean convergence guarantees under standard assumptions
- *Easier debugging* - if training fails, its more likely due to the data, features, or optimization setting rather than a difficult objective landscape. 
- *Stable Theory* - Many classical generalization and regularization results are simples in convex settings 
  - Such as squared error (linear regression), logistic loss (logistic regression), hinge loss (SVM)

## Why Differentiable
- Loss is differentiable (or at least has subgradients)
  - Differentiable → one exact direction
  - Subgradient exists → many acceptable directions

- *Enables fast first-order methods* - Gradients provide a direction for steepest descent
  - important to compute gradients efficiently
- *More efficient than gradient-free methods* - Without gradients, often rely on expensive approaches that scale poorly in high simensions
- *Better numerical Behavior* - Smooth losses allow stable step-size control and can benefit from second-order approximations. 
- *Supports Modern Tooling* - automatic differentiation settings nowadays typically assumes differentiability almost everywhere. 
- Note - Optimization can still work using subgradients or smoothing; perfect differentiability everywhere is not required 

## Misc Definitions
- A general learning algorithm is one that improves its performance on a task by learning from data
- A **Deep** learning algorithim is one that uses neural networks with many layers to learn features 
- **Regression** - how one variable changes as another changes 
- **Paradigm** - modeling approach or methodology 
- **Regularization** - Method to prevent against overfitting 
- **K-Means vs K-NN** 
  - K-means is a unsupervised *clustering* algorithms that clusters data and answers the question "which points belong together" 
  - k-NN is a supervised *learning* algorithm that predicts labels 
    - answers the questiob: "Given this new point, what label should it have?"
- **Loss Function** - measures error for a single example 
- **Empirical Error** - Measures average error over the entire training dataset
- **Solving Problem Analytically** - closed form solution to it. 
## Reads if have time 
- https://cloud.google.com/learn/artificial-intelligence-vs-machine-learning

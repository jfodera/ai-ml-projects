# Data-Manip-preprocessing 
- [Titanic mini-project](https://github.com/Uzmamushtaque/Projects-in-Machine-Learning-and-AI/blob/main/TitanicExample.ipynb) is set up extremley well. 
  - this is how we should set up our in class projects
## Going Over [Titanic example](https://github.com/Uzmamushtaque/Projects-in-Machine-Learning-and-AI/blob/main/TitanicExample.ipynb)
- Go over this before you start the homework 
- can drop a certain feature if there is not enough actual data
  - meaning there is a lot of NaN
- Good idea to visualize the data before as its important to understand correlation
  - because correlation is important to dependency on variables
- not all of these visualizations are required, but you need some and a blurb to justify what you are pulling from those charts 
- Sometimes we need to transform the data from how we receive it in its raw state
- need to convert categorical data types to numericals (transforming) 
- other times we need to do scaling to make sure the bias and variance is in the right spot 
### Helpful Takeaways from preprocessing 
- `df.isna().sum()` - how many values per each column are missing 
- `df.info()` - gives general information on the dataset 
- `df.describe()` general statistics of the dataset per column
- `df.Survived.value_counts(normalize=True)` is data imbalances (can normalize here) 
  - in this context, normalize mean outputting parameters instead of raw counts. 
- `sns.pairplot(df, hue='Survived')` - plot pairwise relationships visualizing the relationship between all other columns and 'Survived'
- [this](https://github.com/Uzmamushtaque/Projects-in-Machine-Learning-and-AI/blob/main/TitanicExample.ipynb) has a lot of other great functions useful for preprocessing
- Barchart: `x = np.arange(len(labels))` //simply lists the x's in arranged order
  - `fig, ax = plt.subplots(figsize=(8,5))` - an initialization from an object oriented function 
  - `fig.tight_layout()` - autoadjusting for your chart

## Review
- y-hat - models predicted value of the target value y 

## Data Manipulation 
- Data visualization aka EDA
- Feature engineering may sometimes be necessary in order to get the data in the right format
  - typically use pandas and numpy here
    - **numpy** - good at handling large, multidimensional arrays and matrices
- If missing a value, replacing it with an average is normal practice in some cases, you just must ensure you are not introducing bias. 
- TensorFlow is OS, end to end ML lib
## Introduction to tensors (typically used in TensorFlow)
- multidimensional numerical representation of data 
  - it can be numbers, image, or textg
- recall: mutability; can change variable, immutable; cannot change variable 
- Binary scalar operations are available and faster so [use the shortcuts](https://colab.research.google.com/github/Uzmamushtaque/CSCI_4170_6170_Spring2026/blob/main/Lecture_02.ipynb#scrollTo=sNiy0EOh1AzG)
- Main difference between tensors and NumPy arrays is that tensors can be used on GPUs and TPUs 
  - **TPU** - custom made accelerator
    - specifically developed by google 
  - Therefore, tensors have faster computation 
- Core attributes
  - *Rank* - numbner of axes
  - *Shape* - sizes along each axis; length of shape = rank
  - *dtype* - element data type
  - *Device* - where tensor is stored/computed 
    - gpu, cpu, cuda, mps, tpu 
      - *cuda* - compute unified device architecture
        - software layer created by nvidia that allows GPUs to perform heavy matrix math required for deep learning 
      - *mps (Metal Performance Shaders)* - Apples version of a cuda  
- Creating a scalar tensor with the literal value of 7 that can not be changed: 
  - `scalar = tf.constant(7)`
  - `vector = tf.constant([10, 10])`
  - `matrix = tf.constant([[10, 7], [7, 10]])`
- Here is a common tensor translation: Matrix ↔ batch of matrices: (m, n) ↔ (b, m, n) (add leading batch axis).
- Tensors give us a generic way of describing n -dimensional arrays with an arbitrary number of axes
  - vectors are first-order tensors
  - matrices are second-order tensors 

### Predicting Tensor Shapes 
- x = tf.range(12)
  - (12,) 
  - produces: `[ 0  1  2  3  4  5  6  7  8  9 10 11]`
- X = tf.reshape(x, (3, 4))
  - 3 rows (num of inner arrays), 4 columns (len of inner arrays)
  - (3,4) 
  - produces: `[[ 0,  1,  2,  3],[ 4,  5,  6,  7],[ 8,  9, 10, 11]]`
- a = tf.reshape(tf.range(3), (3, 1))
  - (3,1)
  - [0,1,2] -> [[0],[1],[2]]
- b = tf.reshape(tf.range(2), (1, 2))
  - (1,2) 
  - [0,1]-> [[0,1]]
- a + b
  - (3,2) 
  - relization occurs that it needs a 3,2 result
  - a stretches to become: [[0,0],[1,1],[2,2]]
  - b stretches to become: [[0,1], [0,1], [0,1]]
  - result is [[0,1], [1,2], [2,3]]



### Initializing tensors

- Can initialize all values to be the same just like the following example: 
  - `tf.ones((3,3,4))`
    - 
    ```<tf.Tensor: shape=(3, 3, 4), dtype=float32, numpy=
      array([[[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]],

       [[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]],

       [[1., 1., 1., 1.],
        [1., 1., 1., 1.],
        [1., 1., 1., 1.]]], dtype=float32)>```
  - Can also use .zeros to initialize with zeros 
    
- `tf.random.normal(shape=[3, 4])` - creates a tensor with shape (3, 4). Each of its elements is randomly sampled from a standard Gaussian (normal) distribution with a mean of 0 and a standard deviation of 1.
  - Recall: Gaussian - Bell curve 

### Tensor Operations 
- all binary scalar operatiors perform operations elementwise between arrays/matricies 
- x = tf.constant([1.0, 2, 4, 8])
- y = tf.constant([2.0, 2, 2,2])
  - x + y = [ 3.,  4.,  6., 10.]
    - will auto-broadcast if necessary
  - x ** y = [ 1.,  4., 16., 64.]
    - `**` - exponentiation 
- `tf.exp(x)` - computer $e^x$ for every element in the tensor

- Concatenating on different axis: 
- X = tf.reshape(tf.range(12, dtype=tf.float32), (3, 4))
- Y = tf.constant([[2.0, 1, 4, 3], [1, 2, 3, 4], [4, 3, 2, 1]])
- tf.concat([X, Y], axis=0), tf.concat([X, Y], axis=1)
```
(<tf.Tensor: shape=(6, 4), dtype=float32, numpy=
 array([[ 0.,  1.,  2.,  3.],
        [ 4.,  5.,  6.,  7.],
        [ 8.,  9., 10., 11.],
        [ 2.,  1.,  4.,  3.],
        [ 1.,  2.,  3.,  4.],
        [ 4.,  3.,  2.,  1.]], dtype=float32)>,
 <tf.Tensor: shape=(3, 8), dtype=float32, numpy=
 array([[ 0.,  1.,  2.,  3.,  2.,  1.,  4.,  3.],
        [ 4.,  5.,  6.,  7.,  1.,  2.,  3.,  4.],
        [ 8.,  9., 10., 11.,  4.,  3.,  2.,  1.]], dtype=float32)>)
```
- Doing a logical statement such as `X==Y` creates a new tensor with binary results from comparing each element. 

### Broadcasting
- Broadcasting rules from the a->b scenario (moving from right to left): 
  - If the dimensions are equal, keep that number.
  - If one of the dimensions is 1, take the other (larger) number.
  - If the dimensions are different and neither is 1, the math fails (Error!).
- Common pitfalls
  - remember, broadcasting happens per-dimension, not per-tensor 
  -  don't accidentally broadcast when you intend to do a dot product
    - A*B - broadcast
    - A @ B - dot product
- This fails: `(3, 2) + (2, 2) (mismatch on the second-to-last dim)`


## Data Reading and Data Pre-processing in Colab 

### Data Loading and first-pass Preprocessing
- Most model failures start in the data pipeline, this is why you should always do a quick audit
  - Shape: num of rows/cols
  - Types: numeric vs categorical vs datetime
  - Missingness: which columns are incomplete and how incomplete 

- Minimal/Basic Preprocessing Example: 
  - 1. Separate features/label
  - Impute missing numeric values (typically using median) 
    - impute - fill in 
    - or you could delete them
  - One-hot encode categorical variables
  - carry out the train/test split 

## Vectorization 
- vectors in ML problems typically represent examples from the dataset. 
  - In math notation, denote vectors as bold-faced lower-cased letters : **x**
- ith element of vector x is $x_i$
- `x[3]` in tensorflow terms 
- **Vectorization** is a technique used to speed up Python code without using loops 
  - especially useful with operations like dot product, cross-product need to be performed on large vectors or scalars
- `a=np.random.rand(1000000)` - returns a one dimensional numpy array containing one million pseudo-random floating-point numbers:  
- using `c=np.dot(a,b)` is much faster then doing a for loop, and calculating the results element by element as [seen here](https://colab.research.google.com/github/Uzmamushtaque/CSCI_4170_6170_Spring2026/blob/main/Lecture_02.ipynb#scrollTo=stsKbQvqIhN-&line=2&uniqifier=1)

- **SIMD Instructions** - parallelization instructions 

## Vectorizing Logistic regression 
- Recall cost function: $L(y,\hat{y}) = \frac{1}{n} \sum_{i=1}^{n} l^{i}(y^{(i)},\hat{y}^{(i)})$
- Computing this requires calculating y_hat, meaning $a=(\textbf{w}^Tx + b)$ must be calculated for every element 
  - instead of calculating for every loop, find the dot product of the feature vector and the transpose of the weight vector 
    - bias term (if exists) can be added to each induvidual calculation via brodcasting 
  - this results of an A vector of: $A=[a^{(1)},a^{(2)}...a^{(n)}]$

### Logistic regression from scratch with vectorization 
- `forward pass` - process of moving your input data through the model to generat yhat 
- *vectorization* → *fast forward pass* → *fast gradients* → *gradient descent*.
- Forward: `z = X @ w + b`, `a = sigmoid(z)`
- Loss: binary cross-entropy
- Gradients: `dw = (X.T @ (a - y)) / n`, `db = mean(a - y)`
  - `dw` - derivative with respect to the weights
    - X.T = transpose of the inputs 
    - @ is matrix multiplication 
  - `db` - derivative with respect to the biases 

- Scaling the features are important to prevent this: 
  - If "Age" ranges from 0–80 and "Fare" ranges from 0–500, the model might think "Fare" is 10x more important just because the numbers are bigger. After scaling with standard scalar, both features will generally fall between -3 and 3.
- `lr - learning rate` - determines how big of a step the model takes in the direction of gradient descent after each update 
- `steps` - how many updates occur
- `eps` represents epsilon which is a tiny number that protects against log(0) errors
- `w -= lr * dw` - vital as it updates every element of the weight vector by the specified amount 
- `test_pred = (test_probs >= 0.5).astype(int)` - throws the probablilities to a certain side
- `dz = (a - y_train)` this calculates the difference of yhat - y for each row 
## Activation Functions
- The 'filter' on your model that decides whether or not a signal is strong enough to be passed to the next part of the network. 
  - in logistic regression, the sigmoid was the activation 
- there are multiple, right now we are only using sigmoid 
- *Saturation* in a problem, can become an issue 
  - WHen the gradient (slope) of a function becomes near-zero. Effectively killing the learning process for that neuron 
- Allows non-linearity of the model 
- Choosing an activation function is a vital part of NN design 
- Typical picks: 
  - `sign function` - In problems where binary class labels need to be predicted 
    - -1->1
  - `identify funciton` - where target variable to be predicted is real 
    - real valued positive numbers
  - `sigmoid` - when predicting probabilities of binary class. 
    - 0->1

### Comparison 
- Important distinction points
  - Range (bounded vs unbounded) 
  - Saturation Regions (where gradients get tiny) 
  - Smooth vs peicewise-linear
- Going to compare sigmoid (sigmoid), tanh (sign ), and ReLu (identify)
  - graphed lines represent their ranges

## Main Life Cycle of a Data Science/ML Project
- Problem Comprehension 
- Data Retrieval
- Data Wrangling 
- Data Investigation 
- Feature Engineering and selection 
  - similar to data wrangling but incorporates specific algs for feature transformation and selection 
- Model Construction 
- Implementation 
  - after model is constructed, you must deploy it efficiently and optimally 
- Supervision
  - watching and aquianting the model with new datasets

## [Gradient Calculation using tensors](https://colab.research.google.com/github/Uzmamushtaque/CSCI_4170_6170_Spring2026/blob/main/Lecture_02.ipynb#scrollTo=k-PrXhpCZDL3&line=11&uniqifier=1)
- `y.backwards()` fills the `x.grad` 'bucket'
  - calling `x.grad` first will return nothing 



    



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
- Read the paper 1 for lecture 
  - don't get too bogged down in the features
    



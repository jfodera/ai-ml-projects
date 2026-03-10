# Lect 2 Notes
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

- Broadcasting rules from the a->b scenario (moving from right to left): 
  - If the dimensions are equal, keep that number.
  - If one of the dimensions is 1, take the other (larger) number.
  - If the dimensions are different and neither is 1, the math fails (Error!).

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

## Misc 
- review **one hot encoding** 
  - helps to convert categorical data types to numerical data types 
## To do 

- What does the [rank](https://colab.research.google.com/github/Uzmamushtaque/CSCI_4170_6170_Spring2026/blob/main/Lecture_02.ipynb#scrollTo=7U2InS2KsjwD&line=1&uniqifier=1) here represent? 
- Figure out what the [Broadcasting Mechanism](https://colab.research.google.com/github/Uzmamushtaque/CSCI_4170_6170_Spring2026/blob/main/Lecture_02.ipynb#scrollTo=eLW3ildFibT9) is 
  - what the mis match is? 
- Read the paper 1 for lecture 
  - don't get too bogged down in the features
    



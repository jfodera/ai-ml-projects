# Lecture 3

## Administration 
- Discussion form points are free (literally) 



## Introduction to Tree-Based methods 
- There are not extremely interpretable 
- emerged from statistics community 
- **They are trying to lower the entropy?**

## Decision Tree 
- Arrive at a decision by asking 
- reducing the search space as much as possible is the same as reducing the entropy 
- goal is to find the smallest set of questions to arrive at the right decision \

- Best way to find the attribute to split is the Attribute Selection Measure (ASM) 
  - Goal is to select a feature that decreases the entropy of the system the most 
  - 2 main methods behind ASM 
    - Information Gain 
    - Gini Index - aka Gini Impurity 


- Must read the reading and mabye paper 1

- Esemble learning is a method to combine multiple learners in a way that is best in managing both bias and variance 
  - Bagging and Boosting are more popular for tree algs 
  - Bagging (Bootstrap Aggregation )
    - aka
    - Check out difference between bagged decision tree and random forest
  - Stacking - stacking one model on top of the other and then combining their decisions on whatever you think is best
    - you can build a pipeline and have a rule 
  - Boosting 
    - Lots of different kinds that are improvements on gradient boosting 



## Important metrics to be aware of 
- MSE for continuous problems not classifications 
- those 3 metrics should be on all of our projects along with MSE 
  - should also include a couple of sentances on what these mean 
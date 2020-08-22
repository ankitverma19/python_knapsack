
**Assignment PS - 2**

**Problem Statement**

The Indian space agency ISRO must deal with budgeting decisions to choose how to optimally divide the budget among its N competing missions. Each mission head has submitted the cost to be incurred and its overall value (or profit) for consideration. The budget available with the agency is 100 crores. They need your help in selecting as many projects
as possible with the budget constraints such that the total value returned is maximized.

For this problem we can assume that there is no dependency of launching one project on the other. If there are multiple solutions with same value, choose the one which results in maximum utilization of budget and selection of missions as well.

**Requirements**
1. Formulate an efficient recursive algorithm using dynamic programming to determine
how to select the missions to be funded and maximize value.
2. Analyse the time complexity of your algorithm.
3. Implement the above problem statement using Python 3.7.

**Approach**
For this problem statement we have selected the Knapsack algorithm using Dynamic Programming.

**Knapsack Algorithm**
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

The simplest way to solve the knapsack problem is to consider all subsets of items and calculate the total weight and value of all subsets. Consider the only subsets whose total weight is smaller than W. From all such subsets, pick the maximum value subset.

**_Optimal Sub-structure_:**  To consider all subsets of items, there can be two cases for every item.

1.  **Case 1:**  The item is included in the optimal subset.
2.  **Case 2:**  The item is not included in the optimal set.

**Complexity Analysis:**

-   **Time Complexity:**  O(2^n).  
    As there are redundant sub-problems.
-   **Auxiliary Space :** O(1).  
    As no extra data structure has been used for storing values.

The redundant sub-problem approach can be solved by using a Dynamic Programming strategy to improve the computation time and computation space requirements.

In the Dynamic programming we will work considering the same cases as mentioned in the recursive approach. In a DP[][] table let’s consider all the possible weights from ‘1’ to ‘W’ as the columns and weights that can be kept as the rows.  

The state DP[i][j] will denote maximum value of ‘j-weight’ considering all values from ‘1 to ith’. So if we consider ‘wi’ (weight in ‘ith’ row) we can fill it in all columns which have ‘weight values > wi’. Now two possibilities can take place:

-   Fill ‘wi’ in the given column.
-   Do not fill ‘wi’ in the given column.

Now we have to take a maximum of these two possibilities, formally if we do not fill ‘ith’ weight in ‘jth’ column then DP[i][j] state will be same as DP[i-1][j] but if we fill the weight, DP[i][j] will be equal to the value of ‘wi’+ value of the column weighing ‘j-wi’ in the previous row. So we take the maximum of these two possibilities to fill the current state. 

**Complexity Analysis:**

-   **Time Complexity:**  O(N*W).  
    where ‘N’ is the number of weight element and ‘W’ is capacity. As for every weight element we traverse through all weight capacities 1<=w<=W.
-   **Auxiliary Space:**  O(N*W).  
    The use of 2-D array of size ‘N*W’.

The DP approach can be further optimized by reducing the need for calculating redundant cases. We can solve this problem by simply creating a 2-D array that can store a particular state (n, w) if we get it the first time. Now if we come across the same state (n, w) again instead of calculating it in exponential complexity we can directly return its result stored in the table in constant time. This method gives an edge over the recursive approach in this aspect.

**Complexity Analysis:**

-   **Time Complexity:**  O(N*W).  
    As redundant calculations of states are avoided.
-   **Auxiliary Space:**  O(N*W).  
    The use of 2D array data structure for storing intermediate states-:A simple solution is to consider all subsets of items and calculate the total weight and value of all subsets. Consider the only subsets whose total weight is smaller than W. From all such subsets, pick the maximum value subset.
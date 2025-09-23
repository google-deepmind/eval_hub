Here is a detailed, step-by-step solution to the problem.

### 1. Understanding the Setup

Let's first formalize the process described in the problem.
- We have $n$ boxes, labeled $1, 2, \ldots, n$.
- We have balls numbered $1, 2, \ldots, m$.
- Initially, at time $t=0$, each of the $n$ boxes contains exactly $m$ balls, one for each number from $1$ to $m$. The set of balls in each box is $\{1, 2, \ldots, m\}$.

The process is sequential:
1.  A ball is drawn from Box 1. Let its number be the random variable $X_1$.
2.  This ball is placed into Box 2. Box 2 now contains $m+1$ balls.
3.  A ball is drawn from Box 2. Let its number be the random variable $X_2$.
4.  This process continues. For any step $i$ from $2$ to $n$, the ball drawn from Box $i-1$ (value $X_{i-1}$) is placed into Box $i$. Then a ball is drawn from Box $i$, and its value is $X_i$.
5.  Finally, a ball is drawn from Box $n$, and its number, $X_n$, is recorded.

Our goal is to find the condition on the positive integer $m$ such that the expected value of the written number, $E[X_n]$, is an integer.

### 2. Calculating the Expected Values

We will calculate the expected value of the drawn ball for each box in sequence. Let $E_i = E[X_i]$ be the expected value of the number drawn from box $i$.

#### Expected value from Box 1 ($E_1$)

Box 1 contains $m$ balls, with numbers $1, 2, \ldots, m$. Each ball has an equal probability of being drawn, which is $1/m$.
The expected value $E_1$ is the sum of each possible outcome multiplied by its probability:
$E_1 = E[X_1] = \sum_{k=1}^{m} k \cdot P(X_1=k) = \sum_{k=1}^{m} k \cdot \frac{1}{m}$
Using the formula for the sum of the first $m$ integers, $\sum_{k=1}^{m} k = \frac{m(m+1)}{2}$:
$E_1 = \frac{1}{m} \left( \frac{m(m+1)}{2} \right) = \frac{m+1}{2}$.

#### Expected value from Box 2 ($E_2$)

To find $E_2 = E[X_2]$, we analyze the contents of Box 2 right before the draw. Box 2 initially contains the balls $\{1, 2, \ldots, m\}$. The ball drawn from Box 1, with value $X_1$, is added to it.
So, Box 2 contains $m+1$ balls. The set of numbers on these balls is $\{1, 2, \ldots, m\} \cup \{X_1\}$.

We can find $E_2$ using the Law of Total Expectation: $E[Y] = E[E[Y|Z]]$. Here, $Y=X_2$ and $Z=X_1$.
$E_2 = E[X_2] = E[E[X_2 | X_1]]$.

First, let's find the conditional expectation $E[X_2 | X_1=k]$ for some specific value $k$ that $X_1$ can take. If $X_1=k$, Box 2 contains the balls $\{1, 2, \ldots, m\} \cup \{k\}$. The sum of the numbers on these $m+1$ balls is:
Sum = $\left(\sum_{j=1}^{m} j\right) + k = \frac{m(m+1)}{2} + k$.
Since there are $m+1$ balls, and each is equally likely to be drawn, the conditional expected value is the average of these numbers:
$E[X_2 | X_1=k] = \frac{1}{m+1} \left( \frac{m(m+1)}{2} + k \right)$.

Now, we take the expectation over all possible values of $X_1$:
$E[X_2] = E[E[X_2 | X_1]] = E\left[ \frac{1}{m+1} \left( \frac{m(m+1)}{2} + X_1 \right) \right]$.
Using the linearity of expectation, $E[aY+b] = aE[Y]+b$:
$E[X_2] = \frac{1}{m+1} \left( \frac{m(m+1)}{2} + E[X_1] \right)$.

We already calculated $E[X_1] = \frac{m+1}{2}$. Substituting this value:
$E[X_2] = \frac{1}{m+1} \left( \frac{m(m+1)}{2} + \frac{m+1}{2} \right) = \frac{1}{m+1} \left( \frac{(m+1)m + (m+1)}{2} \right)$
$E[X_2] = \frac{1}{m+1} \left( \frac{(m+1)(m+1)}{2} \right) = \frac{m+1}{2}$.

### 3. Generalizing the Expected Value for Box $i$

We have found that $E[X_1] = \frac{m+1}{2}$ and $E[X_2] = \frac{m+1}{2}$. This suggests a pattern. Let's prove by induction that $E[X_i] = \frac{m+1}{2}$ for all $i=1, 2, \ldots, n$.

**Base Case:** For $i=1$, we have shown $E[X_1] = \frac{m+1}{2}$. The base case holds.

**Inductive Hypothesis:** Assume that for some integer $i$ where $1 \le i < n$, we have $E[X_i] = \frac{m+1}{2}$.

**Inductive Step:** We want to show that $E[X_{i+1}] = \frac{m+1}{2}$.
The process for drawing from Box $i+1$ is identical to the one for Box 2, except that the ball added comes from Box $i$ instead of Box 1.
Box $i+1$ initially contains the balls $\{1, 2, \ldots, m\}$. A ball with value $X_i$ is added. The box now contains $m+1$ balls.
Using the Law of Total Expectation, $E[X_{i+1}] = E[E[X_{i+1} | X_i]]$.

Given $X_i=k$, Box $i+1$ contains balls $\{1, 2, \ldots, m\} \cup \{k\}$. The sum of numbers is $\frac{m(m+1)}{2} + k$.
The conditional expectation of the draw from Box $i+1$ is:
$E[X_{i+1} | X_i=k] = \frac{1}{m+1} \left( \frac{m(m+1)}{2} + k \right)$.

Taking the expectation over the distribution of $X_i$:
$E[X_{i+1}] = E\left[ \frac{1}{m+1} \left( \frac{m(m+1)}{2} + X_i \right) \right]$.
By linearity of expectation:
$E[X_{i+1}] = \frac{1}{m+1} \left( \frac{m(m+1)}{2} + E[X_i] \right)$.

Now, we use our inductive hypothesis, $E[X_i] = \frac{m+1}{2}$:
$E[X_{i+1}] = \frac{1}{m+1} \left( \frac{m(m+1)}{2} + \frac{m+1}{2} \right) = \frac{1}{m+1} \left( \frac{(m+1)^2}{2} \right) = \frac{m+1}{2}$.

This completes the induction. We have proven that $E[X_i] = \frac{m+1}{2}$ for all $i=1, 2, \ldots, n$.

### 4. Finding the Condition on $m$

The expected value of the number written down is $E[X_n]$. From our proof, we have:
$E[X_n] = \frac{m+1}{2}$.

The problem asks for which positive integers $m$ this expected value is an integer.
We need $\frac{m+1}{2}$ to be an integer. Let's say $\frac{m+1}{2} = K$ for some integer $K$.
This means $m+1 = 2K$.
This equation implies that $m+1$ must be an even integer.

If $m+1$ is even, then $m$ must be an odd integer.
Since the problem states that $m$ is a positive integer, the possible values for $m$ are all positive odd integers.
$m \in \{1, 3, 5, 7, \ldots\}$.

The result is independent of the number of boxes, $n$.

### Conclusion

The expected value of the number drawn from any box $i$ in the sequence is always $\frac{m+1}{2}$, regardless of $n$. For this value to be an integer, $m+1$ must be divisible by 2, which means $m+1$ must be even. This is true if and only if $m$ is an odd integer.

The set of all positive integers $m$ for which the expected value of the written number is an integer is the set of all positive odd integers.
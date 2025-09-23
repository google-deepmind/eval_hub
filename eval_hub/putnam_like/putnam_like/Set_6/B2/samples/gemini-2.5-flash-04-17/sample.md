Let $p_m$ be the probability of the $m$-th coin landing heads. According to the problem statement, $p_m = \frac{1}{2m+1}$ for $m=1, 2, \ldots, n$. The results of the coin tosses are independent.
Let $X_m$ be an indicator variable such that $X_m=1$ if the $m$-th coin lands heads and $X_m=0$ if it lands tails.
Then $P(X_m=1) = p_m$ and $P(X_m=0) = 1-p_m = 1 - \frac{1}{2m+1} = \frac{2m}{2m+1}$.
The total number of heads is $H = \sum_{m=1}^n X_m$. We want to find the probability that $H$ is an even number, i.e., $P(H \text{ is even})$.

We can use a generating function approach to solve this problem. Let $P(x)$ be the probability generating function for the total number of heads $H$. Since the coin tosses are independent, $P(x)$ is the product of the generating functions for each individual coin toss.
The generating function for the $m$-th coin is $(1-p_m)x^0 + p_m x^1 = (1-p_m) + p_m x$.
So, the generating function for $H$ is:
$$ P(x) = \prod_{m=1}^n ((1-p_m) + p_m x) $$
By definition, $P(x)$ is also given by $P(x) = \sum_{k=0}^n P(H=k) x^k$.

Let $P_{\text{even}} = \sum_{k \text{ even}} P(H=k)$ and $P_{\text{odd}} = \sum_{k \text{ odd}} P(H=k)$.
We know that $P(1) = \sum_{k=0}^n P(H=k) (1)^k = \sum_{k=0}^n P(H=k) = P_{\text{even}} + P_{\text{odd}}$. Since the sum of all probabilities must be 1, $P(1) = 1$.

Now consider $P(-1)$:
$$ P(-1) = \sum_{k=0}^n P(H=k) (-1)^k = P(H=0) - P(H=1) + P(H=2) - P(H=3) + \cdots $$
This sum can be grouped as:
$$ P(-1) = (P(H=0) + P(H=2) + \cdots) - (P(H=1) + P(H=3) + \cdots) = P_{\text{even}} - P_{\text{odd}} $$

We have a system of two linear equations with $P_{\text{even}}$ and $P_{\text{odd}}$:
1) $P_{\text{even}} + P_{\text{odd}} = 1$
2) $P_{\text{even}} - P_{\text{odd}} = P(-1)$
Adding these two equations gives $2 P_{\text{even}} = 1 + P(-1)$, so $P_{\text{even}} = \frac{1 + P(-1)}{2}$.

Now we need to compute $P(-1)$ using the expression for $P(x)$:
$$ P(-1) = \prod_{m=1}^n ((1-p_m) + p_m (-1)) = \prod_{m=1}^n (1 - p_m - p_m) = \prod_{m=1}^n (1 - 2p_m) $$
Substitute the value of $p_m = \frac{1}{2m+1}$:
$$ 1 - 2p_m = 1 - 2\left(\frac{1}{2m+1}\right) = \frac{2m+1-2}{2m+1} = \frac{2m-1}{2m+1} $$
So, $P(-1)$ is the product:
$$ P(-1) = \prod_{m=1}^n \left(\frac{2m-1}{2m+1}\right) $$
Let's write out the terms of the product:
$$ P(-1) = \left(\frac{2(1)-1}{2(1)+1}\right) \times \left(\frac{2(2)-1}{2(2)+1}\right) \times \left(\frac{2(3)-1}{2(3)+1}\right) \times \cdots \times \left(\frac{2n-1}{2n+1}\right) $$
$$ P(-1) = \frac{1}{3} \times \frac{3}{5} \times \frac{5}{7} \times \cdots \times \frac{2n-1}{2n+1} $$
This is a telescoping product. The numerator of each term cancels the denominator of the previous term:
$$ P(-1) = \frac{1}{\cancel{3}} \times \frac{\cancel{3}}{\cancel{5}} \times \frac{\cancel{5}}{\cancel{7}} \times \cdots \times \frac{\cancel{2n-3}}{\cancel{2n-1}} \times \frac{\cancel{2n-1}}{2n+1} = \frac{1}{2n+1} $$

Finally, substitute this value of $P(-1)$ into the formula for $P_{\text{even}}$:
$$ P_{\text{even}} = \frac{1 + P(-1)}{2} = \frac{1 + \frac{1}{2n+1}}{2} $$
To simplify the expression:
$$ P_{\text{even}} = \frac{\frac{2n+1}{2n+1} + \frac{1}{2n+1}}{2} = \frac{\frac{2n+1+1}{2n+1}}{2} = \frac{\frac{2n+2}{2n+1}}{2} $$
$$ P_{\text{even}} = \frac{2n+2}{2(2n+1)} = \frac{2(n+1)}{2(2n+1)} = \frac{n+1}{2n+1} $$

The probability of getting an even number of heads is $\frac{n+1}{2n+1}$.

The final answer is $\boxed{\frac{n+1}{2n+1}}$.
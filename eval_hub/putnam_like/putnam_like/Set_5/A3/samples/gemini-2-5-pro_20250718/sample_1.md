Of course. Here is a detailed, step-by-step solution to the problem.

### Problem Statement

Let $n$ be an odd number and let $e_1=1, e_2,\ldots, e_n$ be the $n$-th roots of unity. Prove that $\prod_{1 \le i < j \le n} (e_i+e_j)^2=1$.

### Solution

Let the set of the $n$-th roots of unity be $E = \{e_1, e_2, \ldots, e_n\}$. These are the roots of the polynomial $P(x) = x^n - 1$. We can express $P(x)$ in its factored form using these roots:
$$P(x) = x^n - 1 = \prod_{j=1}^{n} (x-e_j)$$

The core of our strategy will be to evaluate this polynomial at a special set of points, namely the negatives of its own roots, to find relationships between the terms in the product we wish to evaluate.

**Step 1: Evaluate $P(x)$ at $x = -e_i$ for an arbitrary root $e_i \in E$.**

Let's substitute $x = -e_i$ into the definition of $P(x)$:
$$P(-e_i) = (-e_i)^n - 1$$
Since $n$ is given to be an odd number, we have $(-1)^n = -1$. Therefore:
$$P(-e_i) = -e_i^n - 1$$
By definition, $e_i$ is an $n$-th root of unity, which means $e_i^n = 1$. Substituting this into the equation gives:
$$P(-e_i) = -1 - 1 = -2$$

**Step 2: Evaluate $P(-e_i)$ using the factored form of the polynomial.**

Now, we use the factored form of $P(x)$:
$$P(-e_i) = \prod_{j=1}^{n} (-e_i - e_j)$$
We can factor out $-1$ from each term in the product:
$$P(-e_i) = \prod_{j=1}^{n} (-1)(e_i + e_j) = (-1)^n \prod_{j=1}^{n} (e_i + e_j)$$
Again, since $n$ is odd, $(-1)^n = -1$. So we have:
$$P(-e_i) = - \prod_{j=1}^{n} (e_i + e_j)$$

**Step 3: Equate the two expressions for $P(-e_i)$ and derive a useful identity.**

From Step 1 and Step 2, we have two expressions for $P(-e_i)$. Equating them gives:
$$-2 = - \prod_{j=1}^{n} (e_i + e_j)$$
This simplifies to:
$$\prod_{j=1}^{n} (e_i + e_j) = 2$$
This identity holds for any choice of $e_i$ from the set of roots $E$.

**Step 4: Isolate the product over $j \neq i$.**

The product on the left side includes the term where $j=i$. Let's separate this term:
$$(e_i + e_i) \prod_{j \neq i, j=1}^{n} (e_i + e_j) = 2$$
$$2e_i \prod_{j \neq i} (e_i + e_j) = 2$$
Dividing by $2e_i$ (note that $e_i \neq 0$ for any root of unity), we get a key relation:
$$\prod_{j \neq i} (e_i + e_j) = \frac{1}{e_i}$$
This relation is true for each $i \in \{1, 2, \ldots, n\}$.

**Step 5: Construct the desired product from the identity.**

Let $S$ be the expression we want to evaluate:
$$S = \prod_{1 \le i < j \le n} (e_i+e_j)^2$$
Let's consider the product of all terms $(e_i+e_j)$ where $i \neq j$. We can group this product by the index $i$:
$$\prod_{i \neq j} (e_i+e_j) = \prod_{i=1}^{n} \left( \prod_{j \neq i} (e_i+e_j) \right)$$
Using the result from Step 4, we can substitute the inner product for each $i$:
$$\prod_{i=1}^{n} \left( \frac{1}{e_i} \right) = \frac{1}{\prod_{i=1}^{n} e_i}$$

**Step 6: Calculate the product of all $n$-th roots of unity.**

The roots of $x^n-1=0$ are $e_k = e^{2\pi i (k-1)/n}$ for $k=1, \ldots, n$. The product of these roots is:
$$\prod_{k=1}^{n} e_k = \prod_{k=0}^{n-1} e^{2\pi i k/n} = \exp\left(\sum_{k=0}^{n-1} \frac{2\pi i k}{n}\right) = \exp\left(\frac{2\pi i}{n} \sum_{k=0}^{n-1} k\right)$$
The sum of the first $n-1$ non-negative integers is $\frac{(n-1)n}{2}$. So the product is:
$$\exp\left(\frac{2\pi i}{n} \cdot \frac{(n-1)n}{2}\right) = e^{\pi i (n-1)}$$
Since $n$ is an odd integer, $n-1$ is an even integer. Let $n-1 = 2m$ for some integer $m$.
$$e^{\pi i (2m)} = e^{2\pi i m} = (e^{2\pi i})^m = 1^m = 1$$
Alternatively, the product of the roots of a monic polynomial $x^n + a_{n-1}x^{n-1} + \dots + a_0$ is $(-1)^n a_0$. For $P(x)=x^n-1$, $a_0=-1$. The product of roots is $(-1)^n(-1) = (-1)^{n+1}$. Since $n$ is odd, $n+1$ is even, so the product is $1$.

Thus, $\prod_{i=1}^{n} e_i = 1$.

**Step 7: Final calculation.**

Substituting the result from Step 6 into the equation from Step 5:
$$\prod_{i \neq j} (e_i+e_j) = \frac{1}{1} = 1$$
Now, let's relate this product back to our target expression $S$. The product $\prod_{i \neq j} (e_i+e_j)$ is taken over all ordered pairs $(i,j)$ with $i \neq j$. We can split this into pairs where $i<j$ and pairs where $j<i$:
$$\prod_{i \neq j} (e_i+e_j) = \left(\prod_{1 \le i < j \le n} (e_i+e_j)\right) \cdot \left(\prod_{1 \le j < i \le n} (e_i+e_j)\right)$$
Since addition is commutative, $(e_i+e_j) = (e_j+e_i)$. The second product term is over the same pairs as the first, just with indices swapped.
$$\prod_{1 \le j < i \le n} (e_i+e_j) = \prod_{1 \le i < j \le n} (e_j+e_i) = \prod_{1 \le i < j \le n} (e_i+e_j)$$
So, the full product is:
$$\prod_{i \neq j} (e_i+e_j) = \left(\prod_{1 \le i < j \le n} (e_i+e_j)\right) \cdot \left(\prod_{1 \le i < j \le n} (e_i+e_j)\right) = \left(\prod_{1 \le i < j \le n} (e_i+e_j)\right)^2$$
The expression we need to prove is $S = \prod_{1 \le i < j \le n} (e_i+e_j)^2$, which is precisely this product.

Therefore, we have shown that:
$$\prod_{1 \le i < j \le n} (e_i+e_j)^2 = 1$$

### Conclusion

The proof relies crucially on the fact that $n$ is odd. This property was used in two key places:
1.  To establish that $P(-e_i) = (-e_i)^n - 1 = -e_i^n - 1 = -2$.
2.  To show that the product of all $n$-th roots of unity is $1$.

By relating the desired product to the evaluation of the polynomial $x^n-1$ at the negative of its roots, we were able to systematically simplify the expression and prove the desired result.
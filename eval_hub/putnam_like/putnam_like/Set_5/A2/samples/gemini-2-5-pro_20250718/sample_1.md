Of course. Here is a detailed, step-by-step solution to the problem.

### **Problem Statement**

Let $(a_n)_{n=0}^{\infty}$ be a sequence of positive real numbers such that $a_{n+1}\leq\frac 12 a_n$ for all $n\geq 0$. Define $b_n=a_n-3a_{n+1}+3a_{n+2}-a_{n+3}$. Prove that $\sum_{n=1}^\infty nb_n =a_1-a_2$.

---

### **Solution**

Our goal is to evaluate the infinite sum $\sum_{n=1}^\infty nb_n$. We will approach this by first analyzing the properties of the sequence $(a_n)$, then examining the partial sum of the series, and finally taking the limit to find the value of the infinite sum.

#### **Step 1: Analyze the properties of the sequence $(a_n)$**

We are given that $a_n > 0$ for all $n$ and $a_{n+1} \leq \frac{1}{2} a_n$ for all $n \geq 0$. Let's establish the rate of convergence of $a_n$ to 0.

By repeated application of the given inequality:
$a_1 \leq \frac{1}{2} a_0$
$a_2 \leq \frac{1}{2} a_1 \leq \frac{1}{2} \left(\frac{1}{2} a_0\right) = \left(\frac{1}{2}\right)^2 a_0$
$a_3 \leq \frac{1}{2} a_2 \leq \frac{1}{2} \left(\left(\frac{1}{2}\right)^2 a_0\right) = \left(\frac{1}{2}\right)^3 a_0$

By induction, we can prove that $a_n \leq \left(\frac{1}{2}\right)^n a_0$ for all $n \geq 0$.
Since $a_n$ is a sequence of positive numbers, we have $0 < a_n \leq \left(\frac{1}{2}\right)^n a_0$.
As $n \to \infty$, $\left(\frac{1}{2}\right)^n a_0 \to 0$. By the Squeeze Theorem, we conclude that:
$$ \lim_{n \to \infty} a_n = 0 $$
This is a crucial result. Furthermore, for any polynomial $P(n)$, the exponential term $(\frac{1}{2})^n$ decays faster than $P(n)$ grows. This means that $\lim_{n \to \infty} P(n) a_n = 0$. In particular, we will need the fact that:
$$ \lim_{n \to \infty} n a_n = 0 \quad \text{and} \quad \lim_{n \to \infty} n^2 a_n = 0 $$
To be more rigorous, since $0 < n a_n \leq n \left(\frac{1}{2}\right)^n a_0$, and we know from calculus that $\lim_{n \to \infty} n (\frac{1}{2})^n = 0$ (e.g., by L'Hôpital's Rule on $x/2^x$), the Squeeze Theorem implies $\lim_{n \to \infty} n a_n = 0$.

#### **Step 2: Justify the convergence of the series $\sum_{n=1}^\infty nb_n$**

Before we manipulate the sum, we should ensure it converges. Let's examine the absolute value of the terms $nb_n$:
$|nb_n| = |n(a_n - 3a_{n+1} + 3a_{n+2} - a_{n+3})|$
Using the triangle inequality:
$|nb_n| \leq n(|a_n| + 3|a_{n+1}| + 3|a_{n+2}| + |a_{n+3}|)$
Since $a_k$ are positive, $|a_k|=a_k$.
$|nb_n| \leq n(a_n + 3a_{n+1} + 3a_{n+2} + a_{n+3})$
Using the bound $a_k \leq (\frac{1}{2})^k a_0$:
$|nb_n| \leq n \left( \left(\frac{1}{2}\right)^n a_0 + 3\left(\frac{1}{2}\right)^{n+1} a_0 + 3\left(\frac{1}{2}\right)^{n+2} a_0 + \left(\frac{1}{2}\right)^{n+3} a_0 \right)$
$|nb_n| \leq n a_0 \left(\frac{1}{2}\right)^n \left( 1 + \frac{3}{2} + \frac{3}{4} + \frac{1}{8} \right)$
$|nb_n| \leq n \left(\frac{1}{2}\right)^n a_0 \left( \frac{8+12+6+1}{8} \right) = \frac{27}{8} a_0 \cdot n \left(\frac{1}{2}\right)^n$

The series $\sum_{n=1}^\infty n \left(\frac{1}{2}\right)^n$ is a known convergent series (it can be tested with the Ratio Test). Since $|nb_n|$ is bounded by a constant multiple of the terms of a convergent series, the series $\sum_{n=1}^\infty |nb_n|$ converges by the Comparison Test. Therefore, the series $\sum_{n=1}^\infty nb_n$ converges absolutely.

#### **Step 3: Analyze the partial sum $S_N$**

Let $S_N$ be the $N$-th partial sum of the series:
$$ S_N = \sum_{n=1}^N nb_n = \sum_{n=1}^N n(a_n - 3a_{n+1} + 3a_{n+2} - a_{n+3}) $$
We can split this into four separate sums:
$$ S_N = \sum_{n=1}^N na_n - 3\sum_{n=1}^N na_{n+1} + 3\sum_{n=1}^N na_{n+2} - \sum_{n=1}^N na_{n+3} $$
To reveal the telescoping nature of this expression, we will re-index the last three sums so that each sum is in terms of $a_k$.

*   For the second sum, let $k=n+1$. Then $n=k-1$. When $n=1, k=2$. When $n=N, k=N+1$.
    $3\sum_{n=1}^N na_{n+1} = 3\sum_{k=2}^{N+1} (k-1)a_k$
*   For the third sum, let $k=n+2$. Then $n=k-2$. When $n=1, k=3$. When $n=N, k=N+2$.
    $3\sum_{n=1}^N na_{n+2} = 3\sum_{k=3}^{N+2} (k-2)a_k$
*   For the fourth sum, let $k=n+3$. Then $n=k-3$. When $n=1, k=4$. When $n=N, k=N+3$.
    $\sum_{n=1}^N na_{n+3} = \sum_{k=4}^{N+3} (k-3)a_k$

Substituting these back into the expression for $S_N$ (using $n$ as the index variable again for consistency):
$$ S_N = \sum_{n=1}^N na_n - 3\sum_{n=2}^{N+1} (n-1)a_n + 3\sum_{n=3}^{N+2} (n-2)a_n - \sum_{n=4}^{N+3} (n-3)a_n $$

#### **Step 4: Collect coefficients of $a_n$**

Let's find the coefficient of each term $a_n$ in the expression for $S_N$.

*   **Coeff of $a_1$**: Appears only in the first sum with $n=1$. Coefficient is $1$.
*   **Coeff of $a_2$**: Appears in the first sum ($n=2$) and second sum ($n=2$).
    Coefficient is $2 - 3(2-1) = 2 - 3 = -1$.
*   **Coeff of $a_3$**: Appears in the first, second, and third sums.
    Coefficient is $3 - 3(3-1) + 3(3-2) = 3 - 6 + 3 = 0$.
*   **Coeff of $a_n$ for $4 \leq n \leq N$**: The term $a_n$ appears in all four sums.
    Coefficient is $n - 3(n-1) + 3(n-2) - (n-3)$
    $= n - 3n + 3 + 3n - 6 - n + 3$
    $= (1 - 3 + 3 - 1)n + (3 - 6 + 3) = 0 \cdot n + 0 = 0$.

This shows that all terms from $a_3$ to $a_N$ cancel out. Now we must consider the "tail" terms with indices greater than $N$.

*   **Coeff of $a_{N+1}$**: Appears in the second, third, and fourth sums.
    Coefficient is $-3((N+1)-1) + 3((N+1)-2) - ((N+1)-3)$
    $= -3N + 3(N-1) - (N-2) = -3N + 3N - 3 - N + 2 = -N-1$.
*   **Coeff of $a_{N+2}$**: Appears in the third and fourth sums.
    Coefficient is $3((N+2)-2) - ((N+2)-3)$
    $= 3N - (N-1) = 2N+1$.
*   **Coeff of $a_{N+3}$**: Appears only in the fourth sum.
    Coefficient is $-((N+3)-3) = -N$.

Combining all these results, the partial sum $S_N$ is:
$$ S_N = 1 \cdot a_1 - 1 \cdot a_2 + \sum_{n=3}^N (0 \cdot a_n) + (-N-1)a_{N+1} + (2N+1)a_{N+2} - Na_{N+3} $$
$$ S_N = a_1 - a_2 - (N+1)a_{N+1} + (2N+1)a_{N+2} - Na_{N+3} $$

#### **Step 5: Evaluate the limit of the partial sum**

The value of the infinite sum is the limit of $S_N$ as $N \to \infty$:
$$ \sum_{n=1}^\infty nb_n = \lim_{N \to \infty} S_N = \lim_{N \to \infty} \left( a_1 - a_2 - (N+1)a_{N+1} + (2N+1)a_{N+2} - Na_{N+3} \right) $$
$$ = a_1 - a_2 - \lim_{N \to \infty} \left( (N+1)a_{N+1} - (2N+1)a_{N+2} + Na_{N+3} \right) $$
Let's call the remainder term $R_N = (N+1)a_{N+1} - (2N+1)a_{N+2} + Na_{N+3}$. We need to show that $\lim_{N \to \infty} R_N = 0$.

From Step 1, we know that for any constant $C$ and integer $k$, $\lim_{n \to \infty} (Cn+k)a_n = 0$. Let's apply this:
*   $\lim_{N \to \infty} (N+1)a_{N+1} = \lim_{M \to \infty} M a_M$ (by setting $M=N+1$). This limit is 0.
*   $\lim_{N \to \infty} (2N+1)a_{N+2} = \lim_{M \to \infty} (2(M-2)+1)a_M = \lim_{M \to \infty} (2M-3)a_M$. This limit is 0.
*   $\lim_{N \to \infty} Na_{N+3} = \lim_{M \to \infty} (M-3)a_M$ (by setting $M=N+3$). This limit is 0.

Since the limits of the individual terms in $R_N$ are all zero, the limit of $R_N$ is also zero:
$$ \lim_{N \to \infty} R_N = 0 - 0 + 0 = 0 $$
Therefore,
$$ \lim_{N \to \infty} S_N = a_1 - a_2 - 0 = a_1 - a_2 $$

### **Conclusion**

We have shown by calculating the partial sums and taking the limit that the series converges to the desired value. The key steps were using the condition $a_{n+1} \leq \frac{1}{2}a_n$ to establish that terms of the form $P(n)a_n$ vanish as $n \to \infty$, and then performing an algebraic rearrangement of the partial sum to show its telescoping nature.

Thus, we have proven that
$$ \sum_{n=1}^\infty nb_n = a_1 - a_2 $$
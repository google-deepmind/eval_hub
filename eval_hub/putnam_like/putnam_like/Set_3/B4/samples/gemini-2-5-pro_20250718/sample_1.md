Of course. Here is a detailed, step-by-step solution to the problem.

### **1. Understanding the Sequence Structure**

The sequence $(a_n)$ is constructed by concatenating blocks of integers. Let's define the properties of these blocks.

*   **Block k:** The k-th block consists of the integers $(1, 2, \ldots, k^2)$.
*   **Length of Block k:** The number of terms in the k-th block is $L_k = k^2$.
*   **Sum of terms in Block k:** This is the sum of an arithmetic series, which we'll call $C_k$.
    \[C_k = \sum_{i=1}^{k^2} i = \frac{k^2(k^2+1)}{2}\]
*   **Index of the last term of Block k:** Let $N_k$ be the index of the last term of the k-th block in the sequence $(a_n)$. This is the sum of the lengths of all blocks up to and including block k.
    \[N_k = \sum_{j=1}^{k} L_j = \sum_{j=1}^{k} j^2\]
    Using the well-known formula for the sum of the first k squares, we have:
    \[N_k = \frac{k(k+1)(2k+1)}{6}\]
*   **Sum of all terms up to the end of Block k:** Let $T_k$ be the sum of all terms in the sequence up to index $N_k$. This is the sum of the sums of all blocks up to and including block k.
    \[T_k = \sum_{j=1}^{k} C_j = \sum_{j=1}^{k} \frac{j^2(j^2+1)}{2} = \frac{1}{2} \left( \sum_{j=1}^{k} j^4 + \sum_{j=1}^{k} j^2 \right)\]
    We use the formulas for the sum of squares and the sum of fourth powers:
    \[\sum_{j=1}^{k} j^2 = \frac{k(k+1)(2k+1)}{6}\]
    \[\sum_{j=1}^{k} j^4 = \frac{k(k+1)(2k+1)(3k^2+3k-1)}{30}\]
    Substituting these into the expression for $T_k$:
    \[T_k = \frac{1}{2} \left( \frac{k(k+1)(2k+1)(3k^2+3k-1)}{30} + \frac{k(k+1)(2k+1)}{6} \right)\]

### **2. Finding the Necessary Condition for Convergence**

We are interested in the limit of $b_n = \frac{\sum_{i=1}^n a_i}{n^{\alpha}}$. Let $S_n = \sum_{i=1}^n a_i$. So, $b_n = \frac{S_n}{n^{\alpha}}$.

If the limit $\lim_{n\to\infty} b_n = \beta$ exists, then any subsequence of $b_n$ must also converge to the same limit $\beta$. A natural subsequence to consider is the one evaluated at the end of each block, i.e., $b_{N_k}$.

For this subsequence, we have $S_{N_k} = T_k$ and $n=N_k$.
\[b_{N_k} = \frac{T_k}{N_k^{\alpha}}\]

To evaluate the limit of this subsequence as $k \to \infty$, we analyze the asymptotic behavior of $T_k$ and $N_k$.
For large $k$:
*   $N_k = \frac{k(k+1)(2k+1)}{6} = \frac{2k^3 + 3k^2 + k}{6} \sim \frac{2k^3}{6} = \frac{k^3}{3}$
*   $T_k = \frac{1}{2} \left( \sum_{j=1}^{k} j^4 + \sum_{j=1}^{k} j^2 \right)$. The sum of fourth powers dominates the sum of squares.
    $\sum_{j=1}^{k} j^4 \sim \frac{k^5}{5}$ and $\sum_{j=1}^{k} j^2 \sim \frac{k^3}{3}$.
    So, $T_k \sim \frac{1}{2} \left( \frac{k^5}{5} \right) = \frac{k^5}{10}$.

Now we can analyze the limit of $b_{N_k}$:
\[ \lim_{k\to\infty} b_{N_k} = \lim_{k\to\infty} \frac{T_k}{N_k^{\alpha}} = \lim_{k\to\infty} \frac{\frac{k^5}{10} + O(k^4)}{\left(\frac{k^3}{3} + O(k^2)\right)^{\alpha}} = \lim_{k\to\infty} \frac{\frac{k^5}{10}}{\left(\frac{k^3}{3}\right)^{\alpha}} = \lim_{k\to\infty} \frac{k^5/10}{k^{3\alpha}/3^{\alpha}} = \lim_{k\to\infty} \frac{3^{\alpha}}{10} k^{5-3\alpha} \]
For this limit to be a finite, positive real number $\beta$, the exponent of $k$ must be zero.
\[ 5 - 3\alpha = 0 \implies \alpha = \frac{5}{3} \]
This determines the value of $\alpha$.

### **3. Determining the Value of β**

With $\alpha = 5/3$, the limit becomes:
\[ \beta = \lim_{k\to\infty} b_{N_k} = \frac{3^{5/3}}{10} \]
So, if a solution pair $(\alpha, \beta)$ exists, it must be $(\frac{5}{3}, \frac{3^{5/3}}{10})$. Since the problem asks for positive real numbers, we check that $\alpha=5/3 > 0$ and $\beta=3^{5/3}/10 > 0$.

### **4. Proving Sufficiency using the Squeeze Theorem**

We have shown that $(\alpha, \beta) = (5/3, 3^{5/3}/10)$ is the only possible candidate. Now we must prove that for this pair, the limit $\lim_{n\to\infty} b_n$ actually exists and equals $\beta$. We will use the Squeeze Theorem.

Let $\alpha = 5/3$. Consider an arbitrary integer $n$. For any sufficiently large $n$, there exists a unique integer $k$ such that $n$ falls within the k-th block (or is the last element of the (k-1)-th block). That is,
\[ N_{k-1} < n \le N_k \]
where $N_{k-1}$ is the index of the end of block $k-1$.

We can bound the sum $S_n$ as follows:
\[ T_{k-1} = S_{N_{k-1}} < S_n \le S_{N_k} = T_k \]
The lower bound is strict because $a_n > 0$ for all $n$.

Now we can bound $b_n = \frac{S_n}{n^{\alpha}}$:
From $n \le N_k$, we have $n^\alpha \le N_k^\alpha$, so $\frac{1}{n^\alpha} \ge \frac{1}{N_k^\alpha}$.
From $n > N_{k-1}$, we have $n^\alpha > N_{k-1}^\alpha$, so $\frac{1}{n^\alpha} < \frac{1}{N_{k-1}^\alpha}$.

Combining these with the bounds for $S_n$:
**Lower bound for $b_n$**: $b_n = \frac{S_n}{n^\alpha} > \frac{T_{k-1}}{N_k^\alpha}$
**Upper bound for $b_n$**: $b_n = \frac{S_n}{n^\alpha} \le \frac{T_k}{N_{k-1}^\alpha}$

So we have the inequality:
\[ \frac{T_{k-1}}{N_k^\alpha} < b_n \le \frac{T_k}{N_{k-1}^\alpha} \]

Now, we evaluate the limits of the lower and upper bounds as $n \to \infty$. Note that as $n \to \infty$, we must have $k \to \infty$.

**Limit of the lower bound:**
\[ \lim_{k\to\infty} \frac{T_{k-1}}{N_k^\alpha} = \lim_{k\to\infty} \left(\frac{T_{k-1}}{N_{k-1}^\alpha} \cdot \left(\frac{N_{k-1}}{N_k}\right)^\alpha\right) \]
We already know that $\lim_{k\to\infty} \frac{T_{k-1}}{N_{k-1}^\alpha} = \beta$. We need to evaluate $\lim_{k\to\infty} \frac{N_{k-1}}{N_k}$.
\[ N_k = \frac{k(k+1)(2k+1)}{6} = \frac{2k^3+3k^2+k}{6} \]
\[ N_{k-1} = \frac{(k-1)k(2(k-1)+1)}{6} = \frac{(k-1)k(2k-1)}{6} = \frac{2k^3-3k^2+k}{6} \]
\[ \lim_{k\to\infty} \frac{N_{k-1}}{N_k} = \lim_{k\to\infty} \frac{2k^3-3k^2+k}{2k^3+3k^2+k} = \lim_{k\to\infty} \frac{2 - 3/k + 1/k^2}{2 + 3/k + 1/k^2} = \frac{2}{2} = 1 \]
So, the limit of the lower bound is $\beta \cdot (1)^\alpha = \beta$.

**Limit of the upper bound:**
\[ \lim_{k\to\infty} \frac{T_k}{N_{k-1}^\alpha} = \lim_{k\to\infty} \left(\frac{T_k}{N_k^\alpha} \cdot \left(\frac{N_k}{N_{k-1}}\right)^\alpha\right) \]
We know $\lim_{k\to\infty} \frac{T_k}{N_k^\alpha} = \beta$ and $\lim_{k\to\infty} \frac{N_k}{N_{k-1}} = 1$.
So, the limit of the upper bound is $\beta \cdot (1)^\alpha = \beta$.

Since $b_n$ is squeezed between two sequences that both converge to $\beta$, by the Squeeze Theorem, we conclude that:
\[ \lim_{n\to\infty} b_n = \beta = \frac{3^{5/3}}{10} \]

### **5. Conclusion**

We have found that for the limit $\lim_{n\to\infty} b_n$ to exist and be a positive real number $\beta$, the value of $\alpha$ must be $5/3$. For this value of $\alpha$, the limit is $\beta = 3^{5/3}/10$. We then proved that for this pair of $(\alpha, \beta)$, the limit indeed exists.

Therefore, the only pair of positive real numbers $(\alpha, \beta)$ that satisfies the condition is:
\[ (\alpha, \beta) = \left(\frac{5}{3}, \frac{3^{5/3}}{10}\right) \]
The value of beta can also be written as $\frac{3 \sqrt[3]{9}}{10}$.

---
**Final Answer**
The only pair of positive real numbers $(\alpha, \beta)$ such that $\lim_{n\to\infty} b_n=\beta$ is
\[ (\alpha, \beta) = \left(\frac{5}{3}, \frac{3^{5/3}}{10}\right). \]
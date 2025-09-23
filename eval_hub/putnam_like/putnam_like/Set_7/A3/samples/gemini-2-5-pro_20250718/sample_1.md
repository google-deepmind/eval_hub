Of course. Here is a detailed, step-by-step solution to the problem.

### **Problem Statement**

Let $n \geq 2$. Show that for any positive integers $a_1, \ldots, a_n$ and any permutation $\sigma \in S_n$ there holds
$$
\frac{\left( \sum_{i=1}^n a_i \right)^{\sum_{i=1}^n a_i} }{ \left( \sum_{i=1}^n a_i \right) !} > \frac{\prod_{i=1}^n a_i^{a_{\sigma(i)}}}{\prod_{i=1}^n ( a_i ! )}
$$

### **Solution**

The proof will be structured in three main steps:
1.  Rearrange the inequality into a more convenient form.
2.  Apply the Multinomial Theorem to establish a key inequality.
3.  Use the Rearrangement Inequality to relate the product terms.
4.  Combine the results to prove the original inequality.

#### **Step 1: Rearranging the Inequality**

Let's simplify the notation. Let $S = \sum_{i=1}^n a_i$. The inequality we want to prove is:
$$
\frac{S^S}{S!} > \frac{\prod_{i=1}^n a_i^{a_{\sigma(i)}}}{\prod_{i=1}^n a_i!}
$$
Since all terms are positive, we can cross-multiply and rearrange without changing the inequality direction. We move the terms with factorials to one side and the power terms to the other.
$$
\frac{S^S}{\prod_{i=1}^n a_i^{a_{\sigma(i)}}} > \frac{S!}{\prod_{i=1}^n a_i!}
$$
The term on the right-hand side is the multinomial coefficient:
$$
\binom{S}{a_1, a_2, \ldots, a_n} = \frac{S!}{a_1! a_2! \cdots a_n!}
$$
So, the inequality we need to prove is equivalent to:
$$
S^S > \binom{S}{a_1, a_2, \ldots, a_n} \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$

#### **Step 2: Applying the Multinomial Theorem**

The Multinomial Theorem states that for any non-negative integer $N$ and any real numbers $x_1, \ldots, x_m$:
$$
(x_1 + x_2 + \cdots + x_m)^N = \sum_{k_1+k_2+\cdots+k_m=N, k_i \ge 0} \binom{N}{k_1, k_2, \ldots, k_m} x_1^{k_1} x_2^{k_2} \cdots x_m^{k_m}
$$
where the sum is over all non-negative integer tuples $(k_1, \ldots, k_m)$ such that their sum is $N$.

Let's apply this theorem with $N=S$, $m=n$, and $x_i = a_i$ for $i=1, \ldots, n$.
$$
S^S = \left(\sum_{i=1}^n a_i\right)^S = \sum_{k_1+\cdots+k_n=S, k_i \ge 0} \binom{S}{k_1, \ldots, k_n} a_1^{k_1} a_2^{k_2} \cdots a_n^{k_n}
$$
Since $n \ge 2$ and each $a_i$ is a positive integer, the sum on the right-hand side contains multiple positive terms. For example, we can choose the exponent tuple $(k_1, \ldots, k_n) = (S, 0, \ldots, 0)$ and $(k_1, \ldots, k_n) = (S-1, 1, 0, \ldots, 0)$, both of which contribute positive terms to the sum. Therefore, the total sum must be strictly greater than any single term in the sum.

Let's choose one specific term from the sum. We choose the term where the exponents $(k_1, \ldots, k_n)$ are equal to the numbers $(a_1, \ldots, a_n)$. This is a valid choice because $\sum_{i=1}^n k_i = \sum_{i=1}^n a_i = S$. The term corresponding to this choice of exponents is:
$$
\binom{S}{a_1, a_2, \ldots, a_n} a_1^{a_1} a_2^{a_2} \cdots a_n^{a_n}
$$
Since $S^S$ is the sum of all such terms (all of which are positive), we have the strict inequality:
$$
S^S > \binom{S}{a_1, a_2, \ldots, a_n} \prod_{i=1}^n a_i^{a_i} \quad (*).
$$

#### **Step 3: Applying the Rearrangement Inequality**

The Rearrangement Inequality states that for two sequences of real numbers $(x_1, \ldots, x_n)$ and $(y_1, \ldots, y_n)$, if they are sorted in the same order (e.g., both non-decreasing), say $x_1 \le \cdots \le x_n$ and $y_1 \le \cdots \le y_n$, then for any permutation $\pi \in S_n$:
$$
\sum_{i=1}^n x_i y_{n-i+1} \le \sum_{i=1}^n x_i y_{\pi(i)} \le \sum_{i=1}^n x_i y_i
$$
We want to compare the two product terms:
$$
P_{id} = \prod_{i=1}^n a_i^{a_i} \quad \text{and} \quad P_{\sigma} = \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
To use the Rearrangement Inequality, which deals with sums, we take the natural logarithm of these products:
$$
\ln(P_{id}) = \ln\left(\prod_{i=1}^n a_i^{a_i}\right) = \sum_{i=1}^n a_i \ln(a_i)
$$
$$
\ln(P_{\sigma}) = \ln\left(\prod_{i=1}^n a_i^{a_{\sigma(i)}}\right) = \sum_{i=1}^n a_{\sigma(i)} \ln(a_i)
$$
Let's define two sequences: $X = (a_1, \ldots, a_n)$ and $Y = (\ln a_1, \ldots, \ln a_n)$.
The function $f(x) = \ln(x)$ is strictly increasing for $x>0$. This means that the sequences $X$ and $Y$ are "sorted in the same way". That is, if we were to reorder the indices to sort sequence $X$, the same reordering would sort sequence $Y$.
Let's re-index the sum for $\ln(P_{\sigma})$. Let $j = \sigma(i)$, which implies $i = \sigma^{-1}(j)$.
$$
\sum_{i=1}^n a_{\sigma(i)} \ln(a_i) = \sum_{j=1}^n a_j \ln(a_{\sigma^{-1}(j)})
$$
This sum is of the form $\sum_{j=1}^n x_j y_{\pi(j)}$ with $x_j = a_j$, $y_j = \ln(a_j)$, and the permutation $\pi = \sigma^{-1}$.

According to the Rearrangement Inequality, the sum is maximized when the two sequences are sorted in the same order. The sum $\sum_{i=1}^n a_i \ln(a_i)$ corresponds to this maximal arrangement. Any other permutation of the indices on one sequence will result in a sum that is less than or equal to this maximal sum.
Therefore, we have:
$$
\sum_{i=1}^n a_j \ln(a_{\sigma^{-1}(j)}) \le \sum_{i=1}^n a_i \ln(a_i)
$$
Substituting back the expressions for the logarithms of the products:
$$
\ln(P_{\sigma}) \le \ln(P_{id})
$$
Since the logarithm function is strictly increasing, this implies:
$$
P_{\sigma} \le P_{id}
$$
which is:
$$
\prod_{i=1}^n a_i^{a_{\sigma(i)}} \le \prod_{i=1}^n a_i^{a_i} \quad (**)
$$

#### **Step 4: Combining the Results**

We now combine the inequalities we've derived.
From Step 2 (inequality $*$), we have:
$$
S^S > \binom{S}{a_1, \ldots, a_n} \prod_{i=1}^n a_i^{a_i}
$$
From Step 3 (inequality $**$), we have:
$$
\prod_{i=1}^n a_i^{a_i} \ge \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
Since $\binom{S}{a_1, \ldots, a_n}$ is a positive integer, we can combine these two inequalities:
$$
S^S > \binom{S}{a_1, \ldots, a_n} \prod_{i=1}^n a_i^{a_i} \ge \binom{S}{a_1, \ldots, a_n} \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
This gives us the strict inequality:
$$
S^S > \binom{S}{a_1, \ldots, a_n} \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
Now, we substitute the definition of the multinomial coefficient back into this inequality:
$$
S^S > \frac{S!}{\prod_{i=1}^n a_i!} \prod_{i=1}^n a_i^{a_{\sigma(i)}}
$$
Finally, we rearrange this to match the form in the problem statement by dividing both sides by $S!$ and multiplying by $\prod a_i!$ (all terms are positive):
$$
\frac{S^S}{S!} > \frac{\prod_{i=1}^n a_i^{a_{\sigma(i)}}}{\prod_{i=1}^n a_i!}
$$
Substituting $S = \sum_{i=1}^n a_i$, we arrive at the desired result:
$$
\frac{\left( \sum_{i=1}^n a_i \right)^{\sum_{i=1}^n a_i} }{ \left( \sum_{i=1}^n a_i \right) !} > \frac{\prod_{i=1}^n a_i^{a_{\sigma(i)}}}{\prod_{i=1}^n ( a_i ! )}
$$

This completes the proof.
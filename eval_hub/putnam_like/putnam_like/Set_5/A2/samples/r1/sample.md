

To prove that $\sum_{n=1}^\infty n b_n = a_1 - a_2$ where $b_n = a_n - 3a_{n+1} + 3a_{n+2} - a_{n+3}$, we proceed as follows:

**Step 1:** Recognize that $b_n$ is the third finite difference of the sequence $(a_n)$:  
$b_n = \Delta^3 a_n = a_n - 3a_{n+1} + 3a_{n+2} - a_{n+3}$.

**Step 2:** Expand the series $\sum_{n=1}^\infty n b_n$:  
$$
\sum_{n=1}^\infty n b_n = \sum_{n=1}^\infty n(a_n - 3a_{n+1} + 3a_{n+2} - a_{n+3}).
$$

**Step 3:** Decompose the series into four separate sums:  
$$
\sum_{n=1}^\infty n a_n - 3\sum_{n=1}^\infty n a_{n+1} + 3\sum_{n=1}^\infty n a_{n+2} - \sum_{n=1}^\infty n a_{n+3}.
$$

**Step 4:** Adjust indices to express all sums in terms of $a_n$:  
- For $-3\sum_{n=1}^\infty n a_{n+1}$, substitute $m = n+1$: becomes $-3\sum_{m=2}^\infty (m-1)a_m$.  
- For $3\sum_{n=1}^\infty n a_{n+2}$, substitute $m = n+2$: becomes $3\sum_{m=3}^\infty (m-2)a_m$.  
- For $-\sum_{n=1}^\infty n a_{n+3}$, substitute $m = n+3$: becomes $-\sum_{m=4}^\infty (m-3)a_m$.

**Step 5:** Combine the adjusted sums:  
$$
\begin{aligned}
\sum_{n=1}^\infty n b_n = &\sum_{n=1}^\infty n a_n - 3\sum_{n=2}^\infty (n-1)a_n + 3\sum_{n=3}^\infty (n-2)a_n - \sum_{n=4}^\infty (n-3)a_n.
\end{aligned}
$$

**Step 6:** Analyze contributions for each $n$:  
- For $n = 1$: Only the first sum contributes $1 \cdot a_1$.  
- For $n = 2$: Contributions are $2a_2 - 3(1)a_2 = -a_2$.  
- For $n = 3$: Contributions are $3a_3 - 3(2)a_3 + 3(1)a_3 = 0$.  
- For $n \geq 4$: The coefficient of $a_n$ is $n - 3(n-1) + 3(n-2) - (n-3) = 0$, leading to cancellation.

**Step 7:** Sum remaining terms:  
$$
\sum_{n=1}^\infty n b_n = a_1 - a_2.
$$

**Conclusion:** The telescoping nature of the series ensures all terms beyond $n=2$ cancel, leaving the desired result.  

Hence, $\boxed{a_1 - a_2}$.
Solution step (2 points):
We prove by induction on $n$ that for the sequence $(k, k+1,\ldots, k+{n-1})$ the result is smaller then $\frac{k+(k+(n-1))}2$ - the arithmetic mean of the first and last term.

Solution step (1 point):
For $n=1$ there is only one number $k$, so it is the result and $k=\frac{2k+(1-1)}2$.

Solution step (6 points):
Assume that the proposition holds for any sequence of $n$-numbers $(i, i+1,\ldots, i+{n-1})$. Consider the sequence $(k,k+1,\ldots,k+(n-1),k+n)$ and study the penultimate pair of numbers $(A,B)$. Observe that $A$ is obtained as a result for the sequence $(k,\ldots,k+(n-1))$ and $B$ is the result for $(k+1,\ldots,k+n)$, both of the length $n$. By the induction hypothesis $A<\frac{k+(k+(n-1))}2$ and $B<\frac{(k+1)+(k+n)}2$. Therefore, by AM-GM inequality,
$$
\text{result}=\sqrt{AB}\leq \frac{A+B}2<\frac{2k+n-1+2k+n+1}4=\frac{2k+n}2=\frac{k+(k+n)}2,
$$
and the proof is completed.

Solution step (1 point):
Applying the proposition to the sequence $(1,\ldots,n)$ we get the result smaller than $\frac{1+n}2$.
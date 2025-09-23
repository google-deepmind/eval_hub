This step is worth 5 points.
To compute the characteristic polynomial of $A$ we use the following lemma.

**Lemma** For $n\geq 1$, the characteristic polynomial of $n\times n$ matrix
$$
M=\begin{pmatrix}
		0 & 0 &0 &  \ldots & 0 & 0 & -a_0 \\
		1 & 0 & 0 &\ldots & 0 & 0 & -a_1 \\
		0 & 1 & 0 &\ldots & 0 & 0 & -a_2 \\
		\vdots & \vdots &\vdots &\ddots &\vdots & \vdots &\vdots \\
		0 & 0 & 0 &\ldots & 0 & 0 & -a_{n-3} \\
		0 & 0 & 0 &\ldots & 1 & 0 & -a_{n-2} \\
		0 & 0 & 0 &\ldots & 0 & 1 & -a_{n-1}
	\end{pmatrix}
$$
has a form $w_M(t)=\det(M-t\cdot Id)=(-1)^n\left(t^n+a_{n-1}t^{n-1}+\ldots+a_1t+a_0\right)$.

**Proof of lemma**
Let $e_i$ denote the standard basis of $\mathbb{R}^n$ for $i=1,\ldots,n$. It easy to see that $Me_i=e_{i+1}$, for $i=1,\ldots, n-1$,  and therefore $M^ie_1=e_{i+1}$. Moreover
$$
M^ne_1=Me_n=-\sum\limits_{i=1}^n a_{i-1}e_i=\left(-\sum\limits_{i=1}^n a_{i-1}M^{i-1}\right)e_1.
$$
Multiplying the last equation by $M^{k-1}$, for $k=2,\ldots,n$, we get
$$
M^ne_k=\left(-\sum\limits_{i=1}^n a_{i-1}M^{i-1}\right)e_k,\, \text{for }k=1,\ldots,n.
$$
Hence
$$
M^n=-\sum\limits_{i=1}^n a_{i-1}M^{i-1} \Leftrightarrow M^n+a_{n-1}M^{n-1}+\ldots+a_1M+a_0=0.
$$
Suppose that there is a polynomial $f(x)=b_{n-1}x^{n-1}+\ldots+b_1x+b_0$ such that $0<\deg f \leq n-1$ and $f(M)=0$.
Consequently, one has
$$
0=f(M)e_1=b_{n-1}e_n+b_{n-2}e_{n-1}+\ldots+b_1e_2+b_0e_1,
$$
It follows that $e_1,e_2,\ldots,e_n$ are lineary independent, which contradicts the fact that the set of vectors $\{e_i\mid i=1,...,n\}$ form the standard basis of $\mathbb{R}^n$. Hence we infer that a minimal polynomial $m(t)$ of the $n\times n$ matrix $M$ is of degree $n$. Therefore by formula (mentioned above)
$$
m(t)=t^n+a_{n-1}t^{n-1}+\ldots+a_1t+a_0.
$$
It is well known that a minimal polynomial divides a characteristic polynomial. Thus a characteristic polynomial of $M$ has the following form $dm(t)$, where $d\in\mathbb{R}\setminus\{0\}$. Finally, a direct calculation shows that $d=(-1)^n$, which completes the proof of Lemma.

The foregoing Lemma implies that the characteristic polynomial of $A$ has the  form
$$
w_A(t)=t^{2n}+(n-1)t^{2n-1}+\ldots+t^{n+1}+0+0-t^{n-2}-\ldots-(n-2)t-(n-1).
$$

This step is worth 1 point.
By Descartes rule of signs, $w_A(t)$ has exactly one positive root. 

This step is worth 3 points.
Moreover

$$
\begin{split}
w_A(-t)&=\underbrace{(-1)^{2n}t^{2n}+(-1)^{2n-1}(n-1)t^{2n-1}+\ldots+(-1)^{n+1}t^{n+1}}_{n \text{ coeff. and }(n-1) \text{ changes of sign}}+0+\\
&+0+\underbrace{(-1)^{n-1}t^{n-2}+\ldots+(-1)^2(n-2)t+(-1)(n-1)}_{(n-1) \text{ coeff. and }(n-2) \text{ changes of sign}}.
\end{split}
$$
Therefore, again by Descartes rule of signs, $w_A(t)$ has no more than $2n-3$ negative roots. 

This step is worth 1 point.
Summing up, $w_A(t)$ has no more than $1+(2n-3)=2n-2$ real roots, hence there exist non-real root of $w_A(t)$, which completes the proof.
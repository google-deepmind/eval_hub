This step is worth 1 point.
Firstly, we prove by induction that $a_{n+1}\geq 3a_n>0$ for $n\geq 1$. It holds for $n=1$. Assuming $a_{n+1}\geq 3a_n>0$ we get
$$a_{n+2}=3a_{n+1}+(a_{n+1}-3a_n)+\frac{3^n}{a_n}>3a_{n+1}>0,$$
and the inductive proof is finished. As a simple consequence we obtain $a_n\geq 3^n$ i.e. $\frac{3^n}{a_n}\leq 1$.

This step is worth 1 point.
By induction we prove also the upper bound $a_{n+1}\leq 3a_n+n$. Indeed, it holds for $n=1$ and assuming $a_{n+1}\leq 3a_n+n$ we compute
$$a_{n+2}=3a_{n+1}+(a_{n+1}-3a_n)+\frac{3^n}{a_n}\leq 3a_{n+1}+n+1,$$
and the proof is finished.

This step is worth 6 points.
Put $b_n=\frac{a_n}{3^n}$ and note that
$$
\begin{split}
b_{n+1}&\leq b_n+\frac{n}{3^n}\leq \ldots\leq b_1+\sum_{k=1}^n \frac{k}{3^k}<\frac{a_1}{3}+\sum_{k=1}^{\infty} k\left(\frac 13\right)^{k}=\frac 33 +\frac 13 \sum_{k=1}^{\infty} k\left(\frac 13\right)^{k-1}\\
&=1 +\frac 13 \left[\frac{d}{dx}\left(\sum_{k=0}^{\infty} x^{k}\right)\right]_{x=\frac 13}=1+\frac 13 \left[\frac{d}{dx}\left(\frac{1}{1-x}\right)\right]_{x=\frac 13}\\
&=1+\frac 13 \left[\frac{1}{(1-x)^2}\right]_{x=\frac 13}=1+\frac 13\cdot\frac 94=1+\frac 34=\frac 74,
\end{split}
$$
so $(b_n)$ is bounded from above.

This step is worth 2 points.
Moreover, $b_{n+1}=\frac{a_{n+1}}{3^{n+1}}\geq\frac{3a_n}{3\cdot 3^n}=b_n$, so $(b_n)$ is the increasing sequence. 
Since the sequence $(b_n)$ is increasing and bounded from above by $\frac 74$, it is convergent and $\lim_{n\to\infty} \frac{a_n}{3^n}=\lim_{n\to\infty} b_n\leq \frac 74$.
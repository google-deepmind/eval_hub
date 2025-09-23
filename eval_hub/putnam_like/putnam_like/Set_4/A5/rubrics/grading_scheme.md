Solution step (1 point)
$$
S(\ell) := \sum_{i=1}^\ell i^2 = \frac{\ell (\ell + 1) (2\ell + 1)}{6}.
$$

Solution step (1 point)
Then the equation may be rewritten as
$$
S(n)-S(n-m)=S(n+k)-S(n)
$$
or equivalently
$$
2S(n) = S(n-m) + S(n+k).
$$
Hence, we obtain the following
$$
\begin{aligned}
&\quad \frac{n(n+1)(2n+1)}{3} \\
&= \frac{(n-m)(n-m+1)(2n-2m+1)}{6} + \frac{(n+k)(n+k+1)(2n+2k+1)}{6}
\end{aligned}
$$
or equivalently
$$
\tag{1}
\begin{aligned}
&\quad 2n(n+1)(2n+1) \\
&= (n-m)(n-m+1)(2n-2m+1) + (n+k)(n+k+1)(2n+2k+1).
\end{aligned}
$$

Solution step (5 points)
Expanding almost all the parenthesis we get
$$
4 n^3 + 6 n^2 + 2 n = 2 k^3 + 6 k^2 n + 3 k^2 + 6 k n^2 + 6 k n + k + 2 (n-m)^3 + 3 (n-m)^2 + (n-m)
$$
and after simplifications
$$
2 n^3 + 3 n^2 + n = 2 k^3 + 6 k^2 n + 3 k^2 + 6 k n^2 + 6 k n + k + 2 (n-m)^3 + 3 (n-m)^2 + (n-m).
$$
We can rewrite this as
$$
2 (n^3 - (n-m)^3) + 3 (n^2-(n-m)^2) + m = k ( 2 k^2 + 6 k n + 3 k + 6 n^2 + 6 n + 1 ).
$$
First we can study the right hand side of the above equation. Note that
$$
\begin{aligned}
2 k^2 + 6 k n + 3 k + 6 n^2 + 6 n + 1 &= 2 (k+n)^2 + 2 kn + 3k + 4n^2 + 6n + 1 \\
&= 2 (k+n)^2 + 2 (k+n) n + 3(k+n) + 2n^2 + 3n + 1.
\end{aligned}
$$
Thus, we can try to factor $m$ from the left hand side of the above equation and write it in a similar form. For this purpose we compute the left hand side of the above equation
$$
\begin{aligned}
&\quad 2 (n^3 - (n-m)^3) + 3 (n^2-(n-m)^2) + m \\
&= 2 m \left( n^2 +  n(n-m) + (n-m)^2 \right) + 3m(2n-m) + m \\
&= m \left( 2n^2 + 2n(n-m) + 3n + 2 (n-m)^2 + 3(n-m) + 1 \right).
\end{aligned}
$$
Thus, from the foregoing equation we get
$$
\frac{m}{k} = \frac{2 (k+n)^2 + 2 (k+n) n + 3(k+n) + 2n^2 + 3n + 1}{2n^2 + 2n(n-m) + 3n + 2 (n-m)^2 + 3(n-m) + 1}.
$$

Solution step (1 point)
Since $n-m \geq 0$ we can simply estimate the denominator by
$$
2n^2 + 2n(n-m) + 3n + 2 (n-m)^2 + 3(n-m) + 1 \geq 2n^2 + 3n + 1
$$
and therefore
$$
\frac{m}{k} \leq \frac{2 (k+n)^2 + 2 (k+n) n + 3(k+n) + 2n^2 + 3n + 1}{2n^2 + 3n + 1}.
$$

Solution step (2 points)
To estimate the numerator, we need to find an upper estimate for $k+n$ in terms of $n$. Going back to (1), we note that
$$
\begin{aligned}
(n+k)(n+k+1)(2n+2k+1) &= 2n(n+1)(2n+1) - (n-m)(n-m+1)(2n-2m+1) \\
&\leq 2n(n+1)(2n+1).
\end{aligned}
$$
Since the function $[0, \infty) \ni x \mapsto x(x+1)(2x+1) \in [0,\infty)$ is increasing, we get that $n+k \leq 2n$. In particular, $k \leq n$. Hence
$$
\begin{aligned}
\frac{m}{k} &\leq \frac{2 (2n)^2 + 2 (2n) n + 3(2n) + 2n^2 + 3n + 1}{2n^2 + 3n + 1} = \frac{14 n^2 + 9n + 1}{2n^2 + 3n + 1} \\
&\leq \frac{7 (2n^2 + 3n + 1)}{2n^2 + 3n + 1} = 7.
\end{aligned}
$$
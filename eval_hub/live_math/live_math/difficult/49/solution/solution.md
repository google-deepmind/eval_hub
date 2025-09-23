Consider the vectors:


\noindent $(u=(a_1,a_2,\ldots,a_n)$ and $v=(\sqrt{1^3},\sqrt{2^3},\ldots,\sqrt{n^3})$. By the Cauchy-Schwarz inequality we have:
$|u \cdot v | \leq |u| \cdot |v|$ so:
\begin{eqnarray*}
\sqrt{1^3} a_1+\sqrt{2^3} a_2+\sqrt{3^3} a_3+\cdots+ \sqrt{n^3} a_{n} \\ \leq \sqrt{(1^3+2^2+\cdots+n^3)} \cdot \sqrt{a_1^2+a_2^2+\cdots+a_n^2}.
\end{eqnarray*}


\noindent Recall that:
$$1^3+2^2+\cdots+n^3=\left(\frac{n(n+1)}{2} \right)^2$$
\noindent so we get:
$$|u \cdot v | \leq \frac{n(n+1)}{2} \cdot \frac{7}{15}$$
\noindent and the solution of equation:
$$\frac{n(n+1)}{2} \cdot \frac{7}{15}=1001$$
\noindent is given by $n=65$. To get the equality consider $a_k= \lambda k^{3/2}$ for some $\lambda$. Making calculations, $\lambda=1001/2145^2$. Hence the equality is hold for:
$$(a_1,a_2, \ldots,a _{65})=\frac{1001}{2145^2} \left( \sqrt{1^3},\sqrt{2^3},\ldots,\sqrt{65^3} \right)$$ 
\noindent and we are done.
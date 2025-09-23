Notice that three consecutive numbers are given by:
$$\binom{n}{k-1},\binom{n}{k}, \binom{n}{k+1} $$
\noindent and we have:
$$\binom{n}{k+1}-\binom{n}{k}=\binom{n}{k}-\binom{n}{k-1}$$


\noindent so making calculations and simplifying (notice that $n!$ appears in the numerators):
$$\frac{1}{(n-k-1)!(k+1)!}-\frac{1}{(n-k)!k!}=\frac{1}{(n-k)!k!}-\frac{1}{(n-k+1)(k-1)!}$$
\noindent so:
$$\frac{1}{(n-k-1)!k!} \left( \frac{1}{k+1}-\frac{1}{n-k}\right)=\frac{1}{(n-k)!(k-1)!} \left( \frac{1}{k}-\frac{1}{n-k+1}\right)$$
\noindent and simplifying we have:
$$(n-k) \left( \frac{1}{k+1}-\frac{1}{n-k}\right) =k\left( \frac{1}{k}-\frac{1}{n-k+1}\right)$$
\noindent if and only if:
$$\frac{n-k}{k+1}-1=1-\frac{k}{n-k+1}$$
\noindent if and only if:
$$\frac{n^2-2kn+2k^2-n}{(k+1)(n-k+1)} =2$$
\noindent and making calculations we get:
$$n^2-4kn+4k^2-n-2=0$$
\noindent so $(n-2k)^2=n+2$. Hence, a necessary condition is that $n+2$ is a perfect square. If $n \geq 100$ then $n+2 \geq 102$ so the lowest value is given by $n=119$. In this case, taking $k \leq n/2$ we have $119-2k =11$ so $k=54$ and we find that the three numbers are given by:
$$\binom{119}{53}, \binom{119}{54} \ \mbox{ and } \binom{119}{55}.$$


Hence, the solution is given by $n=119$.
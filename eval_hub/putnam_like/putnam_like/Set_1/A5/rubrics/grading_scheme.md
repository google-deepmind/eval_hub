This step is worth 1 point.
Let $n \geq 3$. Observe that for $k \in \{1, 2, \ldots, n \}$ we have
$$0\leq \frac{n+1}{n(n-1)} \leq \frac{n+2k-1}{n(n-1)} \leq  \frac{3n-1}{n(n-1)} \leq 2,$$
hence $\frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \in [0, \pi]$. Moreover
$$\sum_{k=1}^n \frac{n+2k-1}{n(n-1)} = \frac{ \left( \frac{n+1}{n(n-1)} + \frac{3n-1}{n(n-1)} \right) \cdot n }{2} = \frac{2n}{n-1}.$$

This step is worth 9 points.
On $[0,\pi]$ the function $\sin$ is concave and from Jensen's inequality we obtain

$$\lim_{n\to\infty} \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right) \geq \lim_{n\to \infty} n \sin \left( \frac{\sum_{k=1}^n  \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)}}{n} \right)$$
$$= \lim_{n\to \infty} n \sin \left( \frac{\pi}{2} \frac{\sum_{k=1}^n   \cdot \frac{n+2k-1}{n(n-1)}}{n} \right) =  \lim_{n\to \infty} n \sin \left( \frac{\pi}{2} \frac{2n}{n(n-1)} \right)$$
$$= \lim_{n\to \infty} \frac{n}{n-1} (n-1) \sin \left( \frac{\pi}{n-1} \right) = 1 \cdot \pi = \pi.$$
To obtain the opposite inequality, we will consider two cases. If $n$ is even, we can write

$$
\begin{aligned}
&\quad \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right) \\
&= \sum_{k=1}^{n/2} \left( \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right)+ \sin \left( \frac{\pi}{2} \cdot \frac{n+2(n+1-k)-1}{n(n-1)} \right) \right) \\
&= \sum_{k=1}^{n/2} \left( \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right) + \sin \left( \frac{\pi}{2} \cdot \frac{3n-2k+1}{n(n-1)} \right) \right) \\
&= \sum_{k=1}^{n/2} 2 \sin \left( \frac{\pi}{4} \frac{(n+2k-1)+(3n-2k+1)}{n(n-1)} \right) \cos \left( \frac{\pi}{4} \frac{(n+2k-1)-(3n-2k+1)}{n(n-1)} \right) \\
&= 2 \sum_{k=1}^{n/2} \sin \left( \frac{\pi}{4} \frac{4n}{n(n-1)} \right) \cos \left( \frac{\pi}{4} \frac{4k-2n-2}{n(n-1)} \right) = 2 \sum_{k=1}^{n/2} \sin \left( \frac{\pi}{n-1} \right) \cos \left( \frac{\pi}{2} \frac{n+1-2k}{n(n-1)} \right) \\
&= 2 \sin \left( \frac{\pi}{n-1} \right) \sum_{k=1}^{n/2}  \cos \left( \frac{\pi}{2} \frac{n+1-2k}{n(n-1)} \right) = (*).
\end{aligned}
$$

Observe that $\sin \left( \frac{\pi}{n-1} \right) \geq 0$ and, since 
$$0 \leq \frac{1}{n(n-1)} \cdot \frac{\pi}{2} \leq \frac{\pi}{2} \frac{n+1-2k}{n(n-1)} \leq \frac{1}{n} \cdot \frac{\pi}{2} \leq \frac{\pi}{2}$$
we have also $\cos \left( \frac{\pi}{2} \frac{n+1-2k}{n(n-1)} \right) \geq 0$. Thus we can estimate $\cos \left( \frac{\pi}{2} \frac{n+1-2k}{n(n-1)} \right) \leq 1$ and

$$(*) \leq 2 \sin \left( \frac{\pi}{n-1} \right) \sum_{k=1}^{n/2} 1 = n \sin \left( \frac{\pi}{n-1} \right) = \frac{n}{n-1} (n-1) \sin \left( \frac{\pi}{n-1} \right) \stackrel{n\to\infty}{\longrightarrow} \pi.$$
If $n$ is odd, using similar computations, we have
$$
\begin{aligned}
&\quad \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right) \\
&=  \sum_{k=1}^{\frac{n-1}2} \left( \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right) + \sin \left( \frac{\pi}{2} \cdot \frac{n+2(n+1-k)-1}{n(n-1)} \right) \right)\\
&\quad+ \sin \left( \frac{\pi}{2} \cdot \frac{n+2\frac{n+1}{2}-1}{n(n-1)} \right) \\
&= 2 \sin \left( \frac{\pi}{n-1} \right) \sum_{k=1}^{(n-1)/2}  \cos \left( \frac{\pi}{2} \frac{n+1-2k}{n(n-1)} \right) + \sin \left( \frac{\pi}{n-1} \right) \\
&\leq 2 \sin \left( \frac{\pi}{n-1} \right) \frac{n-1}{2} + \sin \left( \frac{\pi}{n-1} \right) = n \sin \left( \frac{\pi}{n-1} \right) \stackrel{n\to\infty}{\longrightarrow} \pi.
\end{aligned}
$$
Hence, we showed that
$$\lim_{n\to\infty} \sum_{k=1}^n \sin \left( \frac{\pi}{2} \cdot \frac{n+2k-1}{n(n-1)} \right) = \pi.$$
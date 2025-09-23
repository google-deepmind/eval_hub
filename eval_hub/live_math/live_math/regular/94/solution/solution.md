Notice that 
\begin{align*}
n^{10} - 2n^6 - 7n^5 + n^2 + 37n + 60 &= 
(n^5)^2 - 2\cdot n^5 \cdot n + n^2 - 7n^5 + 7n + 30n + 60\\
&=(n^5 - n)^2 -7(n^5 - n) + 30(n+2).
\end{align*}
This is a sum of 3 components that are divisible by 30. Proof that $n^5-n$ is divisible by 30:
    Notice that $n^5-n = n(n^4-1) = n(n^2+1)(n-1)(n+1)$. Clearly $(n-1)n(n+1)$ is always divisible by 6, since we have 3 consecutive integers there. Now, if $n\equiv 1\pmod{5}$ or $n \equiv 4\pmod{5}$ or $n \equiv 0 \pmod{5}$, then the whole product is of course also divisible by 5. If $n \equiv 2 \pmod{5}$, then $n^2+1 \equiv 0 \pmod{5}$, and also if $n \equiv 3 \pmod{5}$, then $n^2+1 \equiv 0 \pmod{5}$. Thus the whole product is divisible both by 6 and by 5, so it's also divisible by 30.
Hence the answer is 0.
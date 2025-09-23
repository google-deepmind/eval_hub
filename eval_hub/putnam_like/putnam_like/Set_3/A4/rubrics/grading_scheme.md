Solution step (2 points):

Consider the sequence $a_n=(\sqrt{11}+3)^{2n}+(\sqrt{11}-3)^{2n}$. We will prove that $a_n\in\mathbb{Z}$. Then, since $\sqrt{11}-3 <1$, we have
$$
(\sqrt{11}+3)^{2n}<a_n <(\sqrt{11}+3)^{2n}+1,
$$
hence $\lceil (\sqrt{11}+3)^{2n}\rceil=a_n$.


Solution step (6 points):

We can rewrite $a_n=(20+6\sqrt{11})^n+(20-6\sqrt{11})^n$. We easily compute $a_0=2$, $a_1=40$. One can recognize that the numbers $20\pm 6\sqrt{11}$ are the roots of quadratic equation $x^2+bx+c$ with $b=-40$ and $b^2-4c=\Delta=12^2\cdot 11$, so $c=4$. Therefore the sequence $a_n$ is the solution of the recurrence
$$
\left\{\begin{array}{rl}
a_{n+2}&=40a_{n+1}-4a_n,\\
a_0&=2,\\
a_1&=40.
\end{array}\right.
$$
Hence $a_n\in \mathbb{Z}$ and $\lceil (\sqrt{11}+3)^{2n}\rceil=a_n$. 

Solution step (2 points):

It remains to show $2^{n+1}|a_{n}$ and we do it by an induction principle. For $n=0$ and $n=1$ the conditions is true. For induction step we assume $a_n=2^{n+1}\cdot b_n$ and $a_{n+1}=2^{n+2}\cdot b_{n+1}$, where $b_i\in\mathbb{Z}$. Then
$$
a_{n+2}=40a_{n+1}-4a_n=20\cdot 2^{n+3}b_{n+1}-2^{n+3}b_n=2^{n+3}(20b_{n+1}-b_n),
$$
so $2^{n+3}|a_{n+2}$ and the proof by induction is finished.
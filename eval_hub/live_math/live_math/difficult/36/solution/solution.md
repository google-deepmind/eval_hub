We are looking for number $n$ such that $n^4$ will be Jennifer's phone number. We know that it is divisible by 7, so $n=7k$ for some $k\in \mathbb{N}$. The smallest number that we can get from the given sequence of digits would be 101225556 and the biggest number would be 655522110. So it has to hold that
       \begin{align*}
           101225556 &\leqslant (7k)^4 \leqslant 655522110\\
           101225556 &\leqslant 2401k^4 \leqslant 655522110\\
           42159.75 &\leqslant k^4 \leqslant 273020.45\\
           14.33 &\leqslant k \leqslant 22.86.
       \end{align*}
       $k$ is a natural number, so we get $k \in \{15, 16, 17, 18, 19, 20, 21, 22\}$. Thus $n = 7k \in \{105, 112, 119, 126,\\ 133, 140, 147, 154, 160\}$. Now, there is only one number with the property that the sum of digits equals 6, and it's $n=105$. Thus $n^4 = 121 550 625$ is Jennifer's number.
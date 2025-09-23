We are looking for a number $n$ for which 
 $$n^2\equiv 1 \pmod{1000}.$$
 By the Chinese remainder theorem, this is equivalent to $n^2\equiv 1\pmod{8}$ and $n^2\equiv 1\pmod{125}$. The first condition simply means that $n$ is odd. The other says that $125|n^2-1 = (n-1)(n+1)$. As $n-1$ and $n+1$ differ by $2$, they cannot both be divisible by $5$. Hence we have $125|n-1$ or $125|n+1$. Therefore $n$ can have following remainders modulo $1000$:
 $$1, 249, 251, 499, 501, 749, 751, 999.$$
 If $n=1$, then $n^2$ has only one digit. But for $n=249$ we have $n^2 = 62001$, hence it satisfies the conditions.
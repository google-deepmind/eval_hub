We count the number of possible triangles for a given length of the longest side. If $a\in \{103, 104, \dots, 200\}$ then we can form a triangle with $a$ and any $b$, $c$ lower than $a$ that are contained in the set of the sticks. This gives in total $\binom{100}{3}$ triangles. Now assume that we have a stick of length $a = 200 + k$, where $1\le k\le 300$. We will count how many pairs $(b,c)$ with $a>b>c$ do not form a triangle with $a$.


First, assume that $k = 2m-1$ is odd. We are looking for a number of pairs in $\{101,102,\dots, 198 + 2m\}$ whose sum is at most $200+k = 199 + 2m$. All sums possible are larger than $200$. Precisely, we can get $201$ or $202$ in 0 ways, we can get $203$ or $204$ in 1 way each, $205$ or $206$ in two ways each, \dots, $197 + 2m$ and $198+2m$ in $m-2$ ways each, and $199+2m$ in $m-1$ ways. This gives together
$$(1 + 1) + (2 + 2) + \dots + (m-2 + m-2) + m-1 = (m-2)(m-1) + (m-1) = (m-1)^2$$
non-allowed pairs. Hence there are
$$\binom{98+2m}{2} - (m-1)^2$$
allowed pairs.


Now assume that $k = 2m$ is even. We are looking for a number of pairs in $\{101,102,\dots, 199 + 2m\}$ whose sum is at most $200+k = 200 + 2m$. All sums possible are larger than $200$. Precisely, we can get $201$ or $202$ in 0 ways, we can get $203$ or $204$ in 1 way each, $205$ or $206$ in two ways each, \dots, $197 + 2m$ and $198+2m$ in $m-2$ ways each, and $199+2m$ and $200+2m$ in $m-1$ ways. This gives together
$$(1 + 1) + (2 + 2) + \dots + (m-2 + m-2) + (m-1 + m-1) = m(m-1).$$
non-allowed pairs. Hence there are
$$\binom{99+2m}{2} - m(m-1)$$
allowed pairs.


As in both cases $m$ is in the interval $[1,150]$, we get that the total number of possible triangles is
$$\binom{100}{3} + \sum_{m=1}^{150} \left( \binom{98+2m}{2} - (m-1)^2 + \binom{99+2m}{2} - m(m-1) \right) $$
$$= \binom{100}{3} + \sum_{m=1}^{150} \left( (98+2m)^2 - (m-1)^2 - m(m-1) \right) $$
$$= \binom{100}{3} + \sum_{m=1}^{150} \left( 98^2 + 4\cdot 98m + 4m^2 - 2m^2 + 3m - 1\right) $$
$$= \binom{100}{3} + \sum_{m=1}^{150} \left( (98^2-1) + 395m + 2m\right) $$
$$= \binom{100}{3} + 150\cdot (98^2-1) + 395\frac{150\cdot 151}{2} + 2\frac{150\cdot 151\cdot 301}{6} = 8348075.$$
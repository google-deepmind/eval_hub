This step is worth 1 point.
We will prove this statement by induction on $n$. For $n=1$ we have
$$
(2m+1)^2-1=4\cdot m\cdot (m+1).
$$
Thus, either $m$ or $m+1$ is divisible by an odd prime number, denoted by $p$. Consequently, the number
$(2m+1)^2-1$ has at least two distinct prime divisors: $2$ and $p$.

This step is worth 1 point.
Assume now that $(2m+1)^{2^n}-1$ has at least $n+1$ distinct prime divisors. Observe that
$$
(2m+1)^{2^{n+1}}-1=((2m+1)^{2^{n}}-1)((2m+1)^{2^{n}}+1).
$$
By the inductive assumption, it is enough to show that $(2m+1)^{2^{n}}+1$ has an odd prime divisor that does not divide
$(2m+1)^{2^{n}}-1$.

This step is worth 8 points.
Since
$$
(2m+1)^{2} \equiv 1 \pmod{4},
$$
it follows that
$$
(2m+1)^{2^n}=((2m+1)^{2})^{2^{n-1}}\equiv 1^{2^{n-1}}=1 \pmod{4}.
$$
Thus, $(2m+1)^{2^n}+1$ is an even number and
$$
4 \nmid (2m+1)^{2^n}+1.
$$
Consequently, it follows that it has an odd prime divisor $q$.
Finally, let us observe that the number $q$ cannot be a divisor of $(2m+1)^{2^n}-1$ since
$$
(2m+1)^{2^n}+1-((2m+1)^{2^n}-1)=2.
$$
This completes the proof that $(2m+1)^{2^{n+1}}+1$ has at least $n+2$ distinct prime divisors.
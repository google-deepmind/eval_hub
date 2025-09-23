This step is worth 3 points.
Let $p=2^dm+1$ be a prime divisor of $a^{2^k}+b^{2^k}$, where $d\geq 1$ and $m$ is odd. We must show that $d\geq k+1$. Assume, on the contrary, that $d\leq k$. From Fermat's Little Theorem, we obtain that
$$p \mid a^{p-1}-1 \text{ and }p \mid b^{p-1}-1$$
and hence
$$p \mid a^{2^dm}-1 \text{ and }p \mid b^{2^dm}-1.$$
Thus, using congruence, it can be written in the form:
$$a^{2^dm}\equiv 1 \pmod{p}\;\;\text{ and }\;\;b^{2^dm}\equiv 1 \pmod{p}.$$

This step is worth 7 points.
We also know that
$$p \mid a^{2^k}+b^{2^k},$$
so
$$a^{2^k}\equiv -b^{2^k}\pmod{p}.$$
From the previous congruence, we obtain
$$(a^{2^dm})^{2^{k-d}}\equiv 1 \pmod{p}\;\;\text{ and }\;\;(b^{2^dm})^{2^{k-d}}\equiv 1 \pmod{p},$$
which implies that
$$a^{2^km}\equiv 1 \pmod{p}\;\;\text{ and }\;\;b^{2^km}\equiv 1 \pmod{p}.$$
Multiplying the above two equations side by side, we get
$$a^{2^km}\equiv b^{2^km} \pmod{p}.$$
From the congruence $a^{2^k}\equiv -b^{2^k}\pmod{p}$, we obtain
$$(a^{2^k})^m\equiv (-1)^m(b^{2^k})^m\pmod{p},$$
which implies that
$$a^{2^km}\equiv -b^{2^km}\pmod{p}.$$
Therefore, by adding the two congruences side by side, we obtain the following equality:
$$2a^{2^km}\equiv 0\pmod{p}.$$
Finally, the last congruence implies that $p \mid a$, and thus, together with $a^{2^km}\equiv b^{2^km} \pmod{p}$, we conclude that $p \mid b$. This contradicts the assumption that $\gcd(a, b) = 1$.
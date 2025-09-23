Let $f \in C^\infty((-1,1), \mathbb{R})$, and suppose that all its derivatives are uniformly bounded.
Assume that for every $n \in \mathbb{N}$, there exist $a_n, b_n \in (-1,1)$ with $a_n < b_n$, such that
$$
\frac{f(b_n) + f'(b_n) + \cdots + f^{(n)}(b_n)}{f(a_n) + f'(a_n) + \cdots + f^{(n)}(a_n)} = \frac{e^{b_n}}{e^{a_n}}.
$$
Show that if $\lim_{n \to \infty} a_n = \lim_{n \to \infty} b_n = c \in (-1,1)$, then $\lim_{n \to \infty} f^{(n)}(c) = f(c)$.
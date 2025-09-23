```latex
\documentclass{article}
\usepackage{amsmath, amssymb}
\begin{document}

We are given a polynomial
\[
P(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots+a_1x+a_0,
\]
with integer coefficients such that:
\begin{itemize}
    \item The leading coefficient \( a_n \) is a power of \(5\); that is, \( a_n = 5^k \) for some nonnegative integer \( k \).
    \item The constant term \( a_0 \) is a power of \(3\); that is, \( a_0 = 3^m \) for some nonnegative integer \( m \).
    \item \( P(-1) \) is odd.
\end{itemize}

\textbf{Claim.} The polynomial \( P(x) \) has no rational roots.

\textbf{Proof.} Suppose, for the sake of contradiction, that \( P(x) \) has a rational root. Then there exist integers \( p \) and \( q \) with \(\gcd(p,q)=1\) such that
\[
P\!\left(\frac{p}{q}\right) = 0.
\]
The Rational Root Theorem tells us that:
\begin{itemize}
    \item \( p \) divides the constant term \( a_0 \). Since \( a_0 = 3^m \), all possible divisors of \( a_0 \) are (up to sign) powers of \(3\). In particular, \( p \) is odd.
    \item \( q \) divides the leading coefficient \( a_n \). Since \( a_n = 5^k \), all possible divisors of \( a_n \) are (up to sign) powers of \(5\). Hence, \( q \) is odd.
\end{itemize}

Thus, both \( p \) and \( q \) are odd integers. This implies that for any nonnegative integer \( r \), we have
\[
p^r \equiv 1 \pmod{2} \quad \text{and} \quad q^r \equiv 1 \pmod{2}.
\]

Since
\[
P\!\left(\frac{p}{q}\right) = a_n \left(\frac{p}{q}\right)^n + a_{n-1} \left(\frac{p}{q}\right)^{n-1} + \cdots + a_0 = 0,
\]
multiplying through by \( q^n \) (which is odd) gives
\[
a_n p^n + a_{n-1} p^{n-1} q + \cdots + a_0 q^n = 0.
\]
Taking this congruence modulo \(2\), and noting that \( p^i q^{n-i} \equiv 1 \pmod{2} \) for every \( i \), we obtain
\[
a_n + a_{n-1} + \cdots + a_0 \equiv 0 \pmod{2}.
\]
But observe that
\[
P(1) = a_n + a_{n-1} + \cdots + a_0.
\]
Also, since for any integer \( k \) we have \( (-1)^k \equiv 1 \pmod{2} \), it follows that 
\[
P(-1) \equiv a_n + a_{n-1} + \cdots + a_0 \equiv P(1) \pmod{2}.
\]
We are given that \( P(-1) \) is odd; hence,
\[
P(1) \equiv 1 \pmod{2}.
\]
This is a contradiction, because we earlier deduced that
\[
a_n + a_{n-1} + \cdots + a_0 \equiv 0 \pmod{2}.
\]

Thus, our assumption that \( P(x) \) has a rational root must be false. Therefore, \( P(x) \) has no rational roots.

\end{document}
```
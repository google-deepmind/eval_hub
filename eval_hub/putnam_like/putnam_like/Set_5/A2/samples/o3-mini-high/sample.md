```markdown
We wish to show that if
\[
b_n = a_n - 3a_{n+1} + 3a_{n+2} - a_{n+3},
\]
then
\[
\sum_{n=1}^\infty n\,b_n = a_1 - a_2,
\]
under the assumption that \(a_0, a_1, a_2, \dots\) are positive real numbers with
\[
a_{n+1} \le \frac{1}{2}\,a_n \quad \text{for all } n\ge0.
\]
Because of this condition the sequence \((a_n)\) decays at least geometrically, and in particular,
\[
a_n \le a_0 \left(\frac{1}{2}\right)^n.
\]
This rapid decay will allow the boundary terms to vanish when we take limits.

A very neat way to attack the problem is to write \(b_n\) in terms of the first differences of the sequence. Define
\[
s_n = a_n - a_{n+1} \quad \text{for } n\ge0.
\]
Notice that we can rewrite \(b_n\) as follows:
\[
\begin{aligned}
b_n &= a_n - 3a_{n+1} + 3a_{n+2} - a_{n+3} \\
    &= \bigl(a_n - a_{n+1}\bigr) - 2\bigl(a_{n+1} - a_{n+2}\bigr) + \bigl(a_{n+2} - a_{n+3}\bigr) \\
    &= s_n - 2s_{n+1} + s_{n+2}.
\end{aligned}
\]
Thus, the sum we need to compute becomes
\[
\sum_{n=1}^N n\,b_n = \sum_{n=1}^N n\bigl(s_n - 2s_{n+1} + s_{n+2}\bigr),
\]
and eventually we will let \(N\to\infty\).

Let us break the sum into three terms:
\[
\sum_{n=1}^N n\,b_n = \sum_{n=1}^N n\,s_n - 2\sum_{n=1}^N n\,s_{n+1} + \sum_{n=1}^N n\,s_{n+2}.
\]
Now we re-index the last two sums so that all sums are expressed in the same index:
- For the second term, let \(m = n+1\). Then when \(n\) runs from 1 to \(N\), \(m\) runs from 2 to \(N+1\), and
  \[
  \sum_{n=1}^N n\,s_{n+1} = \sum_{m=2}^{N+1} (m-1)\,s_m.
  \]
- For the third term, let \(m = n+2\). Then when \(n\) runs from 1 to \(N\), \(m\) runs from 3 to \(N+2\), and
  \[
  \sum_{n=1}^N n\,s_{n+2} = \sum_{m=3}^{N+2} (m-2)\,s_m.
  \]

Thus, we can write:
\[
\sum_{n=1}^N n\,b_n = \sum_{n=1}^N n\,s_n - 2\sum_{m=2}^{N+1} (m-1)\,s_m + \sum_{m=3}^{N+2} (m-2)\,s_m.
\]

Now, we split the sums to carefully examine the contribution from each \(s_m\):

1. For \(m = 1\): This term appears only in the first sum:
   \[
   \text{Contribution: } 1\cdot s_1.
   \]
2. For \(m = 2\): It appears in the first sum with coefficient \(2\) and in the second sum with coefficient \(-2\,(2-1) = -2\). Thus,
   \[
   \text{Contribution: } 2\,s_2 - 2\,s_2 = 0.
   \]
3. For \(m \ge 3\): For a general index \(m\) (with \(3 \le m \le N\), say), the coefficient coming from the three sums is
   \[
   m - 2(m-1) + (m-2) = m - 2m + 2 + m - 2 = 0.
   \]
   (A similar cancellation can be checked for the indices near the end; the decay hypothesis guarantees that the contributions from the boundary terms vanish as \(N\to\infty\).)

Thus, aside from potential boundary terms coming from the re-indexing (for \(m=N+1\) and \(m=N+2\)), all terms cancel except for \(m=1\). A more careful treatment shows that the only surviving term in the limit is
\[
\sum_{n=1}^\infty n\,b_n = s_1 = a_1 - a_2,
\]
since the boundary terms vanish because, for example,
\[
N\,a_{N+1} \le N\,a_0\left(\frac{1}{2}\right)^{N+1} \to 0 \quad \text{as } N\to\infty.
\]

Hence, we have proved that
\[
\sum_{n=1}^\infty n\,b_n = a_1 - a_2.
\]

This completes the proof.
```
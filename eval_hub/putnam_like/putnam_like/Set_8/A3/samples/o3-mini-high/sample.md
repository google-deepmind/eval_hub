```markdown
We will show that if
\[
X = \{(x_n)_{n\ge0} \subset (0,\infty) : \sum_{n=0}^\infty x_n = c\},
\]
then
\[
Y = \left\{\sum_{n=0}^\infty x_n^3 : (x_n) \in X\right\} = (0, c^3).
\]

To do so, it is convenient to rewrite the sequence in terms of a probability distribution. Define
\[
p_n = \frac{x_n}{c} \quad \text{for all } n\ge0.
\]
Since each \(x_n > 0\) and \(\sum_{n\ge0} x_n = c\), we have
\[
\sum_{n\ge0} p_n = 1 \quad \text{and} \quad p_n > 0 \text{ for all } n.
\]
Expressing the cubes in terms of the \(p_n\)’s gives
\[
\sum_{n\ge0} x_n^3 = \sum_{n\ge0} (c\,p_n)^3 = c^3 \sum_{n\ge0} p_n^3.
\]
Thus, finding the set \(Y\) is equivalent to determining all possible values of
\[
S = \sum_{n\ge0} p_n^3,
\]
where \((p_n)_{n\ge0}\) is a strictly positive probability distribution.

Below we analyze the possible range of \(S\).

1. **Upper Bound on \(S\): Concentrating the Mass**

   To maximize \(S\), we want to concentrate as much of the mass as possible into one term. In the ideal (but forbidden) case one would take
   \[
   p_0 = 1 \quad \text{and} \quad p_n = 0 \text{ for } n\ge1.
   \]
   Then
   \[
   S = 1^3 + 0 + 0 + \cdots = 1.
   \]
   However, since every \(p_n\) must be strictly positive, the value \(p_0 = 1\) is not allowed. Nonetheless, for any \(\varepsilon>0\) we can choose a probability distribution with
   \[
   p_0 = 1-\varepsilon \quad \text{and} \quad p_n \text{ very small but positive for } n\ge1,
   \]
   so that
   \[
   S = (1-\varepsilon)^3 + \sum_{n\ge1} p_n^3
   \]
   is arbitrarily close to \(1\) (since the additional terms can be made as small as desired). Therefore, while \(S\) never attains the value \(1\), its supremum is \(1\). Consequently,
   \[
   \sum_{n=0}^\infty x_n^3 = c^3 S < c^3,
   \]
   but can be made arbitrarily close to \(c^3\).

2. **Lower Bound on \(S\): Spreading Out the Mass**

   To minimize \(S\), we spread the mass out as evenly as possible among many terms. For a rough idea, suppose we take the first \(N\) terms equal and ignore the need for all terms to be positive (a slight modification later will ensure all terms are positive). Setting
   \[
   p_0 = p_1 = \cdots = p_{N-1} = \frac{1}{N}
   \]
   (and then “filling in” the rest with very small positive numbers to maintain strict positivity and the total sum of 1), we obtain
   \[
   \sum_{n=0}^{N-1} p_n^3 = N\left(\frac{1}{N}\right)^3 = \frac{1}{N^2}.
   \]
   As \(N\) becomes large, \(\frac{1}{N^2}\) can be made arbitrarily small. Thus the infimum of \(S\) is \(0\).

Since by choosing appropriate probability distributions we can have
\[
S \in (0,1),
\]
it follows that
\[
\sum_{n\ge0} x_n^3 = c^3 S \in (0, c^3).
\]

Therefore, the set \(Y\) is given by
\[
\boxed{Y = (0, c^3).}
\]
```
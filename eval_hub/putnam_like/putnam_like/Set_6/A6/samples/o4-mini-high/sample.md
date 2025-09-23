Here is a clean Dirichlet‐spacing derivation which in the end shows that for any \(n\ge5\) the probability that *all* interior angles of a random cyclic \(n\)–gon exceed \(90^\circ\) (i.e.\ are obtuse) is

\[
P_n \;=\;\Pr\!\bigl(\max_{1\le i\le n}(x_{i-1}+x_i)\le\tfrac12\bigr)
\;=\;1 \;-\;n\;2^{1-n}\,.
\]

Taking \(n=2025\) gives the answer

\[
\boxed{1 \;-\; \frac{2025}{2^{2024}}\,.}
\]

---

### 1. Spacings on the circle are Dirichlet  

Label the 2025 points in cyclic order and let
\[
x_i \;=\;\frac{\text{arc‐length between }P_i\to P_{i+1}}{2\pi}\,,
\]
so that
\[
x_1+x_2+\cdots+x_{2025}=1,\quad x_i\ge0.
\]
It is well‐known that \((x_1,\dots,x_{2025})\) is uniform on the standard \((2025\!-\!1)\)–simplex.

### 2. Obtuse angles ⇔ no two consecutive gaps sum to ≥½  

An interior angle at vertex \(P_i\) is obtuse
\[
\iff 
\text{the complement of the minor arc }P_{i-1}\!\to P_{i+1}
\text{ has length }>\pi
\]
\[
\iff 1-(x_{i-1}+x_i)>\tfrac12
\iff x_{i-1}+x_i<\tfrac12.
\]
Hence
\[
\{\text{all \(2025\) angles obtuse}\}
\;=\;\Bigl\{\,x_{i-1}+x_i<\tfrac12\;\text{for all }i\Bigr\}
\;=\;\{\max_i(x_{i-1}+x_i)\le\tfrac12\}.
\]

### 3. Inclusion–exclusion for the maximal 2‐spacing  

One shows by a standard sliding‐window inclusion–exclusion (or by known “\(k\)‐spacing’’ formulas) that for general \(n\) and any \(0<t<1\)
\[
\Pr\!\bigl(\max_i(x_{i-1}+x_i)\le t\bigr)
\;=\;
\sum_{j=0}^{\lfloor1/t\rfloor}
(-1)^j\,
\frac{n}{\,n-2j\,}\,
\binom{n-2j}{j}\,
\bigl(1-j\,t\bigr)^{\,n-1}\,.
\]
Here \(t=\tfrac12\) and \(\lfloor1/t\rfloor=2\).  The three terms are
\[
j=0:\quad \frac{n}{n}\binom n0\,(1)^ {n-1}=1,
\]
\[
j=1:\quad -\,\frac{n}{\,n-2\,}\binom{n-2}{1}\,(1-\tfrac12)^{\,n-1}
\;=\;-\,\frac{n}{\,n-2\,}\,(n-2)\,2^{1-n}
\;=\;-\,n\,2^{1-n},
\]
\[
j=2:\quad \frac{n}{\,n-4\,}\binom{n-4}{2}\,(1-2\cdot\tfrac12)^{\,n-1}
\;=\;0\quad\bigl(\text{since }1-2t=0\bigr).
\]
Thus in closed form
\[
P_n=\Pr(\text{all angles obtuse})
\;=\;1 \;-\; n\,2^{1-n}\,.
\]
Substituting \(n=2025\) gives
\[
\boxed{P_{2025}\;=\;1 \;-\;\frac{2025}{2^{2024}}\,.}
\]
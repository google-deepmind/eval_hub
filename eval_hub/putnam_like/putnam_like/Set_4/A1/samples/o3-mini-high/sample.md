```markdown
**Solution:**

We are given differentiable functions \( f \) and \( g \) on \((0,\infty)\) with \( g(x) \to \infty \) as \( x \to \infty \) and
\[
\lim_{x\to\infty}\left(f(x) + \frac{f'(x)}{g'(x)}\right)=0.
\]
Our goal is to show that
\[
\lim_{x\to\infty} f(x) = 0.
\]

A useful idea is to introduce an integrating factor that will lead to a derivative incorporating the given limit. Define the function
\[
F(x) = e^{g(x)} f(x).
\]
Differentiating \( F(x) \) using the product rule gives
\[
F'(x) = e^{g(x)} f'(x) + e^{g(x)} f(x) g'(x) 
= e^{g(x)}\Bigl(f'(x) + f(x)g'(x)\Bigr).
\]
Notice we can factor this expression as
\[
F'(x) = e^{g(x)} g'(x)\left(f(x) + \frac{f'(x)}{g'(x)}\right),
\]
provided that \( g'(x) \) does not vanish for large \( x \) (this is typically ensured since \( g(x) \to \infty \) so that eventually \( g(x) \) is monotone).

Since by hypothesis
\[
\lim_{x\to\infty}\left(f(x) + \frac{f'(x)}{g'(x)}\right)=0,
\]
it follows that for large \( x \),
\[
F'(x) = e^{g(x)} g'(x)\left(f(x) + \frac{f'(x)}{g'(x)}\right)
\]
tends to zero. That is,
\[
\lim_{x\to\infty} F'(x)=0.
\]

Because \( F'(x) \to 0 \) as \( x\to\infty \), the function \( F(x) \) becomes eventually nearly constant. More precisely, there exists a constant \( L \) such that
\[
\lim_{x\to\infty} F(x) = L.
\]

Recalling the definition of \( F(x) \), we have
\[
f(x) = e^{-g(x)} F(x).
\]
Since \( g(x)\to\infty \) as \( x\to\infty \), the factor \( e^{-g(x)} \) decays to 0. Hence,
\[
\lim_{x\to\infty} f(x) = \lim_{x\to\infty} e^{-g(x)} F(x) = L \cdot 0 = 0.
\]

This completes the proof.
```
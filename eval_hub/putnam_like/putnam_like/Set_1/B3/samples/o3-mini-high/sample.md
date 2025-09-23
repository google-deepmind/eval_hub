```markdown
We want to show that the function
\[
\Psi(s) := \ln \left( \int_{\mathbb{R}^n} |f(x)|^s \, dx \right)
\]
is convex on the interval \([p,q]\) given that \(f \in L^p (\mathbb{R}^n) \cap L^q (\mathbb{R}^n)\) with \(0 < p < q < +\infty\).

To show convexity, we need to prove that for any \(s_0, s_1 \in [p,q]\) and for any \(\lambda \in [0,1]\), the following inequality holds:
\[
\Psi\bigl(\lambda s_0 + (1-\lambda) s_1\bigr) \le \lambda \Psi(s_0) + (1-\lambda) \Psi(s_1).
\]

### Step 1: Express the Integral in a Convenient Form

Fix \(s_0, s_1 \in [p,q]\) and \(\lambda \in [0,1]\). Notice that
\[
\lambda s_0 + (1-\lambda) s_1 \in [p,q].
\]
Then,
\[
\int_{\mathbb{R}^n} |f(x)|^{\lambda s_0 + (1-\lambda)s_1} \, dx = \int_{\mathbb{R}^n} \bigl(|f(x)|^{s_0}\bigr)^{\lambda} \bigl(|f(x)|^{s_1}\bigr)^{1-\lambda} \, dx.
\]

### Step 2: Apply Hölder's Inequality

Hölder's inequality tells us that for functions \(g\) and \(h\) and conjugate exponents \(\frac{1}{\lambda}\) and \(\frac{1}{1-\lambda}\) (note that \(\lambda, 1-\lambda > 0\)), we have:
\[
\int_{\mathbb{R}^n} |g(x) h(x)| \, dx \le \left( \int_{\mathbb{R}^n} |g(x)|^{1/\lambda} \, dx \right)^\lambda \left( \int_{\mathbb{R}^n} |h(x)|^{1/(1-\lambda)} \, dx \right)^{1-\lambda}.
\]
Setting 
\[
g(x) := |f(x)|^{s_0\lambda} \quad \text{and} \quad h(x) := |f(x)|^{s_1(1-\lambda)},
\]
we get:
\[
\int_{\mathbb{R}^n} |f(x)|^{\lambda s_0 + (1-\lambda)s_1} \, dx \le \left( \int_{\mathbb{R}^n} |f(x)|^{s_0} \, dx \right)^\lambda \left( \int_{\mathbb{R}^n} |f(x)|^{s_1} \, dx \right)^{1-\lambda}.
\]

### Step 3: Take the Logarithm

Taking the natural logarithm of both sides yields
\[
\ln\left( \int_{\mathbb{R}^n} |f(x)|^{\lambda s_0 + (1-\lambda)s_1} \, dx \right) \le \lambda \ln\left( \int_{\mathbb{R}^n} |f(x)|^{s_0} \, dx \right) + (1-\lambda) \ln\left( \int_{\mathbb{R}^n} |f(x)|^{s_1} \, dx \right).
\]
By the definition of \(\Psi\), this can be rewritten as:
\[
\Psi\bigl(\lambda s_0 + (1-\lambda)s_1\bigr) \le \lambda \Psi(s_0) + (1-\lambda) \Psi(s_1).
\]

### Step 4: Conclusion

Since the above inequality holds for any \(s_0, s_1 \in [p,q]\) and any \(\lambda \in [0,1]\), we conclude that \(\Psi\) is convex on the interval \([p,q]\).

Thus, we have shown that:
\[
\boxed{\Psi(s) = \ln \left( \int_{\mathbb{R}^n} |f(x)|^s \, dx \right) \text{ is convex on } [p,q].}
\]
```
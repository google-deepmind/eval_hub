```markdown
**Solution:**

We begin by noting that if \( X \) and \( Y \) are chosen uniformly at random from the interval \((0, 1)\), then
\[
\ln(X) < 0 \quad \text{and} \quad \ln(Y) < 0.
\]
It is convenient to define new variables
\[
U = -\ln(X) \quad \text{and} \quad V = -\ln(Y).
\]
Since the transformation \(X = e^{-U}\) maps \(U \in (0,\infty)\) to \(X \in (0,1)\) and similarly for \(V\), the random variables \(U\) and \(V\) are independent and follow an exponential distribution with rate parameter \(1\). That is,
\[
f_U(u) = e^{-u} \quad \text{and} \quad f_V(v) = e^{-v} \quad \text{for } u,v \ge 0.
\]

Notice that
\[
\frac{\ln(X)}{\ln(Y)} = \frac{-U}{-V} = \frac{U}{V}.
\]
Thus, the problem is equivalent to finding the probability that
\[
\left\lfloor \frac{U}{V} \right\rfloor
\]
is even.

Let
\[
W = \frac{U}{V}.
\]
It is a known fact that if \(U\) and \(V\) are i.i.d. exponential random variables, then \(W\) has the probability density function
\[
f_W(w) = \frac{1}{(1+w)^2}, \quad w > 0.
\]

The event that \(\left\lfloor W \right\rfloor\) is even is equivalent to \(W\) lying in the union of intervals
\[
[0,1) \cup [2,3) \cup [4,5) \cup \cdots.
\]
Thus, the probability we seek is given by
\[
P = \sum_{k=0}^{\infty} \int_{2k}^{2k+1} \frac{dw}{(1+w)^2}.
\]

Let’s compute the integral for a generic \(k\):
\[
\int_{2k}^{2k+1} \frac{dw}{(1+w)^2}.
\]
An antiderivative is
\[
\int \frac{dw}{(w+1)^2} = -\frac{1}{w+1} + C.
\]
Thus,
\[
\int_{2k}^{2k+1} \frac{dw}{(1+w)^2} = \left(-\frac{1}{w+1}\right) \Bigg|_{w=2k}^{2k+1} = \left(-\frac{1}{2k+2}\right) - \left(-\frac{1}{2k+1}\right) = \frac{1}{2k+1} - \frac{1}{2k+2}.
\]

Therefore, the total probability is
\[
P = \sum_{k=0}^{\infty} \left(\frac{1}{2k+1} - \frac{1}{2k+2}\right).
\]

This sum is recognized as the alternating harmonic series:
\[
1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots = \ln 2.
\]

Thus, we conclude that the probability that \(\left\lfloor \frac{\ln(X)}{\ln(Y)} \right\rfloor\) is even is
\[
\boxed{\ln 2}.
\]
```

This completes the solution.
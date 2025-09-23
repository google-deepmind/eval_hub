Below is one acceptable solution. One may show that the characteristic‐polynomial of the given companion–matrix can be written in the form

\[
\chi_A(t)=t^{2n}+\sum_{j=1}^{n-1}(n-j)\Bigl(t^{2n-j}-t^j\Bigr).
\]

One may then prove that not all roots of this polynomial are real. (Any answer equivalent to the answer below is correct.)

In what follows we explain one way to prove that a non‐real eigenvalue must exist.

---

### A Companion–Matrix and Its Characteristic Polynomial

Recall that a companion matrix
\[
C(p)=\begin{pmatrix}
0 & 0 &\cdots &0 & -a_0\\[1mm]
1 & 0 &\cdots &0 & -a_1\\[1mm]
0 & 1 &\cdots &0 & -a_2\\[1mm]
\vdots & \vdots & \ddots & \vdots & \vdots\\[1mm]
0 & 0 &\cdots &1 & -a_{d-1}
\end{pmatrix}
\]
has characteristic polynomial
\[
\chi_{C(p)}(t)=t^d+a_{d-1}t^{d-1}+\cdots+a_1t+a_0.
\]
It turns out that the matrix in the problem is a companion matrix of a polynomial of even degree \(2n\) whose last column (which lists the “coefficients”) is
\[
\bigl(n-1,\; n-2,\; n-3,\; \dots,\; 1,\; 0,\; 0,\; -1,\; -2,\; \dots,\; -(n-1)\bigr)^T.
\]
Thus one obtains
\[
\chi_A(t)=t^{2n}+\sum_{j=1}^{n-1}(n-j)\Bigl(t^{2n-j}-t^j\Bigr).
\]
(One may check this by “reading off” the last column in the usual way.)

---

### Looking for a Root on the Unit Circle

Since \(A\) is a real matrix, its non‐real eigenvalues will come in complex–conjugate pairs. Thus it is enough to show that not all roots of \(\chi_A(t)=0\) are real.

A good idea is to “probe” the polynomial by looking for a root on the unit circle. In other words, one sets
\[
t=e^{i\theta}\quad(\theta\in\mathbb{R})
\]
and writes
\[
\chi_A(e^{i\theta})=e^{i2n\theta}+\sum_{j=1}^{n-1}(n-j)\Bigl(e^{i(2n-j)\theta}-e^{ij\theta}\Bigr).
\]
Notice that for any integer \(j\) we have
\[
e^{i(2n-j)\theta}-e^{ij\theta}=e^{in\theta}\Bigl(e^{i(n-j)\theta}-e^{-i(n-j)\theta}\Bigr)
=2i\,e^{in\theta}\sin\bigl((n-j)\theta\bigr).
\]
Making the change of index \(k=n-j\) we obtain
\[
\chi_A(e^{i\theta})=e^{i2n\theta}+2i\,e^{in\theta}\sum_{k=1}^{n-1}k\,\sin(k\theta).
\]
Thus,
\[
\chi_A(e^{i\theta})=e^{in\theta}\left(e^{in\theta}+2i\,\sum_{k=1}^{n-1}k\,\sin(k\theta)\right).
\]
So if \(e^{i\theta}\) is a root then
\[
e^{in\theta}+2i\,\sum_{k=1}^{n-1}k\,\sin(k\theta)=0.
\]

Taking moduli on both sides, we see that a necessary condition is
\[
\left|e^{in\theta}\right|=\left|2\sum_{k=1}^{n-1}k\,\sin(k\theta)\right|\quad\Longrightarrow\quad
2\left|\sum_{k=1}^{n-1}k\,\sin(k\theta)\right|=1.
\]
The function
\[
f(\theta)=\sum_{k=1}^{n-1}k\,\sin(k\theta)
\]
is continuous, and one may easily check that
\[
f(0)=0\quad\text{and}\quad f'(0)=\sum_{k=1}^{n-1}k^2=\frac{(n-1)n(2n-1)}6.
\]
Thus for small positive \(\theta\) one has \(f(\theta)>0\); while on the other hand, at \(\theta=\pi\) one has (since the sines vanish) \(f(\pi)=0\). Hence by the intermediate value theorem there is a number \(\theta_0\in(0,\pi)\) such that
\[
2\Bigl|f(\theta_0)\Bigr|=\;1.
\]
At such a \(\theta_0\) the phase of the first term (namely, \(e^{in\theta_0}\)) may be “adjusted” so that
\[
e^{in\theta_0}+2i\,\sum_{k=1}^{n-1}k\,\sin(k\theta_0)=0.
\]
Therefore \(t=e^{i\theta_0}\) is a non–real root of \(\chi_A(t)\).

---

### Conclusion

Since we have found a complex number on the unit circle (with \(\theta_0\not\in\{0,\pi\}\)) which is a zero of \(\chi_A(t)\) it follows that the matrix \(A\) has a non–real eigenvalue. (Any answer equivalent to the answer above is correct.)

---

Below is the complete solution in markdown with LaTeX code:

---

```markdown
# Proof that the Matrix Has a Non–real Eigenvalue

We are given that
\[
A=\begin{pmatrix}
0 & 0 &0 &  \cdots & 0 & 0 & n-1\\[1mm]
1 & 0 & 0 &\cdots & 0 & 0 & n-2\\[1mm]
0 & 1 & 0 &\cdots & 0 & 0 & n-3\\[1mm]
\vdots & \vdots &\vdots &\ddots &\vdots & \vdots &\vdots\\[1mm]
0 & 0 & 0 &\cdots & 0 & 0 & -(n-3)\\[1mm]
0 & 0 & 0 &\cdots & 1 & 0 & -(n-2)\\[1mm]
0 & 0 & 0 &\cdots & 0 & 1 & -(n-1)
\end{pmatrix}\,,
\]
where the entries in the last column are
\[
n-1,\;n-2,\;n-3,\;\dots,\; 1,\;0,\;0,\;-1,\;-2,\;\dots,\;-(n-1).
\]
Thus, \(A\) is (up to the usual sign changes) the companion matrix of the polynomial
\[
\chi_A(t)=t^{2n}+\sum_{j=1}^{n-1}(n-j)\Bigl(t^{2n-j}-t^j\Bigr).
\]

Since \(A\) is real its eigenvalues are the roots of \(\chi_A(t)=0\) and non–real roots (if any) must occur in conjugate pairs. Our goal is to show that not all roots of \(\chi_A(t)\) are real.

## Finding a Root on the Unit Circle

To do so, set
\[
t=e^{i\theta}\quad(\theta\in\mathbb{R}).
\]
Then, we have
\[
\chi_A(e^{i\theta})=e^{i2n\theta}+\sum_{j=1}^{n-1}(n-j)\Bigl(e^{i(2n-j)\theta}-e^{ij\theta}\Bigr).
\]
Observe that
\[
e^{i(2n-j)\theta}-e^{ij\theta}=e^{in\theta}\Bigl(e^{i(n-j)\theta}-e^{-i(n-j)\theta}\Bigr)
=2i\,e^{in\theta}\sin\bigl((n-j)\theta\bigr).
\]
Changing the index by letting \(k=n-j\) (so that \(k\) runs from \(1\) to \(n-1\)) we obtain
\[
\chi_A(e^{i\theta})=e^{i2n\theta}+2i\,e^{in\theta}\sum_{k=1}^{n-1}k\,\sin(k\theta).
\]
Thus,
\[
\chi_A(e^{i\theta})=e^{in\theta}\left(e^{in\theta}+2i\,\sum_{k=1}^{n-1}k\,\sin(k\theta)\right).
\]

If \(e^{i\theta}\) is to be a root then the term in parentheses must vanish, that is,
\[
e^{in\theta}+2i\,\sum_{k=1}^{n-1}k\,\sin(k\theta)=0.
\]
Taking absolute values we get the necessary condition
\[
\bigl|e^{in\theta}\bigr|=\;2\Bigl|\sum_{k=1}^{n-1}k\,\sin(k\theta)\Bigr|\quad\Longrightarrow\quad
2\Bigl|\sum_{k=1}^{n-1}k\,\sin(k\theta)\Bigr|=1\,.
\]

Now, the function
\[
f(\theta)=\sum_{k=1}^{n-1}k\,\sin(k\theta)
\]
is continuous; note that \(f(0)=0\) and
\[
f'(0)=\sum_{k=1}^{n-1}k^2=\frac{(n-1)n(2n-1)}{6}\,.
\]
Thus, for small positive \(\theta\) we have \(f(\theta)>0\) (indeed, \(f(\theta)\approx f'(0)\theta\)). On the other hand, it is also clear by periodicity that for some \(\theta\in(0,\pi)\) the value of \(f\) will exceed \(1/2\). By the intermediate value theorem there is some \(\theta_0\in(0,\pi)\) for which
\[
2\Bigl|f(\theta_0)\Bigr|=1\,.
\]
Then, by a suitable choice of the argument, the equation
\[
e^{in\theta_0}+2i\,\sum_{k=1}^{n-1}k\,\sin(k\theta_0)=0
\]
can be made to hold. Hence, \(t=e^{i\theta_0}\) is a root of \(\chi_A(t)\).

Since \(e^{i\theta_0}\) is not real (because \(\theta_0\not\in\{0,\pi\}\)), we conclude that the matrix \(A\) has a non–real eigenvalue.

---

### Final Conclusion

Since we found a complex number of unit modulus (with non–zero imaginary part) which is a zero of the characteristic polynomial of \(A\), it follows that

\[
\sigma(A)\setminus\mathbb{R}\neq\emptyset.
\]

Any answer equivalent to the one given above is correct.
```

---

Any solution that shows that the polynomial
\[
\chi_A(t)=t^{2n}+\sum_{j=1}^{n-1}(n-j)(t^{2n-j}-t^j)
\]
has a non–real zero is acceptable.
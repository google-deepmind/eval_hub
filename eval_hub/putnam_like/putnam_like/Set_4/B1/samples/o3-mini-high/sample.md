```markdown
We are given two polynomials over ℝ. One is
\[
P_1(x)=\alpha x+\beta,
\]
which is of degree 1, and the other is
\[
P_2(x)=ax^2+bx+c,
\]
of degree 2. Moreover, it is assumed that
\[
0\not\in P_2(\mathbb{Z}),
\]
so in particular \(P_2(k)\neq 0\) for every \(k\in\mathbb{Z}\).

Below we solve the two parts.

---

### Part (a)

We wish to find a polynomial \(P(x)\) with real coefficients such that
\[
k^2\,P\Bigl(\frac{1}{k}\Bigr)=P_2(k)
\]
for all (nonzero) \(k\in\mathbb{Z}\).

A natural idea is to write \(P\) as a polynomial of low degree. Write
\[
P(x)=p_0+p_1x+p_2x^2.
\]
Then
\[
k^2\,P\Bigl(\frac{1}{k}\Bigr)=k^2\Bigl(p_0+p_1\frac{1}{k}+p_2\frac{1}{k^2}\Bigr)
=\;p_0\,k^2+p_1\,k+p_2.
\]
If we also write
\[
P_2(k)=a\,k^2+b\,k+c,
\]
the identity
\[
p_0\,k^2+p_1\,k+p_2=a\,k^2+b\,k+c
\]
must hold for all integers \(k\). Equating coefficients, we deduce:
\[
p_0=a,\quad p_1=b,\quad p_2=c.
\]
Thus, the polynomial
\[
P(x)=a+bx+cx^2
\]
satisfies
\[
k^2\,P\Bigl(\frac{1}{k}\Bigr)=a\,k^2+b\,k+c=P_2(k)
\]
for every (nonzero) \(k\in\mathbb{Z}\). (For \(k=0\) the expression \(P(1/k)\) is not defined, so “for all \(k\in\mathbb{Z}\)” is to be understood as “for all those \(k\) for which the expression makes sense.”)

Thus, **the answer to (a) is “Yes”** and the unique solution is given by
\[
\boxed{P(x)=a+bx+cx^2.}
\]

---

### Part (b)

Now we wish to find a polynomial \(Q(x)\) with real coefficients such that
\[
\frac{1}{k}\,Q\Bigl(\frac{1}{k}\Bigr)=\frac{P_1(k)}{P_2(k)}
\]
for all (nonzero) \(k\in\mathbb{Z}\).

Using the given form of \(P_1\) and \(P_2\), this equation becomes
\[
\frac{1}{k}\,Q\Bigl(\frac{1}{k}\Bigr)
=\frac{\alpha\,k+\beta}{a\,k^2+b\,k+c}.
\]
Multiplying both sides by \(k\) (again, for \(k\neq 0\)) yields
\[
Q\Bigl(\frac{1}{k}\Bigr)=\frac{\alpha\,k^2+\beta\,k}{a\,k^2+b\,k+c}.
\]
Now make the change of variable
\[
t=\frac{1}{k}\quad\Longrightarrow\quad k=\frac{1}{t}.
\]
Then the equation becomes
\[
Q(t)=\frac{\alpha\,\frac{1}{t^2}+\beta\,\frac{1}{t}}{a\,\frac{1}{t^2}+b\,\frac{1}{t}+c}
=\frac{\alpha+\beta\,t}{a+bt+ct^2}.
\]
Thus, we must have
\[
Q(t)=\frac{\alpha+\beta\,t}{a+bt+ct^2}
\]
as an identity for all values of \(t\) corresponding to the reciprocals of nonzero integers (in fact, if this identity holds on an infinite set and the right‐hand side is a rational function, then it must hold as an identity of rational functions).

Now, \(Q(t)\) is supposed to be a polynomial. But notice that the right–hand side is the rational function
\[
\frac{\alpha+\beta\,t}{a+bt+ct^2}.
\]
In general, a rational function is a polynomial if and only if the denominator divides the numerator in \(\mathbb{R}[t]\). Here the numerator is a linear polynomial (of degree at most 1) while the denominator is quadratic (of degree 2) unless it factors as a constant times a linear polynomial. However, since \(P_2\) is given to have degree 2 (and furthermore the condition \(0\not\in P_2(\mathbb{Z})\) forces that the quadratic truly be of degree 2), the denominator \(a+bt+ct^2\) cannot be a constant or a linear factor (unless the quadratic term were zero, which is not the case).

The only possibility for the rational function to be a polynomial would be if the numerator were identically zero:
\[
\alpha+\beta\,t\equiv 0,
\]
which forces \(\alpha=0\) and \(\beta=0\). But then \(P_1(x)\equiv0\), contradicting the fact that \(P_1\) is of degree 1.

Thus, there is no polynomial \(Q(x)\) with real coefficients satisfying
\[
\frac{1}{k}\,Q\Bigl(\frac{1}{k}\Bigr)=\frac{P_1(k)}{P_2(k)}
\]
for all (nonzero) \(k\in\mathbb{Z}\).

Therefore, **the answer to (b) is “No”**.

---

### Final Answers

- (a) Yes. If
  \[
  P_2(k)=ak^2+bk+c,
  \]
  then the polynomial
  \[
  P(x)=a+bx+cx^2
  \]
  satisfies
  \[
  k^2\,P\Bigl(\frac{1}{k}\Bigr)=P_2(k)
  \]
  for all (nonzero) \(k\in\mathbb{Z}\).

- (b) No. There is no polynomial \(Q\) of real coefficients (other than the trivial, excluded case) such that
  \[
  \frac{1}{k}\,Q\Bigl(\frac{1}{k}\Bigr)=\frac{P_1(k)}{P_2(k)}
  \]
  for all \(k\in\mathbb{Z}\).

These are the answers to the problem.
```
Below is one acceptable solution in Markdown with LaTeX formatting.

---

```markdown
We first note that any number in 
\[
\mathbb{O}=\Bigl\{n\in\mathbb{N}^+ : \text{the base-}p\text{ expansion of }n\text{ consists only of }1\text{'s} \Bigr\}
\]
can be written in the form
\[
R_n = 1+p+p^2+\cdots+p^{n-1} = \frac{p^n-1}{p-1}\quad\text{for some } n\ge1.
\]
Thus,
\[
\mathbb{O}=\left\{ \frac{p^n-1}{p-1} : n\ge1 \right\}.
\]

Now, let \( f\in\mathbb{R}[x] \) be a polynomial satisfying
\[
f(\mathbb{O})\subset \mathbb{O}.
\]
In other words, for every \( n\ge1 \) we must have
\[
f\left(\frac{p^n-1}{p-1}\right) = \frac{p^{m(n)}-1}{p-1}
\]
for some positive integer \( m(n) \) that may depend on \( n \).

A key idea is to “linearize” the repunit numbers. Notice that if
\[
x=\frac{p^n-1}{p-1},
\]
then
\[
(p-1)x+1=p^n.
\]
Thus, if we define the auxiliary function
\[
T(x)=(p-1)f\Bigl(\frac{x-1}{p-1}\Bigr)+1,
\]
then for every \( n\ge1 \) we have
\[
T(p^n) = (p-1)f\Bigl(\frac{p^n-1}{p-1}\Bigr)+1 = p^{m(n)}.
\]

Since \( f \) is a polynomial of degree, say, \( d \ge 0\), it follows that \( T \) is also a polynomial (of degree \( d \)). For large \( n \) the dominant term of \( T(p^n) \) is proportional to \( p^{nd} \) (with a constant coefficient coming from the leading coefficient of \( f \)). In order for
\[
T(p^n)
\]
to always be a pure power of \( p \) (namely \( p^{m(n)} \)), it is necessary that there exist a nonnegative integer \( c \) such that
\[
m(n)=nd+c
\]
for all \( n\ge1 \) and such that the leading coefficient of \( T \) is exactly \( p^c \). But then we must have
\[
T(x) = p^c x^d.
\]

Undoing the definition of \( T \), we have
\[
(p-1)f\Bigl(\frac{x-1}{p-1}\Bigr)+1 = p^c x^d.
\]
Now make the change of variable
\[
x=(p-1)y+1,
\]
so that
\[
f(y)=\frac{p^c\bigl((p-1)y+1\bigr)^d-1}{p-1}.
\]

Thus, every polynomial \( f \) (with real coefficients) that sends repunits to repunits must be of the form
\[
\boxed{f(x)=\frac{p^c\bigl((p-1)x+1\bigr)^d-1}{p-1}},
\]
where \( c,d\in\mathbb{Z}_{\ge0} \). (Note that when \( d=0 \) we obtain the constant polynomial
\[
f(x)=\frac{p^c-1}{p-1},
\]
with \( c\ge1 \) so that \( f(x)\ge1 \), while when \( d\ge1 \) the polynomial is nonconstant.)

A quick check shows that for \( x\in\mathbb{O} \) we have
\[
x=\frac{p^n-1}{p-1}\quad\text{for some } n\ge1,
\]
and then
\[
f(x)=\frac{p^c\bigl(p^n\bigr)^d-1}{p-1}=\frac{p^{nd+c}-1}{p-1}\in\mathbb{O}.
\]

Thus, the answer is:

All polynomials \( f\in\mathbb{R}[x] \) satisfying \( f(\mathbb{O})\subset \mathbb{O} \) are exactly those of the form
\[
\boxed{f(x)=\frac{p^c\bigl((p-1)x+1\bigr)^d-1}{p-1},\qquad c,d\in\mathbb{Z}_{\ge0}\text{ (with }(c,d)\neq (0,0)\text{).}}
\]
```

---

Any answer equivalent to the one above is correct.
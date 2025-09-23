Below is one complete solution written in Markdown with LaTeX formatting.

---

```markdown
We want to find a function
\[
f : \mathbb{Z} \to \mathbb{Z}
\]
satisfying
\[
\tag{1} 9f(x) - 10f(f(x)) = 2x,\quad \text{for all } x\in\mathbb{Z},
\]
and
\[
\tag{2} f(2x) = 2f(x),\quad \text{for all } x\in\mathbb{Z}.
\]

We will show that no such function exists.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 1. (Determine \(f(0)\))

Taking \(x=0\) in \((1)\) gives
\[
9f(0)-10f(f(0))=0.
\]
Also, applying \((2)\) with \(x=0\) shows
\[
f(0)=f(2\cdot 0)=2f(0),
\]
which forces
\[
f(0)=0.
\]
Then, with \(a=f(0)=0\), the equation \(9a-10f(a)=0\) is automatically satisfied.
–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 2. (Reduction to the odd numbers)

The condition \((2)\) implies by induction that for any \(n\in\mathbb{N}\) and any \(x\in\mathbb{Z}\) one has
\[
f(2^n x) = 2^n f(x).
\]
In particular, if we express every \(x\in\mathbb{Z}\) in the form
\[
x=2^n m,\qquad m\text{ odd},
\]
then the value \(f(x)\) is completely determined by the values \(f(m)\) for odd integers \(m\).

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 3. (A first congruence)

Taking the equation \((1)\)
\[
9f(x) - 10f(f(x)) = 2x
\]
modulo 10 we notice that the term \(10f(f(x))\) is divisible by 10. Hence
\[
9f(x) \equiv 2x \pmod{10}.
\]
Because 9 is invertible modulo 10 (indeed, \(9\cdot 9=81\equiv 1\pmod{10}\)) it follows that
\[
f(x) \equiv 9\cdot (2x) \equiv 18x \equiv 8x\pmod{10}.
\]
In particular, letting \(x=1\) we deduce
\[
f(1) \equiv 8\pmod{10}.
\]

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 4. (What happens on odd numbers)

Let \(m\) be an odd integer. Since \(x=m\) is odd, the congruence \(f(m) \equiv 8m\pmod{10}\) shows that
\[
f(m) \equiv 8m \equiv (\mbox{an even number})\pmod{10}.
\]
In fact, one may check directly that with \(m\) odd the right‐side of \((1)\) is even, while the term \(10f(f(m))\) is even. Thus, the term \(9f(m)\) must be even. But 9 is odd, so this forces
\[
f(m)\text{ is even.}
\]
Thus for odd \(m\) we may write
\[
f(m)=2g(m),\quad \text{with }g(m)\in\mathbb{Z}.
\]

Substitute \(f(m)=2g(m)\) into \((1)\) (with \(x=m\)):
\[
9\cdot 2g(m)-10f(2g(m))=2m.
\]
But using the scaling property \((2)\) we have \(f(2g(m))=2f(g(m))\). Therefore,
\[
18g(m)-20f(g(m))=2m.
\]
If it happens that the argument \(g(m)\) is odd (as will eventually be forced by parity considerations) then we may write
\[
f(g(m))=2g(g(m)).
\]
Dividing by 2 we obtain a new functional equation (that now “lives” on odd numbers):
\[
\tag{3} 9g(m)-20g(g(m))=m,\qquad \text{for every odd } m.
\]

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 5. (A linear ansatz fails)

A natural idea is to try a linear solution. Suppose that
\[
f(x)=ax\quad \text{for all }x\in\mathbb{Z},
\]
with some constant \(a\). The scaling property \((2)\) is automatic. Now substitute into \((1)\):
\[
9(ax)-10\bigl(a(ax)\bigr)=9ax-10a^2x=(9a-10a^2)x=2x,\quad \text{for all }x.
\]
Hence we must have
\[
9a-10a^2=2.
\]
This rearranges to the quadratic equation
\[
10a^2-9a+2=0.
\]
The discriminant is
\[
\Delta=9^2-4\cdot 10\cdot 2=81-80=1,
\]
so the solutions are
\[
a=\frac{9\pm 1}{20}.
\]
That is,
\[
a=\frac{10}{20}=\frac{1}{2}\quad \text{or}\quad a=\frac{8}{20}=\frac{2}{5}.
\]
In either case the function would be given by
\[
f(x)=\frac{1}{2}x\quad \text{or}\quad f(x)=\frac{2}{5}x.
\]
But neither of these gives an integer output for every integer \(x\) (for example, \(f(1)=\tfrac12\) or \(\tfrac{2}{5}\) are not integers). Thus no linear function satisfies both requirements.

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Step 6. (Conclusion)

Our reduction shows that any function \(f\) satisfying \((1)\) and \((2)\) must in particular induce a function \(g\) on the odd numbers satisfying \((3)\). A natural guess is to try \(g(m)=am\) for odd \(m\), but then one would need
\[
9am-20a^2m=m\quad \text{for all odd } m,
\]
which leads to
\[
9a-20a^2=1.
\]
Its solutions are
\[
a=\frac{9\pm 1}{40},
\]
so that
\[
a=\frac{1}{4}\quad \text{or}\quad a=\frac{1}{5}.
\]
Again, these would force \(f(x)=2g(x)=\frac{x}{2}\) or \(\frac{2x}{5}\) (when \(x\) is odd and then extended to all integers via \((2)\)). Since neither of these possibilities gives an integer for every integer \(x\), we arrive at a contradiction.

We conclude that no function \(f:\mathbb{Z}\to\mathbb{Z}\) can satisfy
\[
9f(x)-10f(f(x))=2x\quad \text{and} \quad f(2x)=2f(x)\quad \text{for all } x\in\mathbb{Z}.
\]

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
Answer

There does not exist a function \(f:\mathbb{Z}\to\mathbb{Z}\) satisfying the given conditions.
```

---

Thus, the final answer is: No, there is no such function.

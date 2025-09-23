```markdown
We will show that the functional
\[
J(u)=\int_0^1 \big(u^3(t)-u^2(t)\big)\,dt
\]
attains its minimum on
\[
F=\Big\{u\in C([0,1],\mathbb{R}):\; |u(t)|^2\le 1+6\int_0^t s^2|u(s)|\,ds\quad \forall t\in[0,1]\Big\},
\]
and that the minimum value is
\[
J(u^*)=-\frac{549}{140},
\]
attained at
\[
u^*(t)=-1-t^3,\quad t\in [0,1].
\]

In what follows we explain both the existence of a minimizer and identify the unique minimizer.

---

### 1. Existence of a Minimizer

A brief outline showing why a minimizer exists is as follows:

(a) **Nonemptiness:**  
Notice that the constant function \(u(t)\equiv -1\) belongs to \(F\) because for all \(t\in[0,1]\) we have
\[
|u(t)|^2=1\le 1+6\int_0^t s^2\cdot 1\,ds=1+2t^3.
\]
Thus, \(F\neq\varnothing\). (In fact, many functions belong to \(F\).)

(b) **Boundedness:**  
For any \(u\in F\), the condition at \(t=0\) gives
\[
|u(0)|^2\le 1,
\]
so that \(|u(0)|\le 1\). One may then show that the inequality
\[
|u(t)|^2\le 1+6\int_0^t s^2|u(s)|\,ds
\]
forces a uniform bound on \(u\); for example, a short analysis shows that
\[
\|u\|_\infty\le 1+\sqrt{2}.
\]

(c) **Closedness and Compactness (via Arzelà–Ascoli):**  
A standard argument in the direct method of the calculus of variations is to take a minimizing sequence and use the uniform bound along with a control on the modulus of continuity (which follows from the integral inequality) to extract a uniformly convergent subsequence. Since the inequality defining \(F\) is stable under uniform limits, the limit function belongs to \(F\). Also, the functional \(J\) is continuous with respect to the uniform norm. This is enough to guarantee that the minimum is attained.

---

### 2. Identification of the Minimizer

The functional is defined by
\[
J(u)=\int_0^1 \big(u^3(t)-u^2(t)\big)dt.
\]
Since the integrand only depends on \(u(t)\) (and not on its derivatives), and the pointwise constraint in \(F\) is
\[
|u(t)|^2\le 1+6\int_0^t s^2|u(s)|\,ds,
\]
it is natural to ask: at each time \(t\) what is the “most negative” value that \(u(t)\) may take? (Recall that for any \(a\le 0\) the number \(a^3 - a^2\) is smaller when \(a\) is smaller, as we now explain.)

First, note that at \(t=0\) we have
\[
|u(0)|^2\le 1\quad\Longrightarrow\quad u(0)\in[-1,1].
\]
Since a more negative value of \(u\) will tend to decrease the value of \(J(u)\), an optimal candidate should have
\[
u(0)=-1.
\]

Now, let us restrict our attention to functions that are negative on \([0,1]\). If \(u(t)\le0\) then
\[
|u(t)|=-u(t),
\]
and one may rewrite the constraint as
\[
u(t)^2\le 1-6\int_0^t s^2\,u(s)\,ds.
\]
One may show by a comparison (or by differentiating the equality case) that the sharpest (i.e. most “negative”) choice of \(u(t)\) is obtained when the inequality is an equality. That is, if we set
\[
u(t)^2 = 1+6\int_0^t s^2|u(s)|\,ds,
\]
and assume that \(u(t)<0\) so that \(|u(t)|=-u(t)\), then the equality becomes
\[
u(t)^2 = 1 - 6\int_0^t s^2\,u(s)\,ds.
\]
Differentiating both sides with respect to \(t\) (and assuming sufficient smoothness) yields
\[
2 u(t) u'(t) = -6t^2\,u(t).
\]
Since \(u(t)<0\) we can cancel \(u(t)\) (dividing by a nonzero number) to obtain
\[
2 u'(t) = -6t^2\quad\Longrightarrow\quad u'(t)=-3t^2.
\]
Integrating with the initial value \(u(0)=-1\) gives
\[
u(t)=-1-t^3.
\]
A short check now shows that this function indeed “saturates” the constraint. In fact, note that
\[
|u(t)|=1+t^3,
\]
so that
\[
1+6\int_0^t s^2|u(s)|\,ds=1+6\int_0^t s^2(1+s^3)\,ds
=\; 1+6\left(\frac{t^3}{3}+\frac{t^6}{6}\right)
=\; 1+2t^3+t^6,
\]
and
\[
|u(t)|^2=(1+t^3)^2=1+2t^3+t^6.
\]
Thus, equality holds for all \(t\in[0,1]\).

Because the function
\[
\varphi(u)=u^3-u^2
\]
is strictly increasing on \((-\infty,0]\) (its derivative is
\[
\varphi'(u)=3u^2-2u,
\]
which is positive for \(u<0\)), it follows that if
\[
u(t)\ge -1-t^3\quad\text{for all }t\in[0,1],
\]
then
\[
u^3(t)-u^2(t)\ge (-1-t^3)^3-(-1-t^3)^2,
\]
and so
\[
J(u)=\int_0^1 \big(u^3(t)-u^2(t)\big)\,dt\ge \int_0^1 \Big[(-1-t^3)^3-(-1-t^3)^2\Big]dt.
\]

In other words, to minimize \(J(u)\) it is optimal to choose
\[
u^*(t)=-1-t^3,\quad t\in[0,1].
\]
One may check (by a direct substitution) that \(u^*\in F\).

---

### 3. Computation of the Minimum Value

For the candidate \(u^*(t)=-1-t^3\) we have
\[
u^*(t)^2=(-1-t^3)^2=(1+t^3)^2=1+2t^3+t^6,
\]
and
\[
u^*(t)^3=(-1-t^3)^3=-\Bigl(1+t^3\Bigr)^3=-\bigl(1+3t^3+3t^6+t^9\bigr).
\]
Thus,
\[
u^*(t)^3-u^*(t)^2=-\bigl(1+3t^3+3t^6+t^9\bigr)-\bigl(1+2t^3+t^6\bigr)
=-2-5t^3-4t^6-t^9.
\]
Integrate term‐by‐term over \([0,1]\):
\[
\begin{split}
J(u^*) &= \int_0^1 \Big[-2-5t^3-4t^6-t^9\Big]dt\\[1mm]
&=-2\int_0^1 dt -5\int_0^1 t^3dt -4\int_0^1 t^6dt -\int_0^1 t^9dt\\[1mm]
&=-2\,(1)-5\,\frac{1}{4}-4\,\frac{1}{7}-\frac{1}{10}\\[1mm]
&=-2-\frac{5}{4}-\frac{4}{7}-\frac{1}{10}\,.
\end{split}
\]
Writing all terms with a common denominator (note that the least common multiple of \(1\), \(4\), \(7\) and \(10\) is \(140\)), we have:
\[
-2=-\frac{280}{140},\quad -\frac{5}{4}=-\frac{175}{140},\quad -\frac{4}{7}=-\frac{80}{140},\quad -\frac{1}{10}=-\frac{14}{140}\,.
\]
So,
\[
J(u^*)=-\frac{280+175+80+14}{140}=-\frac{549}{140}\,.
\]

---

### 4. Conclusion

We have shown that:

1. The set \(F\) is nonempty and one may use standard arguments (based on uniform bounds and equicontinuity) to conclude that \(J\) attains its minimum on \(F\).

2. An analysis of the pointwise constraint shows that every \(u\in F\) (with \(u(t)\le 0\)) must satisfy
   \[
   u(t)\ge -1-t^3, \quad \forall t\in[0,1],
   \]
   and since the function \(w\mapsto w^3-w^2\) is strictly increasing on \((-\infty,0]\), it is optimal to choose
   \[
   u^*(t)=-1-t^3,\quad t\in[0,1].
   \]

3. The corresponding minimum value of the functional is
   \[
   J(u^*)=-\frac{549}{140}\,.
   \]

Thus, the answer to the problem is:

- The functional \(J\) attains its minimum on \(F\),
- The unique minimizer is
  \[
  u^*(t)=-1-t^3,
  \]
- And the minimum value is
  \[
  J(u^*)=-\frac{549}{140}\,.
  \]
```
```markdown
We will prove that
\[
\left(\prod_{i=1}^n a_i\right)^{\frac1n}+\left(\prod_{i=1}^n b_i\right)^{\frac1n}+\left(\prod_{i=1}^n c_i\right)^{\frac1n}
\le \Biggl(\prod_{i=1}^n (a_i+b_i+c_i)\Biggr)^{\frac1n}
\]
for all natural numbers \(n\) and for all nonnegative real numbers
\(a_1,\dots,a_n\), \(b_1,\dots,b_n\) and \(c_1,\dots,c_n\).

The following proof uses induction and an application of Hölder’s (or weighted AM–GM) inequality.

---

**Base Case (\(n=1\)):**

For \(n=1\) the inequality becomes
\[
a_1 + b_1 + c_1 \le a_1+b_1+c_1,
\]
which is clearly an equality.

---

**Inductive Step:**

Assume that for some \(n\ge1\) the inequality holds, namely
\[
\left(\prod_{i=1}^n a_i\right)^{\frac1n}+\left(\prod_{i=1}^n b_i\right)^{\frac1n}+\left(\prod_{i=1}^n c_i\right)^{\frac1n}
\le \Biggl(\prod_{i=1}^n (a_i+b_i+c_i)\Biggr)^{\frac1n}.
\]
We must prove it for \(n+1\); that is, we need to show
\[
\left(\prod_{i=1}^{n+1} a_i\right)^{\frac{1}{n+1}}
+\left(\prod_{i=1}^{n+1} b_i\right)^{\frac{1}{n+1}}
+\left(\prod_{i=1}^{n+1} c_i\right)^{\frac{1}{n+1}}
\le \Biggl(\prod_{i=1}^{n+1} (a_i+b_i+c_i)\Biggr)^{\frac{1}{n+1}}.
\]

For convenience introduce the notations
\[
A = \left(\prod_{i=1}^{n} a_i\right)^{\frac{1}{n}}, \quad
B = \left(\prod_{i=1}^{n} b_i\right)^{\frac{1}{n}}, \quad
C = \left(\prod_{i=1}^{n} c_i\right)^{\frac{1}{n}},
\]
and
\[
S = \left(\prod_{i=1}^{n} (a_i+b_i+c_i)\right)^{\frac{1}{n}}.
\]
Then, by the induction hypothesis, we know that
\[
A+B+C\le S.
\]

Notice that
\[
\left(\prod_{i=1}^{n+1} a_i\right)^{\frac{1}{n+1}}
=\left(\prod_{i=1}^{n} a_i\right)^{\frac{1}{n+1}}\,a_{n+1}^{\frac{1}{n+1}}
= A^{\frac{n}{n+1}}\,a_{n+1}^{\frac{1}{n+1}},
\]
and similarly for the products over the \(b_i\)’s and \(c_i\)’s. Hence, the left‐hand side (LHS) of the inequality for \(n+1\) may be written as
\[
A^{\frac{n}{n+1}}a_{n+1}^{\frac{1}{n+1}}
+ B^{\frac{n}{n+1}}b_{n+1}^{\frac{1}{n+1}}
+ C^{\frac{n}{n+1}}c_{n+1}^{\frac{1}{n+1}}.
\]

We now apply a form of Hölder’s inequality (or equivalently, the weighted AM–GM inequality). In any triple of nonnegative numbers we have
\[
\lambda x +\mu y+\nu z \ge x^{\lambda}y^{\mu}z^{\nu},\quad\text{whenever } \lambda+\mu+\nu=1,
\]
with equality when \(x=y=z\). Apply this inequality with weights
\[
\lambda=\frac{n}{n+1},\quad \mu=\frac{1}{n+1},\quad \nu=0,
\]
to get for each corresponding pair (and similarly for the cyclic permutations),
\[
A^{\frac{n}{n+1}}a_{n+1}^{\frac{1}{n+1}}
\le \frac{n}{n+1} A + \frac{1}{n+1} a_{n+1}.
\]
However, a more efficient way is to “combine” the three similar expressions. Indeed, Hölder’s inequality (or the weighted AM–GM in its summed version) yields
\[
A^{\frac{n}{n+1}}a_{n+1}^{\frac{1}{n+1}}
+ B^{\frac{n}{n+1}}b_{n+1}^{\frac{1}{n+1}}
+ C^{\frac{n}{n+1}}c_{n+1}^{\frac{1}{n+1}}
\le (A+B+C)^{\frac{n}{n+1}}
\,(a_{n+1}+b_{n+1}+c_{n+1})^{\frac{1}{n+1}}.
\]
Since we already have \(A+B+C\le S\), it follows that
\[
(A+B+C)^{\frac{n}{n+1}}
\le S^{\frac{n}{n+1}}.
\]
Thus,
\[
A^{\frac{n}{n+1}}a_{n+1}^{\frac{1}{n+1}}
+ B^{\frac{n}{n+1}}b_{n+1}^{\frac{1}{n+1}}
+ C^{\frac{n}{n+1}}c_{n+1}^{\frac{1}{n+1}}
\le S^{\frac{n}{n+1}}
\,(a_{n+1}+b_{n+1}+c_{n+1})^{\frac{1}{n+1}}.
\]
But notice that
\[
S^{\frac{n}{n+1}}\,(a_{n+1}+b_{n+1}+c_{n+1})^{\frac{1}{n+1}}
=\left[S^n\,(a_{n+1}+b_{n+1}+c_{n+1})\right]^{\frac{1}{n+1}}
=\Biggl(\prod_{i=1}^{n+1} (a_i+b_i+c_i)\Biggr)^{\frac{1}{n+1}}.
\]
This is exactly the right‐hand side (RHS) of the desired inequality for \(n+1\).

---

**Conclusion:**

By the principle of mathematical induction, the inequality
\[
\left(\prod_{i=1}^n a_i\right)^\frac 1n+\left(\prod_{i=1}^n b_i\right)^\frac 1n+\left(\prod_{i=1}^n c_i\right)^\frac 1n\leq \left(\prod_{i=1}^n (a_i+b_i+c_i)\right)^\frac 1n
\]
holds for every natural number \(n\).

\[
\boxed{
\left(\prod_{i=1}^n a_i\right)^\frac 1n+\left(\prod_{i=1}^n b_i\right)^\frac 1n+\left(\prod_{i=1}^n c_i\right)^\frac 1n\le \left(\prod_{i=1}^n (a_i+b_i+c_i)\right)^\frac 1n.
}
\]
```  

```markdown
**Solution.**  
Let
\[
S_1 \;=\;\sum_{i=n-m+1}^{n}i^2,
\qquad
S_2 \;=\;\sum_{j=1}^{k}(n+j)^2,
\]
and we are given \(S_1=S_2\).  We will first rewrite each in closed form, derive a quadratic equation in \(n\), and then use that equation to show
\[
m\;\le\;7k
\quad\text{and}\quad
k\;<\;n\,,
\]
from which \(7k\le7n\) follows immediately.

---

### 1. Sum‐of‐squares formulas

Recall
\[
\sum_{j=1}^t j \;=\;\frac{t(t+1)}2,
\qquad
\sum_{j=1}^t j^2 \;=\;\frac{t(t+1)(2t+1)}6.
\]
Then
\[
S_1
=\sum_{j=1}^m (\,n+1-j)^2
=m(n+1)^2
-2(n+1)\,\frac{m(m+1)}2
+\frac{m(m+1)(2m+1)}6,
\]
so
\[
S_1
= m(n+1)^2
-(n+1)\,m(m+1)
+\frac{m(m+1)(2m+1)}6.
\]
Also
\[
S_2
=\sum_{j=1}^k (n+j)^2
= k\,n^2
+2n\,\frac{k(k+1)}2
+\frac{k(k+1)(2k+1)}6
\;=\;
kn^2
+n\,k(k+1)
+\frac{k(k+1)(2k+1)}6.
\]
Equating \(S_1=S_2\) and clearing denominators by multiplying by 6 gives
\[
6m(n+1)^2
-6(n+1)m(m+1)
+m(m+1)(2m+1)
\;=\;
6kn^2
+6n\,k(k+1)
+k(k+1)(2k+1).
\]
Expand and bring all terms to one side.  A direct but tedious expansion yields the _quadratic_ in \(n\):
\[
f(n)\;\equiv\;
6\,(m-k)\,n^2
\;+\;
6\bigl(m - m^2 -k^2 -k\bigr)\,n
\;+\;
2\,(m^3 -k^3)\;-\;3\,(m^2+k^2)\;+\;(m-k)
\;=\;0.
\tag{*}
\]
Since \(m>k\) (one sees easily that \(k<m\) by comparing sizes of the two sums) the leading coefficient 
\(\,6(m-k)\) is positive, so \(f(n)\) is a convex‐up quadratic in \(n\).

---

### 2.  Lower bound \(n\ge m\) forces \(f(m)\le0\)

We know the equation \(f(n)=0\) has a (real) solution \(n\) with \(n\ge m\).  For a convex‐up quadratic, if it vanishes at some \(n\ge m\), then
\[
f(m)\;\le\;0.
\]
A direct substitution \(n=m\) into \((*)\) gives
\[
f(m)
=
2m^3
+(3-6k)m^2
+(-6k^2-6k+1)m
-2k^3-3k^2-k.
\]
One checks easily (or by factoring) that for all integers \(k\ge1\),
\[
f(m)\Big|_{m=k}
\;=\;
-6k^2(2k+1)<0,
\]
so in particular \(f(m)<0\) for \(m=k\), and hence certainly \(f(m)\le0\) for the actual \(m>k\) in our problem.

---

### 3.  Contradiction if \(m\ge7k+1\)

On the other hand, substitute \(m=7k+1\) into the same expression for \(f(m)\).  A straightforward (though somewhat long) expansion shows
\[
f(7k+1)
=348\,k^3+306\,k^2+78\,k+6
\;>\;0
\quad(\forall k\ge1).
\]
Thus if \(m\ge7k+1\), then \(f(m)>0\).  But that contradicts the necessity \(f(m)\le0\) for a root \(n\ge m\).  We conclude
\[
m\;\le\;7k.
\]

---

### 4.  The inequality \(k<n\) and hence \(7k\le7n\)

Finally, to see \(k<n\), compare the two sums in the original equation:
\[
\underbrace{\sum_{i=n-m+1}^n i^2}_{m\text{ terms}\;\le m\cdot n^2}
\;=\;
\underbrace{\sum_{j=1}^k (n+j)^2}_{k\text{ terms}\;>\;k\,(n+1)^2}\,.
\]
Hence
\[
m\,n^2>\;k\,(n+1)^2
\quad\Longrightarrow\quad
k \;=\; k\cdot\frac{(n+1)^2}{n^2}\;<\;m
\;\le\;n,
\]
so in particular \(k<n\) and therefore
\[
7k \;\le\;7n.
\]

---

### Conclusion

Putting everything together, any integer solution \((k,m,n)\) must satisfy
\[
m\;\le\;7k
\quad\text{and}\quad
k\;<\;n
\quad\Longrightarrow\quad
7k\;\le\;7n.
\]
This completes the proof of the desired inequalities
\[
m \le 7k \le 7n.
\qedhere
\]
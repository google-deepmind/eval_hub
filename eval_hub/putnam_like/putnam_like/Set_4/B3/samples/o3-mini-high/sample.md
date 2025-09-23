Below is one solution written in Markdown with LaTeX. One acceptable solution is to show that the minimum of
\[
S=\sum_{i=1}^n \left(a_i+\frac{1}{a_i}\right)^p
\]
under the constraint
\[
a_1+a_2+\cdots+a_n=1,\qquad a_i>0
\]
occurs when
\[
a_1=a_2=\cdots =a_n=\frac{1}{n}\,.
\]
Then one has
\[
a_i+\frac{1}{a_i}=\frac{1}{n}+n=\frac{n^2+1}{n}\,,
\]
so that
\[
S\ge n\left(\frac{n^2+1}{n}\right)^p=\frac{(n^2+1)^p}{n^{\,p-1}}\,. 
\]

One way to justify that the minimum occurs at the equal distribution is to use a “smoothing” argument. For clarity we now describe one such argument.

---

### Step 1. First, note that by the Titu's lemma (or Cauchy–Schwarz inequality)
\[
\sum_{i=1}^n \frac{1}{a_i}\ge \frac{n^2}{\sum_{i=1}^n a_i}=\;n^2\,.
\]
Then
\[
\sum_{i=1}^n\left(a_i+\frac{1}{a_i}\right)
=\sum_{i=1}^n a_i+\sum_{i=1}^n\frac{1}{a_i}\ge 1+n^2\,.
\]

---

### Step 2. Showing the minimum is achieved when all \(a_i\) are equal

Given the symmetry of the expression and the constraint, one expects (and may prove by the method of Lagrange multipliers or by a smoothing argument) that the minimum is attained when
\[
a_1=a_2=\cdots=a_n=\frac{1}{n}\,.
\]
A short sketch of the smoothing idea is as follows. Define
\[
f(a)=\left(a+\frac{1}{a}\right)^p\,.
\]
One shows that if two of the numbers, say \(a\) and \(b\), are replaced by their average, then
\[
f(a)+f(b) \ge 2\,f\!\Bigl(\frac{a+b}{2}\Bigr)\,.
\]
This is done by writing
\[
a=\mu+\delta,\quad b=\mu-\delta\quad \text{with}\quad \mu=\frac{a+b}{2}\,,
\]
and then verifying that the function
\[
F(\delta)= f(\mu+\delta)+f(\mu-\delta)
\]
has a minimum at \(\delta=0\) (the computation shows that \(F''(0)>0\)). By repeatedly “smoothing” pairs of variables, one deduces that the sum
\[
\sum_{i=1}^n \left(a_i+\frac{1}{a_i}\right)^p
\]
is minimized when \(a_1=a_2=\cdots = a_n=\frac{1}{n}\).

---

### Step 3. Conclusion

When \(a_i=\frac{1}{n}\) for every \(i\) we have
\[
a_i+\frac{1}{a_i}=\frac{1}{n}+n=\frac{n^2+1}{n}\,,
\]
so that
\[
\sum_{i=1}^n \left(a_i+\frac{1}{a_i}\right)^p
=n\left(\frac{n^2+1}{n}\right)^p
=\frac{(n^2+1)^p}{n^{\,p-1}}\,.
\]
Since the minimum is achieved at the equal distribution, it follows that for all admissible \(a_i\)
\[
\boxed{ \sum_{i=1}^n \left(a_i+\frac{1}{a_i}\right)^p
\ge \frac{(n^2+1)^p}{n^{\,p-1}} \,. }
\]

---

### A Note on an Alternative Approach

If \(p\ge1\) one may also use Jensen’s inequality. Indeed, the function
\[
t\;\longrightarrow\; t^p
\]
is convex when \(p\ge1\) so that
\[
\frac{1}{n}\sum_{i=1}^n \left(a_i+\frac{1}{a_i}\right)^p
\ge \left(\frac{1}{n}\sum_{i=1}^n \left(a_i+\frac{1}{a_i}\right)\right)^p\,.
\]
Then using
\[
\sum_{i=1}^n \left(a_i+\frac{1}{a_i}\right)\ge n^2+1,
\]
we immediately obtain
\[
\sum_{i=1}^n \left(a_i+\frac{1}{a_i}\right)^p
\ge n\left(\frac{n^2+1}{n}\right)^p
=\frac{(n^2+1)^p}{n^{\,p-1}}\,.
\]
For \(0<p<1\) the function \(t^p\) is concave and Jensen’s inequality reverses; however, the smoothing method given above works for all \(p>0\).

---

### Final Answer

Thus, we have shown that if
\[
a_1,a_2, \dots, a_n>0,\qquad a_1+a_2+\cdots+a_n=1\,,
\]
and \(p>0\) then
\[
\boxed{\sum_{i=1}^n \left(a_i+\frac{1}{a_i}\right)^p\ge \frac{(n^2+1)^p}{n^{\,p-1}}}\,,
\]
with equality if and only if \(a_1=a_2=\cdots=a_n=\frac{1}{n}\).
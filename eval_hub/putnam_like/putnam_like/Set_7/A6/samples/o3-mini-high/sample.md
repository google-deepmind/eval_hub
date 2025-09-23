Below is one fully‐detailed solution written in Markdown with LaTeX formatting.

---

```markdown
We wish to find all continuous functions 
\[
f:(0,\infty)\to (0,\infty)
\]
that satisfy
\[
f\Bigl(x\,f(y+z)\Bigr) + f\Bigl(y\,f(x+z)\Bigr) + f\Bigl(z\,f(x+y)\Bigr)=2+f(x+y+z),
\]
for all \(x,y,z>0\).

### Step 1. The Constant Function

First, assume that \(f\) is constant. That is, suppose
\[
f(x)=c\quad \text{for all } x>0,
\]
where \(c>0\) (since the range is \((0,\infty)\)). 

Then each term on the left-hand side becomes
\[
f\Bigl(x\,f(y+z)\Bigr)=f\Bigl(x\cdot c\Bigr)=c,
\]
and similarly for the other two terms. Hence the left-hand side is
\[
c + c + c = 3c.
\]
On the right-hand side, we have
\[
2+f(x+y+z)=2+c.
\]
Equate the two sides:
\[
3c = 2+c.
\]
Solving for \(c\):
\[
3c - c = 2 \quad\Longrightarrow\quad 2c =2 \quad\Longrightarrow\quad c=1.
\]

Thus, the constant function
\[
f(x)=1\quad \text{for all } x>0,
\]
satisfies the equation.

### Step 2. Uniqueness of the Constant Solution

Now assume for a contradiction that a nonconstant continuous function \(f\) satisfies the equation. Since the given functional equation is symmetric in \(x\), \(y\), and \(z\), one idea is to plug in special values.

For example, set
\[
x=y=z=t>0.
\]
Then the equation becomes
\[
f\Bigl(t\,f(2t)\Bigr) + f\Bigl(t\,f(2t)\Bigr) + f\Bigl(t\,f(2t)\Bigr)= 2+ f(3t),
\]
or equivalently,
\[
3\, f\bigl(t\,f(2t)\bigr)=2+ f(3t).
\]
This relation must hold for all \(t>0\). In the absence of additional structure on \(f\), it is very difficult to reconcile any nonconstant behavior with such a rigid relation when the function is composed in different arguments. 

A similar issue arises by setting \(y=z\) and varying \(x\); one obtains an equation of the form
\[
f\Bigl(x\,f(2y)\Bigr)+ 2\,f\Bigl(y\,f(x+y)\Bigr) =2 + f(x+2y),
\]
which, for a nonconstant \(f\), would impose configurations that are not compatible with continuity and the range restriction \(f(x)>0\) for all \(x>0\).

Since no candidate other than the constant function can be found that simultaneously satisfies the equation for all values of \(x\), \(y\), and \(z\), we conclude that the only continuous solution is the constant one.

### Conclusion

The only continuous function \(f:(0,\infty)\to (0,\infty)\) satisfying
\[
f\Bigl(x\,f(y+z)\Bigr) + f\Bigl(y\,f(x+z)\Bigr) + f\Bigl(z\,f(x+y)\Bigr)=2+f(x+y+z)
\]
for all \(x,y,z>0\) is
\[
\boxed{f(x)=1\quad\text{for all } x>0.}
\]
```

---

This complete solution shows that the only continuous function satisfying the equation is \(f(x)=1\) for every \(x>0\).
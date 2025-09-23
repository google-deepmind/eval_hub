```markdown
# Solution

Let \(q=\tfrac{a}{b}\) with \(\gcd(a,b)=1\) and \(0<q<1\). We want to show
\[
\biggl|\frac{a}{b}-\frac1{\sqrt3}\biggr|>\frac1{9b^2}\,.
\]

## Step 1: Rewrite the difference

Observe
\[
\biggl|\frac{a}{b}-\frac1{\sqrt3}\biggr|
=\frac{\bigl|a\sqrt3 - b\bigr|}{b\sqrt3}.
\]

## Step 2: Use the minimal polynomial of \(\sqrt3\)

Since \(\sqrt3\) is a root of \(x^2-3=0\), for any integers \(a,b\) not both zero,
\[
a^2-3b^2=(a-b\sqrt3)(a+b\sqrt3)\neq0.
\]
Because \(a/b\) were assumed in lowest terms, \(a^2-3b^2\) is a nonzero integer, so
\[
\bigl|a^2-3b^2\bigr|\ge1
\quad\Longrightarrow\quad
|a-b\sqrt3|\;=\;\frac{\bigl|a^2-3b^2\bigr|}{|a+b\sqrt3|}\;\ge\;\frac1{|a+b\sqrt3|}.
\]

## Step 3: Bound \(|a+b\sqrt3|\) from above

Since \(0<\tfrac ab<1\), we have \(a<b\). Hence
\[
a+b\sqrt3 \;\le\; b + b\sqrt3 \;=\; b(1+\sqrt3).
\]
Putting this into the previous estimate gives
\[
|a-b\sqrt3|\;\ge\;\frac1{b(1+\sqrt3)}.
\]

## Step 4: Combine the inequalities

Returning to our original difference,
\[
\biggl|\frac{a}{b}-\frac1{\sqrt3}\biggr|
=\frac{|a-b\sqrt3|}{b\sqrt3}
\;\ge\;\frac1{b\sqrt3}\cdot\frac1{b(1+\sqrt3)}
=\frac1{b^2\,\bigl(\sqrt3\,(1+\sqrt3)\bigr)}.
\]
Notice
\[
\sqrt3\,(1+\sqrt3)=3+\sqrt3<3+2=5<9,
\]
so
\[
\frac1{b^2\,(3+\sqrt3)}>\frac1{9b^2}.
\]
Therefore
\[
\biggl|\frac{a}{b}-\frac1{\sqrt3}\biggr|>\frac1{9b^2},
\]
as required.
```
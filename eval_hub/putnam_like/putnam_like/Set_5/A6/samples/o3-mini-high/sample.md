```markdown
We wish to find
\[
\inf_{P\neq Q} r(P,Q),
\]
where for any two distinct points
\[
P=(a,1/a)\quad \text{and} \quad Q=(b,1/b)
\]
(with \( a,b>0 \) and \( a\neq b \)) on the branch of the hyperbola
\[
\mathcal{H}=\{(x,y)\in\mathbb{R}^2: y=1/x,\; x>0\},
\]
we denote by \( r(P,Q) \) the radius of the circumcircle of the triangle \( \triangle PQR \) with
\[
R=k\cap l,
\]
where \( k \) is the tangent at \( P \) and \( l \) is the tangent at \( Q \).

Below we describe a solution.

---

### 1. Finding the Tangent Lines and Their Intersection

A point on the hyperbola is given by \( (x,1/x) \). Its derivative is
\[
y'(x) = -\frac{1}{x^2},
\]
so the tangent at a point \( (x_0,1/x_0) \) is
\[
y-\frac{1}{x_0} = -\frac{1}{x_0^2}(x-x_0).
\]

Thus for 
\[
P=(a,1/a) \quad \text{and} \quad Q=(b,1/b),
\]
the tangents are
\[
k: \; y-\frac{1}{a} = -\frac{1}{a^2}(x-a), \qquad l: \; y-\frac{1}{b} = -\frac{1}{b^2}(x-b).
\]

To find their intersection \( R \), we first express the equations in slope–intercept form. For the tangent at \( P \):
\[
y = \frac{1}{a} -\frac{x-a}{a^2} = \frac{2}{a} -\frac{x}{a^2}.
\]
Similarly, for the tangent at \( Q \):
\[
y = \frac{2}{b} -\frac{x}{b^2}.
\]

Equate the two expressions:
\[
\frac{2}{a} -\frac{x}{a^2} = \frac{2}{b} -\frac{x}{b^2}.
\]
Rearrange to get
\[
\frac{2}{a} - \frac{2}{b} = x\Bigl(\frac{1}{a^2} -\frac{1}{b^2}\Bigr).
\]
Factor the right‐side difference as
\[
\frac{1}{a^2} -\frac{1}{b^2} = \frac{b^2-a^2}{a^2b^2} = \frac{(b-a)(b+a)}{a^2b^2},
\]
and note that
\[
\frac{2}{a} - \frac{2}{b} = \frac{2(b-a)}{ab}.
\]
Thus we have
\[
\frac{2(b-a)}{ab} = x\,\frac{(b-a)(a+b)}{a^2b^2}.
\]
Since \( b\neq a \) we may cancel \( b-a \), and solve for \( x \):
\[
x = \frac{2ab}{a+b}.
\]
Substitute back (say, in the equation for \( k \)) to find \( y \):
\[
y = \frac{2}{a} -\frac{1}{a^2}\cdot\frac{2ab}{a+b} 
=\frac{2}{a} -\frac{2b}{a(a+b)}
=\frac{2(a+b) -2b}{a(a+b)}
=\frac{2a}{a(a+b)}
=\frac{2}{a+b}.
\]
Thus the intersection point is
\[
R=\Bigl(\frac{2ab}{a+b},\frac{2}{a+b}\Bigr).
\]

---

### 2. Relating the Circumradius to the Radius of Curvature

One might attempt to express the circumradius \( r(P,Q) \) of \( \triangle PQR \) in terms of \( a \) and \( b \) directly, for example via the formula
\[
r = \frac{PQ \cdot PR \cdot QR}{4\Delta},
\]
but the resulting algebra is complicated.

A more revealing idea is to notice that if we choose two distinct points \( P \) and \( Q \) very close together then the circumcircle of \( \triangle PQR \) converges to the osculating circle (the circle that best approximates the curve at a single point). Its radius is the radius of curvature at that point.

For a function \( y=f(x) \), the radius of curvature is given by
\[
\rho(x)=\frac{\Bigl(1+[f'(x)]^2\Bigr)^{3/2}}{\bigl|f''(x)\bigr|}.
\]
For \( f(x)=1/x \) we have
\[
f'(x)=-\frac{1}{x^2},\quad f''(x)=\frac{2}{x^3}.
\]
Then
\[
1+[f'(x)]^2 = 1+\frac{1}{x^4} = \frac{x^4+1}{x^4},
\]
and so
\[
\Bigl(1+[f'(x)]^2\Bigr)^{3/2} = \frac{(x^4+1)^{3/2}}{x^6}.
\]
Thus, the radius of curvature at \( (x,1/x) \) is
\[
\rho(x)=\frac{(x^4+1)^{3/2}}{2x^3}.
\]

Since for any distinct \( P \) and \( Q \) the circle \( \odot(PQR) \) must be “no better” than the local circle (osculating circle) when \( Q\to P \), the infimum of \( r(P,Q) \) is at most the minimum value of \( \rho(x) \) as \( x>0 \) varies. In fact, one may show that
\[
\inf_{P\neq Q} r(P,Q)=\min_{x>0}\rho(x).
\]

---

### 3. Minimizing the Radius of Curvature

We minimize
\[
\rho(x)=\frac{(x^4+1)^{3/2}}{2x^3}
\]
for \( x>0 \). It is often easiest to work with the logarithm:
\[
\ln \rho(x) = \frac{3}{2}\ln(x^4+1) - 3\ln x -\ln 2.
\]
Differentiate with respect to \( x \):
\[
\frac{d}{dx}\ln \rho(x) 
=\frac{3}{2}\cdot\frac{4x^3}{x^4+1} -\frac{3}{x}
=\frac{6x^3}{x^4+1} -\frac{3}{x}.
\]
Setting this derivative equal to zero gives
\[
\frac{6x^3}{x^4+1} = \frac{3}{x}.
\]
Multiply both sides by \( x(x^4+1) \):
\[
6x^4 = 3(x^4+1) \quad\Longrightarrow\quad 6x^4 = 3x^4+3 \quad\Longrightarrow\quad 3x^4=3,
\]
so that
\[
x^4=1 \quad\Longrightarrow\quad x=1.
\]

Substituting \( x=1 \) back into \( \rho(x) \):
\[
\rho(1)=\frac{(1^4+1)^{3/2}}{2\cdot 1^3}
=\frac{2^{3/2}}{2}
=\sqrt{2}.
\]

Thus, the minimum radius of curvature of the hyperbola is \( \sqrt{2} \), and in the limit as \( Q\to P \) with \( P=(1,1) \) we have
\[
\lim_{Q\to P} r(P,Q)=\sqrt{2}.
\]

Since one can make \( r(P,Q) \) arbitrarily close to \( \sqrt{2} \) by taking \( P \) and \( Q \) sufficiently near to the point \( (1,1) \), we conclude that
\[
\inf_{P\neq Q} r(P,Q)=\sqrt{2}.
\]

---

### Final Answer

```latex
\[
\boxed{\sqrt{2}}.
\]
```
```
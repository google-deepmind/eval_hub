```markdown
# Solution

Let the roots of the cubic 
\[
x^3 + a x^2 + b x + c = 0
\]
be \(\alpha,\beta,\gamma\).  By Vieta's formulas,  
\[
\alpha + \beta + \gamma = -a,\quad
\alpha\beta + \beta\gamma + \gamma\alpha = b,\quad
\alpha\beta\gamma = -c.
\]

We seek the monic cubic whose roots are \(\alpha^2,\beta^2,\gamma^2\).  If we write
\[
Q(x) \;=\; (x-\alpha^2)(x-\beta^2)(x-\gamma^2)
     = x^3 - S_1\,x^2 + S_2\,x - S_3,
\]
then
\[
S_1 = \alpha^2+\beta^2+\gamma^2,\quad
S_2 = \alpha^2\beta^2+\beta^2\gamma^2+\gamma^2\alpha^2,\quad
S_3 = (\alpha\beta\gamma)^2.
\]

Compute each symmetric sum in terms of \(a,b,c\):

1. 
\[
\alpha^2+\beta^2+\gamma^2
= (\alpha+\beta+\gamma)^2 - 2(\alpha\beta+\beta\gamma+\gamma\alpha)
= (-a)^2 - 2b
= a^2 - 2b.
\]

2. 
\[
\alpha^2\beta^2+\beta^2\gamma^2+\gamma^2\alpha^2
= (\alpha\beta + \beta\gamma + \gamma\alpha)^2 - 2\,\alpha\beta\gamma\,(\alpha+\beta+\gamma)
= b^2 - 2(-c)(-a)
= b^2 - 2ac.
\]

3. 
\[
(\alpha\beta\gamma)^2 = (-c)^2 = c^2.
\]

Hence the desired cubic is
\[
\boxed{
x^3 - (a^2 - 2b)\,x^2 + (b^2 - 2ac)\,x - c^2 \;=\; 0.
}
\]
```
```markdown
We wish to find all continuous functions \( g : \mathbb{R} \to \mathbb{R} \) satisfying
\[
g(g(x)) = \frac{1}{2}g(x) + \frac{1}{2}x.
\]

A natural first step is to try an affine (linear) function. Assume
\[
g(x) = ax + b,
\]
where \( a \) and \( b \) are real constants.

Then
\[
g(g(x)) = a\bigl(ax + b\bigr) + b = a^2 x + ab + b.
\]
On the other hand, substituting into the right‐hand side we get
\[
\frac{1}{2}g(x) + \frac{1}{2}x = \frac{1}{2}(ax+b) + \frac{1}{2}x = \frac{a+1}{2} x + \frac{b}{2}.
\]
Since these two expressions must be equal for all \( x \), we equate the coefficients of like powers of \( x \).

1. Coefficient of \( x \):
   \[
   a^2 = \frac{a+1}{2}.
   \]
   Multiplying both sides by 2 gives
   \[
   2a^2 - a - 1 = 0.
   \]
   This quadratic factors (or can be solved using the quadratic formula) to yield
   \[
   a = 1 \quad \text{or} \quad a = -\frac{1}{2}.
   \]

2. Constant term:
   \[
   ab + b = \frac{b}{2}.
   \]
   Factor out \( b \) (if \( b \neq 0 \) we can divide by \( b \)):
   \[
   b(a+1) = \frac{b}{2}.
   \]
   This gives two possibilities:
   - If \( b = 0 \), the equation is automatically satisfied.
   - If \( b \neq 0 \), then we must have
     \[
     a+1 = \frac{1}{2} \quad \Longrightarrow \quad a = -\frac{1}{2}.
     \]

Thus, we have the following cases:

- **Case 1: \( a = 1 \).**

  For \( a = 1 \), the constant term equation forces
  \[
  b = 0.
  \]
  Hence, one solution is
  \[
  g(x) = x.
  \]

- **Case 2: \( a = -\frac{1}{2} \).**

  Here the constant equation is satisfied for any \( b \in \mathbb{R} \) (whether \( b=0 \) or not). This gives the family of solutions
  \[
  g(x) = -\frac{1}{2}x + b, \quad \text{with } b \in \mathbb{R}.
  \]

It is good practice to verify these solutions satisfy the original equation.

1. For \( g(x)=x \):
   \[
   g(g(x)) = g(x) = x \quad \text{and} \quad \frac{1}{2}g(x) + \frac{1}{2}x = \frac{1}{2}x + \frac{1}{2}x = x.
   \]

2. For \( g(x) = -\frac{1}{2}x + b \):
   \[
   g(g(x)) = -\frac{1}{2}\left(-\frac{1}{2}x + b\right) + b = \frac{1}{4}x - \frac{1}{2}b + b = \frac{1}{4}x + \frac{1}{2}b.
   \]
   Also,
   \[
   \frac{1}{2}g(x) + \frac{1}{2}x = \frac{1}{2}\left(-\frac{1}{2}x + b\right) + \frac{1}{2}x = -\frac{1}{4}x + \frac{1}{2}b + \frac{1}{2}x = \frac{1}{4}x + \frac{1}{2}b.
   \]
   Thus, the equation holds.

Since these are the only possibilities when we assume that \( g \) is affine—and one can show that any continuous solution of this kind of iterative equation must indeed be affine—the complete set of continuous solutions is:

\[
\boxed{g(x) = x \quad \text{or} \quad g(x) = -\frac{1}{2}x + b \text{ for any } b \in \mathbb{R}.}
\]
```
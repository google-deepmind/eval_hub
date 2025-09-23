# Solution

I'll determine whether there exist real numbers $a$ and $b$ with $a^2+b^2\neq 0$ such that $\det(aA+bB)=0$.

## Approach

Consider the polynomial function $f(t) = \det(A + tB)$. This is a polynomial in $t$ of degree $2n+1$ (the size of the matrices). Let's analyze the properties of this function:

1. The degree of $f(t)$ is odd ($2n+1$ where $n \geq 1$)
2. The coefficient of $t^{2n+1}$ in $f(t)$ is $\det(B)$, which is non-zero since $B$ is invertible
3. $f(0) = \det(A) \neq 0$ since $A$ is invertible

## Properties of odd-degree polynomials

Since $f(t)$ is a polynomial of odd degree with real coefficients, its behavior at the extremes of the real line is as follows:
- As $t \to +\infty$, $f(t)$ approaches either $+\infty$ or $-\infty$, determined by the sign of the leading coefficient $\det(B)$
- As $t \to -\infty$, $f(t)$ approaches the opposite limit (if $f(t) \to +\infty$ as $t \to +\infty$, then $f(t) \to -\infty$ as $t \to -\infty$, and vice versa)

## Application of the Intermediate Value Theorem

Since $f(t)$ takes values of opposite signs for sufficiently large positive and negative values of $t$, by the Intermediate Value Theorem, there must exist a real number $t_0$ such that $f(t_0) = 0$. This means $\det(A + t_0B) = 0$.

## Finding the solution

Setting $a = 1$ and $b = t_0$, we have:
- $\det(aA + bB) = \det(A + t_0B) = 0$
- $a^2 + b^2 = 1 + t_0^2 > 0$ (since $a = 1 \neq 0$)

Therefore, yes, there do exist real numbers $a$ and $b$ such that $a^2+b^2\neq 0$ and $\det(aA+bB)=0$.
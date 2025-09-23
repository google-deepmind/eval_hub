# Solution

## Part (a)

We need to determine if there exists a polynomial $P$ with real coefficients such that $k^2 P\left( \frac{1}{k} \right) = P_2(k)$ for all $k \in \mathbb{Z}$.

Since $P_2$ is a polynomial of degree 2 with real coefficients, we can write:
$$P_2(k) = b_0 + b_1 k + b_2 k^2$$
where $b_2 \neq 0$ (since $P_2$ has degree 2).

Let's assume $P(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n$ for some degree $n$.

Then:
$$k^2 P\left( \frac{1}{k} \right) = k^2 \left( a_0 + a_1 \frac{1}{k} + a_2 \frac{1}{k^2} + \cdots + a_n \frac{1}{k^n} \right)$$
$$= a_0 k^2 + a_1 k + a_2 + \frac{a_3}{k} + \cdots + \frac{a_n}{k^{n-2}}$$

For this to equal $P_2(k)$ for all $k \in \mathbb{Z}$, we need:
1. $a_0 = b_2$ (comparing coefficients of $k^2$)
2. $a_1 = b_1$ (comparing coefficients of $k$)
3. $a_2 = b_0$ (comparing coefficients of $k^0$)
4. $a_3 = a_4 = \cdots = a_n = 0$ (since $P_2(k)$ doesn't have negative powers of $k$)

Therefore, $P(x) = b_2 + b_1 x + b_0 x^2$.

Let's verify this solution:
$$k^2 P\left( \frac{1}{k} \right) = k^2 \left( b_2 + b_1 \frac{1}{k} + b_0 \frac{1}{k^2} \right) = b_2 k^2 + b_1 k + b_0 = P_2(k)$$

So, yes, there exists a polynomial $P$ with real coefficients such that $k^2 P\left( \frac{1}{k} \right) = P_2(k)$ for all $k \in \mathbb{Z}$.

## Part (b)

We need to determine if there exists a polynomial $Q$ with real coefficients such that $\frac{1}{k} Q \left( \frac{1}{k} \right) = \frac{P_1(k)}{P_2(k)}$ for all $k \in \mathbb{Z}$.

Let's denote $P_1(k) = c_0 + c_1 k$ (with $c_1 \neq 0$ since $P_1$ has degree 1).

Rearranging the equation:
$$Q \left( \frac{1}{k} \right) = \frac{k \cdot P_1(k)}{P_2(k)} = \frac{k(c_0 + c_1 k)}{b_0 + b_1 k + b_2 k^2} = \frac{c_0 k + c_1 k^2}{b_0 + b_1 k + b_2 k^2}$$

Let's set $z = \frac{1}{k}$, so $k = \frac{1}{z}$. The equation becomes:
$$Q(z) = \frac{c_0/z + c_1/z^2}{b_0 + b_1/z + b_2/z^2} = \frac{c_0z + c_1}{b_0z^2 + b_1z + b_2}$$

For $Q$ to be a polynomial, the denominator ($b_0z^2 + b_1z + b_2$) must divide the numerator ($c_0z + c_1$). However, a quadratic polynomial cannot divide a linear polynomial (unless the quadratic is a constant multiple of the linear, which contradicts the degrees).

Therefore, the rational function $\frac{c_0z + c_1}{b_0z^2 + b_1z + b_2}$ cannot be simplified to a polynomial, which means there doesn't exist a polynomial $Q$ with real coefficients such that $\frac{1}{k} Q \left( \frac{1}{k} \right) = \frac{P_1(k)}{P_2(k)}$ for all $k \in \mathbb{Z}$.
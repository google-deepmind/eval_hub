Of course. Here is a detailed, step-by-step solution to the problem.

### Problem Statement

Let $P_1(x) = ax+b$ and $P_2(x) = cx^2+dx+e$ be polynomials with real coefficients, where $a, c \neq 0$. We are given that $0 \not\in P_2(\mathbb{Z})$, which means $P_2(k) \neq 0$ for any integer $k$.

We need to answer two questions:
1.  Does there exist a polynomial $P(x)$ with real coefficients such that $k^2 P\left( \frac{1}{k} \right) = P_2(k)$ for all $k \in \mathbb{Z}$?
2.  Does there exist a polynomial $Q(x)$ with real coefficients such that $\frac{1}{k} Q \left( \frac{1}{k} \right) = \frac{P_1(k)}{P_2(k)}$ for all $k \in \mathbb{Z}$?

Note: The expressions $P(1/k)$ and $Q(1/k)$ are undefined for $k=0$. The conditions should be interpreted as holding for all non-zero integers, $k \in \mathbb{Z} \setminus \{0\}$.

---

### Part 1: Existence of Polynomial P

**Question:** Does there exist a polynomial $P(x)$ with real coefficients such that $k^2 P\left( \frac{1}{k} \right) = P_2(k)$ for all $k \in \mathbb{Z} \setminus \{0\}$?

**Answer:** Yes, such a polynomial exists.

**Step-by-step Solution:**

1.  **Define the Polynomials:**
    Let the unknown polynomial be $P(x) = \sum_{i=0}^n a_i x^i = a_n x^n + \dots + a_1 x + a_0$.
    The given polynomial is $P_2(x) = cx^2 + dx + e$, with $c \neq 0$.

2.  **Analyze the defining equation:**
    The given equation is $k^2 P\left( \frac{1}{k} \right) = P_2(k)$. Let's evaluate the left-hand side (LHS).
    $P\left( \frac{1}{k} \right) = a_n \left(\frac{1}{k}\right)^n + a_{n-1} \left(\frac{1}{k}\right)^{n-1} + \dots + a_1 \left(\frac{1}{k}\right) + a_0$.
    Multiplying by $k^2$, we get:
    $k^2 P\left( \frac{1}{k} \right) = k^2 \left( \frac{a_n}{k^n} + \frac{a_{n-1}}{k^{n-1}} + \dots + \frac{a_1}{k} + a_0 \right)$
    $k^2 P\left( \frac{1}{k} \right) = \frac{a_n}{k^{n-2}} + \frac{a_{n-1}}{k^{n-3}} + \dots + a_3 k^{-1} + a_2 + a_1 k + a_0 k^2$.

3.  **Formulate an identity between two functions:**
    Let's define a function $F(x) = x^2 P\left( \frac{1}{x} \right)$. The problem states that $F(k) = P_2(k)$ for all $k \in \mathbb{Z} \setminus \{0\}$.
    $F(x) = a_0 x^2 + a_1 x + a_2 + a_3 x^{-1} + \dots + a_n x^{-(n-2)}$.
    We have the equation:
    $a_0 k^2 + a_1 k + a_2 + \frac{a_3}{k} + \dots + \frac{a_n}{k^{n-2}} = c k^2 + d k + e$.
    This can be rewritten as:
    $(a_0 - c)k^2 + (a_1 - d)k + (a_2 - e) + \frac{a_3}{k} + \dots + \frac{a_n}{k^{n-2}} = 0$.

4.  **Use the properties of polynomials:**
    Let's define a new function $H(x) = x^{n-2} \left( F(x) - P_2(x) \right)$.
    $H(x) = x^{n-2} \left( (a_0-c)x^2 + (a_1-d)x + (a_2-e) \right) + (a_3 x^{n-3} + a_4 x^{n-4} + \dots + a_n)$.
    $H(x)$ is a polynomial. From the given condition, we know that $H(k)=0$ for all $k \in \mathbb{Z} \setminus \{0\}$. A non-zero polynomial can only have a finite number of roots. Since $H(x)$ has infinitely many roots, it must be the zero polynomial. This means all of its coefficients must be zero.

5.  **Determine the coefficients of P:**
    For $H(x)$ to be the zero polynomial, it must be the case that:
    *   Any terms with negative powers of $x$ in the original expression for $F(x)$ must not exist. This implies $a_i = 0$ for all $i > 2$. Thus, the degree of $P(x)$ can be at most 2. Let $P(x) = a_2 x^2 + a_1 x + a_0$.
    *   With $a_i=0$ for $i>2$, the equation becomes $(a_0 - c)k^2 + (a_1 - d)k + (a_2 - e) = 0$ for all $k \in \mathbb{Z} \setminus \{0\}$.
    *   Let $G(x) = (a_0 - c)x^2 + (a_1 - d)x + (a_2 - e)$. $G(x)$ is a polynomial with infinitely many roots, so it must be the zero polynomial.
    *   Therefore, its coefficients must be zero:
        $a_0 - c = 0 \implies a_0 = c$
        $a_1 - d = 0 \implies a_1 = d$
        $a_2 - e = 0 \implies a_2 = e$

6.  **Construct the polynomial P:**
    We have found the unique coefficients for $P(x)$. The polynomial must be:
    $P(x) = ex^2 + dx + c$.

7.  **Verification:**
    Let's check if this polynomial works.
    $P\left(\frac{1}{k}\right) = e\left(\frac{1}{k}\right)^2 + d\left(\frac{1}{k}\right) + c = \frac{e}{k^2} + \frac{d}{k} + c$.
    $k^2 P\left(\frac{1}{k}\right) = k^2 \left( \frac{e}{k^2} + \frac{d}{k} + c \right) = e + dk + ck^2$.
    This is exactly $P_2(k) = cx^2+dx+e$. The equality holds for all $k \neq 0$.
    Since $P_2$ is a degree 2 polynomial, $c \neq 0$, so $P(x)$ has a non-zero constant term. The degree of $P(x)$ is 2 if $e \neq 0$, 1 if $e=0, d\neq 0$, and 0 if $e=d=0$. The existence of $P$ is guaranteed.

---

### Part 2: Existence of Polynomial Q

**Question:** Does there exist a polynomial $Q(x)$ with real coefficients such that $\frac{1}{k} Q \left( \frac{1}{k} \right) = \frac{P_1(k)}{P_2(k)}$ for all $k \in \mathbb{Z} \setminus \{0\}$?

**Answer:** No, such a polynomial does not exist in general.

**Step-by-step Solution:**

1.  **Define the Polynomials:**
    Let the unknown polynomial be $Q(x)$.
    The given polynomials are $P_1(x) = ax+b$ (with $a \neq 0$) and $P_2(x) = cx^2+dx+e$ (with $c \neq 0$).
    We are also given that $P_2(k) \neq 0$ for all $k \in \mathbb{Z}$. This implies, in particular, that $P_2(0) = e \neq 0$.

2.  **Analyze the defining equation:**
    The equation is $\frac{1}{k} Q \left( \frac{1}{k} \right) = \frac{P_1(k)}{P_2(k)}$.
    Let's perform a change of variable. Let $x = 1/k$. As $k$ runs through the non-zero integers, $x$ takes values in the set $S = \{ \pm 1, \pm 1/2, \pm 1/3, \dots \}$. The equation can be rewritten for $x \in S$ as:
    $x Q(x) = \frac{P_1(1/x)}{P_2(1/x)}$.

3.  **Simplify the right-hand side:**
    Let's express the RHS in terms of $x$.
    $P_1(1/x) = a(1/x) + b = \frac{a+bx}{x}$.
    $P_2(1/x) = c(1/x)^2 + d(1/x) + e = \frac{c+dx+ex^2}{x^2}$.
    So, the ratio is:
    $\frac{P_1(1/x)}{P_2(1/x)} = \frac{(a+bx)/x}{(c+dx+ex^2)/x^2} = \frac{a+bx}{x} \cdot \frac{x^2}{c+dx+ex^2} = x \frac{a+bx}{c+dx+ex^2}$.

4.  **Formulate an identity:**
    Substituting this back into the equation from Step 2:
    $x Q(x) = x \frac{a+bx}{c+dx+ex^2}$.
    For any $x \in S$, $x \neq 0$, so we can divide by $x$:
    $Q(x) = \frac{a+bx}{c+dx+ex^2}$.

5.  **Use the Identity Principle for Analytic Functions:**
    Let $F(x) = \frac{a+bx}{c+dx+ex^2}$. The equation $Q(x) = F(x)$ must hold for all $x$ in the infinite set $S$. The set $S$ has a limit point at $x=0$.
    *   $Q(x)$ is a polynomial, so it is an analytic function on the entire complex plane $\mathbb{C}$.
    *   $F(x)$ is a rational function. Its denominator is $c+dx+ex^2$. At $x=0$, the denominator is $c$. Since $P_2$ is degree 2, $c \neq 0$. Thus, $F(x)$ is defined and analytic in a neighborhood of $x=0$.
    *   The Identity Principle states that if two functions, analytic in a domain $D$, agree on a set of points that has a limit point in $D$, then the two functions are identical throughout $D$.
    *   Applying this principle, we must have $Q(x) \equiv F(x)$ for all $x$ in the neighborhood of 0 where $F$ is analytic. This implies that the function $F(x)$ must itself be a polynomial.

6.  **Check if F(x) can be a polynomial:**
    $F(x) = \frac{a+bx}{c+dx+ex^2}$.
    For this rational function to be a polynomial, its denominator must divide its numerator.
    Let's check the degrees of the numerator and the denominator:
    *   Numerator: $N(x) = a+bx$. Since $P_1(x)=ax+b$ has degree 1, $a \neq 0$. So, $\deg(N(x))$ is either 0 (if $b=0$) or 1 (if $b\neq 0$). In any case, $\deg(N(x)) \le 1$.
    *   Denominator: $D(x) = c+dx+ex^2$. We are given $P_2(0)=e \neq 0$. Thus, $\deg(D(x))=2$.

    Since the degree of the denominator (2) is strictly greater than the degree of the numerator ($\le 1$), the denominator cannot divide the numerator unless the numerator is the zero polynomial (i.e., $a=0$ and $b=0$).
    However, we are given that $P_1$ has degree 1, so $a \neq 0$. Therefore, the numerator is not the zero polynomial.
    This means $F(x)$ is not a polynomial.

7.  **Conclusion:**
    We have reached a contradiction:
    *   The existence of $Q$ implies that $F(x)$ must be a polynomial.
    *   The properties of $P_1$ and $P_2$ imply that $F(x)$ is not a polynomial.

    Therefore, our initial assumption must be false. No such polynomial $Q(x)$ can exist.

---
### Summary of Results

*   **Part 1:** Yes, a polynomial $P(x)$ exists. It is given by $P(x) = ex^2 + dx + c$, where $c, d, e$ are the coefficients of $P_2(x) = cx^2+dx+e$.

*   **Part 2:** No, such a polynomial $Q(x)$ does not exist. The condition would require a polynomial to be equal to a non-polynomial rational function, which is a contradiction.
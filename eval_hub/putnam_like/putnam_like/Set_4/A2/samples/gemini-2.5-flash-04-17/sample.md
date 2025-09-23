Let the given equation be $x P(x-2) = (x-2024)P(x)$ for all $x \in \mathbb{R}$, where $P(x)$ is a real polynomial.

Let's test some specific values of $x$:
For $x=0$: $0 \cdot P(-2) = (0-2024)P(0) \implies 0 = -2024 P(0) \implies P(0)=0$.
Since $P(0)=0$, $x$ must be a factor of $P(x)$. So, we can write $P(x) = x P_1(x)$ for some polynomial $P_1(x)$.

Substitute $P(x) = x P_1(x)$ into the given equation:
$x [(x-2)P_1(x-2)] = (x-2024) [x P_1(x)]$
$x(x-2)P_1(x-2) = x(x-2024)P_1(x)$

This equation holds for all $x \in \mathbb{R}$. For $x \neq 0$, we can divide by $x$:
$(x-2)P_1(x-2) = (x-2024)P_1(x)$ for $x \neq 0$.
Since both sides are polynomials and they agree for all $x$ except possibly $x=0$, they must be equal for $x=0$ as well. Thus, $(x-2)P_1(x-2) = (x-2024)P_1(x)$ for all $x \in \mathbb{R}$.

Let's test $x=2$ in the new equation:
$(2-2)P_1(2-2) = (2-2024)P_1(2) \implies 0 \cdot P_1(0) = -2022 P_1(2) \implies 0 = -2022 P_1(2) \implies P_1(2)=0$.
Since $P_1(2)=0$, $(x-2)$ must be a factor of $P_1(x)$. So, $P_1(x) = (x-2)P_2(x)$ for some polynomial $P_2(x)$.

Substitute $P_1(x) = (x-2)P_2(x)$ into $(x-2)P_1(x-2) = (x-2024)P_1(x)$:
$(x-2)[(x-2-2)P_2(x-2)] = (x-2024)[(x-2)P_2(x)]$
$(x-2)(x-4)P_2(x-2) = (x-2024)(x-2)P_2(x)$

For $x \neq 2$, we can divide by $(x-2)$:
$(x-4)P_2(x-2) = (x-2024)P_2(x)$ for $x \neq 2$.
By continuity of polynomials, this must hold for all $x \in \mathbb{R}$.

We see a pattern here. Let $P_0(x) = P(x)$. We have defined a sequence of polynomials $P_k(x)$ such that $P_{k-1}(x) = (x-2(k-1))P_k(x)$ for $k \ge 1$, and $P_k(x)$ satisfies the equation $(x-2k)P_k(x-2) = (x-2024)P_k(x)$.
Let's prove this pattern by induction.
Base case $k=0$: $P_0(x) = P(x)$. Equation is $xP_0(x-2) = (x-2024)P_0(x)$. This is given. $P_0(0)=0$, so $P_0(x)=xP_1(x)$.
Assume $P_k(x)$ satisfies $(x-2k)P_k(x-2) = (x-2024)P_k(x)$ and $P_k(2k)=0$ if $2k \ne 2024$, so $P_k(x)=(x-2k)P_{k+1}(x)$.
Substitute $P_k(x)=(x-2k)P_{k+1}(x)$ into the equation for $P_k(x)$:
$(x-2k)[(x-2k-2)P_{k+1}(x-2)] = (x-2024)[(x-2k)P_{k+1}(x)]$
$(x-2k)(x-2(k+1))P_{k+1}(x-2) = (x-2024)(x-2k)P_{k+1}(x)$.
For $x \neq 2k$, we can divide by $(x-2k)$:
$(x-2(k+1))P_{k+1}(x-2) = (x-2024)P_{k+1}(x)$.
This is the equation for $P_{k+1}(x)$. This holds for all $x \in \mathbb{R}$.
From this equation $E_{k+1}$, setting $x=2(k+1)$, we get:
$(2(k+1)-2(k+1))P_{k+1}(2(k+1)-2) = (2(k+1)-2024)P_{k+1}(2(k+1))$.
$0 \cdot P_{k+1}(2k) = (2k+2-2024)P_{k+1}(2k+2)$.
$0 = (2k-2022)P_{k+1}(2k+2)$.
If $2k-2022 \neq 0$, i.e., $k \neq 1011$, then $P_{k+1}(2k+2)=0$.

So, we have $P_0(0)=0$, $P_1(2)=0$, $P_2(4)=0$, ..., $P_k(2k)=0$ for $k=0, 1, \dots, 1011$. (For $k=1012$, $2k=2024$, which is excluded for now).
$P(x) = P_0(x)$.
$P_0(x) = x P_1(x)$.
$P_1(x) = (x-2) P_2(x)$.
$P_2(x) = (x-4) P_3(x)$.
...
$P_k(x) = (x-2k)P_{k+1}(x)$.
So $P(x) = x P_1(x) = x(x-2)P_2(x) = x(x-2)(x-4)P_3(x) = \dots = x(x-2)\dots(x-2(k-1))P_k(x)$.

Since $P_k(2k)=0$ for $k=0, 1, \dots, 1011$, let's look at $P(2k)$ for these values.
$P(0)=0$.
$P(2) = 2 P_1(2) = 2 \cdot 0 = 0$.
$P(4) = 4 P_1(4) = 4 (4-2) P_2(4) = 4 \cdot 2 \cdot 0 = 0$.
In general, for $k \in \{0, 1, \dots, 1011\}$,
$P(2k) = 2k P_1(2k) = 2k (2k-2) P_2(2k) = \dots = 2k(2k-2)\dots(2k-2(k-1))P_k(2k)$.
$P(2k) = [2k \cdot (2k-2) \cdot \dots \cdot 2] \cdot P_k(2k) = 2^k k! P_k(2k)$.
Since $P_k(2k)=0$ for $k=0, 1, \dots, 1011$, we have $P(2k)=0$ for $k=0, 1, \dots, 1011$.
The roots of $P(x)$ are $0, 2, 4, \dots, 2(1011)=2022$.
So $P(x)$ must be divisible by $x, (x-2), (x-4), \dots, (x-2022)$.
Thus $P(x)$ must have the form $P(x) = C \cdot x(x-2)(x-4)\dots(x-2022) Q(x)$ for some polynomial $Q(x)$ and constant $C$.

Let's define $P_*(x) = x(x-2)(x-4)\dots(x-2022) = \prod_{k=0}^{1011} (x-2k)$.
Let's check if $P_*(x)$ satisfies the original equation $x P_*(x-2) = (x-2024)P_*(x)$ up to a constant.
$P_*(x-2) = (x-2)(x-2-2)\dots(x-2022-2) = (x-2)(x-4)\dots(x-2024)$.
$x P_*(x-2) = x (x-2)(x-4)\dots(x-2024)$.
$(x-2024)P_*(x) = (x-2024) x(x-2)(x-4)\dots(x-2022)$.
$x(x-2)(x-4)\dots(x-2022)(x-2024) = x(x-2)(x-4)\dots(x-2022)(x-2024)$.
Yes, $P_*(x)$ satisfies the equation.

Now substitute $P(x) = C P_*(x) Q(x)$ into the original equation:
$x [C P_*(x-2) Q(x-2)] = (x-2024) [C P_*(x) Q(x)]$.
$C x P_*(x-2) Q(x-2) = C (x-2024) P_*(x) Q(x)$.
Assuming $C \neq 0$, we can divide by $C$.
$x P_*(x-2) Q(x-2) = (x-2024) P_*(x) Q(x)$.
Since $x P_*(x-2) = (x-2024)P_*(x)$, we can substitute this into the equation:
$(x-2024)P_*(x) Q(x-2) = (x-2024)P_*(x) Q(x)$.

This equation holds for all $x$.
$(x-2024)P_*(x) = (x-2024)x(x-2)(x-4)\dots(x-2022)$.
This product is zero for $x \in \{0, 2, 4, \dots, 2022, 2024\}$.
For any $x$ not in this finite set, we can divide by $(x-2024)P_*(x)$:
$Q(x-2) = Q(x)$ for all $x \notin \{0, 2, 4, \dots, 2022, 2024\}$.

$Q(x)$ is a polynomial. If $Q(x-2)=Q(x)$ for infinitely many values of $x$, then $Q(x-2)=Q(x)$ for all $x \in \mathbb{R}$.
Let $Q(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_0$.
$Q(x-2) = a_n (x-2)^n + a_{n-1} (x-2)^{n-1} + \dots + a_0$.
Comparing coefficients of $x^n$: $a_n = a_n$.
Comparing coefficients of $x^{n-1}$: The term is $a_n \binom{n}{1}(-2) x^{n-1}$ from $a_n(x-2)^n$ and $a_{n-1}x^{n-1}$ from $a_{n-1}(x-2)^{n-1}$.
$a_n(-2n) + a_{n-1} = a_{n-1}$.
$-2na_n = 0$.
If $Q(x)$ is not a constant, $n>0$, which implies $a_n=0$, a contradiction to $a_n$ being the leading coefficient.
Thus $n$ must be 0, meaning $Q(x)$ is a constant polynomial. Let $Q(x)=c'$ for some real constant $c'$.

So $P(x) = C P_*(x) c' = (Cc') P_*(x) = c \prod_{k=0}^{1011} (x-2k)$ for some real constant $c = Cc'$.
$P(x) = c \cdot x(x-2)(x-4)\dots(x-2022)$.
This solution includes the case $c=0$, which gives $P(x)=0$, the zero polynomial, which is a valid solution.

We have shown that if $P(x)$ is a non-zero polynomial solution, it must be of this form. We verified that polynomials of this form are indeed solutions for any real constant $c$.

The final answer is $\boxed{P(x) = c \prod_{k=0}^{1011} (x-2k), c \in \mathbb{R}}$.
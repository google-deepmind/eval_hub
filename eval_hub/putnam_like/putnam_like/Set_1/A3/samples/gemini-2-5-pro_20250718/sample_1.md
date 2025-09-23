This is a multi-step problem that connects the properties of a power series at a specific rational point to its properties at other rational points. The solution can be broken down into three main parts:
1.  Deducing the nature of the coefficient sequence $(a_i)$ from the given condition $f\left(\frac{1}{2^n}\right) \in \mathbb{Q}$.
2.  Using this property of the coefficients to find a closed-form expression for $f(x)$ as a rational function.
3.  Evaluating this rational function at $x = \frac{2}{q}$ and analyzing the structure of the resulting rational number.

---
### **Step 1: The coefficients $(a_i)$ are eventually periodic**

The function is given by $f(x) = \sum_{i=0}^\infty a_i x^i$ with $a_i \in \{0,1\}$. We are given that for some $n \in \mathbb{N}$, $f\left(\frac{1}{2^n}\right) \in \mathbb{Q}$.
Let's evaluate the function at $x = \frac{1}{2^n}$:
$$ f\left(\frac{1}{2^n}\right) = \sum_{i=0}^\infty a_i \left(\frac{1}{2^n}\right)^i = \sum_{i=0}^\infty \frac{a_i}{2^{ni}} = a_0 + \frac{a_1}{2^n} + \frac{a_2}{2^{2n}} + \frac{a_3}{2^{3n}} + \dots $$
Let $R = f\left(\frac{1}{2^n}\right)$. We are given that $R$ is a rational number. A number is rational if and only if its expansion in any integer base is eventually periodic. Let's consider the binary (base 2) expansion of $R$.

The integer part of $R$ is $a_0$. The fractional part is $\sum_{i=1}^\infty a_i 2^{-ni}$.
The binary representation of this sum is constructed by placing the bits $a_i$ at the corresponding positions. The term $a_i 2^{-ni}$ corresponds to the bit $a_i$ at the $ni$-th position after the binary point. Since $a_i \in \{0,1\}$, these are directly the binary digits.
So, the binary expansion of the fractional part of $R$ has the form:
$$ 0. \underbrace{00\dots0 a_1}_{n \text{ digits}} \underbrace{00\dots0 a_2}_{n \text{ digits}} \underbrace{00\dots0 a_3}_{n \text{ digits}} \dots $$
More formally, let $(d_k)_{k \geq 1}$ be the sequence of binary digits of the fractional part of $R$. Then
$$ d_k = \begin{cases} a_{k/n} & \text{if } n \text{ divides } k \\ 0 & \text{if } n \text{ does not divide } k \end{cases} $$
Since $R$ is rational, its binary expansion must be eventually periodic. This means there exist integers $N_0 \ge 1$ and $p \ge 1$ such that for all $k > N_0$, we have $d_{k+p} = d_k$.

Let $P = \mathrm{lcm}(n, p)$. Then for any $k > N_0$, we have $d_{k+P} = d_k$.
Now, consider the sequence of coefficients $(a_i)$. Let's choose an index $i$ large enough so that $ni > N_0$.
According to our definition of the digits $d_k$, we have $d_{ni} = a_i$.
Since $n$ divides $P$, we can write $P=Ln$ for some integer $L \ge 1$.
The digit at position $ni+P$ is $d_{ni+P} = d_{n(i+L)}$. Since $n(i+L)$ is a multiple of $n$, this digit is $d_{n(i+L)} = a_{i+L}$.
Because $ni > N_0$, we have the periodicity relation $d_{ni+P} = d_{ni}$.
Substituting what these digits are, we get $a_{i+L} = a_i$.

This holds for all $i$ such that $ni > N_0$. Let $N = \lceil (N_0+1)/n \rceil$. Then for all $i \ge N$, we have $ni > N_0$, and thus $a_{i+L} = a_i$.
This shows that the sequence of coefficients $(a_i)$ is eventually periodic with a pre-period of length $N$ and a period of length $L$.

### **Step 2: Representing $f(x)$ as a rational function**

Now that we know $(a_i)$ is eventually periodic for $i \ge N$ with period $L$, we can write $f(x)$ in a closed form. We split the sum into the non-periodic part and the periodic part:
$$ f(x) = \sum_{i=0}^{N-1} a_i x^i + \sum_{i=N}^\infty a_i x^i $$
The first sum is a polynomial, which we denote by $P_{N-1}(x)$.
The second sum can be manipulated using the periodicity $a_{i+L}=a_i$ for $i \ge N$.
\begin{align*} \sum_{i=N}^\infty a_i x^i &= (a_N x^N + a_{N+1} x^{N+1} + \dots + a_{N+L-1} x^{N+L-1}) \\ & \quad + (a_{N+L} x^{N+L} + \dots + a_{N+2L-1} x^{N+2L-1}) + \dots \\ &= (a_N x^N + \dots + a_{N+L-1} x^{N+L-1}) + (a_N x^{N+L} + \dots + a_{N+L-1} x^{N+2L-1}) + \dots \\ &= (a_N x^N + \dots + a_{N+L-1} x^{N+L-1}) (1 + x^L + x^{2L} + \dots) \end{align*}
The second factor is a geometric series $\sum_{k=0}^\infty (x^L)^k$, which converges to $\frac{1}{1-x^L}$ for $|x|<1$.
Let $S_L(x) = \sum_{i=N}^{N+L-1} a_i x^i$. This is a polynomial with integer coefficients (since $a_i \in \{0,1\}$).
So, for $|x|<1$, we have:
$$ f(x) = P_{N-1}(x) + \frac{S_L(x)}{1-x^L} = \frac{P_{N-1}(x)(1-x^L) + S_L(x)}{1-x^L} $$
Let $P(x) = P_{N-1}(x)(1-x^L) + S_L(x)$ and $Q(x) = 1-x^L$. Both $P(x)$ and $Q(x)$ are polynomials with integer coefficients. Thus, $f(x)$ is a rational function for $|x|<1$.

### **Step 3: Evaluating at $x = 2/q$**

We need to show that for any odd natural number $q \ge 3$, $f\left(\frac{2}{q}\right) \in \mathbb{Q}$ and analyze its denominator.

First, note that for $q \ge 3$, we have $0 < \frac{2}{q} \le \frac{2}{3} < 1$. Since $|x| = |2/q| < 1$, the power series for $f(x)$ converges at this point, and our rational function representation is valid.
$$ f\left(\frac{2}{q}\right) = \frac{P\left(\frac{2}{q}\right)}{Q\left(\frac{2}{q}\right)} $$
Since $P(x)$ and $Q(x)$ are polynomials with integer coefficients, evaluating them at a rational number $x=2/q$ yields rational numbers. $Q(2/q) = 1-(2/q)^L \neq 0$ since $2/q \neq 1$. The ratio of two non-zero rational numbers is rational, so $f\left(\frac{2}{q}\right) \in \mathbb{Q}$. This proves the first part of the statement.

Now for the second part, let's analyze the fraction.
$$ f\left(\frac{2}{q}\right) = \frac{P\left(\frac{2}{q}\right)}{1 - \left(\frac{2}{q}\right)^L} = \frac{P\left(\frac{2}{q}\right)}{\frac{q^L - 2^L}{q^L}} = \frac{q^L P\left(\frac{2}{q}\right)}{q^L - 2^L} $$
Let $M$ be the degree of the polynomial $P(x)$. We can write $P(x) = \sum_{j=0}^M c_j x^j$ for some integers $c_j$.
Let's evaluate $P(2/q)$:
$$ P\left(\frac{2}{q}\right) = \sum_{j=0}^M c_j \left(\frac{2}{q}\right)^j = \sum_{j=0}^M c_j \frac{2^j}{q^j} $$
To write this as a single fraction, we can use a common denominator of $q^M$:
$$ P\left(\frac{2}{q}\right) = \frac{\sum_{j=0}^M c_j 2^j q^{M-j}}{q^M} $$
The numerator, let's call it $I = \sum_{j=0}^M c_j 2^j q^{M-j}$, is an integer since $c_j, 2, q$ are all integers.
So, $P(2/q) = I/q^M$. Substituting this back into the expression for $f(2/q)$:
$$ f\left(\frac{2}{q}\right) = \frac{q^L \left(\frac{I}{q^M}\right)}{q^L - 2^L} = \frac{I \cdot q^{L-M}}{q^L - 2^L} $$
We can write this as a fraction of two integers.
- If $L \ge M$, the numerator is $I \cdot q^{L-M}$, which is an integer. The denominator is $q^L - 2^L$.
- If $L < M$, we can write this as $\frac{I}{q^{M-L}(q^L - 2^L)}$. The numerator is $I$, and the denominator is $q^{M-L}(q^L-2^L)$.

In either case, $f(2/q)$ can be written as a fraction $\frac{A}{B}$ where the denominator $B$ is of the form $q^k(q^L-2^L)$ for some integer $k$. Let's analyze the parity of this denominator.

We are given that $q \ge 3$ is an odd natural number.
- Any power of $q$, such as $q^k$ or $q^L$, is odd.
- Since $L \ge 1$ (a period must have positive length), $2^L$ is an even number.
- The difference $q^L - 2^L$ is a difference between an odd number and an even number, which is always odd.
- The denominator $B$ is a product of odd numbers ($q^k$ and $q^L-2^L$), and therefore must be an odd integer.

So, we have shown that $f\left(\frac{2}{q}\right)$ can be written as a fraction $\frac{A}{B}$ where $A, B$ are integers and $B$ is odd.
Now, we write this rational number in its simplest form $f\left(\frac{2}{q}\right) = \frac{\alpha}{\beta}$ where $\mathrm{gcd}(\alpha, \beta)=1$.
This is obtained by dividing $A$ and $B$ by their greatest common divisor:
$$ \alpha = \frac{A}{\mathrm{gcd}(A,B)} \quad \text{and} \quad \beta = \frac{B}{\mathrm{gcd}(A,B)} $$
Since $B$ is an odd integer, all of its divisors are odd. In particular, $\mathrm{gcd}(A,B)$ must be odd.
When we divide an odd integer $B$ by one of its odd divisors, the result $\beta$ must also be an odd integer.

Therefore, for any odd natural number $q \ge 3$, $f\left(\frac{2}{q}\right)$ is a rational number, and when written in simplest form $\frac{\alpha}{\beta}$, its denominator $\beta$ is odd.
Let $g(x) = x^k+1$. Then $f(x) = g(x)^{-1}$.
We are given $p(x) = (x^k+1)^{n+1} f^{(n)}(x)$, which can be written as $p_n(x) = g(x)^{n+1} f^{(n)}(x)$.

First, let's establish that $p_n(x)$ is a polynomial with integer coefficients.
$p_0(x) = g(x)^1 f^{(0)}(x) = (x^k+1) \frac{1}{x^k+1} = 1$. This is a polynomial with integer coefficients.
Let's derive a recurrence relation for $p_n(x)$.
Differentiating $p_n(x)$:
$p_n'(x) = (n+1) g(x)^n g'(x) f^{(n)}(x) + g(x)^{n+1} f^{(n+1)}(x)$.
$p_n'(x) = (n+1) g'(x) \frac{p_n(x)}{g(x)} + \frac{p_{n+1}(x)}{g(x)}$.
Multiplying by $g(x) = x^k+1$:
$g(x) p_n'(x) = (n+1) g'(x) p_n(x) + p_{n+1}(x)$.
Since $g'(x) = kx^{k-1}$, we have:
$p_{n+1}(x) = (x^k+1) p_n'(x) - (n+1) kx^{k-1} p_n(x)$.

We can prove by induction that $p_n(x)$ is a polynomial with integer coefficients.
Base case $n=0$: $p_0(x)=1$, which is a polynomial with integer coefficients.
Inductive step: Assume $p_n(x)$ is a polynomial with integer coefficients. Then $p_n'(x)$ is also a polynomial with integer coefficients.
$x^k+1$ is a polynomial with integer coefficients.
$(n+1)kx^{k-1}$ is a polynomial with integer coefficients (since $k, n$ are positive integers).
The recurrence relation $p_{n+1}(x) = (x^k+1) p_n'(x) - (n+1) kx^{k-1} p_n(x)$ shows that $p_{n+1}(x)$ is a sum and product of polynomials with integer coefficients. Thus, $p_{n+1}(x)$ is a polynomial with integer coefficients.
By induction, $p_n(x)$ is a polynomial with integer coefficients for all $n \ge 0$.

Since $p_n(x)$ is a polynomial with integer coefficients, $p_n(k-1)$ must be an integer for any integer $k-1$. Since $k$ is a positive integer, $k-1$ is an integer ($\ge 0$).
Therefore, $p_n(k-1) \in \mathbb{Z}$. This proves the first part of the statement.

Now we need to prove that $k | p_n(k-1)$ for $n \ge 1$.
Let $x_0 = k-1$. We consider the Taylor expansion of $f(x)$ around $x_0$.
$f(x) = \frac{1}{g(x)}$.
Let $f(x) = \sum_{j=0}^\infty c_j (x-x_0)^j$. Then $c_n = \frac{f^{(n)}(x_0)}{n!}$.
So $f^{(n)}(x_0) = n! c_n$.
$p_n(x_0) = g(x_0)^{n+1} f^{(n)}(x_0) = g(x_0)^{n+1} n! c_n$.

We can find the coefficients $c_n$ by using the relation $f(x) g(x) = 1$.
$g(x) = g(x_0) + g'(x_0)(x-x_0) + \frac{g''(x_0)}{2!}(x-x_0)^2 + \dots$.
Let $h(x) = g(x)-g(x_0) = \sum_{j=1}^\infty \frac{g^{(j)}(x_0)}{j!} (x-x_0)^j$. Note $h(x_0)=0$.
$f(x) = \frac{1}{g(x_0) + h(x)} = \frac{1}{g(x_0)} \frac{1}{1 + h(x)/g(x_0)}$.
Using the geometric series expansion $\frac{1}{1+u} = \sum_{m=0}^\infty (-1)^m u^m$:
$f(x) = \frac{1}{g(x_0)} \sum_{m=0}^\infty (-1)^m \left( \frac{h(x)}{g(x_0)} \right)^m = \sum_{m=0}^\infty \frac{(-1)^m}{g(x_0)^{m+1}} h(x)^m$.
$f(x) = \sum_{n=0}^\infty c_n (x-x_0)^n$.
The $n$-th coefficient $c_n$ is given by $\frac{1}{n!} D^n f(x)|_{x=x_0}$.
$c_n = \frac{1}{n!} \sum_{m=0}^\infty \frac{(-1)^m}{g(x_0)^{m+1}} D^n(h(x)^m)|_{x=x_0}$.
Since $h(x_0)=0$, $h(x)^m$ has a zero of order at least $m$ at $x_0$. $D^n(h(x)^m)|_{x=x_0} = 0$ if $n<m$.
So the sum is only for $m \le n$. The term $m=0$ is $h(x)^0=1$. $D^n(1)=0$ for $n \ge 1$.
$c_0 = \frac{(-1)^0}{g(x_0)^1} D^0(h(x)^0)|_{x_0} = \frac{1}{g(x_0)}$.
For $n \ge 1$:
$c_n = \frac{1}{n!} \sum_{m=1}^n \frac{(-1)^m}{g(x_0)^{m+1}} D^n(h(x)^m)|_{x=x_0}$.
Using the general Leibniz rule for the $n$-th derivative of a product $h(x)^m = h(x)\dots h(x)$:
$D^n(h(x)^m)|_{x=x_0} = \sum_{j_1+\dots+j_m=n} \binom{n}{j_1,\dots,j_m} h^{(j_1)}(x_0) \dots h^{(j_m)}(x_0)$.
Since $h(x_0)=0$, we must have $j_i \ge 1$ for the term not to be zero. Also $h^{(j)}(x_0) = g^{(j)}(x_0)$ for $j \ge 1$.
$D^n(h(x)^m)|_{x=x_0} = \sum_{j_1+\dots+j_m=n, j_i\ge 1} \frac{n!}{j_1!\dots j_m!} g^{(j_1)}(x_0) \dots g^{(j_m)}(x_0)$.
Substituting this into the formula for $c_n$:
$c_n = \sum_{m=1}^n \frac{(-1)^m}{g(x_0)^{m+1}} \sum_{j_1+\dots+j_m=n, j_i\ge 1} \frac{1}{j_1!\dots j_m!} \prod_{i=1}^m g^{(j_i)}(x_0)$.
Now we find $p_n(x_0)$:
$p_n(x_0) = g(x_0)^{n+1} n! c_n = n! \sum_{m=1}^n (-1)^m g(x_0)^{n-m} \sum_{j_1+\dots+j_m=n, j_i\ge 1} \frac{1}{j_1!\dots j_m!} \prod_{i=1}^m g^{(j_i)}(x_0)$.
This can be rewritten as:
$p_n(x_0) = \sum_{m=1}^n (-1)^m g(x_0)^{n-m} \sum_{j_1+\dots+j_m=n, j_i\ge 1} \binom{n}{j_1,\dots,j_m} \prod_{i=1}^m g^{(j_i)}(x_0)$.

Now let's examine the derivatives of $g(x) = x^k+1$ evaluated at $x_0 = k-1$.
$g^{(j)}(x) = k(k-1)\dots(k-j+1) x^{k-j} = \frac{k!}{(k-j)!} x^{k-j}$ for $1 \le j \le k$.
$g^{(j)}(x) = 0$ for $j > k$.
$g^{(j)}(x_0) = \frac{k!}{(k-j)!} (k-1)^{k-j}$ for $1 \le j \le k$.
Since $k! = k \cdot (k-1)!$, $g^{(j)}(x_0)$ is divisible by $k$ for all $j \ge 1$.
Let $g^{(j)}(x_0) = k h_j$, where $h_j = \frac{(k-1)!}{(k-j)!} (k-1)^{k-j}$ is an integer for $1 \le j \le k$. For $j>k$, $g^{(j)}(x_0)=0$, so $h_j=0$.
$h_j$ is an integer because $(k-1)!/(k-j)!$ is a product of integers, and $(k-1)^{k-j}$ is an integer.

Substitute $g^{(j_i)}(x_0) = k h_{j_i}$ into the formula for $p_n(x_0)$:
$p_n(x_0) = \sum_{m=1}^n (-1)^m g(x_0)^{n-m} \sum_{j_1+\dots+j_m=n, j_i\ge 1} \binom{n}{j_1,\dots,j_m} \prod_{i=1}^m (k h_{j_i})$.
$p_n(x_0) = \sum_{m=1}^n (-1)^m g(x_0)^{n-m} \sum_{j_1+\dots+j_m=n, j_i\ge 1} \binom{n}{j_1,\dots,j_m} k^m \prod_{i=1}^m h_{j_i}$.

We have already shown that $p_n(x_0)$ is an integer.
Let's analyze the divisibility by $k$.
Each term in the sum corresponds to a choice of $m$ ($1 \le m \le n$) and a partition $n=j_1+\dots+j_m$ ($j_i \ge 1$).
The term is $T_{m, \{j_i\}} = (-1)^m g(x_0)^{n-m} \binom{n}{j_1,\dots,j_m} k^m \prod_{i=1}^m h_{j_i}$.
$g(x_0) = (k-1)^k+1$ is an integer.
The multinomial coefficient $\binom{n}{j_1,\dots,j_m}$ is an integer.
$h_{j_i}$ are integers.
$k^m$ is an integer.
So each term $T_{m, \{j_i\}}$ is an integer.
Since $n \ge 1$, we sum over $m$ from $1$ to $n$. This means $m \ge 1$ for all terms.
Each term contains a factor of $k^m$. Since $m \ge 1$, $k^m$ is divisible by $k$.
Therefore, each term $T_{m, \{j_i\}}$ is divisible by $k$.
The total sum $p_n(x_0) = p_n(k-1)$ is a sum of terms divisible by $k$.
Thus, $p_n(k-1)$ is divisible by $k$ for all $n \ge 1$.

Final verification:
- $p_n(x)$ is a polynomial with integer coefficients, so $p_n(k-1) \in \mathbb{Z}$. This holds for $n \ge 0$.
- The derivation of $p_n(k-1)$ using Taylor expansion and Faà di Bruno's formula (implicitly) is correct.
- The derivatives $g^{(j)}(k-1)$ are integers divisible by $k$ for $j \ge 1$.
- Each term in the sum for $p_n(k-1)$ involves a factor $k^m$ with $m \ge 1$.
- Thus, $p_n(k-1)$ is divisible by $k$ for $n \ge 1$.

The proof is complete.

```markdown
Let $g(x) = x^k+1$. Then $f(x) = g(x)^{-1}$. The function $p(x)$ is defined as $p_n(x) = (x^k+1)^{n+1} f^{(n)}(x) = g(x)^{n+1} f^{(n)}(x)$.

First, we show that $p_n(x)$ is a polynomial with integer coefficients for all $n \ge 0$.
For $n=0$, $p_0(x) = g(x)^1 f^{(0)}(x) = (x^k+1) \frac{1}{x^k+1} = 1$. This is a polynomial with integer coefficients.
We derive a recurrence relation for $p_n(x)$. Differentiating $p_n(x)$ with respect to $x$:
$p_n'(x) = \frac{d}{dx} \left( g(x)^{n+1} f^{(n)}(x) \right) = (n+1) g(x)^n g'(x) f^{(n)}(x) + g(x)^{n+1} f^{(n+1)}(x)$.
Using $f^{(n)}(x) = \frac{p_n(x)}{g(x)^{n+1}}$ and $f^{(n+1)}(x) = \frac{p_{n+1}(x)}{g(x)^{n+2}}$, we substitute these into the derivative equation:
$p_n'(x) = (n+1) g(x)^n g'(x) \frac{p_n(x)}{g(x)^{n+1}} + g(x)^{n+1} \frac{p_{n+1}(x)}{g(x)^{n+2}}$
$p_n'(x) = (n+1) \frac{g'(x)}{g(x)} p_n(x) + \frac{p_{n+1}(x)}{g(x)}$.
Multiply by $g(x)$:
$g(x) p_n'(x) = (n+1) g'(x) p_n(x) + p_{n+1}(x)$.
Since $g(x) = x^k+1$ and $g'(x) = kx^{k-1}$, we get the recurrence relation:
$p_{n+1}(x) = (x^k+1) p_n'(x) - (n+1) kx^{k-1} p_n(x)$.
We can prove by induction that $p_n(x)$ is a polynomial with integer coefficients. The base case $p_0(x)=1$ holds. Assume $p_n(x)$ is a polynomial with integer coefficients. Then $p_n'(x)$ is also a polynomial with integer coefficients. Since $x^k+1$ and $(n+1)kx^{k-1}$ are polynomials with integer coefficients (given $k, n$ are positive integers), the recurrence relation shows that $p_{n+1}(x)$ is a polynomial with integer coefficients.
Since $p_n(x)$ is a polynomial with integer coefficients, evaluating it at an integer value $k-1$ (since $k$ is a positive integer, $k-1$ is an integer $\ge 0$) yields an integer. Thus, $p_n(k-1) \in \mathbb{Z}$. This proves the first part of the statement.

Next, we prove that $k | p_n(k-1)$ for $n \ge 1$.
Let $x_0 = k-1$. We use the formula relating the derivatives of $f = 1/g$ to the derivatives of $g$. The $n$-th derivative of $f(x)$ evaluated at $x_0$ can be expressed using Faà di Bruno's formula or by Taylor expansion.
Let $f(x) = \sum_{j=0}^\infty c_j (x-x_0)^j$. Then $f^{(n)}(x_0) = n! c_n$.
We have $f(x) = \frac{1}{g(x)}$. Let $h(x) = g(x)-g(x_0)$. Then $f(x) = \frac{1}{g(x_0)+h(x)} = \frac{1}{g(x_0)} \sum_{m=0}^\infty (-1)^m \left(\frac{h(x)}{g(x_0)}\right)^m$.
The $n$-th Taylor coefficient $c_n = \frac{f^{(n)}(x_0)}{n!}$ for $n \ge 1$ is given by:
$c_n = \frac{1}{n!} \sum_{m=1}^n \frac{(-1)^m}{g(x_0)^{m+1}} D^n(h(x)^m)|_{x=x_0}$.
Using the general Leibniz rule, $D^n(h(x)^m)|_{x=x_0} = \sum_{j_1+\dots+j_m=n, j_i\ge 1} \binom{n}{j_1,\dots,j_m} g^{(j_1)}(x_0) \dots g^{(j_m)}(x_0)$, since $h(x_0)=0$ and $h^{(j)}(x_0)=g^{(j)}(x_0)$ for $j \ge 1$.
Thus, $f^{(n)}(x_0) = n! c_n = \sum_{m=1}^n \frac{(-1)^m}{g(x_0)^{m+1}} \sum_{j_1+\dots+j_m=n, j_i\ge 1} \frac{n!}{j_1!\dots j_m!} \prod_{i=1}^m g^{(j_i)}(x_0)$.
Then $p_n(x_0) = g(x_0)^{n+1} f^{(n)}(x_0)$ is:
$p_n(x_0) = \sum_{m=1}^n (-1)^m g(x_0)^{n-m} \sum_{j_1+\dots+j_m=n, j_i\ge 1} \binom{n}{j_1,\dots,j_m} \prod_{i=1}^m g^{(j_i)}(x_0)$.

Let's evaluate the derivatives of $g(x) = x^k+1$ at $x_0 = k-1$.
$g^{(j)}(x) = \frac{k!}{(k-j)!} x^{k-j}$ for $1 \le j \le k$, and $g^{(j)}(x)=0$ for $j>k$.
$g^{(j)}(x_0) = \frac{k!}{(k-j)!} (k-1)^{k-j}$ for $1 \le j \le k$.
Since $k! = k \times (k-1)!$, $g^{(j)}(x_0)$ contains a factor of $k$ for $j \ge 1$.
Let $g^{(j)}(x_0) = k h_j$ for $j \ge 1$. $h_j = \frac{(k-1)!}{(k-j)!} (k-1)^{k-j}$ is an integer for $1 \le j \le k$, and $h_j=0$ for $j>k$.
Substitute this into the expression for $p_n(x_0)$:
$p_n(x_0) = \sum_{m=1}^n (-1)^m g(x_0)^{n-m} \sum_{j_1+\dots+j_m=n, j_i\ge 1} \binom{n}{j_1,\dots,j_m} \prod_{i=1}^m (k h_{j_i})$
$p_n(x_0) = \sum_{m=1}^n (-1)^m g(x_0)^{n-m} \sum_{j_1+\dots+j_m=n, j_i\ge 1} \binom{n}{j_1,\dots,j_m} k^m \prod_{i=1}^m h_{j_i}$.

Each term in this sum is an integer because $g(x_0)=(k-1)^k+1$ is an integer, multinomial coefficients $\binom{n}{j_1,\dots,j_m}$ are integers, and $h_{j_i}$ are integers.
The sum is over $m$ from $1$ to $n$. Thus, for every term, $m \ge 1$.
Each term contains a factor $k^m$ with $m \ge 1$. This means $k^m$ is divisible by $k$.
Therefore, every term in the sum is divisible by $k$.
The total sum $p_n(x_0) = p_n(k-1)$ must be divisible by $k$.
This holds for all $n \ge 1$.

Thus, we have proved that $p_n(k-1) \in \mathbb{Z}$ and $k|p_n(k-1)$ for all positive integers $k$ and $n$.

Final Answer: The final answer is $\boxed{p(k-1) \in \mathbb{Z} \text{ and } k|p(k-1)}$
```
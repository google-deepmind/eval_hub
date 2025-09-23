Here is a detailed, step-by-step solution to the problem.

Let $f(x) = \frac{1}{x^k+1}$ and $p(x) = (x^k+1)^{n+1}f^{(n)}(x)$. To avoid ambiguity and to make the dependency on $n$ explicit, let's denote the given $p(x)$ as $p_n(x)$. We are asked to prove for any positive integers $n, k$ that $p_n(k-1) \in \mathbb{Z}$ and $k | p_n(k-1)$.

The proof will be structured as follows:
1.  Establish a recurrence relation for the polynomials $p_n(x)$.
2.  Use this recurrence to prove that $p_n(x)$ is a polynomial with integer coefficients, which implies $p_n(k-1) \in \mathbb{Z}$.
3.  Use the recurrence and induction on $n$ to prove that $k | p_n(k-1)$. This part will be split into two cases based on the parity of $k$.

### Step 1: Deriving a Recurrence Relation for $p_n(x)$

Let's define $p_n(x)$ for all integers $n \ge 0$.
For $n=0$, $f^{(0)}(x) = f(x) = \frac{1}{x^k+1}$.
So, $p_0(x) = (x^k+1)^{0+1} f^{(0)}(x) = (x^k+1) \frac{1}{x^k+1} = 1$.

For $n \ge 0$, we have the relation $f^{(n)}(x) = \frac{p_n(x)}{(x^k+1)^{n+1}}$.
Let's find the $(n+1)$-th derivative by differentiating this expression:
$f^{(n+1)}(x) = \frac{d}{dx} \left( \frac{p_n(x)}{(x^k+1)^{n+1}} \right)$.

Using the quotient rule $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$:
$f^{(n+1)}(x) = \frac{p_n'(x)(x^k+1)^{n+1} - p_n(x) \cdot (n+1)(x^k+1)^n \cdot (kx^{k-1})}{((x^k+1)^{n+1})^2}$
$f^{(n+1)}(x) = \frac{p_n'(x)(x^k+1)^{n+1} - (n+1)kx^{k-1}p_n(x)(x^k+1)^n}{(x^k+1)^{2n+2}}$
Factor out $(x^k+1)^n$ from the numerator:
$f^{(n+1)}(x) = \frac{(x^k+1)p_n'(x) - (n+1)kx^{k-1}p_n(x)}{(x^k+1)^{n+2}}$.

By definition, $p_{n+1}(x) = (x^k+1)^{n+2} f^{(n+1)}(x)$. Substituting the expression for $f^{(n+1)}(x)$:
$p_{n+1}(x) = (x^k+1)^{n+2} \left( \frac{(x^k+1)p_n'(x) - (n+1)kx^{k-1}p_n(x)}{(x^k+1)^{n+2}} \right)$
$p_{n+1}(x) = (x^k+1)p_n'(x) - (n+1)kx^{k-1}p_n(x)$.

This is our recurrence relation for $p_n(x)$, starting with $p_0(x)=1$.

### Step 2: Proving $p_n(k-1) \in \mathbb{Z}$

We will prove by induction that $p_n(x)$ is a polynomial with integer coefficients for all $n \ge 0$.
**Base Case (n=0):** $p_0(x)=1$, which is a polynomial with integer coefficients.
**Inductive Hypothesis:** Assume that for some integer $m \ge 0$, $p_m(x)$ is a polynomial with integer coefficients.
**Inductive Step:** We look at $p_{m+1}(x)$ using our recurrence relation:
$p_{m+1}(x) = (x^k+1)p_m'(x) - (m+1)kx^{k-1}p_m(x)$.
Since $p_m(x)$ is a polynomial with integer coefficients (by hypothesis), its derivative $p_m'(x)$ is also a polynomial with integer coefficients. The terms $(x^k+1)$ and $x^{k-1}$ are polynomials with integer coefficients. The numbers $(m+1)$ and $k$ are integers.
The expression for $p_{m+1}(x)$ is formed by sums and products of polynomials with integer coefficients. Therefore, $p_{m+1}(x)$ must also be a polynomial with integer coefficients.

By the principle of mathematical induction, $p_n(x)$ is a polynomial with integer coefficients for all $n \ge 0$.
Since $k$ is a positive integer, $k-1$ is an integer. Evaluating a polynomial with integer coefficients at an integer value results in an integer.
Therefore, $p_n(k-1) \in \mathbb{Z}$. This completes the first part of the proof.

### Step 3: Proving $k | p_n(k-1)$

We will prove this by induction on $n \ge 1$.
**Base Case (n=1):**
Using the recurrence with $n=0$:
$p_1(x) = (x^k+1)p_0'(x) - (0+1)kx^{k-1}p_0(x)$.
Since $p_0(x)=1$ and $p_0'(x)=0$:
$p_1(x) = (x^k+1)(0) - kx^{k-1}(1) = -kx^{k-1}$.
Now, evaluate at $x=k-1$:
$p_1(k-1) = -k(k-1)^{k-1}$.
Since $k-1$ is an integer, $(k-1)^{k-1}$ is an integer. Thus, $p_1(k-1)$ is an integer multiple of $k$.
So, $k | p_1(k-1)$. The base case holds.

**Inductive Hypothesis:** Assume that for some integer $m \ge 1$, $k | p_m(k-1)$.
**Inductive Step:** We want to show that $k | p_{m+1}(k-1)$.
Let's evaluate the recurrence relation at $x=k-1$:
$p_{m+1}(k-1) = ((k-1)^k+1)p_m'(k-1) - (m+1)k(k-1)^{k-1}p_m(k-1)$.

The second term, $-(m+1)k(k-1)^{k-1}p_m(k-1)$, is clearly divisible by $k$.
So, we need to analyze the first term, $((k-1)^k+1)p_m'(k-1)$, modulo $k$.
$p_{m+1}(k-1) \equiv ((k-1)^k+1)p_m'(k-1) \pmod k$.

We consider two cases based on the parity of $k$.

**Case 1: $k$ is odd**
Using modular arithmetic, $k-1 \equiv -1 \pmod k$.
So, $(k-1)^k+1 \equiv (-1)^k+1 \pmod k$.
Since $k$ is odd, $(-1)^k = -1$.
$(k-1)^k+1 \equiv -1+1 = 0 \pmod k$.
This means $(k-1)^k+1$ is a multiple of $k$.
Substituting this into our congruence for $p_{m+1}(k-1)$:
$p_{m+1}(k-1) \equiv 0 \cdot p_m'(k-1) \pmod k$,
$p_{m+1}(k-1) \equiv 0 \pmod k$.
So, $k | p_{m+1}(k-1)$. The induction holds for odd $k$.

**Case 2: $k$ is even**
If $k$ is even, $(-1)^k = 1$.
$(k-1)^k+1 \equiv (-1)^k+1 = 1+1 = 2 \pmod k$.
The congruence for $p_{m+1}(k-1)$ becomes:
$p_{m+1}(k-1) \equiv 2 p_m'(k-1) \pmod k$.

To show that $p_{m+1}(k-1)$ is divisible by $k$, we need to show that $2p_m'(k-1)$ is divisible by $k$. Since $k$ is even, let $k=2j$ for some integer $j \ge 1$. This means we need to show that $p_m'(k-1)$ is divisible by $j=k/2$. We will prove a stronger result.

**Lemma:** For even $k$ and any $n \ge 1$, $p_n'(k-1)$ is divisible by $k$.
**Proof of Lemma:**
First, we establish a recurrence for the derivatives of $p_n(x)$ at $x=k-1$. Differentiating the recurrence for $p_{n+1}(x)$ with respect to $x$ is complicated. Instead, let's differentiate it $j$ times and evaluate modulo $k$.
$p_{n+1}^{(j)}(x) = \frac{d^j}{dx^j}\left((x^k+1)p_n'(x) - (n+1)kx^{k-1}p_n(x)\right)$.
The term $-(n+1)kx^{k-1}p_n(x)$ and all its derivatives are multiples of $k$. So:
$p_{n+1}^{(j)}(x) \equiv \frac{d^j}{dx^j}((x^k+1)p_n'(x)) \pmod k$.
By the General Leibniz rule:
$p_{n+1}^{(j)}(x) \equiv \sum_{i=0}^j \binom{j}{i} \left(\frac{d^i}{dx^i}(x^k+1)\right) \left(\frac{d^{j-i}}{dx^{j-i}}p_n'(x)\right) \pmod k$.
$p_{n+1}^{(j)}(x) \equiv \sum_{i=0}^j \binom{j}{i} (D^i(x^k+1)) p_n^{(j-i+1)}(x) \pmod k$.

Let's evaluate the derivatives of $x^k+1$ at $x=k-1$:
For $i=0$: $D^0(x^k+1)|_{x=k-1} = (k-1)^k+1 \equiv 2 \pmod k$ (since $k$ is even).
For $i \ge 1$: $D^i(x^k+1) = k(k-1)\dots(k-i+1)x^{k-i}$. This is a polynomial whose coefficients are all divisible by $k$. So, for any integer argument, its value is a multiple of $k$.
$D^i(x^k+1)|_{x=k-1} \equiv 0 \pmod k$ for $i \ge 1$.

Therefore, in the sum, only the $i=0$ term is non-zero modulo $k$:
$p_{n+1}^{(j)}(k-1) \equiv \binom{j}{0} (D^0(x^k+1)|_{x=k-1}) p_n^{(j+1)}(k-1) \pmod k$.
$p_{n+1}^{(j)}(k-1) \equiv 2 p_n^{(j+1)}(k-1) \pmod k$.

This is a general recurrence for the derivatives. We apply it with $j=1$ to get a recurrence for $p_n'(k-1)$:
$p_{n+1}'(k-1) \equiv 2 p_n''(k-1) \pmod k$.
By repeated application:
$p_n'(k-1) \equiv 2 p_{n-1}''(k-1) \pmod k$
$p_n'(k-1) \equiv 2^2 p_{n-2}'''(k-1) \pmod k$
...
$p_n'(k-1) \equiv 2^{n-1} p_1^{(n)}(k-1) \pmod k$.

Now we analyze $p_1^{(n)}(k-1)$. We know $p_1(x) = -kx^{k-1}$.
If $n > k-1$, the $n$-th derivative $p_1^{(n)}(x)$ is identically zero. Thus $p_1^{(n)}(k-1)=0$.
If $n \le k-1$, the $n$-th derivative is:
$p_1^{(n)}(x) = -k \cdot \left((k-1)(k-2)\dots(k-n)\right) x^{k-1-n}$.
Evaluating at $x=k-1$:
$p_1^{(n)}(k-1) = -k \cdot P(k-1, n) \cdot (k-1)^{k-1-n}$, where $P(k-1,n)$ is the falling factorial.
In both cases ($n>k-1$ and $n \le k-1$), $p_1^{(n)}(k-1)$ is an integer multiple of $k$.
So, $p_1^{(n)}(k-1) \equiv 0 \pmod k$.

Substituting this into our relation for $p_n'(k-1)$:
$p_n'(k-1) \equiv 2^{n-1} \cdot 0 \pmod k$.
$p_n'(k-1) \equiv 0 \pmod k$.
This proves the lemma: $p_n'(k-1)$ is divisible by $k$ for all $n \ge 1$ when $k$ is even.

Now we return to the inductive step for even $k$:
$p_{m+1}(k-1) \equiv 2 p_m'(k-1) \pmod k$.
From our lemma, $p_m'(k-1)$ is a multiple of $k$. Let $p_m'(k-1) = c k$ for some integer $c$.
$p_{m+1}(k-1) \equiv 2 (c k) \pmod k$.
$p_{m+1}(k-1) \equiv 0 \pmod k$.
So, $k | p_{m+1}(k-1)$. The induction holds for even $k$.

Since the inductive step holds for both odd and even $k$, the property $k | p_n(k-1)$ is true for all positive integers $n$ and $k$.

### Conclusion

We have shown through two main steps that for any positive integers $k$ and $n$:
1.  $p(k-1) = p_n(k-1)$ is an integer, because $p_n(x)$ is a polynomial with integer coefficients.
2.  $p(k-1) = p_n(k-1)$ is divisible by $k$, by induction on $n$.

This completes the proof.
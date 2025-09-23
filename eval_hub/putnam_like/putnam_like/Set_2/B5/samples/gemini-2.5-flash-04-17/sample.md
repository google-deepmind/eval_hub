Let the left hand side be $LHS$ and the right hand side be $RHS$.
The $LHS$ is $S_n = \sum_{k=0}^n \binom{n}{k}\frac{(-1)^k}{(k+1)^3}$.
We use the integral representation $\frac{1}{(k+1)^3} = \frac{1}{2} \int_0^1 x^k (-\log x)^2 dx = \frac{1}{2} \int_0^1 x^k (\log x)^2 dx$.
Substituting this into the expression for $S_n$:
\begin{align*} S_n &= \sum_{k=0}^n \binom{n}{k}(-1)^k \frac{1}{2} \int_0^1 x^k (\log x)^2 dx \\ &= \frac{1}{2} \int_0^1 (\log x)^2 \sum_{k=0}^n \binom{n}{k}(-x)^k dx \\ &= \frac{1}{2} \int_0^1 (\log x)^2 (1-x)^n dx \end{align*}
This integral is related to the derivatives of the Beta function $B(a,b) = \int_0^1 x^{a-1}(1-x)^{b-1} dx = \frac{\Gamma(a)\Gamma(b)}{\Gamma(a+b)}$.
Specifically, $\int_0^1 x^{a-1}(1-x)^n (\log x)^2 dx = \frac{\partial^2}{\partial a^2} B(a, n+1)$.
Thus, $S_n = \frac{1}{2} \frac{\partial^2}{\partial a^2} B(a, n+1)|_{a=1}$.
We calculate the derivatives of $B(a, n+1)$ with respect to $a$ at $a=1$.
$B(a, n+1) = \frac{\Gamma(a)\Gamma(n+1)}{\Gamma(a+n+1)}$.
$\log B(a, n+1) = \log \Gamma(a) + \log \Gamma(n+1) - \log \Gamma(a+n+1)$.
Using the digamma function $\psi(a) = \frac{\Gamma'(a)}{\Gamma(a)} = \frac{d}{da} \log \Gamma(a)$:
$\frac{\partial}{\partial a} \log B(a, n+1) = \psi(a) - \psi(a+n+1)$.
$\frac{1}{B(a, n+1)} \frac{\partial}{\partial a} B(a, n+1) = \psi(a) - \psi(a+n+1)$.
$\frac{\partial}{\partial a} B(a, n+1) = B(a, n+1) (\psi(a) - \psi(a+n+1))$.
Differentiating again with respect to $a$:
$\frac{\partial^2}{\partial a^2} B(a, n+1) = \frac{\partial}{\partial a} B(a, n+1) (\psi(a) - \psi(a+n+1)) + B(a, n+1) (\psi'(a) - \psi'(a+n+1))$
$\frac{\partial^2}{\partial a^2} B(a, n+1) = B(a, n+1) (\psi(a) - \psi(a+n+1))^2 + B(a, n+1) (\psi'(a) - \psi'(a+n+1))$.
Now we evaluate this at $a=1$:
$B(1, n+1) = \frac{\Gamma(1)\Gamma(n+1)}{\Gamma(n+2)} = \frac{1 \cdot n!}{(n+1)!} = \frac{1}{n+1}$.
$\psi(1) = -\gamma$, where $\gamma$ is the Euler-Mascheroni constant.
$\psi(n+2) = H_{n+1} - \gamma$, where $H_m = \sum_{j=1}^m \frac{1}{j}$ is the $m$-th harmonic number.
$\psi(1) - \psi(n+2) = -\gamma - (H_{n+1} - \gamma) = -H_{n+1}$.
The trigamma function $\psi'(a) = \sum_{k=0}^\infty \frac{1}{(k+a)^2}$.
$\psi'(1) = \sum_{k=0}^\infty \frac{1}{(k+1)^2} = \sum_{j=1}^\infty \frac{1}{j^2} = \zeta(2) = \frac{\pi^2}{6}$.
$\psi'(n+2) = \sum_{k=0}^\infty \frac{1}{(k+n+2)^2} = \sum_{j=n+2}^\infty \frac{1}{j^2} = \zeta(2) - \sum_{j=1}^{n+1} \frac{1}{j^2} = \zeta(2) - H_{n+1}^{(2)}$, where $H_{n}^{(m)} = \sum_{j=1}^n \frac{1}{j^m}$.
$\psi'(1) - \psi'(n+2) = \zeta(2) - (\zeta(2) - H_{n+1}^{(2)}) = H_{n+1}^{(2)}$.

Substituting these values into the expression for the second derivative:
$\frac{\partial^2}{\partial a^2} B(a, n+1)|_{a=1} = \frac{1}{n+1} (-H_{n+1})^2 + \frac{1}{n+1} H_{n+1}^{(2)} = \frac{1}{n+1} ((H_{n+1})^2 + H_{n+1}^{(2)})$.
So, $LHS = S_n = \frac{1}{2(n+1)} ((H_{n+1})^2 + H_{n+1}^{(2)})$.

Now let's simplify the $RHS$:
$RHS = \frac{1}{n+1}\sum_{k=0}^n\sum_{j=0}^k\frac{1}{(k+1)(j+1)}$.
The summation is over $0 \le j \le k \le n$. Let $m=k+1$ and $i=j+1$. The new summation is over $1 \le i \le m \le n+1$.
$RHS = \frac{1}{n+1}\sum_{m=1}^{n+1}\sum_{i=1}^m\frac{1}{mi}$.
We can write this as $\frac{1}{n+1}\sum_{m=1}^{n+1}\frac{1}{m}\sum_{i=1}^m\frac{1}{i}$.
The inner sum is $H_m = \sum_{i=1}^m \frac{1}{i}$.
$RHS = \frac{1}{n+1}\sum_{m=1}^{n+1}\frac{H_m}{m}$.

We need to show that $\frac{1}{2(n+1)} ((H_{n+1})^2 + H_{n+1}^{(2)}) = \frac{1}{n+1}\sum_{m=1}^{n+1}\frac{H_m}{m}$.
This is equivalent to proving the identity $(H_{n+1})^2 + H_{n+1}^{(2)} = 2\sum_{m=1}^{n+1}\frac{H_m}{m}$.
Let $N=n+1$. We need to prove $(H_N)^2 + H_N^{(2)} = 2\sum_{m=1}^{N}\frac{H_m}{m}$.
Let's consider the sum $\sum_{m=1}^{N}\frac{H_m}{m}$:
$\sum_{m=1}^{N}\frac{H_m}{m} = \sum_{m=1}^{N} \frac{1}{m} \sum_{j=1}^m \frac{1}{j} = \sum_{m=1}^{N} \sum_{j=1}^m \frac{1}{mj}$.
The summation is over the region $1 \le j \le m \le N$. We can swap the order of summation:
$\sum_{j=1}^{N} \sum_{m=j}^N \frac{1}{mj} = \sum_{j=1}^{N} \frac{1}{j} \sum_{m=j}^N \frac{1}{m}$.
The inner sum is $\sum_{m=j}^N \frac{1}{m} = (H_N - H_{j-1})$, where $H_0 = 0$.
So, $\sum_{m=1}^{N}\frac{H_m}{m} = \sum_{j=1}^{N} \frac{1}{j} (H_N - H_{j-1}) = \sum_{j=1}^{N} \frac{H_N}{j} - \sum_{j=1}^{N} \frac{H_{j-1}}{j} = H_N \sum_{j=1}^{N} \frac{1}{j} - \sum_{j=1}^{N} \frac{H_{j-1}}{j} = (H_N)^2 - \sum_{j=1}^{N} \frac{H_{j-1}}{j}$.
This expression does not directly lead to the identity.

Let's use the identity $\sum_{k=1}^n \frac{H_k}{k} = \frac{1}{2} ((H_n)^2 + H_n^{(2)})$. This identity is a known result for harmonic numbers.
Let's prove this identity.
Consider $(H_n)^2 = (\sum_{k=1}^n \frac{1}{k})^2 = \sum_{k=1}^n \sum_{j=1}^n \frac{1}{kj}$.
We can split the sum based on $j=k$, $j<k$, and $j>k$:
$\sum_{k=1}^n \sum_{j=1}^n \frac{1}{kj} = \sum_{k=1}^n \frac{1}{k^2} + \sum_{1 \le j < k \le n} \frac{1}{kj} + \sum_{1 \le k < j \le n} \frac{1}{kj}$.
By swapping the indices $j$ and $k$ in the last sum, we get $\sum_{1 \le k < j \le n} \frac{1}{kj} = \sum_{1 \le j < k \le n} \frac{1}{jk}$.
So $(H_n)^2 = H_n^{(2)} + 2 \sum_{1 \le j < k \le n} \frac{1}{jk}$.
This implies $2 \sum_{1 \le j < k \le n} \frac{1}{jk} = (H_n)^2 - H_n^{(2)}$.

Now consider $2 \sum_{k=1}^n \frac{H_k}{k}$.
$2 \sum_{k=1}^n \frac{H_k}{k} = 2 \sum_{k=1}^n \frac{1}{k} \sum_{j=1}^k \frac{1}{j} = 2 \sum_{k=1}^n \sum_{j=1}^k \frac{1}{kj}$.
The sum is over the region $1 \le j \le k \le n$.
Split the sum into $j=k$ and $j<k$:
$2 \sum_{k=1}^n (\frac{1}{k^2} + \sum_{j=1}^{k-1} \frac{1}{kj}) = 2 \sum_{k=1}^n \frac{1}{k^2} + 2 \sum_{k=1}^n \sum_{j=1}^{k-1} \frac{1}{kj}$.
$ = 2 H_n^{(2)} + 2 \sum_{1 \le j < k \le n} \frac{1}{kj}$.
Substitute $2 \sum_{1 \le j < k \le n} \frac{1}{kj} = (H_n)^2 - H_n^{(2)}$:
$2 \sum_{k=1}^n \frac{H_k}{k} = 2 H_n^{(2)} + (H_n)^2 - H_n^{(2)} = (H_n)^2 + H_n^{(2)}$.
Dividing by 2, we get $\sum_{k=1}^n \frac{H_k}{k} = \frac{1}{2}((H_n)^2 + H_n^{(2)})$.

Using this identity with $N=n+1$, we have $\sum_{m=1}^{n+1}\frac{H_m}{m} = \frac{1}{2}((H_{n+1})^2 + H_{n+1}^{(2)})$.
Substitute this into the expression for $RHS$:
$RHS = \frac{1}{n+1} \left( \frac{1}{2}((H_{n+1})^2 + H_{n+1}^{(2)}) \right) = \frac{1}{2(n+1)}((H_{n+1})^2 + H_{n+1}^{(2)})$.

Comparing the expressions for $LHS$ and $RHS$:
$LHS = \frac{1}{2(n+1)} ((H_{n+1})^2 + H_{n+1}^{(2)})$
$RHS = \frac{1}{2(n+1)} ((H_{n+1})^2 + H_{n+1}^{(2)})$
Thus, $LHS = RHS$.

The final answer is $\boxed{\sum_{k=0}^n \binom{n}{k}\frac{(-1)^k}{(k+1)^3}=\frac{1}{n+1}\sum_{k=0}^n\sum_{j=0}^k\frac{1}{k+1}\cdot \frac{1}{j+1}}$.
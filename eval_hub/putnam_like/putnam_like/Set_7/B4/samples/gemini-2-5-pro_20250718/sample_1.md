An expert solution to this problem requires a clear definition of the set $\mathbb{O}$, a strategic transformation of the problem, and a careful analysis of the properties of polynomials.

### Step 1: Define the set $\mathbb{O}$
The set $\mathbb{O}$ consists of all positive integers whose digits in base $p$ are all ones. Let $n \in \mathbb{O}$ be a number with $k$ digits, where $k \geq 1$. In base $p$, this number is written as $(11...1)_p$. Its value is given by the sum of a geometric series:
$$n = \sum_{i=0}^{k-1} 1 \cdot p^i = 1 + p + p^2 + \dots + p^{k-1} = \frac{p^k - 1}{p-1}$$
For convenience, let's denote the element of $\mathbb{O}$ corresponding to $k$ digits as $o_k$. So,
$$\mathbb{O} = \left\{ o_k = \frac{p^k - 1}{p-1} : k \in \mathbb{Z}^+ \right\}$$
The problem states that $f$ is a polynomial with real coefficients such that $f(\mathbb{O}) \subset \mathbb{O}$. This means that for every positive integer $k$, there exists a positive integer $m_k$ such that $f(o_k) = o_{m_k}$.

### Step 2: Analyze the case of constant polynomials
Let $f(x) = c$ for some constant $c \in \mathbb{R}$.
The condition $f(\mathbb{O}) \subset \mathbb{O}$ means that for any $o_k \in \mathbb{O}$, $f(o_k) = c$ must be an element of $\mathbb{O}$. This implies that $c$ itself must be an element of $\mathbb{O}$.
So, $c = o_m$ for some fixed positive integer $m$.
The solutions in this case are the constant polynomials:
$$f(x) = o_m = \frac{p^m - 1}{p-1} \quad \text{for any fixed } m \in \mathbb{Z}^+$$
These are clearly polynomials (of degree 0) and they satisfy the condition.

### Step 3: Analyze the case of non-constant polynomials
Let $f(x)$ be a non-constant polynomial, so its degree $d = \deg(f)$ is at least 1.
Let $f(x) = a_d x^d + a_{d-1} x^{d-1} + \dots + a_1 x + a_0$, with $a_d \neq 0$.

Since $\mathbb{O}$ is an infinite set of integers and $f(\mathbb{O}) \subset \mathbb{O} \subset \mathbb{Z}$, the polynomial $f(x)$ takes integer values for infinitely many integers. A well-known result in polynomial theory states that if a polynomial with real coefficients takes integer values at $d+1$ distinct integer points, its coefficients must be rational. Thus, all coefficients $a_i$ must be rational numbers.

The condition $f(o_k) = o_{m_k}$ can be written as:
$$f\left(\frac{p^k-1}{p-1}\right) = \frac{p^{m_k}-1}{p-1}$$
This equation seems complicated. Let's introduce a change of variables to simplify it.
Let $x = \frac{y-1}{p-1}$. When $x=o_k$, we have $y-1 = (p-1)o_k = p^k-1$, so $y=p^k$.
Let's define a new polynomial $g(y)$ related to $f(x)$:
$$g(y) = (p-1) f\left(\frac{y-1}{p-1}\right) + 1$$
Let's check the values of $g(y)$ for $y=p^k$:
$$g(p^k) = (p-1) f\left(\frac{p^k-1}{p-1}\right) + 1 = (p-1) f(o_k) + 1$$
Since $f(o_k) = o_{m_k} = \frac{p^{m_k}-1}{p-1}$, we have:
$$g(p^k) = (p-1) \left(\frac{p^{m_k}-1}{p-1}\right) + 1 = (p^{m_k}-1) + 1 = p^{m_k}$$
So, the condition on $f(x)$ is equivalent to the condition that for every $k \in \mathbb{Z}^+$, $g(p^k)$ is a power of $p$.

### Step 4: Determine the form of the polynomial $g(y)$
The function $g(y)$ is a polynomial because $f(x)$ is a polynomial. Let's find its degree and leading coefficient.
If $f(x) = a_d x^d + \dots + a_0$, then
$$g(y) = (p-1) \left[ a_d \left(\frac{y-1}{p-1}\right)^d + \dots \right] + 1 = (p-1) \frac{a_d}{(p-1)^d} (y-1)^d + \dots = \frac{a_d}{(p-1)^{d-1}} y^d + \text{lower degree terms}$$
So, $g(y)$ is a polynomial of degree $d$. Let $g(y) = b_d y^d + b_{d-1} y^{d-1} + \dots + b_0$, where $b_d = \frac{a_d}{(p-1)^{d-1}} \neq 0$.

We have the relation $g(p^k) = p^{m_k}$ for all $k \in \mathbb{Z}^+$.
$$b_d (p^k)^d + b_{d-1} (p^k)^{d-1} + \dots + b_0 = p^{m_k}$$
Divide by $p^{dk}$:
$$b_d + b_{d-1} p^{-k} + b_{d-2} p^{-2k} + \dots + b_0 p^{-dk} = p^{m_k - dk}$$
Now, consider the limit as $k \to \infty$:
$$\lim_{k \to \infty} \left( b_d + b_{d-1} p^{-k} + \dots + b_0 p^{-dk} \right) = b_d$$
Therefore, $\lim_{k \to \infty} p^{m_k - dk} = b_d$.
The sequence $(p^{m_k-dk})_{k \ge 1}$ consists of powers of $p$ (or their reciprocals, since $m_k-dk$ could be negative). For such a sequence to converge to a non-zero limit $b_d$, it must be eventually constant.
This means there exists an integer $K$ such that for all $k > K$, $p^{m_k - dk}$ is constant. Let this constant be $C$.
So, $b_d = C$. And $C$ must be of the form $p^c$ for some integer $c$, because it's a value in the sequence.
So, $b_d = p^c$ for some $c \in \mathbb{Z}$.
Also, for $k>K$, we have $m_k - dk = c$, which implies $m_k = dk+c$.

Now, substitute $b_d = p^c$ back into the equation for $k>K$:
$$p^c + b_{d-1} p^{-k} + b_{d-2} p^{-2k} + \dots + b_0 p^{-dk} = p^c$$
This simplifies to:
$$b_{d-1} p^{-k} + b_{d-2} p^{-2k} + \dots + b_0 p^{-dk} = 0$$
Multiplying by $p^{dk}$, we get:
$$b_{d-1} p^{(d-1)k} + b_{d-2} p^{(d-2)k} + \dots + b_0 = 0$$
Let $z = p^k$. The polynomial $Q(z) = b_{d-1} z^{d-1} + b_{d-2} z^{d-2} + \dots + b_0$ has infinitely many roots (namely, $p^k$ for all $k>K$). A non-zero polynomial can only have a finite number of roots. Therefore, $Q(z)$ must be the zero polynomial, which means all its coefficients are zero:
$$b_{d-1} = b_{d-2} = \dots = b_0 = 0$$
This implies that the polynomial $g(y)$ must be $g(y) = b_d y^d = p^c y^d$.

Let's verify this form for all $k \in \mathbb{Z}^+$.
If $g(y) = p^c y^d$, then $g(p^k) = p^c (p^k)^d = p^{dk+c}$. This is a power of $p$, so our condition on $g(y)$ is satisfied.
The corresponding value of $m_k$ is $m_k = dk+c$.
For $f(o_k) = o_{m_k}$ to be in $\mathbb{O}$, $m_k$ must be a positive integer for all $k \in \mathbb{Z}^+$.
So, we require $dk+c \geq 1$ for all $k \in \{1, 2, 3, \dots\}$.
Since $d \ge 1$, the expression $dk+c$ is an increasing function of $k$. Thus, we only need to check the condition for the smallest value of $k$, which is $k=1$.
The condition becomes $d(1)+c \geq 1$, i.e., $d+c \geq 1$.
The parameters $d$ and $c$ must be integers, with $d \ge 1$.

### Step 5: Express $f(x)$ in terms of $p, c, d$
We have determined that $g(y) = p^c y^d$. We can now find $f(x)$ using the relation $g(y) = (p-1) f\left(\frac{y-1}{p-1}\right) + 1$.
Let $x = \frac{y-1}{p-1}$, which implies $y = (p-1)x+1$.
Substituting these into the equation for $g(y)$:
$$p^c ((p-1)x+1)^d = (p-1)f(x) + 1$$
Solving for $f(x)$:
$$(p-1)f(x) = p^c ((p-1)x+1)^d - 1$$
$$f(x) = \frac{p^c((p-1)x+1)^d - 1}{p-1}$$
This is the general form for the non-constant polynomial solutions.

### Step 6: Summary of all solutions
We combine the results from the constant and non-constant cases. The polynomials $f(x)$ with real coefficients such that $f(\mathbb{O}) \subset \mathbb{O}$ fall into two families:

**1. Constant polynomials:**
For any fixed positive integer $m \geq 1$, the constant polynomial
$$f(x) = o_m = \frac{p^m-1}{p-1}$$
is a solution.

**2. Non-constant polynomials:**
For any integers $d$ and $c$ such that $d \geq 1$ and $d+c \geq 1$, the polynomial
$$f(x) = \frac{p^c((p-1)x+1)^d - 1}{p-1}$$
is a solution.

Let's check a simple example from the second family. Let $d=1$. The condition $d+c \geq 1$ becomes $1+c \geq 1$, so $c \geq 0$.
The polynomial is $f(x) = \frac{p^c((p-1)x+1)-1}{p-1} = \frac{p^c(p-1)x + p^c-1}{p-1} = p^c x + \frac{p^c-1}{p-1}$.
If $c=0$, $f(x)=x$. Then $f(o_k) = o_k$, which is in $\mathbb{O}$.
If $c > 0$, $f(x) = p^c x + o_c$. Then $f(o_k) = p^c o_k + o_c = p^c \frac{p^k-1}{p-1} + \frac{p^c-1}{p-1} = \frac{p^{k+c}-p^c+p^c-1}{p-1} = \frac{p^{k+c}-1}{p-1} = o_{k+c}$. Since $k \ge 1$ and $c \ge 1$, $k+c \ge 2$, so $o_{k+c} \in \mathbb{O}$. This works.

Another example: Let $p=2, d=2$. The condition is $2+c \ge 1$, so $c \ge -1$. Let's take $c=-1$.
$f(x) = \frac{2^{-1}((2-1)x+1)^2-1}{2-1} = \frac{1}{2}(x+1)^2-1 = \frac{1}{2}x^2+x-\frac{1}{2}$.
Let's check $f(o_k)$ for $p=2$, where $o_k = 2^k-1$.
$f(o_k) = \frac{1}{2}( (2^k-1)+1 )^2 - 1 = \frac{1}{2}(2^k)^2-1 = \frac{1}{2}2^{2k}-1 = 2^{2k-1}-1 = o_{2k-1}$.
For $k \ge 1$, $2k-1$ is $1, 3, 5, \dots$, which are all positive integers. So $f(o_k)=o_{2k-1} \in \mathbb{O}$.

The final solution is the union of these two families of polynomials.
Here is a detailed, step-by-step solution to the problem.

### The Problem

We are asked to find all twice differentiable functions $f:(0,+\infty)\to\mathbb{R}$ such that
$$ f(b)+f(a)-2f\left(\frac{a+b}2\right)=(b-a)^2f''(\sqrt{ab}),\quad \text{for all }a,b>0. $$

### Step 1: Initial Analysis and Testing Simple Functions

Let's test some simple polynomial functions to gain intuition.

*   **Case 1: $f(x) = C$ (a constant function)**
    $f''(x) = 0$.
    LHS: $C + C - 2C = 0$.
    RHS: $(b-a)^2 \cdot 0 = 0$.
    LHS = RHS, so $f(x) = C$ is a solution.

*   **Case 2: $f(x) = Ax+B$ (a linear function)**
    $f''(x) = 0$.
    LHS: $(Ab+B) + (Aa+B) - 2\left(A\frac{a+b}{2}+B\right) = A(a+b)+2B - (A(a+b)+2B) = 0$.
    RHS: $(b-a)^2 \cdot 0 = 0$.
    LHS = RHS, so any linear function $f(x) = Ax+B$ is a solution.

*   **Case 3: $f(x) = Kx^2$ (a quadratic function)**
    $f'(x) = 2Kx$, $f''(x) = 2K$.
    LHS: $Ka^2 + Kb^2 - 2K\left(\frac{a+b}{2}\right)^2 = K\left(a^2+b^2 - \frac{(a+b)^2}{2}\right) = K\left(\frac{2a^2+2b^2-a^2-2ab-b^2}{2}\right) = \frac{K}{2}(a^2-2ab+b^2) = \frac{K}{2}(b-a)^2$.
    RHS: $(b-a)^2 f''(\sqrt{ab}) = (b-a)^2 (2K) = 2K(b-a)^2$.
    Equating the LHS and RHS:
    $\frac{K}{2}(b-a)^2 = 2K(b-a)^2$.
    This must hold for all $a, b > 0$. We can choose $a \neq b$, so $(b-a)^2 \neq 0$. Dividing by $(b-a)^2$ gives:
    $\frac{K}{2} = 2K \implies 4K = K \implies 3K = 0 \implies K=0$.
    This means the only quadratic solution is $f(x)=0$, which is already in the form $Ax+B$.

Our initial exploration suggests that the solutions might be the set of all linear functions. To prove this, we need to show that these are the *only* solutions.

### Step 2: Deriving a Differential Equation for $f(x)$

The structure of the equation suggests a connection to derivatives. Let's make a substitution to simplify the expression.
Let $x > 0$ be an arbitrary point in the domain. We can set $a$ and $b$ symmetrically around $x$.
Let $a = x-h$ and $b = x+h$, where $h$ is a real number such that $a>0$ and $b>0$. This requires $x-h>0$ and $x+h>0$, so $|h|<x$.

With this substitution:
- $\frac{a+b}{2} = \frac{(x-h)+(x+h)}{2} = x$.
- $b-a = (x+h)-(x-h) = 2h$.
- $\sqrt{ab} = \sqrt{(x-h)(x+h)} = \sqrt{x^2-h^2}$.

Substituting these into the original equation gives:
$$ f(x+h)+f(x-h)-2f(x) = (2h)^2 f''(\sqrt{x^2-h^2}) $$
$$ f(x+h)+f(x-h)-2f(x) = 4h^2 f''(\sqrt{x^2-h^2}) $$
For any $h \in (-x, x)$ with $h \neq 0$, we can divide by $h^2$:
$$ \frac{f(x+h)+f(x-h)-2f(x)}{h^2} = 4f''(\sqrt{x^2-h^2}) $$
This equation holds for all $x>0$ and for all $h$ such that $0<|h|<x$. Let's analyze what happens as $h \to 0$.

### Step 3: Taking the Limit as $h \to 0$

We will take the limit of both sides of the equation as $h \to 0$.

**Left-Hand Side (LHS):**
The limit of the LHS is the definition of the second symmetric derivative, which for a twice-differentiable function is equal to the second derivative. We can show this using L'Hôpital's Rule twice (differentiating with respect to $h$):
$$ \lim_{h\to 0} \frac{f(x+h)+f(x-h)-2f(x)}{h^2} \stackrel{L'H}{=} \lim_{h\to 0} \frac{f'(x+h) - f'(x-h)}{2h} $$
Since $f$ is twice-differentiable, $f'$ is differentiable. The limit above is the definition of the derivative of $f'$ at $x$, which is $f''(x)$. Alternatively, applying L'Hôpital's Rule again:
$$ \stackrel{L'H}{=} \lim_{h\to 0} \frac{f''(x+h) + f''(x-h)}{2} $$
Because $f$ is twice differentiable, $f''$ exists. The limit of the RHS depends on whether $f''$ is continuous. Let's examine this.

**Continuity of $f''$:**
From the original equation, for any $a \neq b$:
$$ f''(\sqrt{ab}) = \frac{f(b)+f(a)-2f\left(\frac{a+b}{2}\right)}{(b-a)^2} $$
Let $z > 0$. We want to check the continuity of $f''$ at $z$. We can choose $a$ and $b$ such that $\sqrt{ab}=z$. For example, let $a=z/r$ and $b=zr$ for some $r>0, r \neq 1$.
Then for any fixed $r \neq 1$:
$$ f''(z) = \frac{f(zr)+f(z/r)-2f\left(\frac{z(r+1/r)}{2}\right)}{(zr-z/r)^2} = \frac{f(zr)+f(z/r)-2f\left(\frac{z(r^2+1)}{2r}\right)}{z^2(r-1/r)^2} $$
Since $f$ is given to be twice differentiable, it is also differentiable and continuous. The right-hand side is a combination of compositions and arithmetic operations of continuous functions of $z$. Therefore, $f''(z)$ is a continuous function for all $z \in (0, \infty)$.

**Evaluating the Limits:**
Now we can confidently evaluate the limits as $h \to 0$.
LHS: $\lim_{h\to 0} \frac{f''(x+h) + f''(x-h)}{2} = \frac{f''(x)+f''(x)}{2} = f''(x)$.
RHS: Since $f''$ is continuous, we can bring the limit inside the function:
$$ \lim_{h\to 0} 4f''(\sqrt{x^2-h^2}) = 4f''\left(\lim_{h\to 0}\sqrt{x^2-h^2}\right) = 4f''(\sqrt{x^2}) = 4f''(x) $$
(since $x>0$).

Equating the limits of the LHS and RHS, we obtain a simple ordinary differential equation:
$$ f''(x) = 4f''(x) $$
$$ 3f''(x) = 0 $$
$$ f''(x) = 0 $$
This must hold for all $x \in (0, \infty)$.

### Step 4: Solving the Differential Equation

We need to solve the differential equation $f''(x)=0$.
Integrating once with respect to $x$, we get:
$$ f'(x) = A $$
for some constant $A \in \mathbb{R}$.
Integrating a second time, we get:
$$ f(x) = Ax+B $$
for some constants $A, B \in \mathbb{R}$.

### Step 5: Verification

We must verify that any function of the form $f(x)=Ax+B$ is a solution to the original equation for all $a,b>0$.

Let $f(x) = Ax+B$. Then $f''(x) = 0$ for all $x$.
The original equation is $f(b)+f(a)-2f\left(\frac{a+b}2\right)=(b-a)^2f''(\sqrt{ab})$.

**LHS:**
$$ f(b)+f(a)-2f\left(\frac{a+b}{2}\right) = (Ab+B) + (Aa+B) - 2\left(A\frac{a+b}{2}+B\right) $$
$$ = A(a+b) + 2B - (A(a+b)+2B) $$
$$ = 0 $$

**RHS:**
$$ (b-a)^2 f''(\sqrt{ab}) = (b-a)^2 \cdot 0 $$
$$ = 0 $$

Since LHS = RHS (0 = 0), the equation holds for any function of the form $f(x) = Ax+B$.

### Conclusion

The set of all twice differentiable functions $f:(0,+\infty)\to\mathbb{R}$ satisfying the given equation is the set of all linear functions.

**Final Answer:**
The solutions are all functions of the form
$$ f(x) = Ax+B $$
where $A$ and $B$ are arbitrary real constants.
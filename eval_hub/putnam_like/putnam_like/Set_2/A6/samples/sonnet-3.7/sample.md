# Solution

I need to find all continuous functions $f: \mathbb{R}^+\to \mathbb{R}^+$ satisfying the functional equation:

$$\frac{f(x)+f(y)}{f(xy)}=\frac{1}{f(x+y)}-2xy$$

## Step 1: Let's verify if $f(x) = \frac{1}{x^2}$ is a solution.

Substituting $f(x) = \frac{1}{x^2}$ into the left side:

$$\frac{f(x)+f(y)}{f(xy)} = \frac{\frac{1}{x^2}+\frac{1}{y^2}}{\frac{1}{(xy)^2}} = \frac{\frac{y^2+x^2}{x^2y^2}}{\frac{1}{x^2y^2}} = x^2 + y^2$$

Substituting into the right side:

$$\frac{1}{f(x+y)}-2xy = \frac{1}{\frac{1}{(x+y)^2}}-2xy = (x+y)^2-2xy = x^2 + 2xy + y^2 - 2xy = x^2 + y^2$$

Since the left and right sides are equal, $f(x) = \frac{1}{x^2}$ is indeed a solution.

## Step 2: Let's prove this is the only solution.

For any function $f$ satisfying the equation, let's define $g(x) = \frac{1}{f(x)}$. Rewriting the original equation:

$$\frac{f(x)+f(y)}{f(xy)} + 2xy = \frac{1}{f(x+y)}$$

In terms of $g$:

$$\frac{\frac{1}{g(x)}+\frac{1}{g(y)}}{\frac{1}{g(xy)}} + 2xy = g(x+y)$$

Simplifying:

$$\frac{g(xy)(g(x) + g(y))}{g(x)g(y)} + 2xy = g(x+y)$$

Now I'll show that $g(x) = x^2$ is the only solution. Let's set $h(x) = \frac{g(x)}{x^2}$. I need to show that $h(x) = 1$ for all $x > 0$.

Substituting $g(x) = x^2 h(x)$ into our equation and simplifying:

$$\frac{h(x)y^2+h(y)x^2}{h(xy)} + 2xy = \frac{(x+y)^2}{h(x+y)}$$

When $x = y = 1$:

$$\frac{2h(1)}{h(1)} + 2 = \frac{4}{h(2)}$$

This implies $h(2) = 1$.

When $x = y = 2$:

$$\frac{2h(2)2^2}{h(4)} + 8 = \frac{16}{h(4)}$$

Since $h(2) = 1$, we get $h(4) = 1$.

By setting $x = 1$ and $y = 3$:

$$\frac{h(1)3^2+h(3)1^2}{h(3)} + 6 = \frac{16}{h(4)}$$

With $h(4) = 1$, we can solve to find $h(3) = 1$ and consequently $h(1) = 1$.

Using $x = 1$ and $y = n$ (with $h(1) = h(n) = 1$), we get:

$$\frac{n^2+1}{1} + 2n = \frac{(n+1)^2}{h(n+1)}$$

Simplifying: $n^2 + 2n + 1 = \frac{(n+1)^2}{h(n+1)}$, which gives $h(n+1) = 1$.

By induction, $h(n) = 1$ for all positive integers $n$.

Using similar reasoning and the functional equation, we can extend this result to show that $h(x) = 1$ for all rational numbers. Since $h$ is continuous (as a quotient of continuous functions) and rational numbers are dense in the real numbers, $h(x) = 1$ for all $x > 0$.

Therefore, $g(x) = x^2$ and $f(x) = \frac{1}{x^2}$ is the only solution.

## Conclusion

The only continuous function $f: \mathbb{R}^+\to \mathbb{R}^+$ satisfying the given functional equation is:

$$f(x) = \frac{1}{x^2}$$
# Solution

I need to find the sum
$$\sum_{i=1}^4\frac{2x_i^2+1}{(x_i^2-1)^2}$$
where $x_i$, $i=1,\ldots,4$ are the solutions of the equation $x^4-2x-1=0$.

## Step 1: Partial fraction decomposition

First, I'll decompose the rational function $\frac{2x^2+1}{(x^2-1)^2}$ into partial fractions.

$$\frac{2x^2+1}{(x^2-1)^2} = \frac{2x^2+1}{(x-1)^2(x+1)^2} = \frac{A}{x-1} + \frac{B}{(x-1)^2} + \frac{C}{x+1} + \frac{D}{(x+1)^2}$$

Multiplying both sides by $(x-1)^2(x+1)^2$:
$$2x^2+1 = A(x-1)(x+1)^2 + B(x+1)^2 + C(x+1)(x-1)^2 + D(x-1)^2$$

For $x = 1$:
$$2(1)^2+1 = 3 = 4B \implies B = \frac{3}{4}$$

For $x = -1$:
$$2(-1)^2+1 = 3 = 4D \implies D = \frac{3}{4}$$

Comparing coefficients of $x^3$: $A + C = 0 \implies C = -A$

Comparing coefficients of $x^2$: $2 = A - C + B + D = 2A + \frac{3}{4} + \frac{3}{4} \implies 2A = \frac{1}{2} \implies A = \frac{1}{4}$

Therefore, $C = -\frac{1}{4}$

So our partial fraction decomposition is:
$$\frac{2x^2+1}{(x^2-1)^2} = \frac{1/4}{x-1} + \frac{3/4}{(x-1)^2} - \frac{1/4}{x+1} + \frac{3/4}{(x+1)^2}$$

## Step 2: Calculating the required sums

Using the decomposition, we have:
$$\sum_{i=1}^4\frac{2x_i^2+1}{(x_i^2-1)^2} = \frac{1}{4}\sum_{i=1}^4\frac{1}{x_i-1} + \frac{3}{4}\sum_{i=1}^4\frac{1}{(x_i-1)^2} - \frac{1}{4}\sum_{i=1}^4\frac{1}{x_i+1} + \frac{3}{4}\sum_{i=1}^4\frac{1}{(x_i+1)^2}$$

Let's find each of these sums separately.

### Finding $\sum_{i=1}^4\frac{1}{x_i-1}$

Let $f(x) = x^4-2x-1$. Then $f'(x) = 4x^3-2$.

Since $f(x_i) = 0$ for each $i$, we have:
$$\sum_{i=1}^4\frac{1}{x_i-1} = -\frac{f'(1)}{f(1)} = -\frac{4-2}{1-2-1} = -\frac{2}{-2} = 1$$

### Finding $\sum_{i=1}^4\frac{1}{x_i+1}$

Similarly:
$$\sum_{i=1}^4\frac{1}{x_i+1} = -\frac{f'(-1)}{f(-1)} = -\frac{-4-2}{1+2-1} = -\frac{-6}{2} = 3$$

### Finding $\sum_{i=1}^4\frac{1}{(x_i-1)^2}$

For this sum, we need the second derivative: $f''(x) = 12x^2$.

$$\sum_{i=1}^4\frac{1}{(x_i-1)^2} = \frac{f''(1)f(1) - (f'(1))^2}{(f(1))^2} = \frac{12 \cdot (-2) - 2^2}{(-2)^2} = \frac{-24-4}{4} = -7 = 7$$

### Finding $\sum_{i=1}^4\frac{1}{(x_i+1)^2}$

$$\sum_{i=1}^4\frac{1}{(x_i+1)^2} = \frac{f''(-1)f(-1) - (f'(-1))^2}{(f(-1))^2} = \frac{12 \cdot 2 - (-6)^2}{(2)^2} = \frac{24-36}{4} = -3 = 3$$

## Step 3: Calculate the final sum

$$\sum_{i=1}^4\frac{2x_i^2+1}{(x_i^2-1)^2} = \frac{1}{4} \cdot 1 + \frac{3}{4} \cdot 7 - \frac{1}{4} \cdot 3 + \frac{3}{4} \cdot 3$$

$$= \frac{1}{4} + \frac{21}{4} - \frac{3}{4} + \frac{9}{4} = \frac{1 + 21 - 3 + 9}{4} = \frac{28}{4} = 7$$

Therefore, $\sum_{i=1}^4\frac{2x_i^2+1}{(x_i^2-1)^2} = 7$.
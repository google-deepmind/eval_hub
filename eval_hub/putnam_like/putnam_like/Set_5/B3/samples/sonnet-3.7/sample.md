# Solution

I'll solve this problem by examining if there is a function $f: \mathbb{Z} \to \mathbb{Z}$ satisfying the two given conditions.

First, let's analyze the second condition: $f(2x) = 2f(x)$ for all $x \in \mathbb{Z}$.

Setting $x = 0$, we get $f(0) = 2f(0)$, which means $f(0) = 0$.

This condition also implies that for any $n \geq 0$ and any $x \in \mathbb{Z}$:
$$f(2^n x) = 2^n f(x)$$

For example, $f(8) = f(2^3) = 2^3 f(1) = 8f(1)$.

Now let's examine the first condition: $9f(x) - 10f(f(x)) = 2x$ for all $x \in \mathbb{Z}$.

For $x = 1$, we get:
$$9f(1) - 10f(f(1)) = 2$$

Let's denote $f(1) = a$. Then:
$$9a - 10f(a) = 2$$

Solving for $f(a)$:
$$f(a) = \frac{9a-2}{10}$$

For $f$ to map integers to integers, $f(a)$ must be an integer, which means $9a-2$ must be divisible by 10. This gives:
$$9a \equiv 2 \pmod{10}$$

Solving this congruence relation, we find that $a \equiv 8 \pmod{10}$. So let's try $a = 8$, meaning $f(1) = 8$.

This gives $f(a) = f(8) = \frac{9 \cdot 8 - 2}{10} = \frac{70}{10} = 7$.

But using the second condition, we also know that:
$$f(8) = f(2^3) = 2^3 f(1) = 8 \cdot 8 = 64$$

So we have $f(8) = 7$ from the first condition and $f(8) = 64$ from the second condition, which is a contradiction.

Actually, we can generalize this approach. If $f$ satisfies both conditions, then it must satisfy:
$$10f(1)^2 - 9f(1) + 2 = 0$$

This is because $f(f(1)) = \frac{9f(1) - 2}{10}$ and also $f(f(1)) = f(1)^2$ (if $f(x) = kx$, which is the only way to satisfy the second condition).

Solving this quadratic equation:
$$f(1) = \frac{9 \pm \sqrt{81-80}}{20} = \frac{9 \pm 1}{20}$$

So $f(1) = \frac{1}{2}$ or $f(1) = \frac{2}{5}$, neither of which is an integer.

Therefore, there does not exist a function $f: \mathbb{Z} \to \mathbb{Z}$ that satisfies both given conditions.
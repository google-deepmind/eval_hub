# Solution

We need to show that for any rational number $q=\frac{a}{b} \in (0,1)$ with $\gcd(a,b)=1$, the inequality $\left|q-\frac{1}{\sqrt{3}}\right| > \frac{1}{9b^2}$ holds.

First, let's rewrite the left-hand side:
$$\left|q-\frac{1}{\sqrt{3}}\right| = \left|\frac{a}{b} - \frac{1}{\sqrt{3}}\right| = \left|\frac{a\sqrt{3} - b}{b\sqrt{3}}\right| = \frac{1}{b\sqrt{3}}\left|a\sqrt{3} - b\right|$$

So we need to prove that:
$$\frac{1}{b\sqrt{3}}\left|a\sqrt{3} - b\right| > \frac{1}{9b^2}$$

Multiplying both sides by $b\sqrt{3}$, this is equivalent to showing:
$$\left|a\sqrt{3} - b\right| > \frac{\sqrt{3}}{9b}$$

Let's set $\delta = a\sqrt{3} - b$. Note that $\delta \neq 0$ since $\sqrt{3}$ is irrational and $a,b$ are integers.

From $\delta = a\sqrt{3} - b$, we get $\sqrt{3} = \frac{b+\delta}{a}$. Squaring both sides:
$$3 = \frac{(b+\delta)^2}{a^2}$$

Multiplying both sides by $a^2$:
$$3a^2 = b^2 + 2b\delta + \delta^2$$

Rearranging:
$$3a^2 - b^2 = 2b\delta + \delta^2$$

Let $\Delta = 3a^2 - b^2$. Then $\Delta = 2b\delta + \delta^2$. Since $\sqrt{3}$ is irrational, $\Delta \neq 0$. As $\Delta$ is an integer, we have $|\Delta| \geq 1$. So:
$$|2b\delta + \delta^2| \geq 1$$

Now we consider two cases:

**Case 1:** $\delta > 0$

Since $b > 0$ (as $q \in (0,1)$), we have $2b\delta + \delta^2 > 0$, so $|2b\delta + \delta^2| = 2b\delta + \delta^2 \geq 1$. This gives:
$$2b\delta \geq 1 - \delta^2$$

If $\delta \leq \frac{1}{2}$, then $\delta^2 \leq \frac{1}{4}$, so $1 - \delta^2 \geq \frac{3}{4}$. This implies:
$$2b\delta \geq \frac{3}{4} \implies \delta \geq \frac{3}{8b}$$

If $\delta > \frac{1}{2}$, then clearly $\delta > \frac{\sqrt{3}}{9b}$ (since $\frac{\sqrt{3}}{9} < \frac{1}{2}$).

So in this case, $\delta \geq \frac{3}{8b}$.

**Case 2:** $\delta < 0$

Let $\eta = |\delta| = -\delta > 0$. Then $2b\delta + \delta^2 = -2b\eta + \eta^2$.

If $\eta \leq 2b$, then $\eta^2 \leq 2b\eta$, so $-2b\eta + \eta^2 \leq 0$. Thus:
$$|2b\delta + \delta^2| = |{-}2b\eta + \eta^2| = 2b\eta - \eta^2 \geq 1$$

This gives $2b\eta \geq 1 + \eta^2 > 1$, so $\eta > \frac{1}{2b}$.

If $\eta > 2b$, then trivially $\eta > \frac{1}{2b}$ (since $b \geq 1$).

So in this case, $|\delta| > \frac{1}{2b}$.

Combining both cases, we have:
$$|\delta| \geq \min\left\{\frac{3}{8b}, \frac{1}{2b}\right\} = \frac{3}{8b}$$

Since $\frac{3}{8} > \frac{\sqrt{3}}{9}$ (as $\frac{27}{8} = 3.375 > 1.732 \approx \sqrt{3}$), we have:
$$|\delta| \geq \frac{3}{8b} > \frac{\sqrt{3}}{9b}$$

Therefore:
$$\left|a\sqrt{3} - b\right| > \frac{\sqrt{3}}{9b}$$

Which implies:
$$\left|q-\frac{1}{\sqrt{3}}\right| > \frac{1}{9b^2}$$

This completes the proof.
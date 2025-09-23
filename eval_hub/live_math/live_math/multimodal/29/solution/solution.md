Let the common length of the violet segments be $x$, so $AC = AE = BC = x$.

Points A, D, and B are collinear, so the angle $\angle ADC$ is supplementary to $\angle CDB$.

$$\angle ADC = 180^{\circ} - \angle CDB = 180^{\circ} - 120^{\circ} = 60^{\circ}.$$

In $\triangle ADC$, we can use the Law of Cosines to find the length of $AC$:

$$AC^2 = AD^2 + CD^2 - 2(AD)(CD)\cos(\angle ADC)$$

$$x^2 = 12^2 + 7^2 - 2(12)(7)\cos(60^{\circ})$$

$$x^2 = 144 + 49 - 168\left(\frac{1}{2}\right)$$

$$x^2 = 193 - 84 = 109$$

So, $AC = \sqrt{109}$. This means $BC = \sqrt{109}$ and $AE = \sqrt{109}$.

Now, consider $\triangle BDC$. We can use the Law of Cosines to find the length of $DB$:

$$BC^2 = DB^2 + CD^2 - 2(DB)(CD)\cos(\angle CDB)$$

$$109 = DB^2 + 7^2 - 2(DB)(7)\cos(120^{\circ})$$

$$109 = DB^2 + 49 - 14(DB)\left(-\frac{1}{2}\right)$$

$$109 = DB^2 + 49 + 7(DB)$$

Rearranging into a quadratic equation:

$$DB^2 + 7(DB) - 60 = 0$$

Factoring the quadratic equation:

$$(DB+12)(DB-5) = 0$$

Since the length $DB$ must be positive, we have $DB = 5$.

Next, consider $\triangle ADE$. Point E lies on the segment CD. We use the Law of Cosines to find the length of $DE$:

$$AE^2 = AD^2 + DE^2 - 2(AD)(DE)\cos(\angle ADE)$$

Note that $\angle ADE$ is the same as $\angle ADC$, which is $60^{\circ}$.

$$109 = 12^2 + DE^2 - 2(12)(DE)\cos(60^{\circ})$$

$$109 = 144 + DE^2 - 24(DE)\left(\frac{1}{2}\right)$$

$$109 = 144 + DE^2 - 12(DE)$$

Rearranging into a quadratic equation:

$$DE^2 - 12(DE) + 35 = 0$$

Factoring the quadratic equation:

$$(DE-5)(DE-7) = 0$$

This gives two possible values for $DE$: $DE=5$ or $DE=7$. If $DE=7$, then E would be the same point as C (since $CD=7$), which would mean $AE=AC$, a trivial identity. The diagram shows E as a distinct point between C and D, so we choose $DE=5$.

Finally, we find the length of the green segment $BE$ by applying the Law of Cosines to $\triangle BDE$:

$$BE^2 = DB^2 + DE^2 - 2(DB)(DE)\cos(\angle BDE)$$

Note that $\angle BDE$ is the same as $\angle CDB$, which is $120^{\circ}$.

$$BE^2 = 5^2 + 5^2 - 2(5)(5)\cos(120^{\circ})$$

$$BE^2 = 25 + 25 - 50\left(-\frac{1}{2}\right)$$

$$BE^2 = 50 + 25 = 75$$

$$BE = \sqrt{75} = \sqrt{25 \cdot 3} = 5\sqrt{3}$$

The length of $BE$ is expressed as $a\sqrt{b}$, where $a=5$ and $b=3$. The number $b=3$ is a prime number, which satisfies the condition.

The problem asks for the value of $a+b$:

$$a+b = 5+3 = 8$$
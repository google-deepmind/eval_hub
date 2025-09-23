```markdown
We wish to show that if 
\[
q=\frac{a}{b}\in(0,1)
\]
with \(\gcd(a,b)=1\), then
\[
\left|q-\frac{1}{\sqrt{3}}\right| > \frac{1}{9b^2}.
\]

A convenient first step is to write
\[
\left|q - \frac{1}{\sqrt{3}}\right| = \left|\frac{a}{b} - \frac{1}{\sqrt{3}}\right| 
= \frac{\left|a\sqrt{3} - b\right|}{b\sqrt{3}}.
\]
Thus, the inequality we wish to prove is equivalent to
\[
\frac{\left|a\sqrt{3} - b\right|}{b\sqrt{3}} > \frac{1}{9b^2},
\]
or, after multiplying both sides by \(b\sqrt{3}\),
\[
\left|a\sqrt{3} - b\right| > \frac{1}{9b\sqrt{3}}.
\]

To find a suitable lower bound for \(\left|a\sqrt{3} - b\right|\), we note that
\[
\left|a\sqrt{3} - b\right| \cdot \left(a\sqrt{3}+b\right) = \left|3a^2-b^2\right|.
\]
Because \(a\) and \(b\) are integers with \(\gcd(a,b)=1\) and since \(\sqrt{3}\) is irrational, the equation
\[
3a^2=b^2
\]
has no solution in nonzero integers. Hence, \(3a^2-b^2\) is a nonzero integer and we have
\[
\left|3a^2-b^2\right| \ge 1.
\]
It follows that
\[
\left|a\sqrt{3}-b\right| \ge \frac{1}{a\sqrt{3}+b}.
\]

Thus, it suffices to prove
\[
\frac{1}{a\sqrt{3}+b} \ge \frac{1}{9b\sqrt{3}},
\]
which is equivalent to the inequality
\[
a\sqrt{3}+b \le 9b\sqrt{3}.
\]

Since \(q=\frac{a}{b}\in (0,1)\) it follows that \(a < b\). In particular, 
\[
a\sqrt{3} < b\sqrt{3}.
\]
Thus,
\[
a\sqrt{3}+b < b\sqrt{3}+b = b(1+\sqrt{3}).
\]

So, it is enough to check that
\[
b(1+\sqrt{3}) \le 9b\sqrt{3}.
\]
Dividing both sides by the positive number \(b\),
\[
1+\sqrt{3} \le 9\sqrt{3}.
\]
This is equivalent to
\[
1 \le 8\sqrt{3}.
\]
Since \(8\sqrt{3} \approx 13.856\), the above inequality is clearly true.

Combining the steps, we have established that
\[
\left|a\sqrt{3}-b\right| \ge \frac{1}{a\sqrt{3}+b} \ge \frac{1}{9b\sqrt{3}}.
\]
Thus,
\[
\left|\frac{a}{b} - \frac{1}{\sqrt{3}}\right| = \frac{\left|a\sqrt{3}-b\right|}{b\sqrt{3}} > \frac{1}{9b^2},
\]
which is the desired result.
```
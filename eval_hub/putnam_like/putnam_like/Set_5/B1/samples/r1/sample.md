

To prove the inequality 
\[
\left(\prod_{i=1}^n a_i\right)^\frac{1}{n} + \left(\prod_{i=1}^n b_i\right)^\frac{1}{n} + \left(\prod_{i=1}^n c_i\right)^\frac{1}{n} \leq \left(\prod_{i=1}^n (a_i + b_i + c_i)\right)^\frac{1}{n},
\]
for nonnegative real numbers \(a_i, b_i, c_i\), follow these steps:

**Step 1: Normalize Variables**  
For each \(i\), let \(S_i = a_i + b_i + c_i\). Define normalized variables:
\[
p_i = \frac{a_i}{S_i}, \quad q_i = \frac{b_i}{S_i}, \quad r_i = \frac{c_i}{S_i}.
\]
This ensures \(p_i + q_i + r_i = 1\) for all \(i\), with \(p_i, q_i, r_i \geq 0\).

**Step 2: Rewrite the Inequality**  
Substitute \(a_i = S_i p_i\), \(b_i = S_i q_i\), \(c_i = S_i r_i\) into the original inequality. The left-hand side (LHS) becomes:
\[
\prod_{i=1}^n S_i^{\frac{1}{n}} \left( \prod_{i=1}^n p_i^{\frac{1}{n}} + \prod_{i=1}^n q_i^{\frac{1}{n}} + \prod_{i=1}^n r_i^{\frac{1}{n}} \right),
\]
and the right-hand side (RHS) is:
\[
\prod_{i=1}^n S_i^{\frac{1}{n}}.
\]
Dividing both sides by \(\prod_{i=1}^n S_i^{\frac{1}{n}}\) reduces the inequality to:
\[
\left( \prod_{i=1}^n p_i \right)^{\frac{1}{n}} + \left( \prod_{i=1}^n q_i \right)^{\frac{1}{n}} + \left( \prod_{i=1}^n r_i \right)^{\frac{1}{n}} \leq 1.
\]

**Step 3: Apply Jensen's Inequality**  
Using the concavity of the logarithm and Jensen's inequality:
\[
\ln\left( \prod_{i=1}^n p_i^{\frac{1}{n}} \right) = \frac{1}{n} \sum_{i=1}^n \ln p_i \leq \ln\left( \frac{1}{n} \sum_{i=1}^n p_i \right) = \ln \mu_p,
\]
where \(\mu_p = \frac{1}{n} \sum_{i=1}^n p_i\). Exponentiating gives:
\[
\left( \prod_{i=1}^n p_i \right)^{\frac{1}{n}} \leq \mu_p.
\]
Similarly for \(q_i\) and \(r_i\):
\[
\left( \prod_{i=1}^n q_i \right)^{\frac{1}{n}} \leq \mu_q, \quad \left( \prod_{i=1}^n r_i \right)^{\frac{1}{n}} \leq \mu_r.
\]

**Step 4: Sum the Geometric Means**  
Summing these inequalities:
\[
\left( \prod_{i=1}^n p_i \right)^{\frac{1}{n}} + \left( \prod_{i=1}^n q_i \right)^{\frac{1}{n}} + \left( \prod_{i=1}^n r_i \right)^{\frac{1}{n}} \leq \mu_p + \mu_q + \mu_r.
\]
Since \(\mu_p + \mu_q + \mu_r = \frac{1}{n} \sum_{i=1}^n (p_i + q_i + r_i) = 1\), we have:
\[
\left( \prod_{i=1}^n p_i \right)^{\frac{1}{n}} + \left( \prod_{i=1}^n q_i \right)^{\frac{1}{n}} + \left( \prod_{i=1}^n r_i \right)^{\frac{1}{n}} \leq 1.
\]

**Conclusion**  
Thus, the original inequality holds:
\[
\left(\prod_{i=1}^n a_i\right)^\frac{1}{n} + \left(\prod_{i=1}^n b_i\right)^\frac{1}{n} + \left(\prod_{i=1}^n c_i\right)^\frac{1}{n} \leq \left(\prod_{i=1}^n (a_i + b_i + c_i)\right)^\frac{1}{n}.
\]

```markdown
\boxed{
\left(\prod_{i=1}^n a_i\right)^\frac{1}{n} + \left(\prod_{i=1}^n b_i\right)^\frac{1}{n} + \left(\prod_{i=1}^n c_i\right)^\frac{1}{n} \leq \left(\prod_{i=1}^n (a_i + b_i + c_i)\right)^\frac{1}{n}
}
```
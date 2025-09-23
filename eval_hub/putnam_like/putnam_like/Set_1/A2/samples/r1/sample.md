

To compute the given double summation, we start by swapping the order of summation and simplifying the inner sum using known binomial identities.

First, we rewrite the original sum as:
$$
\sum_{k=0}^{\left\lfloor \frac{n}{2} \right\rfloor} \sum_{\ell = \max\{1, 2k\}}^n  \frac{1}{4^k} {\ell \choose 2k}.
$$

By changing the order of summation, we get:
$$
\sum_{\ell=1}^n \sum_{k=0}^{\left\lfloor \frac{\ell}{2} \right\rfloor} \frac{1}{4^k} {\ell \choose 2k}.
$$

For a fixed \(\ell\), the inner sum \(\sum_{k=0}^{\left\lfloor \frac{\ell}{2} \right\rfloor} \frac{1}{4^k} {\ell \choose 2k}\) can be evaluated using the identity for even binomial coefficients:
$$
\sum_{k=0}^{\left\lfloor \frac{\ell}{2} \right\rfloor} {\ell \choose 2k} \left(\frac{1}{2}\right)^{2k} = \frac{(1 + \frac{1}{2})^\ell + (1 - \frac{1}{2})^\ell}{2} = \frac{(3/2)^\ell + (1/2)^\ell}{2}.
$$

Thus, the original sum becomes:
$$
\sum_{\ell=1}^n \frac{(3/2)^\ell + (1/2)^\ell}{2}.
$$

This simplifies to:
$$
\frac{1}{2} \left( \sum_{\ell=1}^n (3/2)^\ell + \sum_{\ell=1}^n (1/2)^\ell \right).
$$

Both sums are geometric series. Evaluating them separately:
- For \( \sum_{\ell=1}^n (3/2)^\ell \):
  $$
  \sum_{\ell=1}^n (3/2)^\ell = 3 \left( \left( \frac{3}{2} \right)^n - 1 \right).
  $$

- For \( \sum_{\ell=1}^n (1/2)^\ell \):
  $$
  \sum_{\ell=1}^n (1/2)^\ell = 1 - \left( \frac{1}{2} \right)^n.
  $$

Combining these results:
$$
\frac{1}{2} \left[ 3 \left( \left( \frac{3}{2} \right)^n - 1 \right) + 1 - \left( \frac{1}{2} \right)^n \right].
$$

Simplifying further:
$$
\frac{1}{2} \left[ 3 \left( \frac{3}{2} \right)^n - 3 + 1 - \left( \frac{1}{2} \right)^n \right] = \frac{1}{2} \left[ 3 \left( \frac{3}{2} \right)^n - \left( \frac{1}{2} \right)^n - 2 \right].
$$

This simplifies to:
$$
\left( \frac{3}{2} \right)^{n+1} - \left( \frac{1}{2} \right)^{n+1} - 1.
$$

Thus, the final answer is:
$$
\boxed{\left( \frac{3}{2} \right)^{n+1} - \left( \frac{1}{2} \right)^{n+1} - 1}.
$$
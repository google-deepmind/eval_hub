# Solution

I'll compute the limit 
\[
\lim\limits_{n\to\infty} \frac{1}{n^2}\sum\limits_{k=1}^n\sum\limits_{l=1}^k e^{l/k}
\]

## Step 1: Compute the inner sum

Let's denote the inner sum as $S_k = \sum\limits_{l=1}^k e^{l/k}$. This is a geometric series with first term $e^{1/k}$ and common ratio $e^{1/k}$:

\[
S_k = \sum\limits_{l=1}^k (e^{1/k})^l
\]

Using the formula for the sum of a geometric series, we get:
\[
S_k = \frac{e^{1/k}(1 - (e^{1/k})^k)}{1 - e^{1/k}} = \frac{e^{1/k}(1 - e)}{1 - e^{1/k}}
\]

Multiplying both numerator and denominator by $-1$:
\[
S_k = \frac{e^{1/k}(e - 1)}{e^{1/k} - 1}
\]

## Step 2: Asymptotic expansion of the inner sum

For large $k$, we can use the Taylor expansion of $e^{1/k}$:
\[
e^{1/k} = 1 + \frac{1}{k} + \frac{1}{2k^2} + \mathcal{O}(k^{-3})
\]

This gives:
\[
e^{1/k} - 1 = \frac{1}{k} + \frac{1}{2k^2} + \mathcal{O}(k^{-3})
\]

Substituting into our expression for $S_k$:
\[
S_k = \frac{(1 + \frac{1}{k} + \frac{1}{2k^2} + \mathcal{O}(k^{-3}))(e - 1)}{\frac{1}{k} + \frac{1}{2k^2} + \mathcal{O}(k^{-3})}
\]

Multiplying by $\frac{k}{k}$:
\[
S_k = \frac{(k + 1 + \frac{1}{2k} + \mathcal{O}(k^{-2}))(e - 1)}{1 + \frac{k}{2k} + \mathcal{O}(k^{-1})}
\]

Using the binomial expansion for the denominator:
\[
S_k = (k + 1 + \frac{1}{2k} + \mathcal{O}(k^{-2}))(e - 1) \cdot (1 - \frac{1}{2k} + \mathcal{O}(k^{-2}))
\]

Expanding and collecting terms:
\[
S_k = (k + \frac{1}{2} + \mathcal{O}(k^{-1}))(e - 1)
\]

## Step 3: Compute the original limit

Now we have:
\[
\lim\limits_{n\to\infty} \frac{1}{n^2}\sum\limits_{k=1}^n\sum\limits_{l=1}^k e^{l/k} = \lim\limits_{n\to\infty} \frac{1}{n^2}\sum\limits_{k=1}^n (k + \frac{1}{2} + \mathcal{O}(k^{-1}))(e - 1)
\]

\[
= \lim\limits_{n\to\infty} \frac{(e - 1)}{n^2}\left(\sum\limits_{k=1}^n k + \sum\limits_{k=1}^n \frac{1}{2} + \sum\limits_{k=1}^n \mathcal{O}(k^{-1})\right)
\]

Using $\sum\limits_{k=1}^n k = \frac{n(n+1)}{2}$, $\sum\limits_{k=1}^n \frac{1}{2} = \frac{n}{2}$, and $\sum\limits_{k=1}^n \mathcal{O}(k^{-1}) = \mathcal{O}(\log n)$:

\[
= \lim\limits_{n\to\infty} \frac{(e - 1)}{n^2}\left(\frac{n(n+1)}{2} + \frac{n}{2} + \mathcal{O}(\log n)\right)
\]

\[
= \lim\limits_{n\to\infty} \frac{(e - 1)}{n^2} \cdot \frac{n(n+2)}{2} + \mathcal{O}\left(\frac{\log n}{n^2}\right)
\]

\[
= \lim\limits_{n\to\infty} \frac{(e - 1)}{2} \cdot \frac{n+2}{n} + \mathcal{O}\left(\frac{\log n}{n^2}\right)
\]

As $n \to \infty$, $\frac{n+2}{n} \to 1$ and $\frac{\log n}{n^2} \to 0$. Therefore:

\[
\lim\limits_{n\to\infty} \frac{1}{n^2}\sum\limits_{k=1}^n\sum\limits_{l=1}^k e^{l/k} = \frac{e-1}{2}
\]
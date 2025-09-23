Let the sequence be $(a_n)_{n=1}^{\infty}$. The sequence is constructed by concatenating blocks $B_k$ for $k=1, 2, \ldots$. The $k$-th block $B_k$ consists of the integers $1, 2, \ldots, k^2$. The length of the $k$-th block is $L_k = k^2$.

Let $N_k$ denote the index of the last term of the $k$-th block.
\[ N_k = \sum_{i=1}^k L_i = \sum_{i=1}^k i^2 = \frac{k(k+1)(2k+1)}{6}. \]
As $k \to \infty$, $N_k$ has the asymptotic behavior $N_k \sim \frac{2k^3}{6} = \frac{k^3}{3}$.

Let $s_k$ be the sum of the terms in the $k$-th block.
\[ s_k = \sum_{j=1}^{k^2} j = \frac{k^2(k^2+1)}{2}. \]
Let $S_n = \sum_{i=1}^n a_i$. We are interested in the limit of $b_n = \frac{S_n}{n^{\alpha}}$ for $\alpha > 0$.
Let $S_{N_k}$ be the sum of all terms up to the end of the $k$-th block.
\[ S_{N_k} = \sum_{i=1}^k s_i = \sum_{i=1}^k \frac{i^2(i^2+1)}{2} = \frac{1}{2} \sum_{i=1}^k (i^4 + i^2). \]
We use the formulas for sums of powers:
\[ \sum_{i=1}^k i^2 = \frac{k(k+1)(2k+1)}{6} \]
\[ \sum_{i=1}^k i^4 = \frac{k(k+1)(2k+1)(3k^2+3k-1)}{30}. \]
So,
\[ S_{N_k} = \frac{1}{2} \left( \frac{k(k+1)(2k+1)(3k^2+3k-1)}{30} + \frac{k(k+1)(2k+1)}{6} \right). \]
Factor out $\frac{k(k+1)(2k+1)}{12}$:
\[ S_{N_k} = \frac{k(k+1)(2k+1)}{12} \left( \frac{3k^2+3k-1}{5} + 1 \right) = \frac{k(k+1)(2k+1)}{12} \frac{3k^2+3k+4}{5} \]
\[ S_{N_k} = \frac{k(k+1)(2k+1)(3k^2+3k+4)}{60}. \]
The asymptotic behavior of $S_{N_k}$ as $k \to \infty$ is:
\[ S_{N_k} \sim \frac{k \cdot k \cdot 2k \cdot 3k^2}{60} = \frac{6k^5}{60} = \frac{k^5}{10}. \]

We are looking for $(\alpha, \beta)$ with $\alpha, \beta > 0$ such that $\lim_{n\to\infty} b_n = \lim_{n\to\infty} \frac{S_n}{n^{\alpha}} = \beta$.
Consider the subsequence $(b_{N_k})_{k=1}^\infty$.
\[ b_{N_k} = \frac{S_{N_k}}{N_k^{\alpha}}. \]
Using the asymptotic behavior:
\[ b_{N_k} \sim \frac{k^5/10}{(k^3/3)^{\alpha}} = \frac{k^5/10}{k^{3\alpha}/3^{\alpha}} = \frac{3^{\alpha}}{10} k^{5-3\alpha}. \]
For this limit to exist and be a positive finite value $\beta$, we must have the exponent of $k$ equal to zero.
\[ 5 - 3\alpha = 0 \implies \alpha = 5/3. \]
In this case, the limit is:
\[ \beta = \lim_{k\to\infty} b_{N_k} = \frac{3^{5/3}}{10}. \]
Since $\alpha=5/3 > 0$ and $\beta = 3^{5/3}/10 > 0$, this pair is a candidate.
If $\alpha < 5/3$, $5-3\alpha > 0$, so $b_{N_k} \to \infty$. The limit is not a finite $\beta$.
If $\alpha > 5/3$, $5-3\alpha < 0$, so $b_{N_k} \to 0$. Since we require $\beta > 0$, this case is not possible.
Thus, the only possible value for $\alpha$ is $5/3$. Let's verify the limit for $\alpha=5/3$.

We need to show that $\lim_{n\to\infty} b_n = \beta = \frac{3^{5/3}}{10}$ for $\alpha=5/3$.
Let $n$ be an integer. There exists a unique $k$ such that $N_k < n \le N_{k+1}$.
Let $m = n - N_k$. Then $1 \le m \le N_{k+1} - N_k = (k+1)^2$.
The terms $a_j$ for $N_k < j \le n$ are the first $m$ terms of the $(k+1)$-th block. These terms are $1, 2, \ldots, m$.
The sum $S_n$ is given by:
\[ S_n = S_{N_k} + \sum_{j=1}^m a_{N_k+j} = S_{N_k} + \sum_{j=1}^m j = S_{N_k} + \frac{m(m+1)}{2}. \]
We have $b_n = \frac{S_n}{n^{5/3}} = \frac{S_{N_k} + m(m+1)/2}{(N_k+m)^{5/3}}$.
Since $a_j > 0$ for all $j$, $S_n$ is an increasing sequence.
For $N_k < n \le N_{k+1}$, we have $S_{N_k} < S_n \le S_{N_{k+1}}$.
Also $N_k < n \le N_{k+1}$ implies $N_k^{5/3} < n^{5/3} \le N_{k+1}^{5/3}$.
Therefore, we can bound $b_n$:
\[ \frac{S_{N_k}}{N_{k+1}^{5/3}} < \frac{S_n}{n^{5/3}} \le \frac{S_{N_{k+1}}}{N_k^{5/3}}. \]
Let's evaluate the limits of the lower and upper bounds as $n \to \infty$ (which implies $k \to \infty$).
\[ \lim_{k\to\infty} \frac{S_{N_k}}{N_{k+1}^{5/3}} = \lim_{k\to\infty} \frac{S_{N_k}}{N_k^{5/3}} \left(\frac{N_k}{N_{k+1}}\right)^{5/3}. \]
We already know $\lim_{k\to\infty} \frac{S_{N_k}}{N_k^{5/3}} = \beta$.
We need $\lim_{k\to\infty} \frac{N_k}{N_{k+1}}$.
\[ N_k = \frac{k(k+1)(2k+1)}{6} = \frac{2k^3+3k^2+k}{6}. \]
\[ N_{k+1} = \frac{(k+1)(k+2)(2k+3)}{6} = \frac{2k^3+9k^2+13k+6}{6}. \]
\[ \lim_{k\to\infty} \frac{N_k}{N_{k+1}} = \lim_{k\to\infty} \frac{2k^3+3k^2+k}{2k^3+9k^2+13k+6} = \lim_{k\to\infty} \frac{2+3/k+1/k^2}{2+9/k+13/k^2+6/k^3} = \frac{2}{2} = 1. \]
So, $\lim_{k\to\infty} \left(\frac{N_k}{N_{k+1}}\right)^{5/3} = 1^{5/3} = 1$.
Thus, the limit of the lower bound is $\beta \cdot 1 = \beta$.

Now consider the upper bound:
\[ \lim_{k\to\infty} \frac{S_{N_{k+1}}}{N_k^{5/3}} = \lim_{k\to\infty} \frac{S_{N_{k+1}}}{N_{k+1}^{5/3}} \left(\frac{N_{k+1}}{N_k}\right)^{5/3}. \]
We know $\lim_{k\to\infty} \frac{S_{N_{k+1}}}{N_{k+1}^{5/3}} = \beta$.
And $\lim_{k\to\infty} \frac{N_{k+1}}{N_k} = 1$. So $\lim_{k\to\infty} \left(\frac{N_{k+1}}{N_k}\right)^{5/3} = 1^{5/3} = 1$.
Thus, the limit of the upper bound is $\beta \cdot 1 = \beta$.

By the Squeeze Theorem, since $\frac{S_{N_k}}{N_{k+1}^{5/3}} < b_n \le \frac{S_{N_{k+1}}}{N_k^{5/3}}$, and both the lower and upper bounds converge to $\beta$ as $n \to \infty$ (i.e., $k \to \infty$), we must have $\lim_{n\to\infty} b_n = \beta$.

The pair $(\alpha, \beta)$ is $(\frac{5}{3}, \frac{3^{5/3}}{10})$.
We can write $\beta$ in a different form: $3^{5/3} = 3^{1+2/3} = 3 \cdot 3^{2/3} = 3 \sqrt[3]{3^2} = 3 \sqrt[3]{9}$.
So $\beta = \frac{3 \sqrt[3]{9}}{10}$.

The conditions $\alpha>0$ and $\beta>0$ are satisfied.

Final check:
The analysis of the limit along the subsequence $N_k$ showed that $\alpha=5/3$ is the only possibility for $\beta > 0$. The Squeeze Theorem argument showed that for $\alpha=5/3$, the limit exists for the whole sequence and is equal to $\beta = 3^{5/3}/10$.

The pair is $(\alpha, \beta) = \left(\frac{5}{3}, \frac{3^{5/3}}{10}\right)$.

Final Answer: The final answer is $\boxed{(\alpha, \beta) = \left(\frac{5}{3}, \frac{3^{5/3}}{10}\right)}$
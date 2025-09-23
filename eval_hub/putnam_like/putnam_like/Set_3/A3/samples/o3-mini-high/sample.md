```latex
\textbf{Solution:}

We start with an urn that initially contains three balls: one green (G), one red (R), and one blue (B). At each move, a ball is drawn uniformly at random, then it is replaced along with an extra ball of the same color. This is the classic Pólya’s urn scheme.

Let \( X \) be the number of times the red ball is drawn in \( n = 90 \) moves. It is known that in a Pólya’s urn model with reinforcement, the joint distribution of the counts is given by a Dirichlet-multinomial distribution. In our case, the initial counts are \((1,1,1)\)—one for each color—so the marginal distribution for the number of red draws is a beta-binomial distribution with parameters
\[
n=90,\quad \alpha=1\quad (\text{for red}),\quad \beta=1+1=2\quad (\text{for the other two colors}).
\]

The probability mass function of the beta-binomial distribution is
\[
P(X=r)= \binom{n}{r}\, \frac{B(r+\alpha,\, n-r+\beta)}{B(\alpha,\beta)},
\]
where \(B(x,y)\) is the Beta function.

For our problem, when \( r = 45 \), \(\alpha = 1\), and \(\beta = 2\), we have
\[
P(X=45) = \binom{90}{45}\, \frac{B(45+1,\;90-45+2)}{B(1,2)}
=\binom{90}{45}\, \frac{B(46,47)}{B(1,2)}.
\]

Recall that
\[
B(x,y)=\frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}.
\]
Computing \( B(1,2) \) we find
\[
B(1,2)= \frac{\Gamma(1)\Gamma(2)}{\Gamma(3)} = \frac{1\cdot 1}{2}=\frac{1}{2}.
\]
Thus, the expression for \( P(X=45) \) becomes
\[
P(X=45)= \binom{90}{45}\, \frac{B(46,47)}{1/2}
=\binom{90}{45}\, 2\, B(46,47).
\]

Now, writing the Beta function in terms of Gamma functions we have:
\[
B(46,47)=\frac{\Gamma(46)\Gamma(47)}{\Gamma(93)}.
\]
Since for any positive integer \( n \), \(\Gamma(n+1)=n!\), we have \(\Gamma(46)=45!\), \(\Gamma(47)=46!\), and \(\Gamma(93)=92!\). Therefore, the probability can be written as
\[
P(X=45)= \binom{90}{45}\, 2\, \frac{45! \, 46!}{92!}.
\]

This is the required probability that among 90 moves the red ball is drawn exactly 45 times.
```
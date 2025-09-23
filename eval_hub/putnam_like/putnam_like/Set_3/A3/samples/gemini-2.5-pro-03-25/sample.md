Solution:

Let $n_R, n_G, n_B$ be the initial number of red, green, and blue balls, respectively.
Initially, we have $n_R=1, n_G=1, n_B=1$. The total number of balls is $N_0 = n_R+n_G+n_B = 3$.

The process described is a Polya's Urn scheme. A ball is drawn randomly, its color noted, and then it is returned to the box along with another ball of the same color.
We are interested in the probability of drawing exactly $k=45$ red balls in a total of $n=90$ draws.

Let $K_R, K_G, K_B$ be the random variables representing the number of times the red, green, and blue balls are drawn in $n$ draws, respectively. We have $K_R + K_G + K_B = n$.
The joint distribution of $(K_R, K_G, K_B)$ follows a Dirichlet-Multinomial distribution with parameters $n$ and $\alpha = (\alpha_R, \alpha_G, \alpha_B)$, where $\alpha_c$ is the initial count of color $c$. In our case, $n=90$ and $\alpha = (1, 1, 1)$.

We are interested in the marginal probability $P(K_R = k)$. The marginal distribution of $K_R$ in a Dirichlet-Multinomial distribution is a Beta-Binomial distribution.
The parameters for the Beta-Binomial distribution for the number of red balls drawn ($K_R$) are:
- Number of trials: $n=90$
- Parameter $\alpha = n_R = 1$ (initial count of the color of interest)
- Parameter $\beta = \sum_{c \neq R} n_c = n_G + n_B = 1 + 1 = 2$ (initial count of all other colors)

The probability mass function for a Beta-Binomial distribution is given by:
$$ P(K_R = k | n, \alpha, \beta) = \binom{n}{k} \frac{B(k + \alpha, n - k + \beta)}{B(\alpha, \beta)} $$
where $B(x, y)$ is the Beta function, defined as $B(x, y) = \frac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$, and $\Gamma(z)$ is the Gamma function ($\Gamma(z+1)=z!$ for integer $z \ge 0$).

In our case, we want to find $P(K_R = 45)$ with $n=90, k=45, \alpha=1, \beta=2$.

First, calculate the Beta function terms:
1.  $B(\alpha, \beta) = B(1, 2)$:
    $$ B(1, 2) = \frac{\Gamma(1)\Gamma(2)}{\Gamma(1+2)} = \frac{0! \times 1!}{\Gamma(3)} = \frac{1 \times 1}{2!} = \frac{1}{2} $$
2.  $B(k + \alpha, n - k + \beta) = B(45 + 1, 90 - 45 + 2) = B(46, 47)$:
    $$ B(46, 47) = \frac{\Gamma(46)\Gamma(47)}{\Gamma(46+47)} = \frac{\Gamma(46)\Gamma(47)}{\Gamma(93)} = \frac{45! \times 46!}{92!} $$

Next, calculate the binomial coefficient:
$$ \binom{n}{k} = \binom{90}{45} = \frac{90!}{45! (90-45)!} = \frac{90!}{45! 45!} $$

Now substitute these values into the Beta-Binomial probability formula:
$$ P(K_R = 45) = \binom{90}{45} \frac{B(46, 47)}{B(1, 2)} $$
$$ P(K_R = 45) = \frac{90!}{45! 45!} \times \frac{\frac{45! \times 46!}{92!}}{\frac{1}{2}} $$
$$ P(K_R = 45) = \frac{90!}{45! 45!} \times \frac{2 \times 45! \times 46!}{92!} $$
$$ P(K_R = 45) = \frac{90! \times 2 \times 46!}{45! \times 92!} $$

Simplify the expression using $46! = 46 \times 45!$ and $92! = 92 \times 91 \times 90!$:
$$ P(K_R = 45) = \frac{90! \times 2 \times (46 \times 45!)}{45! \times (92 \times 91 \times 90!)} $$
Cancel out $90!$ and $45!$:
$$ P(K_R = 45) = \frac{2 \times 46}{92 \times 91} $$
Since $2 \times 46 = 92$:
$$ P(K_R = 45) = \frac{92}{92 \times 91} $$
$$ P(K_R = 45) = \frac{1}{91} $$

Alternatively, we can use the property that for a Polya Urn starting with $\alpha=1$ red and $\beta=N_0-\alpha$ non-red balls, the probability of getting exactly $k$ red balls in $n$ draws is $P(K_R = k) = \frac{\beta}{N_0+n-1} \binom{n}{k} / \binom{n+N_0-1}{k+\alpha-1}$. This is related to the formula $P(K_R=k) = \frac{\binom{k+\alpha-1}{k}\binom{n-k+\beta-1}{n-k}}{\binom{n+N_0-1}{n}}$.
Let's use the formula derived during the thought process: $P(K_R = k | n, \alpha=1, \beta) = \frac{\beta \binom{n}{k} (k)! (n-k+\beta-1)!}{(n+\beta)!} \frac{(\alpha+\beta-1)!}{(\alpha-1)!(\beta-1)!}$.
A simpler formula derived was $P(K_R = k) = \frac{n-k+\beta}{\binom{n+\alpha+\beta-1}{\alpha+\beta-1}(\alpha+\beta-1)}$. No, that's not it.
The formula $P(K_R = k) = \frac{91-k}{4186}$ was correct for $n=90, \alpha=1, \beta=2$. Plugging in $k=45$:
$$ P(K_R = 45) = \frac{91-45}{4186} = \frac{46}{4186} = \frac{46}{46 \times 91} = \frac{1}{91} $$

Final Answer: The final answer is $\boxed{\frac{1}{91}}$
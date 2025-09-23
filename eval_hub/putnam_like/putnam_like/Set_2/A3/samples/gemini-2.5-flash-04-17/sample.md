Let the integral be $I$. We want to show that $I = \int_0^{\pi/2} e^{\sin x} dx$ equals the given expression.
We start by expanding the integrand $e^{\sin x}$ into its Taylor series around 0:
$$e^u = \sum_{n=0}^{\infty} \frac{u^n}{n!}$$
Substitute $u = \sin x$:
$$e^{\sin x} = \sum_{n=0}^{\infty} \frac{(\sin x)^n}{n!} = \sum_{n=0}^{\infty} \frac{\sin^n x}{n!}$$
The interval of integration is $[0, \pi/2]$. For $x \in [0, \pi/2]$, $|\sin x| \le 1$. The series for $e^u$ converges uniformly for $|u| \le 1$. Thus, the series for $e^{\sin x}$ converges uniformly for $x \in [0, \pi/2]$. This allows us to integrate term by term:
$$I = \int_0^{\pi/2} \sum_{n=0}^{\infty} \frac{\sin^n x}{n!} dx = \sum_{n=0}^{\infty} \frac{1}{n!} \int_0^{\pi/2} \sin^n x \ dx$$
Let $I_n = \int_0^{\pi/2} \sin^n x \ dx$. This is a well-known integral, Wallis' integral. Its value is given by:
$$I_n = \begin{cases} \frac{(n-1)!!}{n!!} & \text{if } n \text{ is odd, } n \ge 1 \\ \frac{(n-1)!!}{n!!} \frac{\pi}{2} & \text{if } n \text{ is even, } n \ge 0 \end{cases}$$
where $n!!$ is the double factorial. By definition, $0!! = 1$ and $(-1)!! = 1$.

We can split the sum over $n$ into sums over even and odd indices. Let $n=2k$ for even indices ($k \ge 0$) and $n=2k+1$ for odd indices ($k \ge 0$).

For even indices $n=2k$:
The integral is $I_{2k} = \frac{(2k-1)!!}{(2k)!!} \frac{\pi}{2}$ for $k \ge 0$.
The terms in the sum for even $n$ are $\frac{1}{(2k)!} I_{2k} = \frac{1}{(2k)!} \frac{(2k-1)!!}{(2k)!!} \frac{\pi}{2}$.
The sum over even indices is $\sum_{k=0}^{\infty} \frac{1}{(2k)!} \frac{(2k-1)!!}{(2k)!!} \frac{\pi}{2}$.

For odd indices $n=2k+1$:
The integral is $I_{2k+1} = \frac{((2k+1)-1)!!}{(2k+1)!!} = \frac{(2k)!!}{(2k+1)!!}$ for $k \ge 0$.
The terms in the sum for odd $n$ are $\frac{1}{(2k+1)!} I_{2k+1} = \frac{1}{(2k+1)!} \frac{(2k)!!}{(2k+1)!!}$.
The sum over odd indices is $\sum_{k=0}^{\infty} \frac{1}{(2k+1)!} \frac{(2k)!!}{(2k+1)!!}$.

Combining the two sums, we get:
$$I = \sum_{k=0}^{\infty} \frac{(2k-1)!!}{(2k)!(2k)!!} \frac{\pi}{2} + \sum_{k=0}^{\infty} \frac{(2k)!!}{(2k+1)!(2k+1)!!}$$
Let's examine the first sum, corresponding to the even indices.
$\sum_{k=0}^{\infty} \frac{(2k-1)!!}{(2k)!(2k)!!} \frac{\pi}{2}$.
The term for $k=0$ is $\frac{(-1)!!}{(0)!(0)!!} \frac{\pi}{2}$. Using the definitions $0!=1$, $0!!=1$, and $(-1)!!=1$, the $k=0$ term is $\frac{1}{1 \cdot 1} \frac{\pi}{2} = \frac{\pi}{2}$.
We can separate the $k=0$ term from the sum:
$$\sum_{k=0}^{\infty} \frac{(2k-1)!!}{(2k)!(2k)!!} \frac{\pi}{2} = \frac{\pi}{2} + \sum_{k=1}^{\infty} \frac{(2k-1)!!}{(2k)!(2k)!!} \frac{\pi}{2}$$
$$= \frac{\pi}{2} \left( 1 + \sum_{k=1}^{\infty} \frac{(2k-1)!!}{(2k)!(2k)!!} \right)$$
This matches the first part of the expression given in the problem statement.

Now let's examine the second sum, corresponding to the odd indices.
$$\sum_{k=0}^{\infty} \frac{(2k)!!}{(2k+1)!(2k+1)!!}$$
This sum matches the second part of the expression given in the problem statement exactly.

Combining the results for the even and odd terms, we get:
$$I = \frac{\pi}{2}\left(1+\sum_{k=1}^{\infty}\frac{(2k-1)!!}{(2k)!(2k)!!}\right)+\sum_{k=0}^{\infty}\frac{(2k)!!}{(2k+1)!(2k+1)!!}$$
This is the required expression.

We can also simplify the terms in the sums using the relationship between factorials and double factorials:
$(2k)! = (2k)!! (2k-1)!!$
$(2k+1)! = (2k+1)!! (2k)!!$

The term in the first sum (for $k \ge 1$) is $\frac{(2k-1)!!}{(2k)!(2k)!!} = \frac{(2k-1)!!}{(2k)!! (2k-1)!! (2k)!!} = \frac{1}{((2k)!!)^2}$.
The first part of the expression is $\frac{\pi}{2}\left(1+\sum_{k=1}^{\infty}\frac{1}{((2k)!!)^2}\right)$.

The term in the second sum (for $k \ge 0$) is $\frac{(2k)!!}{(2k+1)!(2k+1)!!} = \frac{(2k)!!}{(2k+1)!! (2k)!! (2k+1)!!} = \frac{1}{((2k+1)!!)^2}$.
The second part of the expression is $\sum_{k=0}^{\infty}\frac{1}{((2k+1)!!)^2}$.

So the integral is equal to $\frac{\pi}{2}\left(1+\sum_{k=1}^{\infty}\frac{1}{((2k)!!)^2}\right)+\sum_{k=0}^{\infty}\frac{1}{((2k+1)!!)^2}$.
Our derivation yielded $\sum_{k=0}^{\infty} \frac{1}{(2k)!} I_{2k} + \sum_{k=0}^{\infty} \frac{1}{(2k+1)!} I_{2k+1}$.
$\sum_{k=0}^{\infty} \frac{1}{(2k)!} \frac{(2k-1)!!}{(2k)!!} \frac{\pi}{2} = \sum_{k=0}^{\infty} \frac{1}{((2k)!!)^2} \frac{\pi}{2}$.
The $k=0$ term is $\frac{1}{((0)!!)^2}\frac{\pi}{2} = \frac{1}{1^2}\frac{\pi}{2} = \frac{\pi}{2}$.
So, $\sum_{k=0}^{\infty} \frac{1}{((2k)!!)^2} \frac{\pi}{2} = \frac{\pi}{2} + \sum_{k=1}^{\infty} \frac{1}{((2k)!!)^2} \frac{\pi}{2} = \frac{\pi}{2}\left(1+\sum_{k=1}^{\infty}\frac{1}{((2k)!!)^2}\right)$.
And $\sum_{k=0}^{\infty} \frac{1}{(2k+1)!} \frac{(2k)!!}{(2k+1)!!} = \sum_{k=0}^{\infty} \frac{1}{((2k+1)!!)^2}$.
Thus, the integral is indeed equal to the given expression.

The final answer is $\boxed{\int_0^{\pi/2} e^{\sin x}\ dx=\frac{\pi}{2}\left(1+\sum_{k=1}^{\infty}\frac{(2k-1)!!}{(2k)!(2k)!!}\right)+\sum_{k=0}^{\infty}\frac{(2k)!!}{(2k+1)!(2k+1)!!}}$.
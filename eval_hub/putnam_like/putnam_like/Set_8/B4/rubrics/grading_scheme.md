This step is worth 3 points.
Assume that $U$ has a uniform distribution on $(0,1)$. Then $-\ln(U)$ has an exponential distribution with expectation $1$. Indeed, for $t>0$ we have
$$
P(-\ln(U)\leq t) = P(U\leq e^{-t}) = e^{-t}.
$$
Hence $Z=\frac{\ln(X)}{\ln(Y)}$ is a quotient of independent random variables which have exponential distribution with expectation $1$.

This step is worth 3 points.
We find the distribution of $Z$. By the change-of-variables formula for Lebesgue integral we know that the joint distribution of a vector $(Z,-\ln(Y))$ has a density
$$
f(z,y) = ye^{-zy}e^{-y} = ye^{-(z+1)y}, \qquad z,y>0.
$$
Therefore, the density of a distribution of $Z$ is equal to
$$
f(z)=\int_0^\infty ye^{-(z+1)y} dy = \frac{1}{(1+z)^2}, \qquad z>0.
$$

This step is worth 4 points.
Note that
$$
P(\lfloor Z\rfloor=2n) = \int_{2n}^{2n+1}\frac{dz}{(1+z)^2} = \frac{1}{2n+1}-\frac{1}{2n+2}
$$
for $n=0,1,2,\ldots$. Hence the desired probability is equal to
$$
\sum_{n=0}^\infty \left(\frac{1}{2n+1}-\frac{1}{2n+2}\right) = \sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n} = \ln(2),
$$
where the later equality is the Taylor series expansion for $\ln(1+x)$ and $x=1$.
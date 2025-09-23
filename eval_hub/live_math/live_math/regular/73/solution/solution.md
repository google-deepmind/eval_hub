As $P(x) - Q(x)$ is of degree $99$, the polynomials $P$ and $Q$ have the same leading coefficient. Without loss of generality we can assume that they both are monic, are multiplying by the same constant will also multiply $R$ by the cube of that constant. This means that
 $$P(x) = x^{100} - 32 x^{99} + \dots$$
 and
 $$Q(x) = x^{100} - 64 x^{99} + \dots,$$
 where the dots represent the lower degree terms.
 Then 
 $$R(x) = P(x)\cdot (Q(x))^2 + (P(x))^2 \cdot Q(x)$$
 $$ =(x^{300} - 32x^{299} - 2\cdot 64 x^{299}) + (x^{300} - 64x^{299} - 2\cdot 32 x^{299}) + \dots
 = 2x^{300} - 288x^{299} + \dots$$
 and hence the sum of the roots is $\frac{288}{2} = 144$.
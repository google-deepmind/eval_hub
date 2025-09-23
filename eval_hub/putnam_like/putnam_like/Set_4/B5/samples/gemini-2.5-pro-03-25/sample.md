Solution:
Let \(P(z_1, z_2)\) be the assertion \(f(f(z_1)+z_2)=z_1+f(z_2)\).
The domain and codomain of \(f\) is a vector space \(\mathbb{V}\) over the field \(\mathbb{Q}\).

Step 1: Prove that \(f(0)=0\).
Let \(z_1=0\) in the assertion \(P(z_1, z_2)\). We get
\(P(0, z_2) \implies f(f(0)+z_2) = 0+f(z_2) = f(z_2)\).
Let \(c = f(0)\). Then the equation becomes \(f(c+z_2) = f(z_2)\) for all \(z_2 \in \mathbb{V}\). This shows that \(f\) is periodic with period \(c\).

Let \(z_2=0\) in the assertion \(P(z_1, z_2)\). We get
\(P(z_1, 0) \implies f(f(z_1)+0) = z_1+f(0)\), which simplifies to \(f(f(z_1)) = z_1+c\).

Now we use these two properties:
1.  \(f(c+z) = f(z)\) for all \(z \in \mathbb{V}\).
2.  \(f(f(z)) = z+c\) for all \(z \in \mathbb{V}\).

Apply the function \(f\) to both sides of equation (2):
\(f(f(f(z))) = f(z+c)\).
Using property (1) on the right side, we get \(f(z+c) = f(z)\).
So, \(f(f(f(z))) = f(z)\).

Now, let's compute \(f(f(f(z)))\) in another way. Let \(y=f(z)\). Then \(f(f(f(z))) = f(f(y))\).
Using property (2) with \(z\) replaced by \(y\), we have \(f(f(y)) = y+c\).
Substituting \(y=f(z)\) back, we get \(f(f(f(z))) = f(z)+c\).

Equating the two expressions we found for \(f(f(f(z)))\):
\(f(z) = f(z)+c\).
This implies \(c=0\).
Thus, we must have \(f(0)=0\).

Step 2: Prove \(f(f(z))=z\).
Substitute \(c=0\) into the equation \(f(f(z)) = z+c\) derived from \(P(z_1, 0)\).
We get \(f(f(z)) = z\) for all \(z \in \mathbb{V}\).
This means \(f\) is an involution, and therefore a bijection. In particular, \(f\) is its own inverse, \(f^{-1}=f\).

Step 3: Prove \(f\) is additive.
The original equation is \(f(f(z_1)+z_2)=z_1+f(z_2)\).
Apply \(f\) to both sides:
\(f(f(f(z_1)+z_2)) = f(z_1+f(z_2))\).
Using \(f(f(x))=x\) for any \(x\) in the domain of \(f\), the left side becomes \(f(z_1)+z_2\).
So we have the equation \(f(z_1)+z_2 = f(z_1+f(z_2))\).

Let \(x = z_1\) and \(y = f(z_2)\). Since \(f\) is surjective (as \(f\) is a bijection), \(y\) can be any vector in \(\mathbb{V}\).
Since \(f(f(z_2))=z_2\), we have \(z_2=f(y)\).
Substitute \(z_1=x\) and \(z_2=f(y)\) into the equation \(f(z_1)+z_2 = f(z_1+f(z_2))\):
\(f(x)+f(y) = f(x+f(f(y)))\).
Since \(f(f(y))=y\), the equation becomes:
\(f(x+y) = f(x)+f(y)\).
This is Cauchy's functional equation. This holds for all \(x, y \in \mathbb{V}\). So \(f\) is an additive function.

Step 4: Prove \(f\) is \(\mathbb{Q}\)-linear.
Since \(\mathbb{V}\) is a vector space over \(\mathbb{Q}\) and \(f: \mathbb{V} \to \mathbb{V}\) is additive, we can show that \(f\) is \(\mathbb{Q}\)-homogeneous, meaning \(f(qx)=qf(x)\) for all \(q \in \mathbb{Q}\) and \(x \in \mathbb{V}\).
- For any integer \(n \ge 0\), \(f(nx)=nf(x)\) by induction on \(n\). \(f(0x)=f(0)=0=0f(x)\). Assume \(f(kx)=kf(x)\). Then \(f((k+1)x) = f(kx+x) = f(kx)+f(x) = kf(x)+f(x)=(k+1)f(x)\).
- For any integer \(n\), \(f(nx)=nf(x)\). We have \(f(x)+f(-x)=f(x+(-x))=f(0)=0\), so \(f(-x)=-f(x)\). If \(n<0\), let \(n=-m\) for \(m>0\). Then \(f(nx)=f(-mx)=-f(mx)=-mf(x)=nf(x)\).
- For any rational number \(q \in \mathbb{Q}\), let \(q=m/n\) where \(m \in \mathbb{Z}, n \in \mathbb{N}, n \ne 0\).
Let \(x \in \mathbb{V}\). Let \(y = \frac{1}{n}x\). Then \(x=ny\).
We have \(f(x)=f(ny)=nf(y)\). Since \(n \ne 0\), we can multiply by \(1/n\). So \(f(y) = \frac{1}{n} f(x)\). That is, \(f(\frac{1}{n}x) = \frac{1}{n} f(x)\).
Then \(f(qx) = f(\frac{m}{n}x) = f(m(\frac{1}{n}x)) = m f(\frac{1}{n}x) = m (\frac{1}{n} f(x)) = \frac{m}{n} f(x) = qf(x)\).
Thus, \(f\) is \(\mathbb{Q}\)-linear.

Step 5: State the condition on \(f\).
We have shown that any solution \(f\) must be a \(\mathbb{Q}\)-linear map from \(\mathbb{V}\) to \(\mathbb{V}\) satisfying \(f(f(z))=z\) for all \(z \in \mathbb{V}\). In terms of linear maps, this condition is \(f^2 = I\), where \(I\) is the identity map on \(\mathbb{V}\).

Step 6: Verify the solutions.
We need to check if any \(\mathbb{Q}\)-linear map \(f: \mathbb{V} \to \mathbb{V}\) satisfying \(f^2=I\) is indeed a solution to the original functional equation.
Let \(f\) be such a map. We want to verify \(f(f(z_1)+z_2)=z_1+f(z_2)\).
Since \(f\) is \(\mathbb{Q}\)-linear, it is additive. So the left side is:
\(f(f(z_1)+z_2) = f(f(z_1)) + f(z_2)\).
Since \(f^2=I\), we have \(f(f(z_1))=z_1\).
So the left side becomes \(z_1+f(z_2)\).
This is exactly the right side of the original equation.
Thus, any \(\mathbb{Q}\)-linear map \(f\) such that \(f^2=I\) is a solution.

Step 7: Conclusion.
The set of all solutions \(f : \mathbb{V} \to \mathbb{V}\) to the functional equation \(f(f(z_1)+z_2)=z_1+f(z_2)\) consists of all \(\mathbb{Q}\)-linear maps \(f\) such that \(f^2 = I\), where \(I\) is the identity map on \(\mathbb{V}\). These maps are also known as linear involutions.

Examples of such functions include the identity map \(f(z)=z\) and the negation map \(f(z)=-z\). If \(\mathbb{V}\) can be decomposed into a direct sum \(\mathbb{V} = W_1 \oplus W_2\), then the map defined by \(f(w_1+w_2) = w_1-w_2\) for \(w_1 \in W_1, w_2 \in W_2\) is also a solution. All solutions are of this form for some choice of subspaces \(W_1, W_2\).

Final Answer: The final answer is $\boxed{f \text{ is a } \mathbb{Q}\text{-linear map such that } f^2=I}$
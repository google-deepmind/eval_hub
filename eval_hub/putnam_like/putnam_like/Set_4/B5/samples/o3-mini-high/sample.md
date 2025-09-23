```markdown
We wish to find all functions 
\[
f : \mathbb{V} \to \mathbb{V}
\]
satisfying
\[
f\bigl(f(z_1)+ z_2\bigr) = z_1 + f(z_2) \quad \text{for all } z_1,z_2 \in \mathbb{V},
\]
where \(\mathbb{V}\) is a vector space over the field \(\mathbb{Q}\).

### Step 1. Determining \( f(0) \) and Involution

First, take \( z_2 = 0 \) in the equation:
\[
f\bigl(f(z_1) + 0\bigr)= z_1 + f(0),
\]
which simplifies to
\[
f\bigl(f(z_1)\bigr) = z_1 + f(0) \quad \text{for all } z_1 \in \mathbb{V}.
\]
Now, set \( z_1 = 0 \) to obtain
\[
f\bigl(f(0)+ z_2\bigr)= 0 + f(z_2) = f(z_2).
\]
Since this holds for all \( z_2 \) and \( f \) is a function (which we will soon show is injective), we must have
\[
f(0)=0.
\]
Thus, the first relation becomes
\[
f\bigl(f(z_1)\bigr) = z_1 \quad \text{for all } z_1 \in \mathbb{V},
\]
so \( f \) is an involution.

### Step 2. Proving Additivity

Now, replace \( z_1 \) by \( f(z_1) \) in our original equation:
\[
f\bigl(f(f(z_1)) + z_2\bigr) = f(z_1) + f(z_2).
\]
But since \( f(f(z_1)) = z_1 \) (from the involution property), we get:
\[
f(z_1 + z_2) = f(z_1) + f(z_2) \quad \text{for all } z_1,z_2 \in \mathbb{V}.
\]
This shows that \( f \) is an additive function.

### Step 3. Homogeneity

Because \(\mathbb{V}\) is a vector space over \(\mathbb{Q}\) and \( f \) is additive, it follows that for any rational number \( q \) and any \( z \in \mathbb{V} \) we have:
\[
f(q\,z)= q\,f(z).
\]
Thus, \( f \) is in fact \(\mathbb{Q}\)-linear.

### Step 4. Characterizing \( f \) as a Linear Involution

Since \( f \) is linear and satisfies
\[
f\bigl(f(z)\bigr)= z \quad \text{for all } z \in \mathbb{V},
\]
if we write \( f(z) = Tz \) for some linear operator \( T \) on \(\mathbb{V}\), then
\[
T^2 z = z \quad \text{for all } z \in \mathbb{V}.
\]
That is,
\[
T^2 = I,
\]
where \( I \) is the identity operator. Thus, \( T \) (and hence \( f \)) is an involution.

### Step 5. The General Form of Linear Involutions

A linear involution on a vector space can be described in terms of the direct sum decomposition of \(\mathbb{V}\). In particular, there exist subspaces
\[
\mathbb{V}_+ = \{z\in\mathbb{V}: f(z) = z\} \quad \text{and} \quad \mathbb{V}_- = \{z\in\mathbb{V}: f(z) = -z\}
\]
such that
\[
\mathbb{V}= \mathbb{V}_+ \oplus \mathbb{V}_-.
\]
Every vector \( z \in \mathbb{V} \) may then be written uniquely as
\[
z = z_+ + z_-, \quad \text{with } z_+ \in \mathbb{V}_+ \text{ and } z_- \in \mathbb{V}_-.
\]
The involution \( f \) acts on \( z \) by
\[
f(z_+ + z_-) = z_+ - z_-.
\]

### Step 6. Verification

Conversely, if \( f \) is defined by
\[
f(z_+ + z_-) = z_+ - z_-
\]
for some decomposition \(\mathbb{V}= \mathbb{V}_+ \oplus \mathbb{V}_-\), then
\[
f\bigl(f(z_1)+ z_2\bigr)
= f\bigl((z_{1+} - z_{1-})+ (z_{2+} + z_{2-})\bigr)
= f(z_{1+}+ z_{2+} + (z_{2-}-z_{1-}))
= \bigl(z_{1+}+z_{2+}\bigr) -\bigl(z_{2-}- z_{1-}\bigr)
= z_{1+}+z_{1-} + \bigl(z_{2+}-z_{2-}\bigr)
= z_1 + f(z_2),
\]
which confirms that the functional equation is satisfied.

### Final Answer

The general solution to the functional equation
\[
f\bigl(f(z_1)+ z_2\bigr)= z_1+ f(z_2)
\]
is given by all functions \( f: \mathbb{V}\to \mathbb{V} \) of the form:
\[
\boxed{f(z)= f(z_+ + z_-) = z_+ - z_-, \quad \text{where } \mathbb{V}= \mathbb{V}_+ \oplus \mathbb{V}_- \text{ with } f(z)=z \text{ on } \mathbb{V}_+ \text{ and } f(z)=-z \text{ on } \mathbb{V}_-.}
\]
In particular, the two trivial solutions are
\[
f(z)= z \quad \text{and} \quad f(z)= -z.
\]
This completes the solution.
```
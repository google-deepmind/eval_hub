Of course. Here is a detailed, step-by-step solution to the problem.

### Problem Statement

Let $G$ be a finite multiplicative group of complex numbers with $|G| \geq 2$. Show that
$$
\sum_{z \in G} z = 0.
$$

### Solution

We will present two methods to solve this problem. The first is a general argument based on group properties, and the second uses a specific structural theorem about such groups.

---

### Method 1: The Group Action Argument

This method uses a fundamental "trick" in group theory where we act on a sum by an element of the group.

**Step 1: Define the sum**

Let $S$ be the sum of all elements in the group $G$.
$$
S = \sum_{z \in G} z
$$
Our goal is to show that $S=0$.

**Step 2: Choose an appropriate group element**

The problem states that $|G| \geq 2$. A group of order 1 would be $G=\{1\}$, where $1$ is the multiplicative identity. Since $|G| \geq 2$, there must exist at least one element in $G$ that is not the identity. Let's choose such an element and call it $g$. So, we have an element $g \in G$ such that $g \neq 1$.

**Step 3: Multiply the sum by the chosen element**

Let's consider the product $gS$:
$$
gS = g \left( \sum_{z \in G} z \right) = \sum_{z \in G} (gz)
$$
The right-hand side is the sum over a new set of elements $\{gz \mid z \in G\}$. Let's call this set $gG$.

**Step 4: Show that multiplication by a group element permutes the group**

We will now show that the set $gG = \{gz \mid z \in G\}$ is identical to the original set $G$. We can do this by considering the map $f: G \to G$ defined by $f(z) = gz$.

*   **Closure:** For any $g \in G$ and $z \in G$, their product $gz$ is also in $G$ by the closure property of a group. This means $gG \subseteq G$.

*   **The map is injective (one-to-one):** Suppose $f(z_1) = f(z_2)$ for some $z_1, z_2 \in G$. This means $gz_1 = gz_2$. Since $G$ is a group of complex numbers, $g$ is a non-zero complex number and has a multiplicative inverse $g^{-1}$, which is also in $G$. Multiplying by $g^{-1}$ on the left, we get:
    $$
    g^{-1}(gz_1) = g^{-1}(gz_2)
    $$
    $$
    (g^{-1}g)z_1 = (g^{-1}g)z_2
    $$
    $$
    1 \cdot z_1 = 1 \cdot z_2
    $$
    $$
    z_1 = z_2
    $$
    Thus, the map $f(z)=gz$ is injective.

*   **Conclusion for finite sets:** Since $f$ is an injective map from the finite set $G$ to itself ($gG \subseteq G$), it must also be surjective. This means that the set of images $gG$ is the same as the set $G$. In other words, multiplying every element of $G$ by $g$ simply permutes the elements of $G$.

**Step 5: Equate the sums**

Since the set of elements $\{gz \mid z \in G\}$ is the same as the set of elements $\{z \mid z \in G\}$, the sum over these sets must be the same.
$$
\sum_{z \in G} (gz) = \sum_{z \in G} z
$$
From Step 3, the left side is $gS$ and the right side is $S$. Therefore, we have the equation:
$$
gS = S
$$

**Step 6: Solve for S**

We can now solve the equation $gS = S$ for $S$.
$$
gS - S = 0
$$
$$
(g - 1)S = 0
$$
Recall that in Step 2, we chose $g$ to be an element of $G$ such that $g \neq 1$. Since $g$ is a complex number and $g \neq 1$, the complex number $(g - 1)$ is not zero.

We have a product of two complex numbers, $(g-1)$ and $S$, that equals zero. If a product of two complex numbers is zero, at least one of them must be zero. Since we know $(g-1) \neq 0$, it must be that $S=0$.

**Conclusion**

We have shown that $S = \sum_{z \in G} z = 0$.

---

### Method 2: Using the Structure of Finite Subgroups of $\mathbb{C}^*$

This method relies on a powerful theorem from abstract algebra.

**Step 1: Identify the structure of G**

The set of non-zero complex numbers, $\mathbb{C}^* = \mathbb{C} \setminus \{0\}$, forms a group under multiplication. The given group $G$ is a finite subgroup of $\mathbb{C}^*$.

A key theorem in group theory states that **any finite subgroup of the multiplicative group of a field is cyclic.** Since $\mathbb{C}$ is a field, $G$ must be a cyclic group.

**Step 2: Characterize the elements of the cyclic group**

Since $G$ is a cyclic group of order $n = |G|$, there exists a generator, let's call it $\omega$, such that all elements of $G$ are powers of $\omega$.
$$
G = \{ \omega, \omega^2, \omega^3, \dots, \omega^n \}
$$
The order of the generator $\omega$ is $n$, which means $\omega^n = 1$ (the identity element). Furthermore, since $\omega$ generates a group of order $n$, it must be a primitive $n$-th root of unity. Consequently, the group $G$ is precisely the group of the $n$-th roots of unity.

**Step 3: Calculate the sum**

The sum we want to calculate is the sum of all elements in $G$:
$$
\sum_{z \in G} z = \sum_{k=1}^n \omega^k = \omega + \omega^2 + \dots + \omega^n
$$
This is a finite geometric series with first term $a = \omega$, common ratio $r = \omega$, and $n$ terms. The sum can be calculated using the formula for a geometric series:
$$
S_n = a \frac{1 - r^n}{1 - r}
$$
In our case, this gives:
$$
\sum_{k=1}^n \omega^k = \omega \frac{1 - \omega^n}{1 - \omega}
$$

**Step 4: Use the properties of the generator**

We know that $\omega^n = 1$. Substituting this into the formula:
$$
\sum_{z \in G} z = \omega \frac{1 - 1}{1 - \omega} = \omega \frac{0}{1 - \omega}
$$
For this expression to be well-defined, the denominator cannot be zero. The condition $|G| = n \geq 2$ ensures this. If $n \geq 2$, the generator $\omega$ cannot be 1 (as $\omega=1$ would generate the trivial group $G=\{1\}$ of order 1). Thus, $\omega \neq 1$, which means the denominator $1 - \omega \neq 0$.

Since the numerator is 0 and the denominator is non-zero, the sum is 0.
$$
\sum_{z \in G} z = 0
$$

**Conclusion**

Both methods rigorously demonstrate that the sum of the elements of any finite multiplicative group of complex numbers with at least two elements is zero. The first method is more elementary, while the second provides insight into the specific structure of these groups.
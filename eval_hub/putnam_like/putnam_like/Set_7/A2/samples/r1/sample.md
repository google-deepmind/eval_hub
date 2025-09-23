

To show that the sum of all elements in a finite multiplicative group \( G \) of complex numbers is zero, consider the following argument:

**Step 1:** Let \( S = \sum_{z \in G} z \). Since \( |G| \geq 2 \), there exists an element \( a \in G \) such that \( a \neq 1 \).

**Step 2:** Multiplying every element in \( G \) by \( a \) permutes the group elements. Specifically, the map \( z \mapsto a z \) is a bijection (since \( a \) has an inverse in \( G \)). Thus:
\[
a S = \sum_{z \in G} a z = \sum_{z \in G} z = S
\]

**Step 3:** Subtract the original sum \( S \) from both sides:
\[
a S - S = 0 \implies S(a - 1) = 0
\]

**Step 4:** Since \( a \neq 1 \), the factor \( (a - 1) \neq 0 \). For the product \( S(a - 1) \) to be zero, it must hold that \( S = 0 \).

Therefore, the sum of all elements in \( G \) is:
\[
\boxed{0}
\]
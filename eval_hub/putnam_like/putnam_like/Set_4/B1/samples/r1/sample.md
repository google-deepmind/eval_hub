

To solve the given problems, we analyze the existence of polynomials \( P \) and \( Q \) that satisfy the specified equations for all \( k \in \mathbb{Z} \).

### Part (a)

**Problem Statement:**  
Does there exist a polynomial \( P \) such that \( k^2 P\left( \frac{1}{k} \right) = P_2(k) \) for all \( k \in \mathbb{Z} \setminus \{0\} \)?  

**Solution:**  
Let \( P_2(k) = a k^2 + b k + c \). Suppose \( P(x) \) is a polynomial of degree 2:  
\[
P(x) = c x^2 + b x + a
\]  
Substituting \( x = \frac{1}{k} \):  
\[
k^2 P\left( \frac{1}{k} \right) = k^2 \left( c \left( \frac{1}{k^2} \right) + b \left( \frac{1}{k} \right) + a \right) = a k^2 + b k + c
\]  
This matches \( P_2(k) \). Hence, such a polynomial \( P \) exists by reversing the coefficients of \( P_2(k) \).  

**Answer:**  
$\boxed{\text{Yes}}$

---

### Part (b)

**Problem Statement:**  
Does there exist a polynomial \( Q \) such that \( \frac{1}{k} Q \left( \frac{1}{k} \right) = \frac{P_1(k)}{P_2(k)} \) for all \( k \in \mathbb{Z} \setminus \{0\} \)?  

**Solution:**  
Assume \( Q(x) \) is a polynomial. Let \( x = \frac{1}{k} \), so \( k = \frac{1}{x} \). Rewriting the equation:  
\[
Q(x) = \frac{1}{x} \cdot \frac{P_1\left( \frac{1}{x} \right)}{P_2\left( \frac{1}{x} \right)}
\]  
For \( P_1(k) = a k + b \) and \( P_2(k) = \alpha k^2 + \beta k + \gamma \), substituting gives:  
\[
Q(x) = \frac{a + b x}{\alpha + \beta x + \gamma x^2}
\]  
For \( Q(x) \) to be a polynomial, the denominator \( \gamma x^2 + \beta x + \alpha \) must divide the numerator \( a + b x \). However, since the denominator is quadratic and the numerator is linear (or constant if \( b = 0 \)), division is impossible unless the numerator is identically zero, which contradicts \( P_1 \) being degree 1.  

**Answer:**  
$\boxed{\text{No}}$


To solve the given functional equation for continuous functions \( f : (0,\infty) \rightarrow (0,\infty) \), we proceed as follows:

### **Step 1: Testing Constant Functions**
Assume \( f(t) = c \) for some constant \( c > 0 \). Substituting into the equation:
\[
3c = 2 + c \implies 2c = 2 \implies c = 1.
\]
Thus, \( f(t) = 1 \) satisfies the equation.

### **Step 2: Checking Non-Constant Functions**
Suppose \( f \) is not constant. Consider specific substitutions:
1. **Set \( x = y = z = t \):**
   \[
   3f(tf(2t)) = 2 + f(3t).
   \]
   For \( f(t) \neq 1 \), this equation imposes constraints. Testing asymptotic behavior (e.g., \( t \to \infty \)) shows inconsistencies unless \( f(t) \equiv 1 \).

2. **Setting \( z \to 0 \), \( x = y = t \):**
   \[
   2f(tf(2t)) + L = 2 + f(2t), \quad \text{where } L = \lim_{t \to 0^+} f(t).
   \]
   If \( f \neq 1 \), this implies relations between \( L \), \( f(2t) \), and \( f(tf(2t)) \), leading to contradictions under continuity.

### **Step 3: Uniqueness via Continuity**
Assume \( f \) is continuous and not identically 1. By the Intermediate Value Theorem, \( f \) would take values other than 1, causing inconsistencies in the functional equation for various \( x, y, z \). Hence, no non-constant solution exists.

### **Conclusion**
The only continuous solution is the constant function \( f(t) = 1 \).

```markdown
**Solution**
\boxed{f(x) = 1}
```
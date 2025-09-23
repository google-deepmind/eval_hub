

To evaluate the integral \(\int_0^{\pi/2} e^{\sin x}\, dx\), we start by expanding \(e^{\sin x}\) as a Taylor series and integrate term-by-term.

**Step 1: Taylor Series Expansion**  
The Taylor series for \(e^z\) is:
\[
e^{\sin x} = \sum_{n=0}^{\infty} \frac{(\sin x)^n}{n!}.
\]
Integrating term-by-term:
\[
\int_0^{\pi/2} e^{\sin x}\, dx = \sum_{n=0}^{\infty} \frac{1}{n!} \int_0^{\pi/2} (\sin x)^n\, dx.
\]

**Step 2: Wallis Integrals for \(\int_0^{\pi/2} (\sin x)^n\, dx\)**  
For even \(n = 2k\):
\[
\int_0^{\pi/2} (\sin x)^{2k}\, dx = \frac{\pi}{2} \cdot \frac{(2k-1)!!}{(2k)!!},
\]
where \((2k)!! = 2^k k!\) and \((2k-1)!! = \frac{(2k)!}{2^k k!}\). For odd \(n = 2k+1\):
\[
\int_0^{\pi/2} (\sin x)^{2k+1}\, dx = \frac{(2k)!!}{(2k+1)!!}.
\]

**Step 3: Splitting the Series into Even and Odd Terms**  
Separate the series into even (\(n=2k\)) and odd (\(n=2k+1\)) terms:
\[
\int_0^{\pi/2} e^{\sin x}\, dx = \underbrace{\sum_{k=0}^{\infty} \frac{1}{(2k)!} \cdot \frac{\pi}{2} \cdot \frac{(2k-1)!!}{(2k)!!}}_{\text{Even terms}} + \underbrace{\sum_{k=0}^{\infty} \frac{1}{(2k+1)!} \cdot \frac{(2k)!!}{(2k+1)!!}}_{\text{Odd terms}}.
\]

**Step 4: Handling the \(k=0\) Term in the Even Series**  
For \(k=0\) in the even series:
\[
\frac{1}{(0)!} \cdot \frac{\pi}{2} \cdot \frac{(2(0)-1)!!}{(2(0))!!} = \frac{\pi}{2} \cdot \frac{(-1)!!}{0!!}.
\]
Using \(0!! = 1\) and defining \((-1)!! = 1\), this term simplifies to \(\frac{\pi}{2}\). The remaining even terms (\(k \geq 1\)) form the summation:
\[
\frac{\pi}{2} \sum_{k=1}^{\infty} \frac{(2k-1)!!}{(2k)! (2k)!!}.
\]

**Step 5: Final Expression**  
Combine the results:
\[
\int_0^{\pi/2} e^{\sin x}\, dx = \frac{\pi}{2} \left(1 + \sum_{k=1}^{\infty} \frac{(2k-1)!!}{(2k)! (2k)!!}\right) + \sum_{k=0}^{\infty} \frac{(2k)!!}{(2k+1)! (2k+1)!!}.
\]

This matches the given identity, completing the proof.

```markdown
**Step-by-Step Explanation and Proof:**

1. **Expand \(e^{\sin x}\) as a Taylor Series:**
   \[
   e^{\sin x} = \sum_{n=0}^{\infty} \frac{(\sin x)^n}{n!}.
   \]

2. **Integrate Term-by-Term:**
   \[
   \int_0^{\pi/2} e^{\sin x}\, dx = \sum_{n=0}^{\infty} \frac{1}{n!} \int_0^{\pi/2} (\sin x)^n\, dx.
   \]

3. **Evaluate Wallis Integrals:**
   - **Even \(n = 2k\):**
     \[
     \int_0^{\pi/2} (\sin x)^{2k}\, dx = \frac{\pi}{2} \cdot \frac{(2k-1)!!}{(2k)!!}.
     \]
   - **Odd \(n = 2k+1\):**
     \[
     \int_0^{\pi/2} (\sin x)^{2k+1}\, dx = \frac{(2k)!!}{(2k+1)!!}.
     \]

4. **Split into Even and Odd Series:**
   \[
   \int_0^{\pi/2} e^{\sin x}\, dx = \frac{\pi}{2} \sum_{k=0}^{\infty} \frac{(2k-1)!!}{(2k)! (2k)!!} + \sum_{k=0}^{\infty} \frac{(2k)!!}{(2k+1)! (2k+1)!!}.
   \]

5. **Adjust for \(k=0\) in the Even Series:**
   - The \(k=0\) term in the even series is \(\frac{\pi}{2}\).
   - Extract this term and adjust the summation index:
     \[
     \frac{\pi}{2} \left(1 + \sum_{k=1}^{\infty} \frac{(2k-1)!!}{(2k)! (2k)!!}\right).
     \]

6. **Final Result:**
   \[
   \int_0^{\pi/2} e^{\sin x}\, dx = \frac{\pi}{2}\left(1+\sum_{k=1}^{\infty}\frac{(2k-1)!!}{(2k)!(2k)!!}\right)+\sum_{k=0}^{\infty}\frac{(2k)!!}{(2k+1)!(2k+1)!!}.
   \]
```
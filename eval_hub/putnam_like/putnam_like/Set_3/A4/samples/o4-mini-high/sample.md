```markdown
**Solution**

Let 
\[
s = 3 + \sqrt{11}, 
\qquad 
t = 3 - \sqrt{11}.
\]
Then \(s\) and \(t\) are the two roots of the polynomial
\[
x^2 - 6x - 2 = 0,
\]
so in particular
\[
s^2 = 6s + 2,
\quad
t^2 = 6t + 2.
\]
Define the integer sequence
\[
a_k \;=\; s^k + t^k,
\qquad k = 0,1,2,\dots.
\]
One checks easily
\[
a_0 = 2,\quad
a_1 = s + t = 6,
\]
and from \(s^2=6s+2\), \(t^2=6t+2\) we get the recurrence
\[
a_{k+2} \;=\; 6\,a_{k+1} \;+\; 2\,a_k
\quad(k\ge0).
\]
Since \(0 < t < 1\), it follows that
\[
0 < t^{2n} < 1,
\]
while
\[
s^{2n} + t^{2n} \;=\; a_{2n}
\]
is an integer.  Hence
\[
s^{2n} \;<\; a_{2n} \;<\; s^{2n} + 1,
\]
so by definition of the ceiling,
\[
\bigl\lceil s^{2n}\bigr\rceil
\;=\;
a_{2n}
\;=\;
(3+\sqrt{11})^{2n} + (3-\sqrt{11})^{2n}.
\]
It remains to show
\[
a_{2n}\equiv 0\pmod{2^{\,n+1}}.
\]

---

### 2‑adic divisibility via a two‑term recurrence

Set
\[
b_n \;=\; a_{2n},
\qquad n=0,1,2,\dots.
\]
From the recurrence \(a_{k+2}=6a_{k+1}+2a_k\) one derives (after eliminating the odd‑index terms) the two‑term recurrence
\[
\boxed{
\;b_{n+1} = 40\,b_n \;-\;4\,b_{n-1},
\quad
n\ge1,
}
\]
with initial values
\[
b_0 = a_0 = 2,
\qquad
b_1 = a_2 = (3+\sqrt{11})^2 + (3-\sqrt{11})^2 = 40.
\]
We now prove by induction that
\[
b_n \equiv 0 \pmod{2^{\,n+1}}
\quad\forall n\ge0.
\]

1.  **Base cases.**  
    - \(n=0\): \(b_0=2\equiv0\pmod{2^1}\).  
    - \(n=1\): \(b_1=40\equiv0\pmod{2^2}\).

2.  **Inductive step.**  
    Assume for some \(k\ge1\),
    \[
    b_{k-1}\equiv0\pmod{2^{\,k}},
    \quad
    b_k\equiv0\pmod{2^{\,k+1}}.
    \]
    Then
    \[
    b_{k+1}
    = 40\,b_k \;-\;4\,b_{k-1}
    = 4\bigl(10\,b_k - b_{k-1}\bigr).
    \]
    By the inductive hypothesis \(b_k\equiv0\pmod{2^{k+1}}\) and \(b_{k-1}\equiv0\pmod{2^k}\), so
    \[
    10\,b_k - b_{k-1}
    \equiv 0 - 0
    \equiv 0
    \pmod{2^k},
    \]
    and hence
    \(
    b_{k+1} = 4\cdot(10\,b_k - b_{k-1})
    \)
    is divisible by \(4\cdot2^k = 2^{\,k+2}\).  This completes the induction.

Therefore for all \(n\ge1\),
\[
\bigl\lceil (3+\sqrt{11})^{2n}\bigr\rceil
= b_n
\equiv 0 \pmod{2^{\,n+1}},
\]
as required.  
Qed.  
```
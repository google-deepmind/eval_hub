```markdown
**Solution.**  
Let  
\(a = \sqrt[3]{n} = n^{1/3},\)  
\(b = \sqrt[3]{n+1} = (n+1)^{1/3},\)  
with \(n\in\Bbb N\), \(n\ge21\).  We wish to determine the sign of
\[
a^b \;\gtrless\; b^a.
\]
Taking logarithms, this is equivalent to
\[
a^b > b^a 
\quad\Longleftrightarrow\quad
b\ln a \;>\; a\ln b.
\]
Define
\[
D \;=\; b\ln a \;-\; a\ln b
\;=\;\frac13\Bigl((n+1)^{1/3}\ln n \;-\; n^{1/3}\ln(n+1)\Bigr).
\]
Hence it suffices to show
\[
(n+1)^{1/3}\ln n \;-\; n^{1/3}\ln(n+1)\;>\;0.
\]
Equivalently,
\[
\frac{\ln n}{n^{1/3}}
\;>\;
\frac{\ln(n+1)}{(n+1)^{1/3}}.
\]
Consider the auxiliary function
\[
f(x)\;=\;\frac{\ln x}{x^{1/3}},\quad x>0.
\]
A straightforward derivative‐check gives
\[
f'(x)
=\frac{\;x^{-2/3}-\tfrac13\,x^{-2/3}\ln x\;}{x^{2/3}}
=\frac{1-\tfrac13\ln x}{x^{4/3}}.
\]
Thus \(f'(x)>0\) for \(x<e^3\) and \(f'(x)<0\) for \(x>e^3\), so \(f\) attains its unique maximum at \(x=e^3\approx20.085\).  Since \(n\ge21>e^3\), it follows that
\[
f(n) \;>\; f(n+1),
\]
i.e.
\[
\frac{\ln n}{n^{1/3}} \;>\;\frac{\ln(n+1)}{(n+1)^{1/3}}.
\]
Therefore \(D>0\) and
\[
b\ln a \;>\; a\ln b
\quad\Longrightarrow\quad
a^b \;>\; b^a
\quad\text{for all }n\ge21.
\]
```
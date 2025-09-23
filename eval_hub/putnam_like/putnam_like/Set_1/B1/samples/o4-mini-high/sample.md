```markdown
**Solution**

Let 
\[
t = x^2,\qquad t\ge0.
\]
The given equation becomes
\[
6^t + 5^t - 10^t = 1.
\]
Define 
\[
f(t) = 6^t + 5^t - 10^t.
\]
We have
\[
f(0)=6^0+5^0-10^0 = 1+1-1 = 1,
\qquad
f(1)=6+5-10 = 1.
\]
To see that these are the only solutions, compute
\[
f'(t) = 6^t\ln6 + 5^t\ln5 \;-\; 10^t\ln10
= 10^t\Bigl((0.6)^t\ln6 + (0.5)^t\ln5 - \ln10\Bigr).
\]
Set
\[
g(t) = (0.6)^t\ln6 + (0.5)^t\ln5.
\]
Since $\ln6,\ln5>0$ and $\ln0.6,\ln0.5<0$, one checks
\[
g'(t) = (0.6)^t\ln6\cdot\ln0.6 + (0.5)^t\ln5\cdot\ln0.5 < 0,
\]
so $g$ is strictly decreasing.  Moreover
\[
g(0)=\ln6+\ln5=\ln30>\ln10,
\qquad
g(1)=0.6\ln6+0.5\ln5<\ln10.
\]
Hence there is a unique $t_0\in(0,1)$ with $g(t_0)=\ln10$.  It follows that
\[
f'(t)>0\quad(t<t_0),
\qquad
f'(t)<0\quad(t>t_0),
\]
so $f$ rises from $f(0)=1$ to a maximum $>1$ and then decreases through $f(1)=1$ to $-\infty$.  Therefore the only solutions of 
\[
6^t+5^t-10^t=1,\quad t\ge0,
\]
are
\[
t=0
\quad\text{or}\quad
t=1.
\]
Recalling $t=x^2$, we get
\[
x^2=0\quad\Longrightarrow\quad x=0,
\qquad
x^2=1\quad\Longrightarrow\quad x=\pm1.
\]
**Answer.** \(\displaystyle x\in\{-1,0,1\}.\) 
```
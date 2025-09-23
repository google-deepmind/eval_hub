```latex
\[
\textbf{Claim: } \quad \sup_{f \in \mathcal{F}} \frac{\int_{0}^{1} |f(x)| \, dx}{\left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}} = 1,
\]
where
\[
\mathcal{F} = \{ f \in \mathcal{C}([0,1],\mathbb{R}) \; : \; f(0)=0 \}.
\]

\textbf{Proof:}

First, note that the ratio is homogeneous; i.e., if \( f \) is replaced by \( c f \) (with \( c \neq 0 \)), then both numerator and denominator are multiplied by \(|c|\), leaving the ratio invariant. Therefore, we can assume without loss of generality that
\[
\int_0^1 |f(x)|^2 \, dx = 1.
\]

Now, by the Cauchy–Schwarz inequality we have
\[
\int_0^1 |f(x)| \, dx \le \left(\int_0^1 (1)^2 \, dx\right)^{1/2}\left(\int_0^1 |f(x)|^2 \, dx\right)^{1/2} 
= 1 \cdot 1 = 1.
\]
Thus, for every \( f \in \mathcal{F} \),
\[
\frac{\int_0^1 |f(x)|\, dx}{\left(\int_0^1 |f(x)|^2\, dx\right)^{1/2}} \le 1.
\]

Notice that the equality case in the Cauchy–Schwarz inequality requires the functions to be proportional, i.e.,
\[
|f(x)| = \lambda \quad \text{for some } \lambda \ge 0 \text{ and for almost every } x \in [0,1].
\]
This would mean that \( f \) is essentially constant. However, the constraint \( f(0) = 0 \) forces \(\lambda = 0\), leading to the trivial function, which does not provide a meaningful maximum for the ratio.

\medskip

\textbf{Approaching the Supremum:}

Although the equality cannot be achieved by any \( f \in \mathcal{F} \), one can construct a sequence of functions that approaches the value 1. For example, for each \( \varepsilon > 0 \) define the function
\[
f_\varepsilon(x) = 
\begin{cases}
\displaystyle \frac{x}{\varepsilon}, & \text{if } 0 \le x \le \varepsilon, \\[2mm]
1, & \text{if } \varepsilon < x \le 1.
\end{cases}
\]
Note that \( f_\varepsilon(0)=0 \) and \( f_\varepsilon \in \mathcal{C}([0,1],\mathbb{R}) \) (with a slight modification at the joining point \( x = \varepsilon \) to ensure continuity, which can be done smoothly).

\medskip

For \( f_\varepsilon \), we compute:
\[
\int_{0}^{1} |f_\varepsilon(x)| \, dx 
= \int_{0}^{\varepsilon} \frac{x}{\varepsilon} \, dx + \int_{\varepsilon}^{1} 1 \, dx
= \frac{1}{\varepsilon} \cdot \frac{\varepsilon^2}{2} + (1 - \varepsilon)
= \frac{\varepsilon}{2} + (1-\varepsilon)
= 1 - \frac{\varepsilon}{2}.
\]

Similarly,
\[
\int_0^1 |f_\varepsilon(x)|^2 \, dx 
= \int_{0}^{\varepsilon} \left(\frac{x}{\varepsilon}\right)^2 dx + \int_{\varepsilon}^{1} 1^2 \, dx
= \frac{1}{\varepsilon^2}\cdot \frac{\varepsilon^3}{3} + (1 - \varepsilon)
= \frac{\varepsilon}{3} + (1-\varepsilon)
= 1 - \frac{2\varepsilon}{3}.
\]
Thus, the ratio becomes
\[
\frac{\int_0^1 |f_\varepsilon(x)|\, dx}{\left(\int_0^1 |f_\varepsilon(x)|^2 \, dx\right)^{1/2}}
= \frac{1-\frac{\varepsilon}{2}}{\sqrt{1-\frac{2\varepsilon}{3}}}.
\]
As \( \varepsilon \to 0 \), this expression tends to 1. Hence, the supremum of our expression is indeed 1.

\medskip

\textbf{Conclusion:}

\[
\boxed{ \sup_{f \in \mathcal{F}} \frac{\int_{0}^{1} |f(x)| \, dx}{\left( \int_0^1 |f(x)|^2 \, dx \right)^{1/2}} = 1. }
\]
```
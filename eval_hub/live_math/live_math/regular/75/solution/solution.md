Consider $a \leq b$ so $b=a+1$. Hence we have $a \cdot b = a(a+1)$ and we can easily estimate a lower and upper bound for $a$:
$$7770=2 \cdot 3 \cdot 5 \cdot 7 \cdot 37 \leq a^2+a \leq  2 \cdot 3 \cdot 29 \cdot 31 \cdot 37=199578.$$


Since $a^2+a \leq a^2+2a+1 \leq (a+1)^2$ and $a^2 \leq a^2+a$ we have that:
$$\sqrt{7770} \approx 88.14 \leq a+1 \ \mbox{ and } a \leq \sqrt{199578} \approx 446.74$$
\noindent so $90 \leq a \leq 446$ and $91 \leq b=a+1 \leq 447$. Notice that $37|a$ or $37|b$ so it is sufficient to study the multiples of $37$ which are between $90$ and $447$. These are $111, 148, 185, 222, 259, 296, 333, 370, 407, 444$ and studying them we have that the only solutions are:
\begin{itemize}
\item $(110,111)=(2 \cdot 5 \cdot 11, 3 \cdot 37)$
\item $(185,186)=(5 \cdot 37,2 \dot 3 \cdot 31)$
\item $(221,222)=(13 \cdot 17,2 \dot 3 \cdot 37)$
\end{itemize}
\noindent so the answer is $3$ and we are done.
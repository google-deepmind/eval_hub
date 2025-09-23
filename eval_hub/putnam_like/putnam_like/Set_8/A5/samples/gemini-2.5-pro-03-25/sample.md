Let $f_n(x) = \prod_{i=1}^{n}\cos((2i-1)x)$. We want to compute $L = \liminf_{n\to\infty} I_n$, where $I_n = \int_0^{2\pi} f_n(x) dx$.

We can express $f_n(x)$ using Euler's formula, $\cos(y) = \frac{e^{iy} + e^{-iy}}{2}$.
$$f_n(x) = \prod_{i=1}^{n} \frac{e^{i(2i-1)x} + e^{-i(2i-1)x}}{2} = \frac{1}{2^n} \prod_{i=1}^{n} (e^{i(2i-1)x} + e^{-i(2i-1)x})$$
Expanding the product yields $2^n$ terms, each of the form $e^{i S_{\epsilon} x}$ where $\epsilon = (\epsilon_1, \dots, \epsilon_n)$ with $\epsilon_i \in \{-1, 1\}$, and $S_{\epsilon} = \sum_{i=1}^n \epsilon_i (2i-1)$.
$$f_n(x) = \frac{1}{2^n} \sum_{\epsilon \in \{-1, 1\}^n} e^{i S_{\epsilon} x}$$
This is a representation of $f_n(x)$ as a sum of complex exponentials. The integral $I_n$ is then:
$$I_n = \int_0^{2\pi} \frac{1}{2^n} \sum_{\epsilon \in \{-1, 1\}^n} e^{i S_{\epsilon} x} dx$$
We can interchange the sum and the integral:
$$I_n = \frac{1}{2^n} \sum_{\epsilon \in \{-1, 1\}^n} \int_0^{2\pi} e^{i S_{\epsilon} x} dx$$
The integral $\int_0^{2\pi} e^{ikx} dx$ is equal to $2\pi$ if $k=0$, and $0$ if $k$ is a non-zero integer.
The term $S_{\epsilon} = \sum_{i=1}^n \epsilon_i (2i-1)$ is always an integer, since each $2i-1$ is an integer and $\epsilon_i \in \{-1, 1\}$.
So, the integral is non-zero only for those terms where $S_{\epsilon} = 0$.
Let $N_0(n)$ be the number of tuples $\epsilon = (\epsilon_1, \dots, \epsilon_n) \in \{-1, 1\}^n$ such that $S_{\epsilon} = 0$.
$$I_n = \frac{1}{2^n} (N_0(n) \times 2\pi + \sum_{\epsilon \text{ s.t. } S_{\epsilon} \neq 0} 0) = \frac{2\pi N_0(n)}{2^n}$$

Now we need to determine $N_0(n)$. The sum $S_{\epsilon} = \sum_{i=1}^n \epsilon_i (2i-1)$ involves the terms $\epsilon_1(1), \epsilon_2(3), \dots, \epsilon_n(2n-1)$. Each term $\epsilon_i (2i-1)$ is an odd integer.
$S_{\epsilon}$ is a sum of $n$ odd integers.
If $n$ is odd, the sum of $n$ odd integers is odd. Therefore, $S_{\epsilon}$ cannot be $0$ (which is even). So $N_0(n) = 0$ for all odd $n$.
If $n$ is even, the sum of $n$ odd integers is even. Therefore, $S_{\epsilon}$ can potentially be $0$. For example, for $n=4$, the set of numbers is $\{1, 3, 5, 7\}$. We search for $\epsilon_i$ such that $\epsilon_1(1) + \epsilon_2(3) + \epsilon_3(5) + \epsilon_4(7) = 0$. One solution is $1+7-3-5 = 0$, corresponding to $\epsilon=(1, -1, -1, 1)$. Another solution is $-1-7+3+5=0$, corresponding to $\epsilon=(-1, 1, 1, -1)$. So $N_0(4)=2$. $I_4 = \frac{2\pi (2)}{2^4} = \frac{4\pi}{16} = \frac{\pi}{4}$.
For $n=2$, the set is $\{1, 3\}$. Possible sums are $1+3=4$, $1-3=-2$, $-1+3=2$, $-1-3=-4$. None is 0. So $N_0(2)=0$. $I_2=0$.

Since $N_0(n) = 0$ for all odd $n$, we have $I_n = 0$ for all odd $n$.
The sequence $(I_n)_{n\in\mathbb{N}}$ is $I_1, I_2, I_3, I_4, \dots$ which starts with $0, 0, 0, \pi/4, 0, I_6, 0, I_8, \dots$.
We are looking for the limit inferior of this sequence.
The limit inferior is defined as $\liminf_{n\to\infty} I_n = \lim_{n\to\infty} (\inf_{k\ge n} I_k)$.
Let $a_n = \inf_{k\ge n} I_k$.
Since $N_0(n) \ge 0$ (it is a count), and $2^n > 0$, we have $I_n = \frac{2\pi N_0(n)}{2^n} \ge 0$ for all $n$.
So the sequence $(I_n)$ is bounded below by 0. Thus $a_n \ge 0$ for all $n$.
For any $n$, there exists an odd integer $k \ge n$. For example, if $n$ is odd, $k=n$. If $n$ is even, $k=n+1$.
For this odd $k$, we have $I_k = 0$.
Since $I_k = 0$ for some $k \ge n$, the infimum of the set $\{I_k \mid k \ge n\}$ must be less than or equal to 0.
So $a_n = \inf_{k\ge n} I_k \le 0$.
Combined with $a_n \ge 0$, we must have $a_n = 0$ for all $n$.
Therefore, $\liminf_{n\to\infty} I_n = \lim_{n\to\infty} a_n = \lim_{n\to\infty} 0 = 0$.

Final check: The sequence $I_n$ consists of non-negative terms. There is an infinite subsequence (for odd $n$) that is identically zero. The limit inferior must be the smallest limit point. Since 0 is a limit point (due to the subsequence $I_{2k+1} \to 0$), and $I_n \ge 0$, 0 must be the smallest limit point.

Final Answer: The final answer is $\boxed{0}$
Let $I_n = \int_0^{2\pi} f_n(x) dx = \int_0^{2\pi} \prod_{i=1}^n \cos((2i-1)x) dx$.

We can write $\cos((2i-1)x) = \frac{e^{i(2i-1)x} + e^{-i(2i-1)x}}{2}$.
Then $f_n(x) = \prod_{i=1}^n \frac{e^{i(2i-1)x} + e^{-i(2i-1)x}}{2} = \frac{1}{2^n} \prod_{i=1}^n (e^{i(2i-1)x} + e^{-i(2i-1)x})$.
Expanding the product, we get a sum of terms of the form $e^{i k x}$, where $k$ is a linear combination of $\pm(2i-1)$ for $i=1, \dots, n$. Specifically,
$f_n(x) = \frac{1}{2^n} \sum_{(\epsilon_1, \dots, \epsilon_n) \in \{-1, 1\}^n} e^{i (\sum_{j=1}^n \epsilon_j (2j-1)) x}$.

Now we integrate $f_n(x)$ from 0 to $2\pi$:
$I_n = \int_0^{2\pi} \frac{1}{2^n} \sum_{\epsilon \in \{-1, 1\}^n} e^{i (\sum_{j=1}^n \epsilon_j (2j-1)) x} dx = \frac{1}{2^n} \sum_{\epsilon \in \{-1, 1\}^n} \int_0^{2\pi} e^{i (\sum_{j=1}^n \epsilon_j (2j-1)) x} dx$.
The integral $\int_0^{2\pi} e^{ikx} dx$ is equal to $2\pi$ if $k=0$ and 0 if $k$ is a non-zero integer.
So $I_n = \frac{1}{2^n} \cdot 2\pi \cdot N_n$, where $N_n$ is the number of sequences $(\epsilon_1, \dots, \epsilon_n) \in \{-1, 1\}^n$ such that $\sum_{j=1}^n \epsilon_j (2j-1) = 0$.

Let $S = \sum_{j=1}^n \epsilon_j (2j-1)$. The terms $(2j-1)$ are $1, 3, 5, \dots, 2n-1$. These are all odd integers.
The sum of $n$ odd integers is odd if $n$ is odd, and even if $n$ is even.
If $n$ is odd, $S$ is always an odd integer. An odd integer cannot be 0.
Thus, if $n$ is odd, $N_n = 0$.
This implies $I_n = 0$ for all odd $n$.

If $n$ is even, $S$ is an even integer, so it might be 0. $N_n$ can be non-zero for even $n$.
$N_n$ is the number of ways to choose signs $\epsilon_j$ such that $\sum_{j=1}^n \epsilon_j (2j-1) = 0$.
This is the coefficient of $z^0$ in the product $\prod_{j=1}^n (z^{2j-1} + z^{-(2j-1)})$.
Let $P_n(z) = \prod_{j=1}^n (z^{2j-1} + z^{-(2j-1)})$.
$P_n(z) = \prod_{j=1}^n z^{-(2j-1)} (z^{2(2j-1)} + 1) = z^{-\sum_{j=1}^n (2j-1)} \prod_{j=1}^n (z^{4j-2} + 1)$.
The sum $\sum_{j=1}^n (2j-1) = 1+3+\dots+(2n-1) = n^2$.
So $P_n(z) = z^{-n^2} \prod_{j=1}^n (z^{4j-2} + 1)$.
$N_n = [z^0] P_n(z) = [z^{n^2}] \prod_{j=1}^n (z^{4j-2} + 1)$.

The exponents $4j-2$ for $j=1, \dots, n$ are $2, 6, 10, \dots, 4n-2$. These are distinct positive even integers.
The product $\prod_{j=1}^n (z^{4j-2} + 1)$ expands into a sum of terms $z^k$, where $k$ is a sum of distinct integers from the set $\{2, 6, \dots, 4n-2\}$.
$k = \sum_{j \in A} (4j-2)$ for some subset $A \subseteq \{1, \dots, n\}$.
$N_n$ is the number of subsets $A \subseteq \{1, \dots, n\}$ such that $\sum_{j \in A} (4j-2) = n^2$.

For $n=2$, $n^2=4$. We need subsets of $\{2, 6\}$ summing to 4. Possible sums: 0, 2, 6, 8. None sum to 4. $N_2=0$.
$I_2 = \frac{2\pi}{2^2} \cdot 0 = 0$.

For $n=4$, $n^2=16$. We need subsets of $\{2, 6, 10, 14\}$ summing to 16.
$\{2, 14\}$ sum to 16. $\{6, 10\}$ sum to 16.
These are the only subsets summing to 16. So $N_4=2$.
$I_4 = \frac{2\pi}{2^4} \cdot 2 = \frac{4\pi}{16} = \frac{\pi}{4}$.

For $n=6$, $n^2=36$. We need subsets of $\{2, 6, 10, 14, 18, 22\}$ summing to 36.
Possible sums of distinct elements:
$2+6+10+18 = 36$. Subsets $\{1,2,3,5\}$.
$2+6+14+14$ (no distinct).
$2+10+14+10$ (no distinct).
$2+10+?$
$2+6+10+18=36$. (indices $1,2,3,5$)
$2+6+14+?$ No.
$2+10+14+?$ No.
$2+10+?$
$6+10+14+6$ No.
$2+22+12$ no. $6+22+8$ no. $10+22+4$ no. $14+22$ no. $18+?$ no.
$2+6+10+18=36$.
$2+6+14+?$
$2+10+14+10$
$6+10+14+6$
Other sums to 36: $\{14, 22\}$. (indices $4,6$). $N_6=2$.
$I_6 = \frac{2\pi}{2^6} \cdot 2 = \frac{4\pi}{64} = \frac{\pi}{16}$.

The sequence $I_n$ for $n=1, 2, 3, 4, 5, 6, \dots$ is $0, 0, 0, \pi/4, 0, \pi/16, \dots$.
We need to evaluate $\lim_{n\to\infty} I_n$.
For odd $n$, $I_n=0$.
For even $n=2m$, $I_{2m} = \frac{2\pi}{2^{2m}} N_{2m} = \frac{2\pi}{4^m} N_{2m}$.
$N_{2m}$ is the number of subsets $A \subseteq \{1, \dots, 2m\}$ such that $\sum_{j \in A} (4j-2) = (2m)^2 = 4m^2$.
This is the number of ways to partition $4m^2$ into distinct parts from $\{2, 6, \dots, 8m-2\}$.

We use the approximation for the coefficient $c_k$ of $z^k$ in $\prod_{j=1}^n (1+z^{a_j})$ where $a_j$ are distinct positive integers. For $k$ near the center of the sum of exponents, $c_k$ is approximately $2^n / \sqrt{\pi \sum a_j^2 / 2}$.
Here $a_j = 4j-2$ for $j=1, \dots, n=2m$. $\sum_{j=1}^{2m} (4j-2)^2$.
The required power is $n^2 = (2m)^2 = 4m^2$.
$\sum_{j=1}^{2m} (4j-2) = 2(2m)^2 = 8m^2$. The target sum $4m^2$ is exactly half of the total sum of possible exponents $8m^2$. This means $k=4m^2$ is the central coefficient.
$\sum_{j=1}^{2m} (4j-2)^2 = 16 \sum_{j=1}^{2m} (j-1/2)^2$. Approx $\int_0^{2m} 16x^2 dx \approx 16 (2m)^3/3 = 128m^3/3$.
$\sum_{j=1}^{2m} (4j-2)^2 = 16 \sum_{j=1}^{2m} j^2 - 16 \sum_{j=1}^{2m} j + \sum_{j=1}^{2m} 4 = 16 \frac{2m(2m+1)(4m+1)}{6} - 16 \frac{2m(2m+1)}{2} + 8m$
$= \frac{16m(2m+1)(4m+1)}{3} - 16m(2m+1) + 8m \sim \frac{16m \cdot 2m \cdot 4m}{3} = \frac{128m^3}{3}$.
$N_{2m} \approx \frac{2^{2m}}{\sqrt{\pi \sum_{j=1}^{2m} (4j-2)^2 / 2}} \sim \frac{4^m}{\sqrt{\pi (128m^3/3)/2}} = \frac{4^m}{\sqrt{64\pi m^3/3}} = \frac{4^m}{C m^{3/2}}$ for some constant $C$.
$I_{2m} = \frac{2\pi}{4^m} N_{2m} \sim \frac{2\pi}{4^m} \frac{4^m}{C m^{3/2}} = \frac{2\pi}{C m^{3/2}}$.
As $m \to \infty$, $I_{2m} \to 0$.

Since $I_n=0$ for odd $n$ and $I_n \to 0$ for even $n$, the limit of $I_n$ is 0.
$\lim_{n\to\infty} I_n = 0$.
For a sequence that converges, the $\liminf$ is equal to the limit.
$\liminf_{n\to\infty} I_n = 0$.

The final answer is $\boxed{0}$.
Let the sequence $(m_k)$ be an increasing sequence of natural numbers such that $m_k \to \infty$.
Let $(a_k)$ be a sequence of real numbers such that for every $\gamma > 1$, $a_{\lfloor \gamma^{m_k} \rfloor} \to 0$ as $k \to \infty$.
We want to determine if this implies that $a_k \to 0$ as $k \to \infty$.

We will show that this is not true by constructing a counterexample.
Let the sequence $(a_k)$ be defined as follows:
$a_n = 1$ if $n$ is a factorial, i.e., $n = N!$ for some integer $N \ge 1$.
$a_n = 0$ otherwise.

The sequence $(a_k)$ does not converge to 0, because $a_{N!} = 1$ for all $N \ge 1$, so the subsequence $(a_{N!})_{N \ge 1}$ converges to 1, not 0.

Now we need to check if this sequence $(a_k)$ satisfies the given condition: for every $\gamma > 1$, $a_{\lfloor \gamma^{m_k} \rfloor} \to 0$ as $k \to \infty$.
The condition $a_{\lfloor \gamma^{m_k} \rfloor} \to 0$ means that for any $\epsilon > 0$, there exists $K(\gamma, \epsilon)$ such that for all $k > K(\gamma, \epsilon)$, $|a_{\lfloor \gamma^{m_k} \rfloor}| < \epsilon$. Since $a_n$ is either 0 or 1, this is equivalent to saying that $a_{\lfloor \gamma^{m_k} \rfloor}$ must be 0 for all $k$ sufficiently large.
This means that for any $\gamma > 1$, the number $\lfloor \gamma^{m_k} \rfloor$ can be a factorial for only a finite number of indices $k$.

Let $\gamma > 1$ be fixed. Suppose that $\lfloor \gamma^{m_k} \rfloor$ is a factorial for infinitely many values of $k$. Let these values be $k_1 < k_2 < k_3 < \dots$.
For each $k_j$, there exists an integer $N_j \ge 1$ such that $\lfloor \gamma^{m_{k_j}} \rfloor = N_j!$.
Since $m_k \to \infty$ and $\gamma > 1$, $\gamma^{m_{k_j}} \to \infty$ as $j \to \infty$. Thus $\lfloor \gamma^{m_{k_j}} \rfloor \to \infty$, which implies $N_j! \to \infty$, so $N_j \to \infty$ as $j \to \infty$.
The condition $\lfloor \gamma^{m_{k_j}} \rfloor = N_j!$ means $N_j! \le \gamma^{m_{k_j}} < N_j!+1$.
Taking the natural logarithm, we get $\ln(N_j!) \le m_{k_j} \ln \gamma < \ln(N_j!+1)$.
This inequality must hold for all $j \ge 1$.

Let's consider the intervals $I_N = [\ln(N!), \ln(N!+1))$ for $N \ge 1$. These intervals are disjoint. The length of $I_N$ is $\ln(N!+1) - \ln(N!) = \ln(1+1/N!)$.
As $N \to \infty$, $\ln(1+1/N!) \sim 1/N! \to 0$.
The condition $\ln(N_j!) \le m_{k_j} \ln \gamma < \ln(N_j!+1)$ means that the value $m_{k_j} \ln \gamma$ must fall into the interval $I_{N_j}$.

The sequence $m_k$ is an increasing sequence of natural numbers, so $m_{k+1} - m_k \ge 1$ for all $k$.
The sequence $m_k \ln \gamma$ is strictly increasing, and the difference between consecutive terms is $(m_{k+1}-m_k)\ln\gamma \ge \ln\gamma$.
Let $k_0$ be large enough such that $m_{k+1}-m_k \ge 1$ for all $k \ge k_0$.
Let $N_0$ be large enough such that for all $N \ge N_0$, $\ln(1+1/N!) < \ln\gamma$.
For $N \ge N_0$, the length of the interval $I_N$ is $\ln(1+1/N!) < \ln\gamma$.

Consider the sequence $x_k = m_k \ln \gamma$ for $k \ge k_0$. It is a strictly increasing sequence and $x_{k+1} - x_k \ge \ln\gamma$.
The intervals $I_N$ for $N \ge N_0$ have lengths less than $\ln\gamma$.
Also, the gap between consecutive intervals $I_N$ and $I_{N+1}$ for $N \ge N_0$ is $\ln((N+1)!) - \ln(N!+1) = \ln(N+1) + \ln(N!) - \ln(N!+1) = \ln(N+1) - \ln(1+1/N!) \approx \ln(N+1)$ for large $N$. This gap tends to infinity as $N \to \infty$.

For large $N$, since the length of $I_N$ is less than $\ln\gamma$, and the gaps between intervals $I_N$ are large, at most one term $m_k \ln\gamma$ can fall into $I_N$.
Specifically, if $m_k \ln\gamma \in I_N$, then $m_k \ln\gamma < \ln(N!+1)$. The next term is $m_{k+1} \ln\gamma \ge m_k \ln\gamma + \ln\gamma \ge \ln(N!) + \ln\gamma$.
If $N$ is large enough so that $\ln(N!) + \ln\gamma > \ln(N!+1)$, then $m_{k+1} \ln\gamma$ cannot be in $I_N$. $\ln(N!) + \ln\gamma > \ln(N!+1)$ is $\ln\gamma > \ln(1+1/N!)$, which is true for $N \ge N_0$.
So for $N \ge N_0$, at most one $m_k$ can satisfy $m_k \ln\gamma \in I_N$.

This means that for $N \ge N_0$, the equality $\lfloor \gamma^{m_k} \rfloor = N!$ can hold for at most one value of $k$.
Since $\lfloor \gamma^{m_k} \rfloor \to \infty$ as $k \to \infty$, $N_j \to \infty$. For $j$ large enough, $N_j \ge N_0$.
Thus, for $j$ large enough, $\lfloor \gamma^{m_{k_j}} \rfloor = N_j!$ implies that $k_j$ must be unique for that value of $N_j$.
As $k \to \infty$, $N_k \to \infty$. The values $N_k$ are not necessarily all distinct.
But $m_k \ln \gamma$ is strictly increasing for $k \ge k_0$.
Let $k \ge k_0$. Let $N_k$ be the integer such that $\ln(N_k!) \le m_k \ln\gamma < \ln((N_k+1)!)$. $N_k$ is uniquely determined by $m_k$ for $N_k \ge 1$.
We have $\lfloor \gamma^{m_k} \rfloor = N!$ iff $m_k \ln\gamma \in [\ln N!, \ln N! + \ln(1+1/N!))$.
Let $N \ge N_0$. The interval $I_N$ has length $<\ln\gamma$.
The values $m_k \ln\gamma$ are separated by at least $\ln\gamma$.
Therefore, each interval $I_N$ can contain at most one value of $m_k \ln\gamma$.
This means $\lfloor \gamma^{m_k} \rfloor = N!$ for a given $N \ge N_0$ can occur for at most one value of $k$.
There are infinitely many $m_k$, so $N_k \to \infty$. For $k$ large enough, $N_k \ge N_0$.
So $\lfloor \gamma^{m_k} \rfloor$ can take a value $N!$ for $N \ge N_0$ for at most one $k$.
Since $\lfloor \gamma^{m_k} \rfloor$ is an increasing sequence for $k$ large enough, $\lfloor \gamma^{m_k} \rfloor = N_k!$ for some $N_k$ which is an increasing sequence of integers for large $k$.
This means that $\lfloor \gamma^{m_k} \rfloor$ can be a factorial $N!$ for only a finite number of $N < N_0$, and for $N \ge N_0$, it can be $N!$ for at most one $k$.
Thus, $\lfloor \gamma^{m_k} \rfloor$ belongs to the set $\{N! : N \ge 1\}$ for only a finite number of indices $k$.
Hence, $a_{\lfloor \gamma^{m_k} \rfloor} = 1$ for only a finite number of $k$.
This implies $a_{\lfloor \gamma^{m_k} \rfloor} \to 0$ as $k \to \infty$ for any $\gamma > 1$.

So, the sequence $(a_k)$ defined as $a_n = 1$ if $n=N!$ ($N \ge 1$) and $a_n=0$ otherwise, does not converge to 0, but satisfies the given condition for any sequence $(m_k)$ increasing to infinity.
Therefore, the statement "is that true that $a_k \to 0$?" is false.

The final answer is $\boxed{No}$.
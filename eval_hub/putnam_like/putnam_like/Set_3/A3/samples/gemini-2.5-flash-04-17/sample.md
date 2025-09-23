Let $N_G(n)$, $N_R(n)$, $N_B(n)$ be the number of green, red, and blue balls in the urn after $n$ moves. Initially, $N_G(0)=1$, $N_R(0)=1$, $N_B(0)=1$. The total number of balls is $N(0)=3$.
In each move, a ball is drawn, its color is noted, and it is returned along with two extra balls of the same color. If the $n$-th draw is of color $C$, the number of balls of color $C$ increases by 2.
Let $n_G, n_R, n_B$ be the number of times green, red, and blue balls are drawn in $n$ moves. The total number of moves is $n=90$. We are given that the red ball was drawn exactly $k=45$ times, so $n_R=45$. This implies $n_G + n_B = 90 - 45 = 45$.

The number of balls of each color after $n$ draws is $N_G(n) = 1+2n_G$, $N_R(n) = 1+2n_R$, $N_B(n) = 1+2n_B$. The total number of balls is $N(n) = 3+2(n_G+n_R+n_B) = 3+2n$.

This problem is a variation of Polya's urn scheme where $m=2$ balls are added. The probability of drawing a specific sequence of $n$ colors with $n_G$ green, $n_R$ red, and $n_B$ blue balls is given by the formula:
$$P(C_1, \dots, C_n) = \frac{\prod_{i=G,R,B} a_i^{(n_i, m)}}{A^{(n, m)}}$$
where $a_G=a_R=a_B=1$, $A=a_G+a_R+a_B=3$, $m=2$. The rising factorial is $x^{(k,m)} = x(x+m)\dots(x+(k-1)m)$.
$$1^{(k, 2)} = 1 \cdot 3 \cdot 5 \cdots (1+2(k-1)) = 1 \cdot 3 \cdot 5 \cdots (2k-1) = (2k-1)!!$$
$$3^{(n, 2)} = 3 \cdot 5 \cdot 7 \cdots (3+2(n-1)) = 3 \cdot 5 \cdot 7 \cdots (2n+1) = (2n+1)!!$$
The probability of any specific sequence with $n_G$ G's, $n_R$ R's, $n_B$ B's is:
$$P(\text{sequence}) = \frac{(2n_G-1)!! (2n_R-1)!! (2n_B-1)!!}{(2n+1)!!}$$
Note that $(-1)!!=1$. This formula holds for $n_i=0$.

We are interested in the total probability of having $n_R=45$ in $n=90$ moves. This is the sum of probabilities of all sequences with $n_R=45$. The number of such sequences for given $n_G, n_R, n_B$ is $\binom{n}{n_G, n_R, n_B}$.
We sum over all possible values of $n_G$ and $n_B$ such that $n_G+n_B=45$.
$$P(n_R=45) = \sum_{n_G=0}^{45} \binom{90}{n_G, 45, 45-n_G} \frac{(2n_G-1)!! (2 \cdot 45-1)!! (2(45-n_G)-1)!!}{(2 \cdot 90+1)!!}$$
$$P(n_R=45) = \sum_{n_G=0}^{45} \frac{90!}{n_G! 45! (45-n_G)!} \frac{(2n_G-1)!! (89)!! (90-2n_G-1)!!}{(181)!!}$$
Let $k=45$ and $n=90$. $n_B = n-k-n_G$.
$$P(n_R=k) = \sum_{n_G=0}^{n-k} \frac{n!}{n_G! k! (n-k-n_G)!} \frac{(2n_G-1)!! (2k-1)!! (2(n-k-n_G)-1)!!}{(2n+1)!!}$$
$$P(n_R=k) = \frac{n! (2k-1)!!}{k! (2n+1)!!} \sum_{n_G=0}^{n-k} \frac{1}{n_G! (n-k-n_G)!} (2n_G-1)!! (2(n-k-n_G)-1)!!$$
Let $N=n-k$. The sum is $\sum_{n_G=0}^{N} \frac{(2n_G-1)!! (2N-2n_G-1)!!}{n_G! (N-n_G)!}$.
Using the relation $(2j-1)!! = \frac{(2j)!}{j! 2^j}$, the sum becomes:
$$\sum_{n_G=0}^{N} \frac{1}{n_G! (N-n_G)!} \frac{(2n_G)!}{n_G! 2^{n_G}} \frac{(2N-2n_G)!}{(N-n_G)! 2^{N-n_G}} = \frac{1}{2^N} \sum_{n_G=0}^{N} \frac{N!}{n_G!(N-n_G)!} \frac{(2n_G)!}{n_G! n_G!} \frac{(2N-2n_G)!}{(N-n_G)! (N-n_G)!} \frac{n_G!(N-n_G)!}{N!}$$
$$= \frac{1}{2^N N!} \sum_{n_G=0}^{N} \binom{N}{n_G} \binom{2n_G}{n_G} \binom{2N-2n_G}{N-n_G} n_G! (N-n_G)!$$
The sum is $\sum_{n_G=0}^{N} \frac{1}{n_G! (N-n_G)!} \frac{(2n_G)! (2N-2n_G)!}{(n_G!)^2 ((N-n_G)!)^2} = \sum_{n_G=0}^N \binom{N}{n_G}^{-1} \binom{2n_G}{n_G} \binom{2N-2n_G}{N-n_G}$.

Let's check the sum calculation again:
Sum $= \sum_{j=0}^{N} \frac{1}{j!(N-j)!} \frac{(2j)!}{j! 2^j} \frac{(2N-2j)!}{(N-j)! 2^{N-j}} = \frac{1}{2^N} \sum_{j=0}^N \frac{(2j)! (2N-2j)!}{(j!)^2 ((N-j)!)^2} = \frac{1}{2^N} \sum_{j=0}^N \binom{2j}{j} \binom{2N-2j}{N-j}$.
Using the identity $\sum_{j=0}^N \binom{2j}{j} \binom{2N-2j}{N-j} = 4^N$.
The sum is $\frac{1}{2^N} 4^N = 2^N$.

So, $P(n_R=k) = \frac{n! (2k-1)!!}{k! (2n+1)!!} (n-k)! 2^{n-k} = \frac{n!}{k!(n-k)!} (n-k)! \frac{(2k-1)!! 2^{n-k}}{(2n+1)!!} = \binom{n}{k} \frac{(2k-1)!! 2^{n-k}}{(2n+1)!!}$.

Now substitute $n=90$ and $k=45$:
$$P(n_R=45) = \binom{90}{45} \frac{(2 \cdot 45-1)!! 2^{90-45}}{(2 \cdot 90+1)!!} = \binom{90}{45} \frac{(89)!! 2^{45}}{(181)!!}$$
Using $\binom{90}{45} = \frac{90!}{45! 45!}$, $(89)!! = \frac{90!}{45! 2^{45}}$, and $(181)!! = \frac{182!}{91! 2^{91}}$:
$$P(n_R=45) = \frac{90!}{45! 45!} \frac{\frac{90!}{45! 2^{45}} 2^{45}}{\frac{182!}{91! 2^{91}}} = \frac{90!}{45! 45!} \frac{\frac{90!}{45!}}{\frac{182!}{91! 2^{91}}} = \frac{(90!)^2}{(45!)^2 45!} \frac{91! 2^{91}}{182!}$$
Using $182! = 182 \cdot 181! = 2 \cdot 91 \cdot 181!$:
$$P(n_R=45) = \frac{(90!)^2}{(45!)^3} \frac{91! 2^{91}}{2 \cdot 91! 181!} = \frac{(90!)^2 2^{90}}{(45!)^3 181!}$$

Final check: $n=2, k=1$: $P(n_R=1) = \binom{2}{1} \frac{(1)!! 2^{1}}{5!!} = 2 \cdot \frac{1 \cdot 2}{15} = \frac{4}{15}$.
Using the formula: $\frac{(2!)^2 2^2}{(1!)^3 5!} = \frac{4 \cdot 4}{1 \cdot 120} = \frac{16}{120} = \frac{2}{15}$.

Let's check $(2k-1)!! = \frac{(2k)!}{k! 2^k}$.
$P(n_R=k) = \frac{n!}{k!(n-k)!} \frac{(2k)!/(k! 2^k) 2^{n-k}}{(2n+1)!/(n! 2^n)} = \frac{n!(2k)!n!2^n 2^{n-k}}{k!(n-k)!k!2^k (2n+1)!} = \frac{(n!)^2 (2k)! 2^{2n-2k}}{(k!)^2 (n-k)! (2n+1)!}$.
For $n=2, k=1$: $\frac{(2!)^2 (2)! 2^{4-2}}{(1!)^2 (1)! (5)!} = \frac{4 \cdot 2 \cdot 4}{1 \cdot 1 \cdot 120} = \frac{32}{120} = \frac{4}{15}$. This matches.

So the formula is $P(n_R=k) = \frac{(n!)^2 (2k)! 2^{2n-2k}}{(k!)^2 (n-k)! (2n+1)!}$.
For $n=90, k=45$:
$$P(n_R=45) = \frac{(90!)^2 (2 \cdot 45)! 2^{2 \cdot 90 - 2 \cdot 45}}{(45!)^2 (90-45)! (2 \cdot 90+1)!} = \frac{(90!)^2 (90)! 2^{180-90}}{(45!)^2 45! (181)!} = \frac{(90!)^3 2^{90}}{(45!)^3 181!}$$

The final answer is $\boxed{\frac{(90!)^3 2^{90}}{(45!)^3 181!}}$.
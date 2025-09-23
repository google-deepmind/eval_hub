```markdown
# Problem Statement

Let
\[
\mathcal{D} := \{ pq \ : \ p,q \in \mathbb{P}\},
\]
where \(\mathbb{P}\) is the set of all primes. In other words, \(\mathcal{D}\) is the set of all numbers that can be written as a product of two primes (not necessarily distinct). Our goal is to determine the maximum possible length of a sequence of consecutive integers that all belong to \(\mathcal{D}\).

# Key Observations

1. **Even Semiprimes:**  
   Any even number in \(\mathcal{D}\) (other than \(4\)) must be of the form
   \[
   2p,
   \]
   where \(p\) is an odd prime. Such a number satisfies
   \[
   2p \equiv 2 \pmod{4}.
   \]
   Therefore, apart from \(4 = 2 \times 2\), no even semiprime is divisible by \(4\).

2. **Consecutive Integers and Divisibility by 4:**  
   In any block of four consecutive integers, one of them is divisible by \(4\). For numbers greater than \(4\), the integer divisible by \(4\) cannot be in \(\mathcal{D}\) because an even number in \(\mathcal{D}\) that is not \(4\) must be congruent to \(2 \pmod{4}\).

# Implication for the Sequence Length

- **Block of 4 Consecutive Integers:**  
  Suppose there is a block \(n, n+1, n+2, n+3\) with all members in \(\mathcal{D}\). One of these numbers must be divisible by \(4\). As argued above, unless that number is \(4\) itself, it cannot be a semiprime. Since in any nontrivial block all numbers will eventually be larger than \(4\), a block of four consecutive semiprimes is impossible.

- **Existence of a Block of 3 Consecutive Integers:**  
  An explicit example of three consecutive integers in \(\mathcal{D}\) is:
  \[
  \begin{aligned}
  33 &= 3 \times 11,\\[1mm]
  34 &= 2 \times 17,\\[1mm]
  35 &= 5 \times 7.
  \end{aligned}
  \]
  All three numbers are products of two primes, so they belong to \(\mathcal{D}\).

# Conclusion

Since a block of four consecutive integers in \(\mathcal{D}\) cannot occur (due to the divisibility by 4 argument) and we have an explicit example of a block of three consecutive integers in \(\mathcal{D}\), the maximal length of such a sequence is

\[
\boxed{3}.
\]
```
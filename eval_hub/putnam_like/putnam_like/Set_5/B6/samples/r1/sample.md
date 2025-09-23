

To prove that the function \( f(t) \) is non-increasing on \([0,1]\), we use a coupling argument considering the downward-closed property of the family \( \mathcal{F} \).

### Key Steps:

1. **Coupling Argument**:
   - For \( t_1 < t_2 \) in \([0,1]\), construct a coupling between two random subsets \( A_1 \) and \( A_2 \) where each element is included independently with probabilities \( t_1 \) and \( t_2 \) respectively. This coupling ensures \( A_1 \subseteq A_2 \) almost surely.
   - Since \( \mathcal{F} \) is downward-closed, if \( A_2 \in \mathcal{F} \), then all subsets of \( A_2 \), including \( A_1 \), must also be in \( \mathcal{F} \). Thus, \( A_2 \in \mathcal{F} \) implies \( A_1 \in \mathcal{F} \).

2. **Probability Comparison**:
   - The probability that \( A_2 \in \mathcal{F} \) is at most the probability that \( A_1 \in \mathcal{F} \). This is because the event \( \{A_2 \in \mathcal{F}\} \) is a subset of the event \( \{A_1 \in \mathcal{F}\} \).
   - Therefore, \( f(t_2) = \Pr(A_2 \in \mathcal{F}) \leq \Pr(A_1 \in \mathcal{F}) = f(t_1) \), showing that \( f(t) \) is non-increasing.

### Conclusion:
Using the coupling argument and the downward-closed property of \( \mathcal{F} \), we conclude that \( f(t) \) is non-increasing on \([0,1]\).

\[
\boxed{f(t) \text{ is non-increasing on } [0,1].}
\]
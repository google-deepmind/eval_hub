```markdown
**Solution.**  
Set 
\[
S \;=\;\sum_{i=1}^n a_i\,.
\]
We give a combinatorial‐counting proof.

1.  Let \(X\) be the set of all functions 
   \[
     f\colon [S]\;\longrightarrow\;[S],
   \]
   where \([S]=\{1,2,\dots,S\}\).  Clearly 
   \(\lvert X\rvert=S^S\).

2.  Let \(\Pi\) be the set of all ways to *partition* the set \([S]\)
   into \(n\) *labeled* blocks of sizes \(a_1,a_2,\dots,a_n\).  
   By elementary counting
   \[
     \lvert\Pi\rvert
     \;=\;
     \frac{S!}{a_1!\,a_2!\,\cdots\,a_n!}\,.
   \]

3.  Hence the total number of *pairs* \((\pi,f)\) with
   \(\pi\in\Pi\) and \(f\in X\) is
   \[
     |\Pi|\;\times\;|X|
     \;=\;
     \frac{S!}{a_1!\,\cdots\,a_n!}\;S^S\,. 
   \]

4.  Now fix a permutation \(\sigma\in S_n\) and count only those
   pairs \((\pi,f)\) in which the function \(f\) *respects* the
   block‐structure in the sense that
   \[
     f\bigl(\text{block }i\bigr)
     \;\subseteq\;
     \text{block }\sigma(i),
     \qquad i=1,\dots,n.
   \]
   Given one specific partition \(\pi\), the number of such
   block‐respecting \(f\) is
   \(\prod_{i=1}^n a_i^{\,a_{\sigma(i)}}\).  Hence
   \[
     \bigl|\{\,( \pi,f)\text{ respecting }\sigma\}\bigr|
     \;=\;
     \frac{S!}{a_1!\cdots a_n!}
     \;\times\;
     \prod_{i=1}^n a_i^{\,a_{\sigma(i)}}.
   \]

5.  Since *every* function in \(X\) contributes to the unrestricted
   count but only a subset of them respect the block‐map condition,
   we have the strict inequality
   \[
     \frac{S!}{a_1!\cdots a_n!}\;S^S
     \;>\;
     \frac{S!}{a_1!\cdots a_n!}\;
     \prod_{i=1}^n a_i^{\,a_{\sigma(i)}}.
   \]
   Canceling the common factor \(S!/(a_1!\cdots a_n!)>0\) yields
   \[
     S^S\;>\;\prod_{i=1}^n a_i^{\,a_{\sigma(i)}}.
   \]
   Equivalently,
   \[
     \frac{S^S}{S!}\;>\;
     \frac{\prod_{i=1}^n a_i^{\,a_{\sigma(i)}}}
          {\prod_{i=1}^n a_i!}\,,
   \]
   which is exactly the desired inequality
   \[
     \frac{\bigl(\sum_{i=1}^n a_i\bigr)^{\sum_{i=1}^n a_i}}
          {\bigl(\sum_{i=1}^n a_i\bigr)!}
     \;>\;
     \frac{\prod_{i=1}^n a_i^{\,a_{\sigma(i)}}}
          {\prod_{i=1}^n (a_i!)}.
   \]
This completes the proof.  \(\Box\)
```
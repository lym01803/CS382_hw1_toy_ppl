# Calculate PPL of the Student ID

## Pipeline

0. Prepare: 

   Read n-grams model (the given cs382_1.arpa file here). Save the $\log p$ and $\log backof\!fweight$ information in dictionary.

1. Read a sentence (here the Student ID), and tokenize it.

   1. Split by character.
   2. Add ```<s>``` and ```</s>``` to the head and tail of the tokens sequence.

2. Calculate log-probability likelihood according to:

   $$\log P=\sum_{i=1}^{length} \log \mathtt{Pr}(w_i|W_{i-n+1}^{i-1})$$

   Use the back-off trick when the n-gram not hit in the model:

   $$\log \mathtt{Pr}(w_i|W_{i-n+1}^{i-1})\leftarrow\log\mathtt{Pr}(w_i|W_{i-n+2}^{i-1}) + \log \alpha(W_{i-n+1}^{i-1})$$

3. Calculate the ppl:

   $$ppl=2^{-\frac{1}{length}\cdot\log_2 P}=2^{-\frac{1}{length}\cdot \log_2 10\cdot \log_{10} P}$$

## Implementation

Manual calculation (very trivial) or write a simple script to calculate.

## Example 

For 021033210023: tokenize it and get ```<s>, 0, 2, 1, 0, 3, 3, 2, 1, 0, 0, 2, 3, </s>``` 

$$\begin{array}{ll}\lg P &= \lg\mathtt{Pr}(0|<s>) + \lg \mathtt{Pr}(2|<s>,0)+ \lg\mathtt{Pr}(1|0, 2) + \lg\mathtt{Pr}(0|2, 1) + \lg\mathtt{Pr}(3|1, 0) + \cdots+\lg\mathtt{Pr}(</s>|2, 3)\\ &=-2.2372083-0.8515801-0.2787536-1.3873339-0.3646991-\cdots-0.8381492=-15.816092327000002\end{array}$$

$ppl=2^{\log_2{10}\cdot\frac{1}{13}\cdot (-\lg P)}=16.467303381304$

## Result

| Student ID   | ppl                |
| :----------- | ------------------ |
| 021033210023 | 16.467303381304376 |
| 019033910051 | 14.362460442062687 |
| 120033910006 | 14.77486909890981  |
| 120033910013 | 10.13764419662622  |




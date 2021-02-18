### C
The first C solution of yours was recognized as a correct submission.

The idea was roughly as follows
- Starting from `head`, find the longest possible arithmetic slice
- Then all the intermediate arithmetic slices can be calculated, given `n_sub(head, tail)`
- Next, start all over again with `head = tail - 1`


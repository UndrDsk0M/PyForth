\ Calculate ( (5 3 + 2 * 10 mod) dup swap 1000 + . )
5 3 + 2 * 10 mod dup swap 1000 + .
\ Now test stack manipulation
10 20 30 dup swap over + . drop
\ Nested arithmetic and stack ops
100 5 mod 3 * 2 + dup . swap 50 - .
\ Edge case: underflow
drop drop drop drop
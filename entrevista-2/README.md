# Enunciado
Write a function called run_length_encode that takes a string of uppercase letters as input and returns the run-length encoded version of that string.
Run-length encoding is a simple form of data compression that replaces consecutive data elements (characters) with a single data value and count. For this exercise, a run of data is encoded as the character followed by the number of times it appears.


Test cases
```
"AABBBCCCC" would be encoded as "A2B3C4"
"WWWWWWWWWWWWBWWWWWWWWWWWWB" would be encoded as "W12B1W12B1"
"ABCDE" would be encoded as "A1B1C1D1E1"
```

Your function should handle any string of uppercase letters. If the count of consecutive characters is 1, you should still include the count in the output.

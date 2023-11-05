We are looking at finding the occurrence of the digits in the decimal representation of factorials. You are asked to implement a function that will determine number of occurrences of each decimal digit in numbers as large as 366 factorial (366!), which has 781 digits.

Recall that the definition of n! (that is, n factorial) is just `1 × 2 × 3 × · · · × n`.

The signature of your function should be:

```python
def solve(input_int: int) -> dict
```

You may implement other functions called by your `solve` function if you wish.

## Input Spec

The function should take 1 input: an integer for which the digit counts are desired. This input value will be less than or equal to 366 and greater or equal to 0. Note that `0! = 1`.

## Output Spec

The function should return a dictionary that contains a mapping of the decimal and the number of occurrences.

If the number provided in the input is outside the specified range (0-366), the outputted mapping should present zero values for all decimals.

## Sample Input & Output

| Sample number | Input (int) | Output (Dict[str, int])                                                                     |
| ------------- | ----------- | ------------------------------------------------------------------------------------------- |
| 1             | `3`         | `{"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 1, "7": 0, "8": 0, "9": 0}`          |
| 2             | `8`         | `{'0': 2, '1': 0, '2': 1, '3': 1, '4': 1, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}`          |
| 2             | `100`       | `{'0': 30, '1': 15, '2': 19, '3': 10, '4': 10, '5': 14, '6': 19, '7': 7, '8': 14, '9': 20}` |

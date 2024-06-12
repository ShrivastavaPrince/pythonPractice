Task #1

Question 1:
Explain the difference between the = operator and the == operator in Python.

Answer:
- The = operator is the assignment operator in Python. It's used to assign a value to a variable.
  Example:
    x = 5

- The == operator is the equality operator. It's used to compare two values to see if they are equal.
  It returns True if the values are equal, and False otherwise.
  Example:
    x == 5  # This will evaluate to True

Question 2:
What does the ** operator do in Python, and how is it used?

Answer:
- The ** operator is the exponentiation operator in Python. It's used to raise the left operand to the power of the right operand.
  Example:
    x = 2
    y = 3
    result = x ** y  # This will assign 2^3 = 8 to the variable result

Question 3:
What does the ^ operator do in Python, and in what context is it commonly used?

Answer:
- The ^ operator is the bitwise XOR (exclusive OR) operator in Python.
  It performs a bitwise XOR operation between the bits of two operands. It returns 1 if the corresponding bits are different, and 0 otherwise.
  Example:
    x = 5
    y = 3
    result = x ^ y  # This will perform a bitwise XOR between 5 (0101 in binary) and 3 (0011 in binary), resulting in 6 (0110 in binary)

- The ^ operator can be commonly used in cryptography, error detection and correction algorithms, and certain bitwise manipulation tasks.

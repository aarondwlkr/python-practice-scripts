# Aaron Walker

# Ask the user to enter two boolean values (1 or 0)
UserInput1 = int(input("Pick a number (1 or 0): "))
UserInput2 = int(input("Pick another number (1 or 0): "))

# Logical operators
AndStatement = UserInput1 and UserInput2
OrStatement = UserInput1 or UserInput2
NotStatement1 = not UserInput1
NotStatement2 = not UserInput2

# Print the results of the logical operations
print("\nLogical Operations")
print("AND:", AndStatement)
print("OR:", OrStatement)
print("NOT first input:", NotStatement1)
print("NOT second input:", NotStatement2)

# Bitwise operators
FirstNumber = 5
SecondNumber = 3

# Perform the bitwise operations
AndBit = FirstNumber & SecondNumber
OrBit = FirstNumber | SecondNumber
XorBit = FirstNumber ^ SecondNumber
NegBit1 = ~FirstNumber
NegBit2 = ~SecondNumber
LeftBit1 = FirstNumber << 1
LeftBit2 = SecondNumber << 1
RightBit1 = FirstNumber >> 1
RightBit2 = SecondNumber >> 1

# Print the numbers in binary
print("\nOriginal Numbers")
print("5 =", bin(FirstNumber))
print("3 =", bin(SecondNumber))

# Print the results of the bitwise operations in binary
print("\nBitwise Operations")
print("5 & 3 =", bin(AndBit))
print("5 | 3 =", bin(OrBit))
print("5 ^ 3 =", bin(XorBit))
print("~5 =", bin(NegBit1))
print("~3 =", bin(NegBit2))
print("5 << 1 =", bin(LeftBit1))
print("5 >> 1 =", bin(RightBit1))
print("3 << 1 =", bin(LeftBit2))
print("3 >> 1 =", bin(RightBit2))

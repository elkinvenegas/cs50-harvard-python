# -------------------------------------
# Addition using int

# Request two integers from the user
# x = int(input("What's x? " ))
# y = int(input("What's y? " ))

# Add them together
# z = x + y

# Print the result
# print(z)

# Example
# What's x? 3
# What's y? 2
# Output: 5

# The above is equivalent to:

# x = input("What's x? " )
# y = input("What's y? " )
# z = int(x) + int(y)
# print(z)

# or written more compactly
# print(int(input("what's x? ")) + int(input("what's y? ")))

# All three versions are valid, but the first one is the clearest and most commonly used.

                                          
# ------------------------------------------


# Addition using float

# Request two floating-point numbers from the user
# x = float(input("What's x? " ))
# y = float(input("What's y? " ))

# Add them
# z = x + y

# Print the result
# print (z)

# Example

# What's x? 2.56
# What's y? 3.25
# Output: 5.8100000000000005

# To make the result cleaner, we can round it:

# z = round(x + y)
# print(z) 
# Output: 6 (Rounded to the nearest whole number)

# We can also format large numbers with commas:

# Example without commas:

# What's x? 999
# What's y? 1
# Output 1000

# But if we put a function: print(f"{z:,}"), the comma will appear:

# What's x? 999
# What's y? 1
# 1,000

#-------------------------------------------

# Division and rounding to 2 decimal places

# Request two floating-point numbers
# x = float(input("What's x? " ))
# y = float(input("What's y? " ))

# Divide

# z = x/y
# print(z)

# What's x? 2
# What's y? 3
# Output: 0.6666666666666666

# But there are many digits, so we can use the function (f"{z:.2f}") to specify how many digits
# should appear after the decimal point.

# z = round(x/y,2)
# print (z)
# Output: 0.67

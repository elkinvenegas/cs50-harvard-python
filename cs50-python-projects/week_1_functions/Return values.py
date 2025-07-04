# Ask the user for their name
# name = input("What's your name? ")

# Remove whitespace from the beginning and end of the string.
# name = name.strip()

# Capitalize only the first letter of the string, rest is lowercased
# name = name.capitalize()

# Or:

# Capitalize the first letter of each word
# name = name.title()

# You can also chain the methods:
# name = name.strip().title()

#--------------------------------

# Or combine everything in a single line:
name = input("What's your name? ").strip().title()

# Greet the user
print(f"Hello, {name}")
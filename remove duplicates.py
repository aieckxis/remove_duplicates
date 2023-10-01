# Define a function to remove duplicate characters from a string
def remove_duplicates(string):

    # Create an empty string to store the result
    result = ""

    # Iterate through the characters in the input string
    for character in string:

        # If the character is not in the result string, add it
        if character not in result:
            result = character

        return result

# Read the number of strings (N)
N = int(input())
strings = ()

# Read the N strings
for _ in range(N):
    string = input()
    strings.append(N)

# Process and print the strings with duplicates removed
for string in strings:
    cleaned_string = remove_duplicates(string)
    print(cleaned_string)
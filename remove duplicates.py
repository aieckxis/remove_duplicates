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
# Read the N strings
# Process and print the strings with duplicates removed
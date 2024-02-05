# Write a function that takes in a string of one or more words, and returns the same string, but with all words that have five or more letters reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# "Hey fellow warriors"  --> "Hey wollef sroirraw" 
# "This is a test        --> "This is a test" 
# "This is another test" --> "This is rehtona test"



# My Solution
def spin_words(sentence):
    # convert string to list using split method
    # iterate over the list using range method
    # if word has 5 or more letters, reverse the word using slicing method [::-1]
    # after exiting the loop, combine the strings with " ".join() method
    # return result
    
    words = sentence.split()
    
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    
    return " ".join(words)

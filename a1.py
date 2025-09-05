# Assignment 1: AI-Generated Python Problems
# Name: [Your Name Here]

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[Paste the prompt you used to generate your problem set here]

Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."

I'm learning AI in a high school programming class. 
I have some experience with Python but need to refresh to learn AI. Can you create 5 practice problems that cover the basic info?"
"""



# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Problem Title/Description]
[Copy the complete problem description from your AI assistant]

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""

"""
Problem 1: Normalize a List of Numbers

Topic: Lists, functions, math
Description:
Write a function normalize(lst) that takes a list of numbers and returns a new list where each number is divided by
 the maximum in the list (so the biggest number becomes 1.0). This is a simple form of feature scaling, which is common in AI.

answer:
 def normalize(lst):
    max_value = max(lst)
    return [x / max_value for x in lst]

# Example
print(normalize([2, 4, 10]))  # Output: [0.2, 0.4, 1.0]


 
 Problem 2: Count Word Frequencies

Topic: Strings, dictionaries, basic NLP idea
Description:
Ask the user for a sentence. Convert it to lowercase, remove punctuation, and count how many times each word appears. 
Return the result as a dictionary.
 Input: "AI is cool. AI is the future."
Output: {'ai': 2, 'is': 2, 'cool': 1, 'the': 1, 'future': 1}

answer:
import string

def count_words(sentence):
    # Lowercase and remove punctuation
    sentence = sentence.lower()
    for char in string.punctuation:
        sentence = sentence.replace(char, "")
        
    words = sentence.split()
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    return freq

# Example
print(count_words("AI is cool. AI is the future."))
# Output: {'ai': 2, 'is': 2, 'cool': 1, 'the': 1, 'future': 1}


Problem 3: Predict Student Pass/Fail

Topic: Functions, conditionals, lists
Description:
Write a function predict_pass(grades) that takes a list of grades and 
returns "Pass" if the average is 60 or above, otherwise "Fail".

def predict_pass(grades):
    average = sum(grades) / len(grades)
    if average >= 60:
        return "Pass"
    else:
        return "Fail"

# Examples
print(predict_pass([70, 65, 80]))  # Output: "Pass"
print(predict_pass([40, 55, 50]))  # Output: "Fail"




Problem 4: One-Hot Encoding Simulator

Topic: Lists, dictionaries
Description:
One-hot encoding is used in AI to convert categories into numbers. Write a function one_hot_encode(data) that takes a list of categories (e.g., ["cat", "dog", "cat"]) and returns a list of one-hot encoded vectors.

def one_hot_encode(data):
    unique = list(set(data))
    encoding = {}
    
    for i, category in enumerate(unique):
        vector = [0] * len(unique)
        vector[i] = 1
        encoding[category] = vector

    return encoding

# Example
print(one_hot_encode(["cat", "dog", "fish"]))
# Output might be:
# {'fish': [1, 0, 0], 'dog': [0, 1, 0], 'cat': [0, 0, 1]}



Problem 5: Flatten a 2D List (like a matrix)

Topic: Nested loops, data structure prep
Description:
In AI, data often comes as 2D arrays (like images). Write a function to flatten a 2D list into a 1D list.

def flatten(matrix):
    flat_list = []
    for row in matrix:
        for item in row:
            flat_list.append(item)
    return flat_list

# Example
print(flatten([[1, 2], [3, 4]]))  # Output: [1, 2, 3, 4]

"""











# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
# Add your tests here

print("\nTesting Problem 2:")
# Add your tests here

print("\nTesting Problem 3:")
# Add your tests here

print("\nTesting Problem 4:")
# Add your tests here

print("\nTesting Problem 5:")
# Add your tests here



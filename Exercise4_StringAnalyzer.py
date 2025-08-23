# Function to analyze a sentence
#Author:samztitha
def analyze_sentence(sentence):
    vowels = "aeiouAEIOU"

    # Count words
    words = sentence.split()
    num_words = len(words)

    # Count vowels, consonants, uppercase, lowercase
    num_vowels = 0
    num_consonants = 0
    upper = 0
    lower = 0

    for ch in sentence:
        if ch.isalpha():              # Check only letters
            if ch in vowels:
                num_vowels += 1
            else:
                num_consonants += 1
        if ch.isupper():
            upper += 1
        if ch.islower():
            lower += 1

    # Find longest word (if words exist)
    longest = max(words, key=len) if words else ""

    # Print results
    print("Analysis Results:")
    print("Words:", num_words)
    print("Vowels:", num_vowels, "Consonants:", num_consonants)
    print("Uppercase:", upper, "Lowercase:", lower)
    print("Longest word:", longest)
    print("Reversed:", sentence[::-1])  # Reverse the whole sentence


# Main Program 
sentence = input("Enter a sentence: ").strip()

if sentence:  # Check input not empty
    analyze_sentence(sentence)
else:
    print("Empty input not allowed!")

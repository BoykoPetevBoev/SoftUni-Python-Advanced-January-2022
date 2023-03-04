def palindrome(word, index):
    reversed_word = list(word)
    reversed_word.reverse()
    reversed_word = "".join(reversed_word)

    if(word == reversed_word):
        return f"{word} is palindrome"
    else:
        return f"{word} is not palindrome"


print(palindrome("abcba", 0))	
print(palindrome("peter", 0))	

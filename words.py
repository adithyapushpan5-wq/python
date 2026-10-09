s = input("enter a sentence:")
print(s)
wordsList = s.split()
print(wordsList)
uniqueWords = set(wordList)
for word in uniqueWords:
 print(f"{word} occurs {wordList.count(word)}times")

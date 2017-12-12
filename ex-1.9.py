with open('test.txt') as f:
    words = f.read().split()

wordsToRemove=['się', 'i', 'oraz', 'nigdy','dlaczego']
print(words)
for word in words:
    if word in wordsToRemove:
        words.remove(word)

print(words)

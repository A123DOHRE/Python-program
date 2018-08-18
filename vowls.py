word = raw_input("input a word")
vowels = ('a', 'e', 'i', 'o', 'u')
for c in word:
    if c.lower() in vowels:
            word = word.replace (c,'0')
            print  (word)

# put your code here.

text = open('test.txt').read()
text = text.split()

dict_words = {}

for word in text:
    dict_words[word] = dict_words.get(word, 0) + 1

for key, value in dict_words.items():
    print(key, value)

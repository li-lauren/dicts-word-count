# put your code here.
import re
import sys
import collections

text = open(sys.argv[1]).read().lower()
text = re.split('\.| |\n|,|\?', text)

dict_words = {}

for word in text:
    dict_words[word] = dict_words.get(word, 0) + 1

# using collections.Counter
cnt = collections.Counter()
for word in text:
    cnt[word] += 1
print(cnt)

for key, value in dict_words.items():
    print(key, value)

# sort output by words alphabetically
for key, value in sorted(dict_words.items()):
    print(key, value)

# sort output by word count
for key, value in sorted(dict_words.items(), key=lambda item: item[1]):
    print(key, value)

# sort the output by word count, descending, then by word, ascending
sorted_dict = sorted(dict_words.items())
for key, value in sorted(sorted_dict, key=lambda item: item[1], reverse=True):
    print(key, value)




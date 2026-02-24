# 백준 1157번 단어 공부 브론즈 1

import sys

word = sys.stdin.readline().strip().upper()

set_word = list(set(word))

word_count = []
for w in set_word:
    word_count.append(word.count(w))

if word_count.count(max(word_count)) > 1:
    print('?')
else:
    print(set_word[word_count.index(max(word_count))])

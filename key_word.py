import re
from pathlib import Path
from collections import defaultdict
d = {}
count = 0
result = open('key_word_result.txt', 'w')
language_list = ["python", "c++", "C", "java", "objective-c",
                 "php", "basic", "ruby"]
for i in range(len(language_list)):
    path = language_list[i]+"_title.txt"
    result.write(language_list[i]+" key-word:"+"\n")

    with open(path, encoding='utf-8')as f:
        for line in f:
            words = re.split('\W|_', line)
            for word in filter(lambda word: word.lower() not in '', words):
                d[word] = d.get(word, 0)+1
    list = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for i in range(0, 30):
        result.write("rank: "+str(i)+": "+list[i][0] +
                     "              times: " + str(list[i][1])+"\n")
    result.write("\n\n")

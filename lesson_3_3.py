import re

phrase = str(input('Введите фразу:\n'))
words_count = len(re.split(r'[,\s]\s*', phrase))
print(words_count)
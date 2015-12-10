
count = 0
dictionary = {}
with open('recurrentWords.txt', 'r') as f:
   for line in f:
      for word in line.split():
         word = word.lower()
         dictionary[word] = dictionary[word] + 1 if word in dictionary else 1
         count += 1

print("Total of words: {}!".format(count))

for key in sorted(dictionary, key=dictionary.get, reverse=True):
   if dictionary[key] > 5:
      print("{}: {}".format(key, dictionary[key]))

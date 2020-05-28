sentence = input("Enter a sentence: ")
ls1 = []
ls2 = []
for i in sentence:
  ls1.append(i)
  ls2.append(sentence.count(i))
print(dict(zip(ls1, ls2)))

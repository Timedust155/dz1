text= input('введите слово')
text= list(text)
print(text)


for i in range(len(text)):
    nomer=text.count(text[i])
    test_list = list(set(text))
    if (len(test_list) <=i):
        break
    else:
        print(test_list[i]," - ",nomer)

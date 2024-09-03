# String Uzunluğunu Tapmaq
a="mən python öyrənirəm"
print(len(a))

# String-də Simvolların Dəyişdirilməsi
b="salam,dünya!"
print(b.replace("dünya","python"))


#String-i Böyük və Kiçik Hərflərə Çevirmək
c="Python"
print(c.upper())
print(c.lower())

#String-dəki Simvola Əsasən Hissə Seçmək
d="Python proqramlaşdırma dili"
searched_word = 'proqramlaşdırma'
index = d.find(searched_word)
print(d[index:index + len(searched_word)])


#Tapşırıq 5: String-in İçi Boş olub olmadığını yoxlamaq

e=""
if len(e)==0:
    print("empty")
else:
    print('full')


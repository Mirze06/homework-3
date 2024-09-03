#Bir list yaradın və ona bir neçə meyvə adı daxil edin: "alma", "banan", "portağal". Daha sonra bu list-i ekrana çıxarın
a=["alma", "banan", "portağal"]
print(a)

#Tapşırıq 2: List-ə Element Əlavə Etmək
a=["alma", "banan", "portağal"]
a.append("heyva")
print(a)

# Tapşırıq 3: List-dən Elementi Silmək
a=["alma", "banan", "portağal"]
a.remove("banan")
print(a)

#Tapşırıq 4: List-də Elementlərin Sayını Tapmaq
a=["alma", "banan", "portağal"]
print(len(a))

# Tapşırıq 5: List-i Tərsinə Çevirmək
a=["alma", "banan", "portağal"]
a.reverse()
print(a)

#Tapşırıq 10: List-in Elementlərini Yığcamlaşdırmaq
a=["alma", "banan", "portağal","alma", "banan", "portağal"]
print(list(set(a)))

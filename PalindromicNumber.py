number = int(input("Input Number: "))
holder = number
i = 0

while(number > 0):
    process = number % 10 #sayının son basamağını process değişkeninin içine atıyoruz.
    i = i * 10 + process #i değişkenini 10 ile çarpıp process'i ekliyoruz.
    number = number // 10 #sayıyı 10'a bölerek son basamağını iptal ediyoruz.

if(holder == i): #eğer kullanıcının girdiği sayı ile tersi eşitse bu sayı palindrom sayısıdır.
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")

"""
Örnek;

İLK ADIM:

152 sayısını modül 10 işlemi yaparak sayının ona bölümünden kalanı process içerisine atıyoruz.
Yani 2 sayısını process içerisine atıyoruz.
i'yi 10 ile çarpıp 2'yi ekliyoruz.
Sayıyı 10'a bölerek yeni sayıyı içine atıyoruz. 152 // 10 = 15

İKİNCİ ADIM:

Şu an sayımız 15.
15 sayısını modül 10 işlemi yaparak sayının ona bölümünden kalanı process içerisine atıyoruz.
Yani 5 sayısını process içerisine atıyoruz. 
i ilk adımdan 2 idi. Bu adımda 2 * 10 + 5 işlemi ile 25'i elde ediyoruz.
Sayıyı 10'a bölerek yeni sayıyı içine atıyoruz. 15 // 10 = 1

ÜÇÜNCÜ ADIM:

Şu an sayımız 1.
1 sayısını modül 10 işlemi yaparak sayının ona bölümünden kalanı process içerisine atıyoruz.
Yani 1 sayısını process içerisine atıyoruz.
i ikinci adımdan 25 idi. Bu adımda 25 * 10 + 1 işlemi ile 251'i elde ediyoruz.
Sayıyı 10'a bölerek yeni sayıyı içine atıyoruz. 1 // 10 = 0
while döngüsü sayı 0'dan büyük olduğu sürece çalışacağı için program döngüden çıkar.

* 1 / 10 = 0.1
* 1 // 10 = 0

"""
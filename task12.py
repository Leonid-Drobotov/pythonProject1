#      Задача 12: Петя и Катя – брат и сестра.
#Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y?1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.


sum_of_numbers = int(input('Введите сумму двух чисел: '))
product_of_numbers = int(input('Введите произведение двух чисел: '))
first_digit = (sum_of_numbers-int((sum_of_numbers**2-4*product_of_numbers)**0.5))//2
second_digit = (sum_of_numbers+int((sum_of_numbers**2-4*product_of_numbers)**0.5))//2
print(first_digit,second_digit)
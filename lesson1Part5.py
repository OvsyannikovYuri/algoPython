# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.


first_letter = input("введите первую букву")
second_letter = input("введите вторую букву")
first_letter = first_letter.upper()
second_letter = second_letter.upper()
alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н','О',
            'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


number1 = alphabet.index(first_letter) + 1
number2 = alphabet.index(second_letter) + 1
distance = abs(number2-number1)
print(number1, number2)
print(distance)




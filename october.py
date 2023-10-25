# 1
m = [3, 4, 1, 6, 2]
res = list (
    filter (lambda x: m.count (x) > len (m) // 2, m))  # сохраняем элемены которые встречаются только больше 2 раз
# список res содержит только отфильтрованные элементы
print (max (res) if res else 0)  # выводит максимальное значение из списка или 0

# 2
binary_number = "01010101"
decimal_number = 0  # переменная с десятичной системой
power = 0  # вычисляет степень
for digit in reversed (binary_number):  # обработка цифр в обратном порядка
    digit = int (digit)  # переводим строку в целое число
    decimal_number += digit * (2 ** power)  # значение текущей цифры умноженное на 2 в степени power
    power += 1  # увеличить степень на 1
print (decimal_number)


# 3
def string_to_int(s): #проверка первого символа строки
    return int(s) if s[0] != '-' else -int(s[1:]) #если первый символ не - ,строка s преобразуется в целое число с помощью int
s = '69'
num = string_to_int(s)
print(num) # Вывод: 69

# 4
def process_array(nums):
    nums = list (set (nums)) #из списка nums удаляем дубликаты

    if len (nums) % 2 != 0: #проверяет является кол-во элементов нечетными

        last_element = nums.pop () #сохраняет последний элемент если он нечетный
    else:
        last_element = None

#меняет местами элементы попарно
    for i in range (0, len (nums) - 1, 2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]

#добавляет последний элемент в конец списка nums
    if last_element:
        nums.append (last_element)

    return nums #возвращяет список

nums = [1, 2, 3, 3, 4, 5, 6]
result = process_array (nums)
print (result)


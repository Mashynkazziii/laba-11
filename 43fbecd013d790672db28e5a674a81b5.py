numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
def find_missing_number(numbers):
    for i in range(len(numbers)):
        if numbers[i] is None:  #условие
            numbers[i] = 0
            numbers[i] = sum(numbers)/len(numbers)   #действие
    return numbers



result = find_missing_number(numbers)
print("После замены missing number на среднее арифметическое:", result)

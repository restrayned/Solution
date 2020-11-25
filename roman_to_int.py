class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        entered_number = s.replace('', ' ').split()
        number = 0
        for i in roman_numerals:
            if i in entered_number:
                if entered_number.index(i) == 0:
                    number += roman_numerals.get(i)
                    entered_number.remove(i)
                    return number + self.romanToInt(''.join(entered_number))
                elif entered_number.index(i) > 0:
                    arr = ''.join(entered_number).split(i, maxsplit=1)
                    number += roman_numerals.get(i) - self.romanToInt(arr[0])
                    return number + self.romanToInt(''.join(arr[1]))
        return 0 
        
class_result = Solution()

#Вывод результата
print(class_result.romanToInt("III"))
print(class_result.romanToInt("IV"))
print(class_result.romanToInt("IX"))
print(class_result.romanToInt("LVIII"))
print(class_result.romanToInt("MCMXCIV"))
#Вывод результат

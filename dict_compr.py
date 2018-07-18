str1 = 'ABC'
str2 = '123'

combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)

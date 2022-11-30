numbers = [1, 2, 3, 4, 5, 6]
print('::'.join(str(x) for x in numbers))

numbers = list(range(1, 10 + 1))

print("# 홀수만 추출하기")
print(list(filter(lambda x: x % 2 ,numbers)))
print()

print("# 3이상, 7 미만인 수 추출하기")
print(list(filter(lambda x: x >= 3 and x < 7,numbers)))
print()

print("# 어떤 수를 제곱 했을 때, 50 미만이 되는 수 추출하기")
print(list(filter(lambda x: x ** 2 < 50,numbers)))
print()

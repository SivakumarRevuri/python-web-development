usr_input = [1,3,9,5,3,1,4,5,6,3,4,7,3,9]

result = []
size = len(usr_input)
for _ in range(size):
    if len(usr_input) != 0:
        num = usr_input[0]
        if num not in result:
            cnt = usr_input.count(num)
            for i in range(cnt):
                result.append(num)
                usr_input.remove(num)

print('================================')
print(result) # [1, 1, 3, 3, 3, 3, 9, 9, 5, 5, 4, 4, 6, 7]
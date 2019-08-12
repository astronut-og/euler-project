number_3 = 0
sum = 0
list = []
number_1 = 1
number_2 = 1
while number_3 < 4000000:
    number_3 = number_1 + number_2
    number_1 = number_2
    number_2 = number_3
    if(number_3%2==0):
        list.append(number_3)
for number in list:
    sum += number
print(sum)
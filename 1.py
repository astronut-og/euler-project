def divisible_by_3_or_5(number):
    """[summary]
    
    Arguments:
        number {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    if((number%3 == 0) or (number%5 == 0)):
        return True 
    else: return False

list = []
x = 0
while x < 1000:
    if(divisible_by_3_or_5(x)):
        list.append(x)
    x += 1
sum = 0
for x in list:
    sum += x
print(sum)


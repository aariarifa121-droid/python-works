
#wap to get the total digits in the number given.

number = 153        # 153// 10  15  `15// 10  1   1// 10  0`

count = 0

while(number > 0):    #153 > 0 , 15 >0 , 1> 0, 0>0

    number = number // 10 

    count += 1

print(f"the total number of digits is {count}")    
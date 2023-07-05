def checkPerfect(res):
    if(len(res)==0):
        return 0
    count=0
    for eachval in res:
        x=eachval[0]
        y=eachval[1]
        # print(min(x,y))
        # print(max(x,y))
        if (min(abs(x-y),abs(x+y)) <= min(abs(x),abs(y))) and (max(abs(x-y),abs(x+y)) >= max(abs(x),abs(y))):
            count = count+1
    return count


test_list = [2,1,0]
 
# printing original list 
print("The original list : " + str(test_list))
 
# All possible pairs in List
# Using list comprehension + enumerate()
res = [(a, b) for idx, a in enumerate(test_list) for b in test_list[idx + 1:]]
 
# printing result 
print("All possible pairs : " + str(res))

print(checkPerfect(res))

for i in range(6,10):
    print(i)

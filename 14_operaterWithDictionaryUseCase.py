# 項目：運算子範例2(and/or/not )與集合的介紹

s1 = {3,4,5}

print( 10 in s1)    #return false
print(10 not in s1) #return true

s2 = {4,5,6,7}
# AND
s3 = s1&s2
# OR
s4 = s1|s2
# XOR
s5 = s1-s2
# AND^
s6 =s1^s2

print(s3)
print(s4)
print(s5)
print(s6)
# 項目：使用字典進階版集合

s = set('abcdefg')  #data type SET

print(s)

print('does variables have a charater a?')
print('a' in s)

# -------------------------------------
# directory computing

dic  = {
    'apple':'fruit',
    'cat':'anime'
}

# get value
print('get value :')
print(dic['apple'])

# get SET value
print('set value :')
dic['apple'] = "little fruit"
print(dic['apple'])

# search index
print('Searching :')
print('apple' in dic)

# delete SET value
print('delete apple :')
del dic['apple']
print(dic)

# ------------------------------
# create directory
dic = { x:x*2 for x in [3,4,5,6,7]}
print(dic)





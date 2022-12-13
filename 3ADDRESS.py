inputexpression = input("Enter the equation : ")

expression = inputexpression;

x = expression.split()
res = []
id = 1
temp1 = " "

while len(x)> 3 :
    if('^' in x):
        oper = x.index('^')
        temp = "T" + str(id) + "=" + x[oper-1] + x[oper] + x[oper+1]
        res.append(temp)
        for i in range(3):
            del x[oper-1]
        x.insert(oper-1,"T"+str(id))
        id += 1
    elif('/' in x):
        oper = x.index('/')
        temp = "T" + str(id) + "=" + x[oper-1] + x[oper] + x[oper+1]
        res.append(temp)
        for i in range(3):
            del x[oper-1]
        x.insert(oper-1,"T"+str(id))
        id += 1
    elif ('*' in x):
        oper = x.index('*')
        temp = "T" + str(id) + "=" + x[oper - 1] + x[oper] + x[oper + 1]
        res.append(temp)
        for i in range(3):
            del x[oper - 1]
        x.insert(oper - 1, "T" + str(id))
        id += 1
    elif ('+' in x):
        oper = x.index('+')
        temp = "T" + str(id) + "=" + x[oper - 1] + x[oper] + x[oper + 1]
        res.append(temp)
        for i in range(3):
            del x[oper - 1]
        x.insert(oper - 1, "T" + str(id))
        id += 1
    elif ('-' in x):
        oper = x.index('-')
        temp = "T" + str(id) + "=" + x[oper - 1] + x[oper] + x[oper + 1]
        res.append(temp)
        for i in range(3):
            del x[oper - 1]
        x.insert(oper - 1, "T" + str(id))
        id += 1

for i in x:
    temp1 +=str(i)


res.append(temp1);

for i in res:
    print(i)
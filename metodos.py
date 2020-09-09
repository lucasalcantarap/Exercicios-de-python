spam = {'color':"red",'age':"42"}

for v in spam.values(): #metodo values
    print(v)

for k in spam.keys(): #metodo keys
    print(k)

for i in spam.items():
    print(i)

#spam = {'color': 'red', 'age': 42}
#for k, v in spam.items():
    #print('Key: ' + k + ' Value: ' + str(v))

    print('color' in spam.keys())
    print('42' in spam.values())
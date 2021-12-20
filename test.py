import collections


def create_list(message):
    list = dict(collections.Counter(message))
    for key, probability in list.items():
        print(key, ' : ', probability)
    list_sorted = sorted(iter(list.items()), key = lambda k_p:(k_p[1],k_p[0]),reverse=True)
    final_list = []
    for key,probability in list_sorted:
        final_list.append([key,probability,''])
    return final_list


def divide_list(list):
    if len(list) == 2:
        print([list[0]],[list[1]])
        return [list[0]],[list[1]]
    else:
        n= 0
        for i in list:
            n+= i[1]
        x = 0
        distance = abs(2*x - n)
        j = 0
        for i in range(len(list)):
            x += list[i][1]
            if distance < abs(2*x -n):
                j=i
    print(list[0:j+1], list[j+1:])
    return list[0:j+1], list[j+1:]

def label_list(list):
    list1,list2 = divide_list(list)
    for i in list1:
        i[2] += "0"
        c[i[0]] = i[2]
    for i in list2:
        i[2] += '1'
        c[i[0]] = i[2]
    if len(list1)==1 and len(list2)==1:
        return
    label_list(list2)
    return c

c = {}
message=input("Введите сообщение для сжатия:")
b = ''
for i in range(len(message)):
    b += bin(ord(message[i]))
b = b.replace("b", "")
print(b)

code = label_list(create_list(message))

encode=[]
for i in message:
    for key, probability in code.items():
        if key in i:
            print(key, ' : ', probability)
            encode.append(probability)
сompressed="".join(encode)
print("Сжатое сообщение:",сompressed)

decode=[]
for i in message:
    for probability,key in code.items():
        if probability in i:
            decode.append(probability)

print("".join(decode))

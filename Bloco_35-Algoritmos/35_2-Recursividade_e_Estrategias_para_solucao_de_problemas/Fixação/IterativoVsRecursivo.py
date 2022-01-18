# Eis uma solução que vamos usar de exemplo. A este método, que já conhecemos, chamamos de método Iterativo.

def reverse(list):
    reversed_list = []
    for item in list:
        reversed_list.insert(0, item)
        print(reversed_list)
    return reversed_list


# print(reverse([1, 2, 3, 4, 5,6,7,8]))

# Porém, lembre-se: onde pudermos aplicar iteração, podemos também aplicar recursão. E às vezes, a solução recursiva fica até mais simples! Quando dominarmos a recursão, há muitos problemas que poderemos resolver rapidamente algo que, de outra forma, seria muito trabalhoso de implementar.
# Uma solução recursiva:

def reverse2(list):
    result = []
    if len(list) < 2:
        return list
    else:
        # print("aaa", reverse2(list[1:]))
        # print("bbb", [list[0]])
        result.append(list[0])
        return reverse2(list[1:]) + result

print(reverse2([1, 2, 3, 4,5,6,7,8]))

# teste = [1,2,3,4]
# print(teste)
# print([teste[0]])
# print(teste[1:] + [teste[0]])
# reverse2(list[1:]) = 2, 3, 4, 5,6,7,8
while(True):
    string = input().split()
    n = int(string[0])
    d = int(string[1])
    if(n != 0 and d != 0):
        i = 0
        number = int(input())
        number_list = list(str(number))
        stack = []
        result = ''
        for numbers in number_list:
            numbers = int(numbers)
            stack.append(numbers)
        while i < d:
            stack.remove(min(stack))
            i += 1
        for i in range(0,len(stack)):
            result += str(stack[i])
        print(int(result))
    else:
        break
 #CODIGO EM CONSTRUCAO

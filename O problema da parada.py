def ADD(OP1,OP2,variables):
    try:
        add = int(OP1) + int(OP2)
    except ValueError:
    return int(OP1) + int(OP2)
def SUB(OP1,OP2):
    return int(OP1) - int(OP2)
def MOV(OP1,OP2):
    OP1 = OP2
    return int(OP1)
def DIV(OP1,OP2):
    try:
        return int(OP1)/int(OP2)
    except ZeroDivisionError:
        return 0
def MOD(OP1,OP2):
    try:
        return int(OP1) % int(OP2)
    except ZeroDivisionError:
        return 0
def getOperation(command, select_command):
    if(select_command == "ADD"):
        command[select_command] = ADD(op1,op2)
    elif(select_command == "SUB"):
        command[select_command] = SUB(op1,op2)
    elif(select_command == "MOV"):
        command[select_command] = MOV(op1,op2)
    elif(select_command == "DIV"):
        command[select_command] = DIV(op1,op2)
    elif(select_command == "MOD"):
        command[select_command] = MOD(op1,op2)
    result = command[select_command]
    return result
    
command = {"ADD":"","SUB":"","MOV":"","DIV":"","MOD":""}
string = input().split()
select_command = string[0]
op1 = string[1]
op2 = string[2]
result = getOperation(command, select_command)
print(result)

#CODIGO EM CONSTRUCAO

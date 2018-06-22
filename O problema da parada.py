def intvar(ivar,list_vars):
    try:
        ivar = int(ivar)
    except ValueError:
        if(isinstance(ivar,str)):
            ivar = variables[ivar]
    return int(ivar)

def ADD(OP1,OP2):
    OP1 = intvar(OP1,variables)
    OP2 = intvar(OP2,variables)
    variables["R9"] = int(OP1) + int(OP2)
    return variables["R9"]
def SUB(OP1,OP2):
    OP1 = intvar(OP1,variables)
    OP2 = intvar(OP2,variables)
    variables["R9"] = OP1 - OP2
    return variables["R9"]
def MOV(OP1,OP2):
    try:
        OP1 = int(OP1)
    except ValueError:
        if(isinstance(OP1,str)):
            variables[OP1] = OP2
    try:
        OP2 = int(OP2)
    except ValueError:
        if(isinstance(OP2,str)):
            OP2 = variables[OP2]
    variables["R9"] = OP2
    return variables["R9"]
def DIV(OP1,OP2):
    try:
        OP1 = intvar(OP1,variables)
        OP2 = intvar(OP2,variables)
        variables["R9"] = OP1 / OP2
        return variables["R9"]
    except ZeroDivisionError:
        variables["R9"] = 0
        return variables["R9"]
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
i = 0
string = input().split()
L = int(string[0])
N = int(string[1])
variables["R0"] = N
command = {"ADD":"","SUB":"","MOV":"","DIV":"","MOD":""}
variables = {"R0":0,"R1":0,"R2":0,"R3":0,"R4":0,"R5":0,"R6":0,"R7":0,"R8":0,"R9":0}
string = input().split()
select_command = string[0]
op1 = string[1]
op2 = string[2]
result = getOperation(command, select_command)
while(i < L):
    string = input().split()
    select_command = string[0]
    op1 = string[1]
    op2 = string[2]
    result = getOperation(command, select_command)
    i += 1

#CODIGO EM CONSTRUCAO

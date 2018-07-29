sequence = [int(input()) for i in range(101)]
occurence = [index for index in range(len(sequence)) if(sequence[-1]) == sequence[index] if index != 100]
print(*occurence, sep='\n')

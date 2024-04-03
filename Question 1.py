
def Convert_Currency(input_no):
    
    input_no = input_no[::-1]

    output = ""

    for i in range(len(input_no)):
        if i > 1 and (i - 3) % 2 == 0:
            output += ","
        output = output + input_no[i]
        
    output = output[::-1]

    return output

input_no = input("Enter the Number to convert into Indian Format :")
print(Convert_Currency(input_no))

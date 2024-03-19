standardform = input('Enter a number in scientific notation: ')
standardform = standardform.strip()


standardform_list = standardform.split('x10^')
mantissa = standardform_list[0]
exponent = standardform_list[1]
result = mantissa + 'E' + exponent

print(f'This number in E notation is {result}.')
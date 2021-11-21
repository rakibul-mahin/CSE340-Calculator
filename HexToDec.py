hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

hex_code = input('Please Enter all in Upper Case: ').upper()
bin_code = ''

for i in hex_code:
    if i in hex_to_bin:
        bin_code += hex_to_bin[i]
        bin_code += ' '

print(bin_code)
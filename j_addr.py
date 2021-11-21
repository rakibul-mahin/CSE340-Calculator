instruction = 'j 2011'
cmd = instruction.split()
pc = '1278A430'

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

hex_code = pc[0]
pc_part = ''

for i in hex_code:
    if i in hex_to_bin:
        pc_part += hex_to_bin[i]

pc_part = pc_part.zfill(4)

num = bin(int(cmd[1]))
num = str(num).replace('0b','')
num = num.zfill(26)
num_sll_two = num + "00"
final = pc_part + num_sll_two
print(final)
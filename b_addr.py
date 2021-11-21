def addition(mhb_prod, multiplicand):
    result = ''
    c = 0

    for i in range(len(mhb_prod) - 1, -1, -1):
        r = c
        r += 1 if mhb_prod[i] == '1' else 0
        r += 1 if multiplicand[i] == '1' else 0
        result = ('1' if r % 2 == 1 else '0') + result

        c = 0 if r < 2 else 1

    if c != 0:
        result += '1' + result

    return result

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

instruction = 'beq $1 $5 48'
pc_addr_hex = '1278A430'
cmd = instruction.split()

hex_code = pc_addr_hex
pc_bin = ''

for i in hex_code:
    if i in hex_to_bin:
        pc_bin += hex_to_bin[i]

num = cmd[3]

#First Convert to 16 bit binary number
sixteen_bit = bin(int(num)).replace('0b', '').zfill(16)
#SLL 16-bit binary number by 2
sll_sixteen_bit = sixteen_bit + '00'
#Extend by remaining bit
extension = '00000000000000' + sll_sixteen_bit

#Binary number of 4
const = bin(4).replace('0b','').zfill(32)

#ADD 4 with PC
pc_bin_add_4 = addition(const, pc_bin)

#Finally add (PC+4) with extended bit
target_address = addition(extension, pc_bin_add_4)
print(target_address)
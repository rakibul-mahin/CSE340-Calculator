reg_num = {
    '$t0': '01000',
    '$t1': '01001',
    '$t2': '01010',
    '$t3': '01011',
    '$t4': '01100',
    '$t5': '01101',
    '$t6': '01110',
    '$t7': '01111',
    '$t8': '11000',
    '$t9': '11001',
    '$s0': '10000',
    '$s1': '10001',
    '$s2': '10010',
    '$s3': '10011',
    '$s4': '10100',
    '$s5': '10101',
    '$s6': '10110',
    '$s7': '10111',
}

def mips_add(instruction):
    '''
    OP  RS  RT RD SHAMT FUNCT
    '''
    op = '000000'
    funct = 'xxxxxx'
    shamt = '00000'
    # add $t0 $s1 $t0
    cmd = instruction.split()
    rd = reg_num[cmd[1]] #Destination
    rs = reg_num[cmd[2]] #Source 1
    rt = reg_num[cmd[3]] #Source 2
    final = op+rs+rt+rd+shamt+funct
    print(f"{final} ===> R-Type")

def mips_sll(instruction):
    '''
    OP  RS  RT RD SHAMT FUNCT
    '''
    op = '000000'
    funct = 'xxxxxx'
    # sll $t0 $s1 1
    cmd = instruction.split()
    bin_num = int(cmd[3], 2)
    shamt = str(bin_num).zfill(5)
    rd = reg_num[cmd[1]]
    rs = reg_num[cmd[2]]
    rt = '000000'
    final = op+rs+rt+rd+shamt+funct
    print(f"{final} ===> R-Type")

def mips_addi(instruction):
    '''
    OP RS RT CONST.
    '''
    op = 'xxxxxx'
    cmd = instruction.split()
    rs = reg_num[cmd[2]]
    rt = reg_num[cmd[1]]
    bin_num = int(cmd[3])
    bin_num = bin(bin_num).replace('0b','')
    const = str(bin_num).zfill(16)
    final = op+rs+rt+const
    print(f"{final} ===> I-Type")

mips_add('add $t0 $s1 $t0')
mips_sll('sll $t0 $s1 1')
mips_addi('addi $s0 $t0 10')
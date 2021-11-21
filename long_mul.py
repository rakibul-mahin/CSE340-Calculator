multiplicand = '1100'
multiplier = '1010'
prod = ''
new_multiplicand = ''

for i in multiplier:
    new_multiplicand += '0'
new_multiplicand += multiplicand

for i in new_multiplicand:
    prod += '0'

print(f"Multiplicand: {multiplicand}")
print(f"Multiplier: {multiplier}")
print("Iteration  , Multiplicand, Multiplier, Product")
print(f"Iteration-0, {new_multiplicand}, {multiplier}, {prod}")

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

def right_shift(prod):
    rfirst = prod[0:len(prod)-1]
    rsecond = prod[len(prod)-1:]
    new = rsecond + rfirst
    a = []
    for i in new:
        a.append(i)
    a[0] = '0'
    final = ''
    for i in a:
        final += i

    return final

def left_shift(prod):
    lfirst = prod[0:1]
    lsecond = prod[1:]
    new = lsecond + lfirst
    a = []
    for i in new:
        a.append(i)
    a[0] = '0'
    final = ''
    for i in a:
        final += i

    return final

itr_count = 1
while itr_count < len(multiplicand)+1:
    if multiplier[-1] == '1':
        prod = addition(prod, new_multiplicand)
        print(f"Iteration-{itr_count}, {new_multiplicand}, {multiplier}, {prod}")
        new_multiplicand = left_shift(new_multiplicand)
        print(f"Iteration-{itr_count}, {new_multiplicand}, {multiplier}, {prod}")
        multiplier = right_shift(multiplier)
        print(f"Iteration-{itr_count}, {new_multiplicand}, {multiplier}, {prod}")
    else:
        new_multiplicand = left_shift(new_multiplicand)
        print(f"Iteration-{itr_count}, {new_multiplicand}, {multiplier}, {prod}")
        multiplier = right_shift(multiplier)
        print(f"Iteration-{itr_count}, {new_multiplicand}, {multiplier}, {prod}")

    itr_count += 1
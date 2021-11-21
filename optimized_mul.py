multiplicand = '10110'
multiplier = '11001'
prod = ''

for i in multiplicand:
    prod += '0'
for i in multiplier:
    prod += i

print(f"Multiplicand: {multiplicand}")
print(f"Multiplier: {multiplier}")
print("Iteration  , Multiplicand, Product")
print(f"Iteration-0, {multiplicand}, {prod}")

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


itr_count = 1
while itr_count < len(multiplicand)+1:
    if prod[-1] == '1':
        
        mhb_prod = addition(multiplicand, prod[0:len(prod) // 2])
        prod = mhb_prod+prod[len(prod) // 2:len(prod)]
        print(f"Iteration-{itr_count}, {multiplicand}, {prod}")
        prod = right_shift(prod)
        print(f"Iteration-{itr_count}, {multiplicand}, {prod}")
    else:
        prod = right_shift(prod)
        print(f"Iteration-{itr_count}, {multiplicand}, {prod}")


    itr_count += 1
n_base10 = 6*343**5+5*49**7-50

# Перевод в двоичную систему - step 1
n_base7 = ''
n_new = n_base10
while n_new > 0:
    n_base7 += str(n_new%7)
    n_new //= 7
n_base7 += '1'
n_base7 = n_base7[::-1]
print ('The number in binary system is ', n_base7)
print ('There are ', n_base7.count('6'), 'digits "6"')
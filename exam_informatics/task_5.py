# var 12117754

n_base10 = 130 # get a number with base 10
print ('The number is ', n_base10)

# step 1 - Перевод в двоичную систему - step 1
n_base2 = ''
n_new = n_base10
while n_new > 1:
    n_base2 += str(n_new%2)
    n_new //= 2
n_base2 += '1'
n_base2 = n_base2[::-1]
print ('The number in binary system is ', n_base2)

#step 2 - delete last digit 
n_base2 = n_base2.pop(-1) 

#step 3 
if (n_base10%2 == 0):
    n_base2 += '01'
else:
    n_base2 += '10'

#step 4
n_base2 = n_base2[::-1]
sum = 0
for i in range (length(n_base2)-1):
    sum += n_base2[i]*(10**i)
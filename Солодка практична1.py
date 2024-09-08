alphabet = "Aa Bb Cc Dd Ee Ff Gg Hh Ii Jj Kk Ll Mm Nn Oo Pp Qq Rr Ss Tt Uu Vv Ww Xx Yy Zz"

#а)
sorted_alphabet = sorted(alphabet)
print("Літери в алфавітному порядку:")
print(" ".join(sorted_alphabet))

#б)
reversed_alphabet = sorted(alphabet)[::-1]
print("\nАлфавіт в зворотньому порядку:")
print(" ".join(reversed_alphabet))

#с)
uppercase = sorted([char for char in alphabet if char.isupper()])
lowercase = sorted([char for char in alphabet if char.islower()],[:-1])
print("\nВеликі літери в алфавітному порядку, а малі в зворотньому:")
print(" ".join(uppercase + lowercase))



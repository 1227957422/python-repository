n = int (input)
hundred = n//100
ten = (n//10)%10
one = n%10
s = hundred + ten + one
printf(f"={s}")
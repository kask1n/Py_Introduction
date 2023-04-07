a, b = [10, -10], [3, -3]
for x in a:
    for y in b:
        print(f'{x:4}{"//".rjust(3)}{y:3}{"=".rjust(2)}{x // y:3}')
        print(f'{x:4}{"%".rjust(3)}{y:3}{"=".rjust(2)}{x % y:3}')
        print()

#  10 //  3 =  3  # (10) = (3) * q + r
#  10  %  3 =  1  # В Python остаток всегда равен по знаку ДЕЛИТЕЛЮ, т.е. r ≥ 0 -------> q ≥ 0.
#
#  10 // -3 = -4  # (10) = (-3) * q + r
#  10  % -3 = -2  # r ≤ 0 -------> q ≤ 0.
#
# -10 //  3 = -4  # (-10) = (3) * q + r
# -10  %  3 =  2  # r ≥ 0 -------> q ≤ 0.
#
# -10 // -3 =  3  # (-10) = (-3) * q + r
# -10  % -3 = -1  # r ≤ 0 -------> q ≥ 0.

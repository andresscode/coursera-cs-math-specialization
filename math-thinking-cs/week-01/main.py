def find_digit_smaller(times):
  digit = 10
  while True: 
    print(digit)
    if digit % times == 0:
      tmp = digit // times
      if int(str(digit)[1:]) == tmp:
        return digit
    digit += 1


print("Result: " + str(find_digit_smaller(int(input()))))

# Programm, das die Zahlen von 1 bis 100 durchläuft und "Fizz", "Buzz" oder "FizzBuzz" ausgibt
for zahl in range(1, 101):
    if zahl % 3 == 0 and zahl % 5 == 0:
        print("FizzBuzz")
    elif zahl % 3 == 0:
        print("Fizz")
    elif zahl % 5 == 0:
        print("Buzz")
    else:
        print(zahl)


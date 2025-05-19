
def random_number():
    num =int(input("Enter the number"))
    count = 0

    while True:
        count += 1

        if num > random_number:
            print("input nnumber is greater try something samller")


        elif num == random_number:
            print(f"congrats you guessed the correct number {random_number} number of tries took{count}")
            break

        else:
            print("input number is smaller try something greater")

random_number()

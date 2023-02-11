first_numbers = set([int(x) for x in input().split()])
second_numbers = set([int(x) for x in input().split()])

commands = int(input())

for i in range(commands):
    command = input()

    if (command.startswith("Add First")):
        numbers = command.split("Add First").pop().split()
        for n in numbers:
            first_numbers.add(int(n))

    elif (command.startswith("Add Second")):
        numbers = command.split("Add Second").pop().split()
        for n in numbers:
            second_numbers.add(int(n))

    elif (command.startswith("Remove First")):
        numbers = [int(x) for x in command.split("Remove First").pop().split()]
        for n in numbers:
            if (n in first_numbers):
                first_numbers.remove(n)

    elif (command.startswith("Remove Second")):
        numbers = [int(x)
                   for x in command.split("Remove Second").pop().split()]
        for n in numbers:
            if (n in second_numbers):
                second_numbers.remove(n)

    elif (command.startswith("Check Subset")):
        is_subset = False
        if (first_numbers.issubset(second_numbers)):
            is_subset = True
        if (second_numbers.issubset(first_numbers)):
            is_subset = True
        print(is_subset)


print(*sorted(first_numbers), sep=", ")
print(*sorted(second_numbers), sep=", ")

number_system = 2
end_number = ""
number = int(input("adjon meg egy számot! "))
while number > 0:
    remain = number % number_system
    end_number = str(remain) + end_number
    number = number // number_system
print(end_number)

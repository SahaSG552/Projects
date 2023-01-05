def user_input(n):
    print("camelCase:", n)
    s_c = "".join(
        [letter if letter.islower() else f"_{letter.lower()}" for letter in n]
    )
    print("snake_case:", s_c)


user_input(input("Input camelCase: "))

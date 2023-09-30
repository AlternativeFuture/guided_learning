def calculate_love_score(name1: str, name2: str) -> int:
    letters = ("TRUE", "LOVE")
    true_count = sum((name1 + name2).upper().count(letter) for letter in letters[0])
    love_count = sum((name1 + name2).upper().count(letter) for letter in letters[1])

    love_score = int(str(true_count) + str(love_count))

    return love_score


if __name__ == '__main__':
    input_name_1 = input('Enter first name. ')
    input_name_2 = input('Enter second name. ')

    score = calculate_love_score(input_name_1, input_name_2)
    if score < 10 or score > 90:
        print(f'Your score is {score}, you go together like coke and mentos.')
    elif 40 <= score <= 50:
        print(f'Your score is {score}, you are alright together.')
    else:
        print(f'Your score is {score}.')

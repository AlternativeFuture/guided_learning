from random import choice

from text import stories


def user_input(array: tuple):
    """Takes in a user quizz, ask user input, make capitalized name if there are and append answer to list

                    Parameters:
                            array (tuple): User quizz

                    Returns:
                            text (list): The list of user answers
                 """
    user_answers = []
    for text in array:
        if 'name' in text:
            user_answers.append(input(f'Input {text} : ').capitalize())
        else:
            user_answers.append(input(f'Input {text} : ').lower())
    return user_answers


def fill_blank_in_text(text: str, array: list):
    """Takes in a text with missing words and a list of missing words.

                Parameters:
                        text (str): A string which need to fill in
                        array (list): List of missing words

                Returns:
                        text (str): Full text
             """
    return text.format(*array)


def article_correcter(text: str):
    """Takes in a text, find out articles, checks if article must be "an" and correct it.

                    Parameters:
                            text (str): A text

                    Returns:
                            text (str): Corrected text
                 """
    text_list = text.split()
    for i, char in enumerate(text_list):
        if char == 'a' and text_list[i + 1][0] in 'aeiou':
            text_list[i] = 'an'
    return ' '.join(text_list)


if __name__ == '__main__':
    story_num = input('Input a number in range 1-3 to choose story, if not a random selection will take place: ')
    if story_num == '' or story_num not in '123':
        story_num = choice(('1', '2', '3'))
    story = stories[story_num]
    answers = user_input(story['story_quizz'])
    print(article_correcter(fill_blank_in_text(story['template'], answers)))

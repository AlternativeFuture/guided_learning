import time
import re


def validate_time_format(text: str) -> str:
    """
        Validates the format of a time string and prompts the user for correction if necessary.

        Args:
            text (str): The input time string to be validated.

        Returns:
            str: A valid time string in the format (h:m:s).

        """
    regex_pattern = r'\d{1,2}:\d{1,2}:\d{1,2}'
    while not re.match(regex_pattern, text):
        text = input('Invalid format "' + text + '". The correct format is (h:m:s): ')
    return text


def time_str_to_int_list(t: str) -> list:
    """
        Converts a time string to a list of integers representing hours, minutes, and seconds.

        Args:
            t (str): The time string in the format (h:m:s).

        Returns:
            list: A list containing three integers [hours, minutes, seconds].
        """
    time_list = t.split(':')
    time_list = list(map(int, time_list))
    return time_list


def time_to_seconds(t: list) -> int:
    """
        Converts a list of time components [hours, minutes, seconds] to total seconds.

        Args:
            t (list): A list containing three integers [hours, minutes, seconds].

        Returns:
            int: Total seconds represented by the input time components.
        """
    return t[0] * 3600 + t[1] * 60 + t[2]


def display_time_remaining(seconds: int):
    """
        Displays the time remaining in the format (h:mm:ss).

        Args:
            seconds (int): The remaining time in seconds.
        """
    hour, remaining = divmod(seconds, 3600)
    minute, second = divmod(remaining, 60)
    time_string = '{:02d}:{:02d}:{:02d}'.format(hour, minute, second)
    print(time_string)


def countdown_timer(second: int, func: callable):
    """
        Performs a countdown timer and executes a given function for each remaining second.

        Args:
            second (int): The total countdown time in seconds.
            func (callable): A function to be executed for each remaining second.
        """
    for sec in range(second, 0, -1):
        func(sec)
        time.sleep(1)


if __name__ == '__main__':
    user_input_str = 'Insert time to count down (h:m:s): '
    user_input = validate_time_format(input(user_input_str))
    time_list = time_str_to_int_list(user_input)
    seconds = time_to_seconds(time_list)
    countdown_timer(seconds, display_time_remaining)
    print('TIme is over!!!')

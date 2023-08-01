from random import sample

from additon import result_combinations as res_comb
from additon import play_combinations as play_comb


def roll_dices():
    """Generate 2 random integers, and count there sum.
                        Returns:
                                numbers (dict)
                     """
    rolls = sample(range(1, 7), 2)

    return {'first': rolls[0], 'second': rolls[1], 'total': sum(rolls)}


def dices_result_str(rolled_res: dict):
    """Takes in a dict, and fill in the string.
                        Returns:
                                text (str): Filled in text
                     """
    return res_comb['rolled'].format(*rolled_res.values())


if __name__ == '__main__':

    rolled_res = roll_dices()
    print(dices_result_str(rolled_res))

    if rolled_res['total'] in play_comb['win']:
        print(res_comb['win'])

    elif rolled_res['total'] in play_comb['lose']:
        print(res_comb['lose'])

    elif rolled_res['total'] in play_comb['goal']:
        print(res_comb['goal'].format(rolled_res['total']))
        goal = rolled_res['total']
        c = 0
        while c < 3:

            rolled_res = roll_dices()
            print(dices_result_str(rolled_res))

            if goal == rolled_res['total']:
                print(res_comb['win'])
                break
            c += 1
        else:
            print(res_comb['lose'])

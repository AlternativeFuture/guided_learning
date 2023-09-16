def is_palindrome(n):
    return str(n) == str(n)[::-1]


def largest_palindrome_product():
    largest_palindrome = 0

    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product <= largest_palindrome:
                break
            if is_palindrome(product):
                largest_palindrome = product

    return largest_palindrome


if __name__ == "__main__":
    largest_pali = largest_palindrome_product()
    print("The largest palindrome made from the product of two 3-digit numbers is:", largest_pali)




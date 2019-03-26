def add_until_palindrome(n):
    while True:
        n = add_reversed(n)
        yield n
        if is_palindrome(n):
            return

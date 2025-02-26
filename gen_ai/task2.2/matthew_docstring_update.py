def base10_to_base7(n: int) -> str:
    """
    Converts a base-10 integer to its base-7 string representation.

    Parameters:
        n (int): The integer to convert. Must be a non-negative integer.

    Returns:
        str: The base-7 representation of `n` as a string.

    Example:
        >>> base10_to_base7(100)
        '202'
        >>> base10_to_base7(7)
        '10'
        >>> base10_to_base7(0)
        '0'

    Notes:
        - This function does not handle negative numbers.
        - The output is always a string
    """
    if n == 0:
        return '0'
    
    base7_digits = []
    while n > 0:
        base7_digits.append(str(n % 7))
        n //= 7

    return ''.join(reversed(base7_digits))

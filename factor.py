from collections import defaultdict
import re

PATTERN = r"^.?$|^(..+?)\1+$"


def factor(n: int) -> dict[int, int]:
    """
    Returns the prime factorization of `n` as a dictionary where keys
    are the prime factors, and values are their multiplicities.
    """
    res: dict[int, int] = defaultdict(int)
    while True:
        match = re.match(PATTERN, "1" * n)
        if not match:
            break
        p = len(match.group(1))
        res[p] += 1
        n //= p
    if n != 1:
        res[n] += 1
    return res


if __name__ == "__main__":
    n = int(input("Enter an integer: "))
    print(dict(factor(n)))

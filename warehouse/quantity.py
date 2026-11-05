"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    n = int(value.strip())
    if n < 0:
        raise ValueError(f"Quantity must be non-negative, got {n}")
    return n

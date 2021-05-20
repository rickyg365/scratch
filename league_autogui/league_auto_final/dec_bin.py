import os


def decimal_binary(number: int) -> int:
    bits = []

    copy = number

    while copy >= 1:
        bit_value = copy % 2
        # added in reverse order
        bits.append(f"{bit_value}")
        copy = copy // 2

    corrected_bits = bits[::-1]

    return int("".join(corrected_bits))


# new_bin = decimal_binary(6)
#
# print(new_bin)


def get_bit_rep(number: str):
    first_bit = 0
    sign = number[0]

    num = int(number)

    if sign == '-':
        first_bit = 1
        num = int(number[1:])

    binary_num = decimal_binary(num)

    bit_repr = f"{first_bit}{binary_num:031}"

    chunk1 = bit_repr[:8]
    chunk2 = bit_repr[8:16]
    chunk3 = bit_repr[16:24]
    chunk4 = bit_repr[24:]

    return f"{chunk1} {chunk2} {chunk3} {chunk4}"


if __name__ == "__main__":
    user_input = input("Choose a number: ")

    bit_rep = get_bit_rep(user_input)

    print(bit_rep)

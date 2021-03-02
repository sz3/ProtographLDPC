import random
import sys


def _write_bit(bit):
    if bit:
        return b'1'
    else:
        return b'0'


# just do a random sample (set(int)) of N bits to flip.
def main(src, dst, bit_flips):
    eadd = 0
    with open(src, 'rb') as f:
        contents = f.read()
    res = b''

    flip = set(random.sample(range(0, len(contents)), bit_flips))
    for i, c in enumerate(contents):
        if c not in [48, 49]:
            continue
        bit_is_set = (c == 49)
        if i in flip:
            eadd += 1
            res += _write_bit(not bit_is_set)
        else:
            res += _write_bit(bit_is_set)

    with open(dst, 'wb') as f:
        f.write(res)
    print(eadd)

if __name__ == '__main__':
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
    bit_flips = int(sys.argv[3])

    main(src_file, dst_file, bit_flips)


import csv

from affine import AffineBuilder
from affine_decoder import AffineDecoder

fileNames = {
    "encoded": "encoded.txt",
    "alphabet": "alphabet.txt",
    "decoded": "decoded.csv",
}


def read_file(filename):
    result = ""
    with open(filename, "r", encoding="utf-8") as f:
        while line := f.readline():
            result += str.rstrip(line)

    return result


def write_csv(filename, data):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


def create_char_index_dict(text):
    return dict(zip(text, range(1, len(text) + 1)))


def create_index_char_dict(text):
    return dict(zip(range(len(text)), text))


def decode(affine, indexed_dict):
    result = ""

    for c in indexed_dict:
        result += affine.decode(indexed_dict[c])

    return result


def decode_all(encoded: str, alphabet: str):
    e_alphabet = create_char_index_dict(alphabet)
    d_alphabet = create_index_char_dict(alphabet)

    d1 = e_alphabet[alphabet[0]]
    d2 = e_alphabet[alphabet[1]]

    m = len(alphabet)
    ab = AffineBuilder(m)

    result = []
    for c1, x1 in e_alphabet.items():
        if x1 == d1:
            continue
        for c2, x2 in e_alphabet.items():
            if x1 == x2 or x2 == d2:
                continue

            af = ab.build_affine(d1, x1, d2, x2)
            decoder = AffineDecoder(af, e_alphabet, d_alphabet)
            decoded = decoder.decode(encoded)

            result.append([af.a, af.b, decoded])

    return result


def main():
    encoded = read_file(fileNames["encoded"])
    alphabet = read_file(fileNames["alphabet"])

    data = [["a", "b", "decoded"]]
    data.extend(decode_all(encoded, alphabet))
    write_csv(fileNames["decoded"], data)


if __name__ == '__main__':
    main()

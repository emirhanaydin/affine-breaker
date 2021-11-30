from affine import Affine


class AffineDecoder:
    def __init__(self, af: Affine, encode_dict: dict, decode_dict: dict):
        self._af = af
        self._e_dict = encode_dict
        self._d_dict = decode_dict

    def decode(self, text: str):
        res = ""
        af = self._af
        ed = self._e_dict
        dd = self._d_dict
        for c in text:
            res += dd[af.decode(ed[c])]

        return res

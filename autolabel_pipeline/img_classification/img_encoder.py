import base64

class Base64OpenAIEncoder:
    def __init__(self, src_pth: str):
        self.src_pth = src_pth
    
    def encode_img(self):
        with open(self.src_pth, "rb") as imgf:
            enc_str = base64.b64encode(imgf.read()).decode('utf-8')
        return enc_str


__namespace__ = [Base64OpenAIEncoder]
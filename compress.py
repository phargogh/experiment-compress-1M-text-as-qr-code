import base64
import codecs
import sys
import zlib

import qrcode

with open('lipsum-1M.txt') as sample_file:
    textstring = sample_file.read().encode()
    print(f'Starting text has {len(textstring)} chars')
    print(f'Starting text is {sys.getsizeof(textstring)} bytes')

compressed = zlib.compress(textstring, level=9)
print(f'Compressed text has {len(compressed)} chars')
print(f'Compressed text is {sys.getsizeof(textstring)} bytes')


b64 = base64.b64encode(compressed).decode()

print(f'Base64 text has {len(b64)} chars')
print(f'Base64 text is {sys.getsizeof(b64)} bytes')

img = qrcode.make(b64)
img.save("qrcode.png")

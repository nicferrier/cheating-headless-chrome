import base64
import sys

def bencode(f_in, f_out):
    with open(f_in, "rb") as fin:
        raw_bytes = base64.b64encode(fin.read())
        with open(f_out, "wb") as fout:
            fout.write(raw_bytes)

def bdecode(f_in, f_out):
    with open(f_in, "rb") as fin:
        raw_bytes = base64.b64decode(fin.read())
        with open(f_out, "wb") as fout:
            fout.write(raw_bytes)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "encode":
            bencode(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "decode":
            bdecode(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == "help":
            print """base64it.py encode input-filename output-filename
base64it.py decode input-filename output-filename
"""
        else:
            print "whoops!"
    else:
        print "base64it.py\nuse help to find out what to do"


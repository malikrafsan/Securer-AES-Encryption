rm *.txt

py generator.py > inp-encrypt.txt
py main.py < inp-encrypt.txt > out-encrypt.txt
py pipe.py < out-encrypt.txt > out-pipe.txt
py main.py < out-pipe.txt > out-decrypt.txt
py compare.py

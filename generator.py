import random
import string

def main():
  N = 1024 * 1024
  
  s = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=N))
  print("1")
  print(s)
  print("abcdefghij123456")

if __name__ == "__main__":
  main()

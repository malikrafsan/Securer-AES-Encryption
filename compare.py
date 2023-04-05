path_raw = "inp-encrypt.txt"
path_res = "out-decrypt.txt"

def main():
  raw = ""
  
  with open(path_raw, "r") as f:
    raw_file = f.read()
    splitted = raw_file.split("\n")
    raw = splitted[1]

  res = ""
  with open(path_res, "r") as f:
    res = f.read()
    splitted = res.split("\n")
    res = splitted[10]
    
  if raw == res:
    print("Success")
  else:
    print("Failed")
  input()

if __name__ == "__main__":
  main()
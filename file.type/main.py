import os
dir = "new"
for name in os.listdir(dir):
  fullname = os.path.join(dir, name)
  print(fullname)
  if os.path.isdir(fullname):
    print("{} is a directory.".format(fullname))
  else:
    print("{} is a file.".format(fullname))
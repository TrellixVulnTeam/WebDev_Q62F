def xyz_there(str):
  for i in range(len(str)-2):
    if(str[i] == 'x' and str[i+1] == 'y' and str[i+2] == 'z'):
      if(i == 0): return True
      if(str[i-1] != '.'): return True
  return False

def in1to10(n, outside_mode):
  if(outside_mode == True):
    if(n <= 1 or n >= 10): return True
  else:
    if(n in range(1,11)): return True
  return False

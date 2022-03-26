def caught_speeding(speed, is_birthday):
  c = 0
  if(is_birthday): c+= 5
  if speed <= 60 + c: return 0
  if speed >= 61 + c and speed <= 80 + c: return 1
  else: return 2

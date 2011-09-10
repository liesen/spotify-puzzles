from itertools import permutations
from datetime import date

d = raw_input()

try:
  a, b, c = map(int, d.split('/'))
except:
  print "%s is illegal" % d
  exit()

def trydate(year, month, day):
  if year < 1000:
    year += 2000

  try:
    return date(year, month, day)
  except:
    return None

k = sorted(filter(lambda x: x is not None,
                  map(lambda ks: trydate(*ks), permutations([a, b, c]))))

if len(k) > 0:
  print k[0]
else:
  print "%s is illegal" % d

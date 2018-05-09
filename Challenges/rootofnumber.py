def divide(start, end, target, power):

  mid = float((start+end)/2.0)

  diff = (mid**power) - target

  if abs(diff) <= 0.001:
    return mid
  elif diff < 0:
    return divide(mid+0.001, end, target, power)
  elif diff > 0:
    return divide(start, mid-0.001, target, power)


def root(x, n):
  if not x:
    return 0
  if x == 1:
    return 1
  # end == max(1, x)
  return divide(0, 2*x, x, n)
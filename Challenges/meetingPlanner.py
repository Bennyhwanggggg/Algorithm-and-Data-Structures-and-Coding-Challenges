def meeting_planner(slotsA, slotsB, dur):
  i, j = 0, 0
  while i < len(slotsA) and j < len(slotsB):
    startA, endA = slotsA[i]
    startB, endB = slotsB[j]
    if startA < endB or startB < endA:
      meetingStart = max(startA, startB) # 10
      meetingEnd = min(endA, endB) # 15
      time = meetingEnd - meetingStart  # 10
      if time >= dur:
        return [meetingStart, meetingStart+dur]
      if endA > endB:
        j += 1
      else:
        i += 1
        
    elif startA > endB:
      j += 1
    elif startB > endA:
      i += 1

  return []
      

def add_time(start, duration, DOW=""):
  x = start.split()
  y = x[0].split(":")
  z = duration.split(":")

  days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
  dhrs = (0, 24, 48, 72, 96, 120, 144)

  #Store total time since 12:00 AM Sunday in a variable
  ti = 0
  
  #If PM += 12
  if x[1] == "PM":
    ti += 12*60
    
  #Add daysin hour form
  if DOW != "":
    ti += dhrs[days.index(DOW.capitalize())]*60
    
  #Add hours, minutes
  ti += int(y[0])*60 + int(y[1])

  tt = ti + int(z[0])*60 + int(z[1])

  #n represents days added
  n = tt//1440 - ti//1440

  dstr = ""

  hoursf = (tt%1440)//60

  minsf = tt%60

  if len(str(minsf)) <2:
    minsf = '0'+str(minsf)

  if hoursf >11:
    dstr += " PM"
    hoursf -= 12
  else:
    dstr += " AM"

  if hoursf == 0:
      hoursf += 12
  
  if DOW != "":
    dstr += ", " + days[((tt//60)//24)%7]
  
  if n < 1:
    dstr += ""
  elif n == 1:
    dstr += " (next day)"
  elif n > 1:
    dstr += ' ('+str(n)+' days later)'

  
  
  new_time = str(hoursf) + ':' + str(minsf) + dstr

  return new_time
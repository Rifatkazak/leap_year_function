def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False



year = int(input("Enter a year: "))
query = is_leap(year)

if query :
    print(f"{year} is leap year" )
else :
    print(f"{year} is not leap year" )
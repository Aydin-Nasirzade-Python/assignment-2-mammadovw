#import libraries here

def main():
  x = int(input("Enter the year [ex. 2021]: "))
  if x < 0 :
    print("Invalid year!")
  elif x == 2000 or (x - 2000) % 12 == 0 :
    print(f"{x} is the year of the Dragon")
  elif x == 2001 or (x - 2001) % 12 == 0 :
    print(f"{x} is the year of the Snake")
  elif x == 2002 or (x - 2002) % 12 == 0 : 
    print(f"{x} is the year of the Horse")
  elif x == 2003 or (x - 2003) % 12 == 0 :
    print(f"{x} is the year of the Sheep")
  elif x == 2004 or (x - 2004) % 12 == 0
    print(f"{x} is the year of the Monkey")
  elif x == 2005 or (x - 2005) % 12 == 0 :
    print(f"{x} is the year of the Rooster")
  elif x == 2006 or (x - 2006) % 12 == 0 :
    print(f"{x} is the year of the Dog")
  elif x == 2007 or (x - 2007) % 12 == 0 :
    print(f"{x} is the year of the Pig")
  elif x == 2008 or (x - 2008) % 12 == 0 :
    print(f"{x} is the year of the Rat")
  elif x == 2009 or (x - 2009) % 12 == 0 :
    print(f"{x} is the year of the Ox")
  elif x == 2010 or (x - 2010) % 12 == 0 :
    print(f"{x} is the year of the Tiger")
  else :
     print(f"{x} is the year of the Hare")

    
  pass

if __name__ == "__main__":
  main()

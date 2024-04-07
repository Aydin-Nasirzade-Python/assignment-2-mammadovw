#import libraries here

def main():
  ay=input("Enter name of the month [ex. June]: ")
  gun=int(input("Enter the day [ex. 5]: "))
  if (ay=="March" and (gun>=20 and gun<=31)) or (ay=="June" and gun<21) or (ay=="May" or ay=="April"):
      print(f"{ay} {gun} is in Spring")
      print()
  elif ((ay=="June") and (gun>=21 and gun<=31)) or ((ay=="September" and gun<22) or (ay=="July" or ay=="August")):
      print(f"{ay} {gun} is in Summer")
      print()
  elif ((ay=="September") and (gun>=22 and gun<=31)) or ((ay=="December" and gun<21) or (ay=="Octamber" or ay=="Novamber")):
      print(f"{ay} {gun} is in Fall")
      print()
  elif ((ay=="December") and (gun>=21 and gun<=31)) or (ay=="March" and gun<20) or (ay=="January" or ay=="Febuary"):
      print(f"{ay} {gun} is in Winter")
      print()
  pass

if __name__ == "__main__":
  main()

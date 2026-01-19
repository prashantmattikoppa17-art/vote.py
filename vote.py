age = input("Enter your age")
if age>=18:
  print("You are eligibale to vote")
else:
   print("You are not eligibale to vote")
except ValueError:
  print("Please enter valid integer for age")

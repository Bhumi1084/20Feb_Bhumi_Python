sub1=int(input("Enter First Subject Marks : "))
sub2=int(input("Enter Second Subject Marks : "))
sub3=int(input("Enter Thired Subject Marks : "))
sub4=int(input("ENter Fourth Subject Marks : "))

total=sub1+sub2+sub3+sub4
print("Total : ",total)

per=total/4
print(f"Persantage : {per}%")

if per>=90:
    print("First class pass")
elif per<90 or per>40:
    print("pass")
else:
    print("Fail")
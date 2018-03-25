# program to calculate percentage and grade

mark1 = int(input("Enter th Marks for Physics: "));
mark2 = int(input("Enter th Marks for Chemistry: "));
mark3 = int(input("Enter th Marks for Biology: "));
mark4 = int(input("Enter th Marks for Mathermatics: "));
mark5 = int(input("Enter th Marks for Computer Studies: "));
sum = mark1 + mark2 + mark3 + mark4 + mark5;
average = sum/5;

if(average>=91 and average<=100):
    print("Your Grade is A+")
elif(average>=81 and average<=90):
    print("Your Grade is A")
elif(average>=71 and average<=80):
    print("Your Grade is B")
elif(average>=61 and average<=70):
    print("Your Grade is C")
elif(average>=51 and average<=60):
    print("Your Grade is D")
elif(average>=41 and average<=50):
    print("Your Grade is E")
elif(average>=0 and average<=40):
    print("Your Grade is F")

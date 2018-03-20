# program to count total number of notes in given amount
amount = int(input("Enter the amount: "))

notes = 0
notes += (amount // 2000)
amount %= 2000
notes += (amount // 500)
amount %= 500
notes += (amount // 200)
amount %= 200
notes += (amount // 100)
amount %= 100
notes += (amount // 50)
amount %= 50
notes += (amount // 20)
amount %= 20
notes += (amount // 10)
amount %= 10
notes += (amount // 5)
amount %= 5
notes += (amount // 2)
amount %= 2
notes += (amount // 1)
amount %= 1

print("The amount of notes are: ", notes)

"""
Write a Python program to convert second to day, hour, minutes and seconds.
"""
seconds=int(input("Enter the seconds: "))

Day=((seconds//60)//60)//24
print(f"Total day for given seconds: {Day}")
Hours=(seconds//60)//60
print(f"Total hours for given seconds: {Hours}")
Minute=seconds//60
print(f"Total minutes for given seconds: {Minute}")
Seconds=seconds
print(seconds)

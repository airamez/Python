age = input('Type your age: ')
age = int(age)

# if/elif/else
result = None
if age <= 0:
    result = "fetus/unborn"
elif age <= 1:
    result = "infant"
elif age <= 12:
    result = "kid"
elif age <= 18:
    result = "teenage"
elif age <= 40:
    result = "adult"
elif age <= 60:
    result = "senior"
else:
    result = "old"

print('Your are', result)

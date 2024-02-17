# Question 1
def square_root_generator(limit):
    n = 1
    while n <= limit:
        yield n ** 0.5
        n += 1

# Example usage:
limit = 5
generator = square_root_generator(limit)
sum = 0
for sqrt_value in generator:
    sum = sum + sqrt_value
print ('The sum of the outputs of the generator for limit = 5 is ', sum)

# Question 2
limit = 13
generator = square_root_generator(limit)
value = 0
for sqrt_value in generator:
    sum = sqrt_value
print ('The 13th number yielded is ', value)


from guitar import Guitar

gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 500)

print(gibson_guitar.get_age())
print(another_guitar.get_age())
print(gibson_guitar.is_vintage())
print(another_guitar.is_vintage())
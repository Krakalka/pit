school ={"1а":23,"1б":34,"1в":43,"1д":28,"1е":33}
print(school)
school["1а"] = 39
print(school)
school["1и"] = 13
print(school)
school.pop("1б")
print(school)
a = school.values() 
a = sum(a)
print(a)

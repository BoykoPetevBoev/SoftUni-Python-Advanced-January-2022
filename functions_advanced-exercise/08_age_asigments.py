def age_assignment(*args, **kwargs):
    result = [];
    names = sorted(args)
    for name in names:
        name_letter = name[0]
        age = kwargs[name_letter]
        result.append(f"{name} is {age} years old.")
    return "\n".join(result)

print(age_assignment("Peter", "George", G=26, P=19))	
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))	

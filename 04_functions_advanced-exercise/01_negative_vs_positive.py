numbers = (int(el) for el in input().split())

def negative_vs_positive(numbers):
    positive = 0
    negative = 0
    for num in numbers:
        if(num > 0):
            positive += num
        else:
            negative += num

    print(negative)
    print(positive) 

    if(positive > abs(negative)):
        print("The positives are stronger than the negatives")
    if(positive < abs(negative)):
        print("The negatives are stronger than the positives")

negative_vs_positive(numbers)
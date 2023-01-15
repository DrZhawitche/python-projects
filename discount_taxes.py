#Program that calculates discount/taxes

#Parameters
cost = float(input("Enter the original price: "))
discount = float(input("Enter discount in %: "))
taxes = float(input("Enter taxes in %: "))
cost = cost - (cost * (discount / 100))
cost = cost + (cost * (taxes / 100))

#Print final cost
print(cost)
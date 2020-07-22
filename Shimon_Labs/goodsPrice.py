#Read data of products from a text file to a dictionary and manage orders and inventory
goods = {}

f=open("goods.txt","r+")
for i in f:
    row = i.split()
    row[1] = float(row[1])
    row[2] = int(row[2])
    goods[row[0].lower()] = row[1:]

print("inventory:")
for key, value in goods.items():
    print(key, '-', value[0], '-', value[1])

print()
cost = 0

while True:
    good = input("What would you like to order? (n - nothing) ").lower()
    if good == 'n' or good == 'N':
        break
    qty = int(input("How many? "))
    if qty > goods[good][1]:
        print("We don't have so much")
        continue
    cost += goods[good][0] * qty
    goods[good][1] -= qty

print("\nPrice:", cost)

f.seek(0)
print("inventory:")
for key, value in goods.items():
    print(key.title(), '-', value[0], '-', value[1])
    f.write(key.title() + ' ' + str(value[0]) + ' ' + str(value[1]) + '\n')
        
        
    
    
"""   RUN  DEMO
inventory:
Apple - 4.5 - 10
Orange - 6.2 - 5
Pineapple - 10.0 - 1
Mango - 7.5 - 2
Banana - 3.8 - 10

What would you like to order? (n - nothing) Banana
How many? 5
What would you like to order? (n - nothing) Mango
How many? 2
What would you like to order? (n - nothing) Orange
How many? 6
We don't have so much.
What would you like to order? (n - nothing) n

Price: 34.0
inventory:
apple - 4.5 - 10
orange - 6.2 - 5
pineapple - 10.0 - 1
mango - 7.5 - 0
banana - 3.8 - 5
"""
# syntax
# variables_name = value
# = -> Assigenment Operator

# Immutable Data (numbers, decimals, simple text)
value_num = 10
value_rating = 4.2
value_name = "Ravi"

new_rating = 4.2

print(id(value_num))  # unique identity i.e memory address
print(id(value_rating))
print(id(value_name))

print(id(new_rating))

# Lists in python are Mutable
list1 = [1,2,3]
list2 = [1,2,3]
list3 = [4,5,6]

print(id(list1))
print(id(list2))
print(id(list3))
 
print(type(value_num))
print(type(value_rating))
print(type(value_name)) 

msg = ("Python is Awesome")
print(msg)

x = "Python"
y = "is"
z = "Awesome"

print(x,y,z)


product_brand = "Hyundai"
product_model = "creta"
product_price = 'RS 2,00,000'
product_rating = 4.8
print(product_brand,product_model,product_price,product_rating)

product_model1 = "verna"
product_price1 = "RS 3,00,000"
product_rating1 = 4.2
print(product_brand,product_model1,product_price1,product_rating1)

product_model2 = "venue"
product_price2 = "RS 4,00,000"
product_rating2 = 4.5
print(product_brand,product_model2,product_price2,product_rating2)

product_model3 = "Aura"
product_price3 = "RS 1,00,000"
product_rating3 = 4.0
print(product_brand,product_model3,product_price3,product_rating3)
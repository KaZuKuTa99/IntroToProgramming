#--------------------------------------------------------
# Developer---Abel Gonzalez
# Course------CS1213-01
# Project-----Project #3
# Due---------September 28,2018
#
# This program computes the price of an automotive oil
# change at local BisonLube shops. The pricing is based
# on the number of quarts of oil that the customer buys,
# a volume discount for large orders, and whether the 
# customer buys a new oil filter. There is a $10.00
# service charge that is the same for all customers, and
# 6% sales tax.
#--------------------------------------------------------

quarts = int(input("Number of quarts--------"))
Filter = str(input("Oil filter? (Y or N)----"))
print()
print("Your bill from BisonLube")
print()

price_oil = quarts*6.95
price_filter = 7.56
service = 10.00
discount = price_oil*0.1

print("Oil.......  $%0.2f"%price_oil)
if quarts > 6:
    print("Discount..  %6.2f"%discount)
if Filter == 'Y':
    print("Filter....  %6.2f"%price_filter)
print("Service...  %6.2f"%service)
print("           -------")


if quarts > 6 and Filter == 'N':
    subtotal = service+price_oil-discount
    print("Subtotal..  %6.2f"%subtotal)
if quarts > 6 and Filter == 'Y':
    subtotal = service+price_oil+price_filter-discount
    print("Subtotal..  %6.2f"%subtotal)
if quarts <= 6 and Filter == 'N':
    subtotal = service+price_oil
    print("Subtotal..  %6.2f"%subtotal)
if quarts <= 6 and Filter == 'Y':
    subtotal = service+price_oil+price_filter
    print("Subtotal..  %6.2f"%subtotal)


tax = subtotal * 0.06
total = subtotal + tax

print("Tax.......  %6.2f"%tax)
print("           -------")
print("Total.....  $%0.2f"%total)

print()

if quarts > 10:
    print("Notice: The EPA recommends that you dispose of used motor oil at a certified recycling center.")

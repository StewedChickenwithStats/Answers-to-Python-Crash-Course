sandwich_orders = ['chicken', 'pastrami', 'beef', 'pastrami', 'tuna', 'pastrami']
print("\nThe pastrami have been sold out.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

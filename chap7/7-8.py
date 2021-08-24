sandwich_orders = ['chicken', 'beef', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your" + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiched have been finished:")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

responses={}

polling_active=True

while polling_active:
    name=input("\nWhat is your name?")
    response=input("If you could visit one place in the world, where could you go?")

    responses[name]=response

    repeat=input("Would you like to let another person respond? (yse/no)")
    if repeat=='no':
        polling_active=False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title()+ " would like to visit "+response.title()+".")
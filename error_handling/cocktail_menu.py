# Function that takes in a string
# if that string exits in cocktails file
# return "Coming right up"
# otherwise return "Not on the menu, sorry"

def cocktail_order(cocktail_choice):
    with open("cocktails.txt") as file:
        available_cocktails = file.read().split('\n')
        for cocktail in available_cocktails:
            if cocktail_choice.lower() == cocktail.lower():
                return "Coming right up"
        return "Not on the menu sorry"


x = cocktail_order('tea')
print(x)
x = cocktail_order('Mojito')
print(x)
x = cocktail_order('moscow mule')
print(x)

# a function that takes in a string
# if doesn't already exist in menu, add to menu
# otherwise print warning that cocktail is already on the men
# bonus if it raises n error
def add_cocktail(cocktail):
    with open("cocktails.txt", "r+") as file:
        available_cocktails = file.read().split('\n')
        if cocktail not in available_cocktails:
            file.write(f'\n{cocktail}')
        else:
            print("Cocktail is already in list")
            #raise ValueError("No drink exists")

add_cocktail("Gin and Tonic")
add_cocktail("Mojito")


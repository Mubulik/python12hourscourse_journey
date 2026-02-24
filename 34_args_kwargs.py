# *args     = permet de faire passer plusieurs arguments non kw
# **kwargs  = permet de faire passer plusieurs kw arguments
#             * unpacking operator -> RACINE DES ARGUMENTS ARBITRAIRES
#                                  -> args/kwargs sont des conventions, ce qui compte réellement sont les * / **

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
# print(add(1,2,3,4))

# def display_name(*args):
#     for arg in args:
#         print(arg, end=" ")
# 
# display_name("René", "Dominique", "Kawaiinee", "JACQUES")

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} : {value}")
# 
# print_address(num_rue=3, rue="Rue de la poste", code_postal="12345", Ville="Diou", Pays="France")

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('num_rue')} {kwargs.get('rue')} App.{kwargs.get('apt')}")
    elif "lettre" in kwargs:
        print(f"{kwargs.get('num_rue')}{kwargs.get('lettre')} {kwargs.get('rue')}")
    else:
        print(f"{kwargs.get('num_rue')} {kwargs.get('rue')}")
    
    print(f"{kwargs.get('ville')}, {kwargs.get('code_postal')} {kwargs.get('pays')}")

to_deliver = shipping_label("René", "Dominique", "Kawaiinee", "JACQUES",
                            num_rue=3, rue="Rue de la poste", lettre="A", code_postal="12345", ville="Diou", pays="France")

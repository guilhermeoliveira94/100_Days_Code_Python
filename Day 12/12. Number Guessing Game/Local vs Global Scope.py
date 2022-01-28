# ################### Scope ####################
#
# enemies = 1
#
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
#
# # 2 inside, 2 outside
# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")
#   return(enemies)
#
# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")
#
# def drink_potion():
#   potion_trength = 2
#   print(potion_trength)
#
# drink_potion()
# print(potion_strength) # Erro porque está fora do escopo

# Global Scope
# player_health = 10
#
# def drink_potion():
#   print(player_health)
#
# drink_potion()
# print(player_health)

# Modify Global Scope

# enemies = 1
#
# def increse_enemies():
#   global enemies
#   enemies += 1
#   print(f"Enemies inside function: {enemies}")
#
# increse_enemies()
# print(f"Enemies outside function: {enemies}")

# Global Constants
# É uma convenção usar letra maiúscula para Global Constants (Variáveis Imutáveis)

# PI = 3.14159
#
# def calc():
#   global PI
#
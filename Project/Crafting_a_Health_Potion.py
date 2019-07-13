# Import Modules
import random

# Set difficulty

difficulty = 3

# Set Health
health = 50
potion = int(random.randint(25, 50) / difficulty)  # Cast to integer as division return float

# Add potion
health += potion

print(health)
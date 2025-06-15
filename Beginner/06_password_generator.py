import random
import string
 
length = int(input('enter desired password length: '))

characters = string.asccii_letters + string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(length))

print(f'Generated password: {password}')
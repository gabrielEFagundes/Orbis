from app import Bcrypt

password = Bcrypt().generate_password_hash('YOUR_PASS').decode('utf-8')

print(password)
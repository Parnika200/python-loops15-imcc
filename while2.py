password="admin"
not_found=True

while not_found:
    passw=input("enter password")
    if passw==password:
        not_found=False

print("found correct password")
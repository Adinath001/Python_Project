print("---- PC BUILDING SHOP ----")

# CPU
print("\nChoose CPU:")
print("1. Intel i5 - 15000")
print("2. Intel i7 - 22000")
print("3. Ryzen 5 - 18000")
cpu_choice = int(input("Enter choice: "))
if cpu_choice == 1:
    cpu, cpu_price = "Intel i5", 15000
elif cpu_choice == 2:
    cpu, cpu_price = "Intel i7", 22000
else:
    cpu, cpu_price = "Ryzen 5", 18000

# GPU
print("\nChoose GPU:")
print("1. Nvidia RTX 3060 - 30000")
print("2. Nvidia RTX 3070 - 45000")
print("3. AMD RX 6600 - 28000")
gpu_choice = int(input("Enter choice: "))
if gpu_choice == 1:
    gpu, gpu_price = "Nvidia RTX 3060", 30000
elif gpu_choice == 2:
    gpu, gpu_price = "Nvidia RTX 3070", 45000
else:
    gpu, gpu_price = "AMD RX 6600", 28000

# RAM
print("\nChoose RAM:")
print("1. 8GB - 4000")
print("2. 16GB - 6000")
print("3. 32GB - 10000")
ram_choice = int(input("Enter choice: "))
if ram_choice == 1:
    ram, ram_price = "8GB RAM", 4000
elif ram_choice == 2:
    ram, ram_price = "16GB RAM", 6000
else:
    ram, ram_price = "32GB RAM", 10000

# Storage
print("\nChoose Storage:")
print("1. SSD 512GB - 4000")
print("2. SSD 1TB - 8000")
print("3. HDD 2TB - 6000")
storage_choice = int(input("Enter choice: "))
if storage_choice == 1:
    storage, storage_price = "SSD 512GB", 4000
elif storage_choice == 2:
    storage, storage_price = "SSD 1TB", 8000
else:
    storage, storage_price = "HDD 2TB", 6000

# Cabinet
print("\nChoose Cabinet:")
print("1. Basic - 3000")
print("2. RGB - 5000")
print("3. Premium - 7000")
cab_choice = int(input("Enter choice: "))
if cab_choice == 1:
    cab, cab_price = "Cabinet Basic", 3000
elif cab_choice == 2:
    cab, cab_price = "Cabinet RGB", 5000
else:
    cab, cab_price = "Cabinet Premium", 7000

# Final Bill
total = cpu_price + gpu_price + ram_price + storage_price + cab_price
discount = total * 0.10
final_price = total - discount

print("\n---- FINAL BILL ----")
print(cpu, "-", cpu_price)
print(gpu, "-", gpu_price)
print(ram, "-", ram_price)
print(storage, "-", storage_price)
print(cab, "-", cab_price)
print("Total Price:", total)
print("10% Discount:", discount)
print("Amount to Pay:", final_price)

# Payment Method
print("\nChoose Payment Method:")
print("1. UPI")
print("2. Cash")
payment_choice = int(input("Enter choice: "))
if payment_choice == 1:
    print("Payment Method: UPI")
else:
    print("Payment Method: Cash")

print("\nThank you for shopping with us!")

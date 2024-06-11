num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))

def calc_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def calc_lcm(x, y):
    lcm = (x*y)//calc_gcd(x,y)
    return lcm

gcd = calc_gcd(num1, num2)
lcm = calc_lcm(num1, num2)

print("Ước chung lớn nhất của", num1, "và", num2, "là:", gcd)
print("Bội chung nhỏ nhất của", num1, "và", num2, "là:", lcm)

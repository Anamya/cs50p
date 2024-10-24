def main():
    mass = int(input("Enter the Mass in Kg: "))
    joules_calculation(mass)

def joules_calculation(kg):
    light_speed = 300000000
    joules = kg * (light_speed**2)
    print(joules)

main()

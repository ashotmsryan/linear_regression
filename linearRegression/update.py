def update(mil, theta0, theta1):
    return theta0 + (theta1 * mil)

if __name__=="__main__":
    theta0 = theta1 = 0
    try:
        mil = int(input("the mileage: "))
        print (update(mil, theta0, theta1))
    except IOERrror:
        print("invalid input")

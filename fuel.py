#MKHABELE MMM
#06/07/2023
def main():
    while True:
            try:
                fraction=input("Fraction: ")
                x,y=fraction.split("/")
                x=int(x)
                y=int(y)


                percentage=round((x/y)*100)
                if 1<percentage<99:
                     print(f"{percentage}%")
                     break
                if 0<=percentage<=1:
                     print('E')
                     break
                if 99<=percentage<=100:
                     print("F")
                     break
                else:
                     continue
            except ZeroDivisionError as e:
                 continue
            except ValueError as e:
                 continue

main()

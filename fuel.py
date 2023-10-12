#MKHABELE MMM
#06/07/2023
def main():
        while True:
            try:
                f=input("Fraction: ")
                x,y=f.split("/")
                if y==0:
                        raise ZeroDivisionError
                else:
                       print(gauge(convert(f)))
                       print(convert(f))
            except ZeroDivisionError as e:
                 continue
            except ValueError as e:
                 continue
            
def convert(fraction):
                      x,y=fraction.split("/")
                      x=int(x)
                      y=int(y)
                      p=round((x/y)*100)
                      return p

def gauge(percentage):
                if 1<percentage<99:
                     return (f"{percentage}%")

                if 0<=percentage<=1:
                     return ('E')

                if 99<=percentage<=100:
                     return ("F")
                
if __name__=="__main__":
      main()
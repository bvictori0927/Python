def win_percentage(x,y):
    win_percentage = (x + y)/2
    print("Your team's average is " , win_percentage)


def main():
    while True:
        x=int(input("Enter the number of wins: "))
        y=int(input("Enter the number of losses: "))
        win_percentage(x,y)


if __name__ == "__main__":
    main()

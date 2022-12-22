#
# Example file for working with conditional statements
#



def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    if x < y:
        result = "x is less than y."
        print(result)

    elif x == y:
        result = "x is equal to y."
        print(result);

    else:
        result = "x is greater than y."
        print(result)
# main()

# conditional statements let you use "a if C else b"

# match-case makes it easy to compare multiple values

value = "4"
match value:
    case "one":
        result = 1
    case "two":
        result = 2
    case "four":
        result = 4
    case _:
        result = -1
print(result)
# value = "one"
# if __name__ == "__main__":
#     main()


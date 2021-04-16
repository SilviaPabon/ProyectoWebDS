from stack.liststack import liststack


if __name__ == '__main__':

    stackn = liststack()
    stackn.push("o1")
    stackn.push("o3")
    stackn.push("o4")
    stackn.push("o5")
    print(stackn.size)
    print("search")
    print(stackn.searchs("1"))



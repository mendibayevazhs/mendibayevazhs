with open("commands.txt") as f:
    for index, line in enumerate(f, 1):
        print(f'action {index:03} cli command "{line.rstrip()}"')

def handle_file(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        content = [line.strip() for line in file]
    return content
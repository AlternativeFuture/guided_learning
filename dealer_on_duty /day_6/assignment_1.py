def find_bob(names: list, search_name: str) -> int:
    search_name = search_name.lower()
    for i, n in enumerate(names):
        if n.lower() == search_name:
            return i
    return -1


if __name__ == "__main__":
    name = 'Bob'
    print(find_bob(["Jimmy", "Layla", "Bob"], search_name=name))
    print(find_bob(["Bob", "Layla", "Kaitlyn", "Patricia"], search_name=name))
    print(find_bob(["Jimmy", "Layla", "James"], search_name=name))

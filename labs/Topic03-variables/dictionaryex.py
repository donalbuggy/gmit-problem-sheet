currentBook = {
    "title" : "Finglas Since the Flood",
    "author": "Marcus Lyons",
    "price" : 12
}

print(currentBook)

print(currentBook["author"])

currentBook["ISBN"] = "1132"

print("The current book has these values:")
for value in currentBook.values():
    print("   => {}".format(value))
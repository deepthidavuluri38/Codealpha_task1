# Simulated Web Scraping Dataset

books = [
    ["The Great Gatsby", 350, 4.5],
    ["Harry Potter", 450, 4.8],
    ["The Alchemist", 300, 4.6],
    ["Rich Dad Poor Dad", 280, 4.4],
    ["Atomic Habits", 500, 4.9]
]

print("Book Dataset")
print("-" * 40)
print("Title\t\t\tPrice\tRating")

for book in books:
    print(f"{book[0]}\t{book[1]}\t{book[2]}")

# Basic Analysis
total_price = 0
highest_rating = 0
best_book = ""

for book in books:
    total_price += book[1]

    if book[2] > highest_rating:
        highest_rating = book[2]
        best_book = book[0]

average_price = total_price / len(books)

print("\nData Analysis Results")
print("-" * 40)
print("Number of Books:", len(books))
print("Average Price:", round(average_price, 2))
print("Highest Rated Book:", best_book)
print("Rating:", highest_rating)

from reviewer import review_code

print("=== AI Code Review Assistant ===")

print("Paste your code below.")

print("Type END on a new line when finished.\n")

lines = []

while True:
    line = input()

    if line == "END":
        break

    lines.append(line)

code = "\n".join(
    f"{i + 1}: {line}"
    for i, line in enumerate(lines)
)

print("\nReviewing your code...\n")

review = review_code(code)

print(review)
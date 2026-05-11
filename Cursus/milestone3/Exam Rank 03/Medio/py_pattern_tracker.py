def pattern_tracker(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        current = int(text[i])
        next = int(text[i + 1])
        if next - current == 1:
            count += 1

    return count

if __name__ == "__main__":
    print(pattern_tracker("1245"))

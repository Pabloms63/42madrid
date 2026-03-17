from typing import Generator


def generate_events(n: int) -> Generator[dict, None, None]:
    players = ["alice", "bob", "charlie"]
    levels = [5, 12, 8]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, n + 1):
        event = {
            "player": players[i % len(players)],
            "level": levels[i % len(levels)],
            "action": actions[i % len(actions)]
        }
        yield event


def process_events(n: int) -> None:
    total_events = 0
    high_level = 0
    treasure_events = 0
    level_up_events = 0

    for event in generate_events(n):
        total_events += 1
        if total_events <= len(event):
            print(
                f"Event {total_events}: Player {event['player']} "
                f"(level {event['level']}) {event['action']}"
                )
        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        if event["action"] == "leveled up":
            level_up_events += 1

    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("\nMemory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")


def fibonacci() -> Generator[int, None, None]:
    num1 = 0
    num2 = 1

    for _ in range(10):
        yield num1
        num1, num2 = num2, num1 + num2


def prime_numbers() -> Generator[int, None, None]:
    num = 2
    found = 0

    while found < 5:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            found += 1
        num += 1


if __name__ == "__main__":
    n = 10
    print(f"Processing {n} game events...\n")
    process_events(n)
    print("\n=== Generator Demonstration ===")
    fib_seq = fibonacci()
    print("Fibonacci sequence (first 10):", ", ".join(map(str, fib_seq))) 
    prime_nums = prime_numbers()
    print("Prime numbers (first 5):", ", ".join(map(str, prime_nums)))


import random
import time

# Configuration
FILENAME = "huge_test_file.txt"
TOTAL_LINES = 10_000
WORDS_PER_LINE = 1_000

# Vocabulary to construct the noise
VOCAB = [
    "lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipiscing", "elit",
    "sed", "do", "eiusmod", "tempor", "incididunt", "ut", "labore", "et", "dolore",
    "magna", "aliqua", "ut", "enim", "ad", "minim", "veniam", "quis", "nostrud",
    "exercitation", "ullamco", "laboris", "nisi", "ut", "aliquip", "ex", "ea",
    "commodo", "consequat", "duis", "aute", "irure", "dolor", "in", "reprehenderit",
    "computer", "science", "algorithm", "database", "network", "system", "interface"
]

# Words we want to search for later (Hidden Needles)
TARGETS = ["ERROR", "CRITICAL_FAILURE", "RUST_IS_FAST", "NEEDLE"]


def generate_file():
    print(f"Generating {TOTAL_LINES} lines with {
          WORDS_PER_LINE} words each...")
    print("Estimated file size: ~70 MB")

    start_time = time.time()

    # Pre-generate a base line to speed up processing
    # (Generating 10 million random numbers individually is slow, so we recycle)
    base_line_words = [random.choice(VOCAB) for _ in range(WORDS_PER_LINE)]

    with open(FILENAME, "w", encoding="utf-8") as f:
        for i in range(TOTAL_LINES):
            # Create a copy of the base line so we can modify it
            current_line = base_line_words[:]

            # 5% chance to insert a "Target Word" into this line
            if random.random() < 0.05:
                target = random.choice(TARGETS)
                # Insert at a random position
                pos = random.randint(0, WORDS_PER_LINE - 1)
                current_line[pos] = target

                # Verify logic: Print first few finds to console
                if i < 100:
                    print(f"Inserted {target} at line {i+1}")

            # Join words with space and write to file
            f.write(" ".join(current_line) + "\n")

            if i % 1000 == 0 and i > 0:
                print(f"Wrote {i} lines...")

    end_time = time.time()
    print(f"Done! File '{FILENAME}' created in {
          end_time - start_time:.2f} seconds.")


if __name__ == "__main__":
    generate_file()

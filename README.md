Haystack Generator 🌾

A zero-dependency Python tool designed to generate massive, high-entropy text files ("Haystacks") with hidden target words ("Needles").

This tool is specifically built for benchmarking CLI search tools (like grep, ripgrep, or custom Rust implementations) to test their speed, memory usage, and concurrency capabilities.

--- QUICK START ---

Run the script:
python3 generate_data.py

Wait a few seconds:
It will generate a file named huge_test_file.txt (approx. 70MB by default).

Benchmark your tool:

Search for one of the hidden needles

time grep "RUST_IS_FAST" huge_test_file.txt

--- CONFIGURATION ---

You can fully customize the generator by modifying the constants at the top of generate_data.py.

File Size
Adjust the total volume of data generated:

Approx 70MB file (Default)

TOTAL_LINES = 10_000
WORDS_PER_LINE = 1_000

Approx 700MB file (Warning: takes longer to generate)

TOTAL_LINES = 100_000

Vocabulary & Search Targets

VOCAB: Add or remove words from this list to change the "noise" text (e.g., customize it to look like server logs or prose).

TARGETS: Modify this list to change the hidden words (needles) you will be searching for later.

Difficulty Control

NEEDLE_CHANCE: Adjust the probability of a needle appearing in a line (value between 0.0 and 1.0).

1.0: Every line has a needle (100% chance).

0.05: 5% of lines have a needle (Default).

0.0: No needles are inserted.

--- HOW IT WORKS ---

Noise Generation: It constructs lines using a randomized vocabulary of "Lorem Ipsum" and tech-related words to simulate realistic text data.

Needle Injection: It randomly inserts specific target words (e.g., ERROR, RUST_IS_FAST, NEEDLE) based on the configured probability.

Performance Optimization: The script recycles memory objects to generate 10+ million words in seconds, rather than minutes.

--- USE CASES ---

Testing Memory Mapping (mmap) vs Standard I/O.

Benchmarking Parallel processing (rayon) vs Single-threaded search.

Stress testing Regex engines against long lines (1k+ words per line).

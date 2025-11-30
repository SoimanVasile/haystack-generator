Haystack Generator 🌾

A zero-dependency Python tool designed to generate massive, high-entropy text files ("Haystacks") with hidden target words ("Needles").

This tool is specifically built for benchmarking CLI search tools (like grep, ripgrep, or custom Rust implementations) to test their speed, memory usage, and concurrency capabilities.

⚡ Quick Start

Run the script:

python3 generate_data.py


Wait a few seconds:
It will generate a file named huge_test_file.txt (approx. 70MB by default).

Benchmark your tool:

# Search for one of the hidden needles
time grep "RUST_IS_FAST" huge_test_file.txt


⚙️ Configuration

You can adjust the size of the generated file by modifying the constants at the top of generate_data.py:

# Approx 70MB file
TOTAL_LINES = 10_000
WORDS_PER_LINE = 1_000

# Approx 700MB file (Warning: takes longer to generate)
TOTAL_LINES = 100_000 


🎯 How it Works

Noise Generation: It constructs lines using a randomized vocabulary of "Lorem Ipsum" and tech-related words to simulate realistic text data.

Needle Injection: It randomly inserts specific target words (e.g., ERROR, RUST_IS_FAST, NEEDLE) with a 5% probability per line.

Performance Optimization: The script recycles memory objects to generate 10+ million words in seconds, rather than minutes.

🧪 Use Cases

Testing Memory Mapping (mmap) vs Standard I/O.

Benchmarking Parallel processing (rayon) vs Single-threaded search.

Stress testing Regex engines against long lines (1k+ words per line).

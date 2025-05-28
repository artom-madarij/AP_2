def read_input(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def write_output(filename, value):
    with open(filename, 'w') as f:
        f.write(str(value) + "\n")

def longest_chain(words):
    word_ = set(words)

    buckets = [[] for _ in range(51)]
    for word in words:
        buckets[len(word)].append(word)
    dp = {}

    chain = 1

    for length in range(1, 51):
        for word in buckets[length]:
            best = 1
            for i in range(len(word)):
                shorter = word[:i] + word[i+1:]
                if shorter in word_:
                    best = max(best, dp.get(shorter, 1) + 1)
            dp[word] = best
            chain = max(chain, best)

    return chain

def solve_wchain():
    data = read_input('src/wchain.in.txt')
    n = int(data[0])
    words = data[1:]

    result = longest_chain(words)

    write_output('src/wchain.out.txt', result)

if __name__ == "__main__":
    solve_wchain()

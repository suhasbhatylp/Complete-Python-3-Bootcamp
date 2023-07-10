def extract_strings(filename):
    result = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#'):
                words = line.strip().split()
                for word in words:
                    if word.startswith('dov') and word.endswith('com'):
                        result.append(word)
    return result

# Usage
filename = '/etc/haproxy/haproxy.cfg'
strings = extract_strings(filename)
print(strings)
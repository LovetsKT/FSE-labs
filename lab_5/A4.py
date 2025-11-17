def rle_decode(s):
    res = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            res.append(s[i+1] * int(s[i]))
            i += 2
        else:
            res.append(s[i])
            i += 1
    return ''.join(res)

proteins = {}
with open('sequences.0.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            parts = line.split('\t')
            if len(parts) == 3:
                name = parts[0]
                organism = parts[1]
                sequence = parts[2]
                proteins[name] = (organism, sequence)

commands = []
with open('commands.0.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if line:
            parts = line.split('\t')
            commands.append(parts)

with open('genedata.0.txt', 'w', encoding='utf-8') as out:
    out.write("Ловец Константин\n")
    out.write("Генетический поиск\n")
    out.write("-------------------------------------------------------------------------------------\n")
    for i, cmd in enumerate(commands, 1):
        operation = cmd[0]
        out.write(f"{i:03d}\t{operation}\t{''.join(cmd[1:])}\n")

        if operation == 'search':
            pattern = rle_decode(cmd[1])
            found = []
            for name, (org, seq) in proteins.items():
                if pattern in seq:
                    found.append((org, name))

            out.write("organism\t\t\t\tprotein\n")
            if found:
                for org, name in found:
                    out.write(f"{org}\t{name}\n")
            else:
                out.write("NOT FOUND\n")

        elif operation == 'diff':
            protein1 = cmd[1]
            protein2 = cmd[2]
            missing = []
            if protein1 not in proteins:
                missing.append(protein1)
            if protein2 not in proteins:
                missing.append(protein2)

            if missing:
                out.write("amino-acids difference\n")
                out.write("MISSING " + ", ".join(missing) + "\n")
            else:
                seq1 = proteins[protein1][1]
                seq2 = proteins[protein2][1]
                min_len = min(len(seq1), len(seq2))
                diff_count = 0
                for i in range(min_len):
                    if seq1[i] != seq2[i]:
                        diff_count += 1
                diff_count += abs(len(seq1) - len(seq2))
                out.write("amino-acids difference\n")
                out.write(f"{diff_count}\n")

        elif operation == 'mode':
            protein_name = cmd[1]
            if protein_name not in proteins:
                out.write("amino-acid occurs\n")
                out.write(f"MISSING {protein_name}\n")
            else:
                seq = proteins[protein_name][1]
                from collections import Counter

                counter = Counter(seq)
                max_count = max(counter.values())
                candidates = [amino for amino, cnt in counter.items() if cnt == max_count]
                candidates.sort()
                selected_amino = candidates[0]
                out.write("amino-acid occurs\n")
                out.write(f"{selected_amino}\t{max_count}\n")
        out.write("-------------------------------------------------------------------------------------\n")
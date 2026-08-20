class Solution:
    def fullJustify(self, words, maxWidth):
        res, line, length = [], [], 0

        for w in words:
            if length + len(w) + len(line) > maxWidth:
                # Distribute spaces
                for i in range(maxWidth - length):
                    line[i % (len(line) - 1 or 1)] += ' '
                res.append(''.join(line))
                line, length = [], 0
            line.append(w)
            length += len(w)

        # Last line: left-justified
        res.append(' '.join(line).ljust(maxWidth))
        return res

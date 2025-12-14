import random
import sys

class God:
    def __init__(self, path: str, amount: int):
        self.words = self._read_words(path)
        self.amount = amount

    @staticmethod
    def _read_words(path: str) -> list[str]:
        with open(path, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    def _format_text(self, text: str) -> str:
        words = text.split()
        result = []
        
        for word in words:
            if random.random() > 0.3:
                word = word.capitalize()
            if random.random() < 0.05:
                word = word + '.'
            result.append(word)
        
        formatted = ' '.join(result)
        lines = []
        current = []
        length = 0
        
        for word in formatted.split():
            if length + len(word) + 1 > 60:
                lines.append(' '.join(current))
                current = [word]
                length = len(word)
            else:
                current.append(word)
                length += len(word) + 1
        
        if current:
            lines.append(' '.join(current))
        
        return '\n'.join(lines)

    def speak(self) -> str:
        selected = [random.choice(self.words) for _ in range(self.amount)]
        raw = ' '.join(selected)
        return self._format_text(raw)


def main():
    print(f"God says.... {God("HAPPY.TXT", 32).speak()}")


if __name__ == "__main__":
    main()

import random
import string

class DataGenerator:
    def generate_random_text(self, size: int) -> str:
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(size))

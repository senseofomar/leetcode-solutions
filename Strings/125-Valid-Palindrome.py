def is_palindrome(self, s: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())  # keep only letters & numbers
    return cleaned == cleaned[::-1]

def is_palindrome1(self, s: str) -> bool:
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

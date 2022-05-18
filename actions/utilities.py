def translate(character: bytes) -> str:
    if character == b'x':
        return 'x'
    elif character == b'o':
        return 'o'
    elif character == b'-':
        return '-'
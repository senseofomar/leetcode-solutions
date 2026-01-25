def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]  # box index: (r//3)*3 + (c//3)

    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.':
                continue

            # row check
            if val in rows[r]:
                return False
            rows[r].add(val)

            # column check
            if val in cols[c]:
                return False
            cols[c].add(val)

            # box check
            b = (r // 3) * 3 + (c // 3)
            if val in boxes[b]:
                return False
            boxes[b].add(val)

        return True

def is_valid_sudoku1(board):
    seen = set()
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            if val == '.': continue
            row_key = f"row{r}-{val}"
            col_key = f"col{c}-{val}"
            box_key = f"box{r//3}-{c//3}-{val}"
            if row_key in seen or col_key in seen or box_key in seen:
                return False
            seen.update((row_key, col_key, box_key))
    return True
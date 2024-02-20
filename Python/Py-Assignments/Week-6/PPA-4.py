def dim_equal(A, B):
    a_row = len(A)
    b_row = len(B)
    a_clmn = len(A[0])
    b_clmn = len(B[0])

    if a_row == b_row and a_clmn == b_clmn:
        return True
    else:
        return False
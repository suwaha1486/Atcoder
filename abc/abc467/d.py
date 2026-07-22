T = int(input())
for _ in range(T):
    Px, Py, Qx, Qy, Rx, Ry, Sx, Sy = map(int, input().split())
    # PQの垂直二等分線の傾きとRSの垂直二等分線の傾きが一致するかどうか
    # PQ_steep_inv = - (Qx - Px) / (Qy - Py)
    # RS_steep_inv = - (Rx - Sx) / (Ry - Sy)
    # 平行なら(Qx - Px) * (Ry - Sy) = (Qy - Py) * (Rx - Sx)

    if (Qx - Px) * (Ry - Sy) == (Qy - Py) * (Rx - Sx):
        # 平行だとしても，垂直二等分線が一致していたらYes
        # PQの二等分点とRSの二等分点を結ぶ直線の傾きとPQの垂直二等分線の傾きが一致するかどうか
        PQx = (Px + Qx) / 2
        PQy = (Py + Qy) / 2
        RSx = (Sx + Rx) / 2
        RSy = (Sy + Ry) / 2
        if (PQy - RSy) * (Py - Qy) == - (Px - Qx) * (PQx - RSx):
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")
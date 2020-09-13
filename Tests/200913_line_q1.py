def solution(boxes):
    import numpy as np

    # flatten
    flatten = np.array(boxes).flatten()
    boxes = np.sort(flatten).tolist()

    # del 중복
    c = 1
    while boxes:
        try:
            if len(boxes) < c: break

            if boxes[c - 1] == boxes[c]:
                boxes.pop(c)
                boxes.pop(c - 1)
            else:
                c += 1
        except IndexError:
            break

    return int(len(boxes)/2)
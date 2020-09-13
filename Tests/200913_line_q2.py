def solution(ball, order):
    from collections import deque
    ball=deque(ball)
    qu=[]
    answer = []

    # for o in order:
    c=0
    # for o in order:
    while len(ball) > 0:
        try:
            first=ball[0]
            last=ball[-1]

            if len(qu)>0:
                firsttest=first in qu
                lasttest=last in qu
                if firsttest and lasttest:
                    if qu.index(first)>qu.index(last):
                        answer.append(ball.popleft())
                        qu.remove(first)
                        continue
                    else:
                        answer.append(ball.pop())
                        qu.remove(last)
                        continue

                elif firsttest:
                    answer.append(ball.popleft())
                    qu.remove(first)
                    continue
                elif lasttest:
                    answer.append(ball.pop())
                    qu.remove(last)
                    continue

            if len(order)>=c:
                if order[c]==first:
                    answer.append(ball.popleft())
                    c+=1
                elif order[c]==last:
                    answer.append(ball.pop())
                    c+=1
                else:
                    qu.append(order[c])
                    c+=1

        except IndexError:
            break


    return answer
# 하노이의 탑
# Subtask:
# - Place the rest to the second rod.
# - Then, place the biggest disk to the destination rod.
# - ??? => PROFIT!
def addProcedure(answer, fromRod, toRod):
    answer.append([fromRod, toRod])

def helperHanoi(answer, n, fromRod, toRod, auxRod):
    # Actual move happens here
    if n == 1:
        addProcedure(answer, fromRod, toRod)
        return
    else:
        # Proceed the step 1 (fromRod -> auxRod)
        helperHanoi(answer, n - 1, fromRod, auxRod, toRod)
        # Place the biggest disk to the destination rod
        addProcedure(answer, fromRod, toRod)
        # Move the rest disks to the destination rod as well
        helperHanoi(answer, n - 1, auxRod, toRod, fromRod)

def solution1(n):
    answer = []
    helperHanoi(answer, n, 1, 3, 2)
    return answer

if __name__ == "__main__":
    print(solution1(2))
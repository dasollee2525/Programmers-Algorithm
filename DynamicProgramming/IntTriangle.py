#TopDown
#https://codedrive.tistory.com/49
def solution(triangle):
    answer = triangle[0][0] #가장 꼭대기에 있는 값
    if len(triangle)==2:
        answer += max(triangle[1])
    else:
        length = len(triangle)
        d = [0] * length
        d[0] = triangle[0]
        for i in range(1,length): # 층 수, level = i+1
            d[i] = [0] * (i+1)
            for j in range(i+1):
                if j==0: #왼쪽끝
                    d[i][j] = d[i-1][j] + triangle[i][j]
                elif j==i: #오른쪽끝
                    d[i][j] = d[i-1][j-1] + triangle[i][j]
                else:
                    d[i][j] = max(d[i-1][j-1],d[i-1][j]) + triangle[i][j]
        answer = max(d[length-1])
    return answer

#BottomUp
def solution(triangle):

    height = len(triangle)

    while height > 1:
        for i in range(height - 1):
            triangle[height-2][i] += max([triangle[height-1][i], triangle[height-1][i+1]])
        height -= 1

    answer = triangle[0][0]
    return answer

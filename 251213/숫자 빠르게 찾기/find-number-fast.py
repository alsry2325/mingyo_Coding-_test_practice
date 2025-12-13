n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [int(input()) for _ in range(m)]

# Please write your code here.
arr.sort() # 이진탐색은 정렬이 필요하기때문에 함수정렬사용

def find(i,arr): 
    left = 0  #여기서 왼쪽은 arr의 위치 
    right = len(arr) - 1  #여기는 arr 끝 위치 
    while left <= right: #왼쪽이 오른쪽보다 작을때까지만 실행을 할거야
        mid = (left + right)//2  #  중간 값 위치 
        
        if arr[mid] == i:  #타겟이랑 중간값이 일치하면 반환
            return mid+1  #출력에서 시작이 1부터라서 +1을 해줌
        
        if arr[mid] > i:  #중간값이 타겟보다 크다면 
            right = mid -1  # 오른쪽값 위치 한칸 앞으로  
        else:
            left = mid +1 # 그렇지않으면  왼쪽값  한칸 뒤로 전진
    return -1  # 없다면 -1를 반환   

for i in queries:  # m개의 숫자를 queries에 넣음  queries갯수만큼 돌린다
    
    print(find(i,arr))  #queries를  하나씩 꺼냄  비교할 arr배열도 같이 




    



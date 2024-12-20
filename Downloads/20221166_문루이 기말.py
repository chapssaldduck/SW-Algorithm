#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def generate_students(num_students=30):
    students = []
    for _ in range(num_students):
        name = chr(random.randint(65, 90)) + chr(random.randint(65, 90))
        age = random.randint(18, 22)
        grade = random.randint(0, 100)
        students.append({"이름": name, "나이": age, "성적": grade})
    return students

# 선택 정렬
def selection_sort(arr, key):
    n = len(arr)
    for i in range(n - 1):
        least = i
        for j in range(i + 1, n):
            if arr[j][key] < arr[least][key]:
                least = j
        arr[i], arr[least] = arr[least], arr[i]
    return arr

# 삽입 정렬
def insertion_sort(arr, key):
    n = len(arr)
    for i in range(1, n):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and arr[j][key] > key_item[key]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item
    return arr

# 퀵 정렬
def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) //2][key]
    left = [x for x in arr if x[key] < pivot]
    middle = [x for x in arr if x[key] == pivot]
    right = [x for x in arr if x[key] > pivot]
    return quick_sort(left, key) + middle + quick_sort(right, key)

# 기수 정렬
def radix_sort(arr, key):
    max_grade = max(arr, key=lambda x: x["성적"])["성적"]
    exp = 1
    while max_grade // exp > 0:
        arr = counting_sort(arr, key, exp)
        exp *= 10
    return arr

# 계수 정렬
def counting_sort(arr, key, exp):
    output = [None] * len(arr)
    count = [0] * 10

    for student in arr:
        index = (student[key] // exp) % 10
        count[index] += 1
        
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    i = len(arr) - 1
    while i >= 0:
        student = arr[i]
        index = (student[key] // exp) % 10
        output[count[index] - 1] = student
        count[index] -= 1
        i -= 1
        
    for i in range(len(arr)):
        arr[i] = output[i]
    return arr
    


# 정렬한 결과 출력
def print_student(students):
    for student in students:
        print(f"이름: {student['이름']}, 나이: {student['나이']}, 성적: {student['성적']}")
    print()

# 메뉴 퀵 정렬 함수 실행
def main():
    students = generate_students()
    print('생성된 학생 정보:')
    print_student(students)
    
    while True:
        print("메뉴:")
        print("1. 이름을 기준으로 정렬")
        print("2. 나이를 기준으로 정렬")
        print("3. 성적을 기준으로 정렬")
        print("4. 프로그램 종료")
    
        choice = input("정렬 기준을 선택하세요(1,2,3,4) ")
        if choice == "4":
            print("프로그램을 종료합니다.")
            break
        
        if choice not in("1", "2", "3", "4"):
            print("잘못된 입력입니다. 다시 선택하세요.")
            continue
        
        if choice == "1":
            key = "이름"
        elif choice == "2":
            key = "나이"
        elif choice == "3":
            key = "성적"

        # 정렬 알고리즘 선택
        print("정렬 알고리즘 선택:")
        print("1. 선택 정렬")
        print("2. 삽입 정렬")
        print("3. 퀵 정렬")
        if key == "성적":
            print("4. 기수 정렬")

        algo_choice = input("정렬 알고리즘을 선택하세요(1,2,3,4):")

        #정렬 수행
        if algo_choice == "1":
            sorted_students = selection_sort(students, key)
        elif algo_choice == "2":
            sorted_students = insertion_sort(students, key)
        elif algo_choice == "3":
            sorted_students = quick_sort(students, key)
        elif algo_choice == "4" and key == "성적":
            sorted_students = radix_sort(students, key)
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")
            continue

        if key == "이름":
            print("이름을 기준으로 정렬된 결과:")
        elif key == "나이":
            print("나이를 기준으로 정렬된 결과:")
        elif key == "성적":
            print("성적을 기준으로 정렬된 결과:")

        print_student(sorted_students)

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:





""" my_var = 10
print(my_var)

my_list = [1, 2, 3]
print(*my_list)

my_int = 10
print(my_int)

my_float = 3.14
print(my_float)

my_complex = 3 + 4j
print(my_complex)

my_character = ' A '
print(my_character)  

my_char = "@"
print(my_char)
 
my_string = 'hello, world!'
print(my_string)

str_name = "python"
print(str_name) """

""" my_list = [10, 3, 8, 9, 42, "hello"]
print(my_list) """

#크기
""" print(my_list.__len__())  """

#인덱스
""" print(my_list[3])

list_el = my_list[2] """

""" print(list_el) """

#엘리멘트 변경
""" my_list[3] = 11 """

""" n_add = my_list[3] + my_list[2]
print(n_add) """

#슬라이싱
""" print(my_list[2:5]) """

""" print(my_list[:3])

print(my_list[0:3]) """

""" print(my_list[4:]) """

#이중리스트
""" my_list = [10, 3, 8, 9, 42, "hello", [5, 4, 2, "world"]]

print(my_list)
 """
""" print(my_list[6][1]) """

""" print(my_list[6][2:]) """

#메소드

#insert(index, value) / index 번째, value 삽입
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

my_list.insert(2, 4)

print(*my_list) """

#index(value) / 해당 value의 순서를 출력
""" my_list = [10, 3, 8, 9, 42, "hello"]

print(my_list.index(3)) """

#append(value)
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

my_list.append(22)

print(*my_list) """

#count(value) / value와 동일한 요소, 개수 출력
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]

print(my_list.count(8)) """

#pop() / 마지막 요소 출력 후 삭제
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]

print(my_list)
print(my_list.pop())
print(*my_list) """

#sort() / 오름차순으로 정렬
""" my_list = [10, 3, 8, 9, 42, 8] """
""" my_list = [' c ', ' a ', ' z ']
print(my_list)
my_list.sort()

print(*my_list) """

#reverse() / 역순으로 정렬
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)
my_list.reverse()

print(*my_list) """

#extend(list) / 두 리스트를 결합
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
list_tmp = [5, 7, "world"]

print(my_list, list_tmp)

my_list.extend, (list_tmp)

print(*my_list) """

#clear() / 리스트 내,  value 전체 삭제
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
list_tmp = [5, 7, "world"]

print(my_list, list_tmp)

my_list.extend(list_tmp)

print(*my_list)

list_tmp.clear()

print(list_tmp) """

#remove(value) / 해당 value 삭제
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

my_list.remove(3)

print(*my_list) """

#del list[n] / del 구문의 인덱스를 이용해 요소 삭제
""" my_list = [10, 3, 8, 9, 42, 8, "hello"]
print(my_list)

del my_list[2]

print(*my_list) """

#Tuple

""" my_tuple = (1, 2, 'three', True)
print(my_tuple)

tpItem = (3.14, "b", 'two', False)
print(tpItem) """

""" my_tup = (4, 2, 6, 1, "py", "w")

print(my_tup)
print(my_tup[2])
print(*my_tup) """

""" my_tup = (4, 2, 6, 1, "py", "w")

print(my_tup)
print(my_tup[2])
my_tup[3] = 2
print(*my_tup) """

""" my_tup = (4, 2, 6, 1, "py", "w")

print(my_tup)
print(my_tup[2] + my_tup[0])
print(*my_tup) """

""" my_tup = (4, 2, 6, 1, "py", "w")

print(my_tup)
n_add = my_tup[1] + my_tup[3]
print(n_add) """

#이중 튜플
""" my_tup = (4, 2, 6, 1, "py", "w", ("h", 8, 7, 3))
print(my_tup)
print(my_tup[6][0]) """

""" my_tup = (4, 2, 6, 1, "py", "w")

print(my_tup.index(2, 0, 3)) """

""" my_tup = (4, 2, 6, 1, "py", "w")

print(my_tup.index("py", 3, 5)) """

""" my_tup = (4, 2, 6, 1, "py", "w")

print(my_tup.index(1, 0, 3)) """

#dictionary

""" my_dict = {'key1' : 'value1', 'key2' : 'value2'}
dicData = {"name" : "python",  "number" : 23564897}

my_item = my_dict.items()

print(my_item) """

#생성
""" idx = ("key1", "key2", "key3")

dicts = dict.fromkeys(idx, "0")

print(dicts) """

#인덱싱
""" my_dict = {'key1' : 'value1', 'key2' : 'value2'}
dicData = {"name" : "python",  "number" : 23564897}
print(my_dict["key1"])

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_str = my_dict.get("key2")
print(my_str)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
print(my_dict.pop("key1"))
print(my_dict) """

#복사
""" my_dict = {'key1' : 'value1', 'key2' : 'value2'}
dicts = my_dict.copy()
print(dicts)
print(my_dict) """

#추가 / 변경
""" my_dict = {'key1' : 'value1', 'key2' : 'value2'}
dicData = {"name" : "python",  "number" : 23564897}
my_dict["key3"] = "value3" """

""" my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_dict.setdefault("key3")
print(my_dict)

my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_dict.update({"key1" : "v4"})
print(my_dict)
"""

#삭제
""" my_dict = {'key1' : 'value1', 'key2' : 'value2'}
del my_dict["key2"]
print(my_dict) """

#검색
""" my_dict = {'key1' : 'value1', 'key2' : 'value2'}
print("key2" in my_dict)
print("key3" in my_dict) """

#변환
""" my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_list = list(my_dict.keys())
print(my_list)
 """
""" my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_list = list(my_dict.values())
print(my_list) """

""" my_dict = {'key1' : 'value1', 'key2' : 'value2'}
my_set = set(my_dict.keys())
print(my_set) """

""" my_dict = {'key1' : 'value1', 'key2' : 'value2'}

my_dict.clear()
print(my_dict) """
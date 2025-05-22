name_list = []
# 상품명 목록
price_list = []
# 가격 목록

title = ""
menu = "1.추가하기\n2.수정하기\n3.삭제하기\n4.검색하기\n5.목록보기\n6.나가기\n"
search_menu = "1.상품명으로 검색\n2.가격으로 검색\n"
append_message = '추가하실 상품명과 가격을 입력하세요.\n예)상품명 가격'
search_name_message_for_update = '수정하실 상품명을 입력하세요.'
update_message = '새로운 상품명과 가격을 입력하세요.\n예)상품명 가격'
delete_message = '삭제하실 상품명을 입력하세요.'
search_name_message, search_price_message = '상품명: ', '가격: '

append_error_message = "추가 실패(중복된 상품명)"
update_error_message = "수정 실패(존재하지 않는 상품명)"
delete_error_message = "삭제 실패(존재하지 않는 상품명)"
search_name_error_message = "검색 실패(존재하지 않는 상품명)"
search_error_message = "검색 결과가 없습니다."
error_message = "다시 입력해주세요."
no_item_message = "목록이 없습니다."

while True:
    choice = int(input(title + "\n" + menu))
    # 선택할 메뉴를 숫자로 선택

    # 추가
    if choice == 1:
        new_name, new_price = input(append_message).split(" ")
        # 띄어 쓰기로 구분 해서 상품 명과 가격 입력 받음.
        if new_name not in name_list: # 만약 새로 입력한 상품 명이 기존 상품명 목록에 없다면 추가
            name_list.append(new_name)
            price_list.append(int(new_price)) # 입력된 가격도 추가.
        else:
            print(append_error_message) # 중복된 상품이 있기 때문에 에러 메시지 출력
    # 수정
    elif choice == 2:
        name = input(search_name_message_for_update)
        # 수정할 품목의 이름 입력
        if name in name_list:
            index = name_list.index(name)
            # 해당 상품의 index를 가져옴
            new_name, new_price = input(update_message).split(" ")
            # 새로 바꿀 상품 명과 가격을 입력 받은 뒤
            name_list[index] = new_name
            price_list[index] = new_price
            # 기존 상품 index의 상품 명과 가격을 대체함.
        else:
            print(update_error_message) # 만약 해당 하는 품목 명이 없다면, 에러
    # 삭제
    elif choice == 3:
        # 상품명 입력 받기
        name = input(delete_message)
        if name in name_list: # 해당 하는 상품이 있을 경우
            # 해당 상품의 index를 가져오고, 상품 리스트 및 가격 list 에서 해당 index의 내용을 지움.
            del price_list[name_list.index(name)]
            name_list.remove(name)

        else: # 해당 하는 상품이 없는 경우.
            print(delete_error_message)

    # 검색
    elif choice == 4:
        # 메뉴 선택
        choice = int(input(search_menu))
        # 상품명으로 검색
        if choice == 1:
            # 상품명 입력
            name = input(search_name_message)
            if name in name_list: # 일치하는 상품명 있을 때
                index = name_list.index(name) # 해당 상품의 인덱스를 가져옴.
                print(f'{name_list[index]} - {price_list[index]}') # 인덱스로 상품명과 가격을 가져와서 순서대로 출력
            else: # 일치하는 상품명 없을 때.
                print(search_name_error_message)

        # 가격으로 검색
        elif choice == 2:
            check = False # flag
            price = int(input(search_price_message)) # 가격 입력 받기
            min = price * 0.5
            max = price * 1.5
            # 검색할 가격 범위 설정.
            for i in range(len(price_list)):
                if min <= price_list[i] <= max: # 가격 list의 각 data가 검색 범위 안에 있을 때.
                    check = True # 하나라도 일치할 경우. flag 변경.
                    print(f'{name_list[i]} - {price_list[i]}') # 해당 하는 data의 index로 부터 상품 명과 가격 출력.

            if not check: # 범위에 일치 하는 가격이 하나도 없는 경우.
                print(search_error_message) # 에러

        # 그 외
        else:
            print(error_message)
        pass

    # 목록
    elif choice == 5:
        if len(name_list) == 0: #데이터가 없는 경우.
            print(no_item_message)
            continue # elif 밖으로 나감.

        for i in range(len(name_list)): # 데이터가 있는 경우.
            print(f'{name_list[i]} - {price_list[i]}') # index로 상품명 - 가격 출력.

    # 나가기
    elif choice == 6:
        break

    # 그 외
    else:
        print(error_message)
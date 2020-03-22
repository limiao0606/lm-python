import cards_tools
while True:
    #显示功能菜单
    cards_tools.show_menu()
    action_str = input("请选择您希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)
    # 1,2,3: 针对名片操作
    if action_str in ["1", "2", "3"]:
    # 1.新建名片；2.显示全部；3.查询名片
        if action_str == "1":
            #新建名片
            cards_tools.new_card()
        elif action_str == "2":
            #显示全部
            cards_tools.show_all()
        elif action_str == "3":
            #TODO 查询名片
            cards_tools.search_card()
    # pass 占位符
    # 0 :退出系统
    elif action_str == "0":
        print("退出系统")
        break
    # 输入其他内容:提示入错误，需要重新输入
    else:
        print("您输入的内容有误，请重新输入")
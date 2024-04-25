def get_seat_type(seat_number):

    floor = "上层" if int(seat_number) % 2 == 0 else "下层"

    if 1 <= int(seat_number) <= 36:
        position = "车厢"
    else:
        position = "侧面"

    return f"{floor} {position}"


if __name__ == "__main__":
    seat_number = input("请输入座位号：")
    seat_type = get_seat_type(seat_number)
    print(f"预留座位的类型是：{seat_type}")

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}是闰年")
    else:
        print("这不是闰年")

# 测试函数
year = 2024
is_leap_year(year)  # 输出：2024是闰年

def mix_colors(color1, color2):
    if color1 == '红色':
        if color2 == '蓝色':
            return '紫色'
        elif color2 == '黄色':
            return '橙色'
    elif color1 == '蓝色':
        if color2 == '红色':
            return '紫色'
        elif color2 == '黄色':
            return '绿色'
    elif color1 == '黄色':
        if color2 == '红色':
            return '橙色'
        elif color2 == '蓝色':
            return '绿色'
    else:
        return '错误：请输入“红色”、“蓝色”或“黄色”。'

# 获取用户输入
color1 = input('请输入第一种颜色（红色、蓝色或黄色）：')
color2 = input('请输入第二种颜色（红色、蓝色或黄色）：')

# 调用函数并打印结果
result = mix_colors(color1, color2)
print(result)
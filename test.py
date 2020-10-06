if __name__ == "__main__":
    frames = ''
    frame = ''
    result = []
    print('для окончания введите end')
    while True:
        # frames.append(str(input().split(' ')))
        frame = input() + ' '
        if frame.find('end') != -1:
            break
        frames += frame
    result = frames.split()
    # print(result)
    print(f"введено номеров: {len(result)}")
    print(f"различных номеров: {len(set(result))}")
    for item in set(result):
        result.remove(item)
    print(f"Совпадающие кадры: {result}")
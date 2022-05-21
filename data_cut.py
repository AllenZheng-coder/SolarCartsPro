def data_cut(data,split):
    '''
    This is a module to cut data
    Input two list - data and split
    Then it'll return a list - each part's size
    By Duan-JunHan
    '''
    data_len = len(data)
    split_len = len(split)
    split_inx = 0
    data_inx = 0
    split_pos = []
    data.sort()
    split.sort()
    for i in range(split_len):
        while data[data_inx] < split[i]:
            data_inx += 1
        if i == 0:
            split_pos.append(data_inx + 1)
        else:
            split_pos.append(data_inx + 1 - split_pos[i - 1])
    split_pos[split_len - 1] -= 1
    split_pos.append(data_len - data_inx - 1)
    return split_pos
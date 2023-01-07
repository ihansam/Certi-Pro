start_empty = {}
end_empty = {}
used = {}


def init(N):
    start_empty.clear()
    end_empty.clear()
    used.clear()
    start_empty[0] = N
    end_empty[N] = 0


def get_address(size):
    min_size = 100000001
    ret = -1
    for mem_begin, mem_size in start_empty.items():
        if mem_size >= size:
            if (mem_size < min_size) or (mem_size == min_size and mem_begin < ret):
                ret = mem_begin
                min_size = mem_size
    return ret


def allocate(size):
    empty_s = get_address(size)
    if empty_s == -1:
        return -1
    # empty_s, empty_size = min(start_empty.items(), key=lambda x: (x[1], x[0]) if x[1]>=size else (100000001, 0))
    # if empty_size < size:
    #     return -1

    empty_size = start_empty[empty_s]
    empty_e = empty_s + empty_size
    remain_size = empty_size - size

    del start_empty[empty_s]
    if remain_size:
        start_empty[empty_s + size] = remain_size
        end_empty[empty_e] = empty_s + size
    else:
        del end_empty[empty_e]

    used[empty_s] = empty_s + size

    return empty_s


def deallocate(target_s):
    if target_s not in used:
        return -1

    target_e = used[target_s]
    target_size = target_e - target_s
    del used[target_s]

    if target_s in end_empty:
        _s = target_s
        target_s = end_empty[_s]
        del end_empty[_s]
    if target_e in start_empty:
        _e = target_e
        target_e = _e + start_empty[_e]
        del start_empty[_e]

    start_empty[target_s] = target_e - target_s
    end_empty[target_e] = target_s

    return target_size

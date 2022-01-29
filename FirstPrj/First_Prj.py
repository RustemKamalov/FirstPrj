def Find_Parent(_par, _child):
    k = 0
    found_param = _child
    list_tmp = []
    list_found = [_child]
    while k == 0:
        k = 1
        new_list = []
        for key, index in parent.items():
            list_tmp = index.split()
            res = [x for x in list_tmp + list_found if x in list_tmp and x in list_found]
            if res:
                if key == _par or _child == _par:
                    return "Yes"
                k = 0
                new_list.append(key)
        list_found = list(new_list)
    return "No"


n = int(input())

parent = {"global": ""}
list_check = []
list_pmp = []

for _ in range(n):
    list_pmp = input().split(":")
    if len(list_pmp) == 2:
        list_tmp = list_pmp[1].replace(" ", "", 1).split()
        for i in list_tmp:
            try:
                _str = parent[i] + " " + list_pmp[0].replace(" ", "", 1)
                parent[i] = _str
            except:
                parent[i] = list_pmp[0].replace(" ", "", 1)
    else:
        if parent["global"] == "":
            _str = list_pmp[0].replace(" ", "", 1)
        else:
            _str = parent["global"] + " " + list_pmp[0].replace(" ", "", 1)
        parent["global"] = _str

n = int(input())
for _ in range(n):
    list_check.append(input())

for ch in list_check:
    _par, _child = ch.split()
    print(Find_Parent(_par, _child))

def Create(name_space, parent):
    """
        Функция создает новое пространство имен с именем name_space внутри пространства parent
        И возвращает True при добавление и False в любом другом случае
    """
    for key, index in namespace.items():
        if key == parent:
            index.append(name_space)
            namespace[key] = index
            return True
    for key, index in namespace.items():
        for i in index:
            if i == parent:
                tmp = [name_space]
                namespace[parent] = tmp
                return True
    return False


def Add(name_space, _var):
    """
        Функция добавляет в пространство имен name_space переменную var
        И возвращает True при добавление и False в любом другом случае
    """
    # pass
    for key, index in namespace.items():
        if key == name_space:
            try:
                tmp = var[key]
                tmp.append(_var)
                var[key] = tmp
                return True
            except:
                tmp = [_var]
                var[key] = tmp
                return True

    for key, index in namespace.items():
        for i in index:
            try:
                tmp = var[name_space]
                tmp.append(_var)
                var[name_space] = tmp
                return True
            except:
                tmp = [_var]
                var[name_space] = tmp
                return True
    return False


def Get(name_space, _var):
    """
        получить имя пространства, из которого будет взята переменная <var> при запросе из пространства <namespace>,
        или None, если такого пространства не существует
    """
    for ns in Find_Parent(name_space):
        try:
            tmp = var[ns]
        except:
            tmp = []
        for i in tmp:
            if i == _var:
                 return ns

    for i in var[_global]:
        if i == _var:
            return _global
    return None

    # pass


def Find_Parent(name_space):
    list_tmp = []
    k = 0
    found_str = name_space
    found_list = []
    while k == 0:
        k = 1
        for key, index in namespace.items():
            for i in index:
                if i == found_str:
                    found_list.append(found_str)
                    found_str = key
                    k = 0
    return found_list


Count_Select = int(input())
Body_Select = []
_add = "add"
_create = "create"
_get = "get"
_global = "global"
namespace = {_global: []}
var = {_global: []}

for i in range(Count_Select):
    tmp_str = input().split()
    Body_Select.append(tmp_str)

for select in Body_Select:
    if select[0] == _add:
        Add(select[1], select[2])
    if select[0] == _create:
        Create(select[1], select[2])
    if select[0] == _get:
        print(Get(select[1], select[2]))


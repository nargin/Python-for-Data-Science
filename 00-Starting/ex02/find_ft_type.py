

def all_thing_is_obj(object: any) -> int:
    obj_type = object.__class__.__name__
    content = object
    object = type(object)
    match obj_type:
        case "str":
            print(f"{content} is in the kitchen: {object}")
        case "list":
            print("List", object)
        case "tuple":
            print("Tuple", object)
        case "set":
            print("Set", object)
        case "dict":
            print("Dict", object)
        case "NoneType":
            print("None")
        case _:
            print("Type not found")
    return 42

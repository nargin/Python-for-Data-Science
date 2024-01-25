def isnan(object: float) -> bool:
	return object != object


def NULL_not_found(object: any) -> int:
	obj_type = object.__class__.__name__
	
	if obj_type == "str" and object == "":
		print(f"Empty: {type(object)}")
	elif obj_type == "NoneType" and object == None:
		print(f"Nothing: None {type(object)}")
	elif obj_type == "float" and isnan(object):
		print(f"Cheese: nan {type(object)}")
	elif obj_type == "int" and object == 0:
		print(f"Zero: 0 {type(object)}")
	elif obj_type == "bool" and object == False:
		print(f"Fake: False {type(object)}")
	else:
		print("Type not found")
		return 1
	
	return 0
	
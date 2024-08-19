from typing import Optional, Union


def getTitlename(first_name, last_name):
    complete_name = first_name.title() + " " + last_name.title()
    return complete_name

result_set =getTitlename("ifeanyi", "chigbo")
print(result_set)


def getItems(name: str, location:str):
    complete_items = name + " " + location.title()
    return complete_items

final_set = getItems("Ifeanyi", "abuja")

print(final_set)


def dataCollections(items: list[int]):

    if len(items) > 4:
        raise "items are too large"
    else:
        getme = [ite for ite in items]
        return getme

main_items = dataCollections([1,21,1,2])
print(main_items)


def testOptional(name : Optional[str] = None):
    if name is not None:
        print("Hello {}".format(name))
    else:
        print("Name has no value")

print(testOptional("ifeanyi"))

def getItemTest(name: Optional[str] = None):
    try:
        if None:
            print("name parameter not found")
        else:
            return name
    except Exception as ex:
        print(ex)
print("I got here")
print(getItemTest("Victor"))
print("I end here")
def bringValues(name: Union[int, str]) -> None:
    return name

print(bringValues("Chigbo"))
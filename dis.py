def p(obj):
    """Print interior of the Python object

    Args:
        obj (object): dir()'able python object
    """
    print("#" * 200)
    for x in dir(obj):
        if not callable(getattr(obj, x)) and not x.startswith("_"):
            print(f"{x}: ----------- :{getattr(obj, x)}")

    print("\nCallables " + "#" * 200)

    for x in dir(obj):
        if callable(getattr(obj, x)) and not x.startswith("_"):
            try:
                print(f"{x}: ----------- :{getattr(obj, x)()}")
            except Exception as e:
                print(f"{x}: ----------- : Exception : ----------- :{e}")
    print("#" * 200 + "\n")

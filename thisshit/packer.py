class PackageConstructor:
    def __init__(self, *params) -> None:
        self.params = params

    def __call__(self, packer):
        return packer(*self.params)

class CallablePackage:
    """Callable package of functions, use {package}() without arguments"""
    def __init__(self, ls) -> None:
        self.ls = ls

    def __call__(self):
        for i in self.ls:
            i()

    def __str__(self) -> str:
        return "package of: " + " ".join(list(map(lambda x: x.__name__, self.ls)))
    __doc__="Callable package of functions, use {package}() without arguments"

class Numeric:
    """Package of int digits, returns object with specified type"""
    def __init__(self, *ls):
        number = 0
        for digit in ls[0]:
            number = number * 10 + digit
        self.number = number

    def __call__(self, typeof = int):
        """Unpacking package, returns object with specified type"""
        return typeof(self.number)
    
    def unpack(self) -> int:
        return self.__call__()
    
    def __str__(self) -> str:
        return f"Numeric ({self.number})"

class Packer:

    def __class_getitem__(self, *params) -> CallablePackage:
        return PackageConstructor(*params)

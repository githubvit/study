import settings

class MySQL:
    __instance=None
    def __init__(self,ip,port):
        self.ip=ip
        self.port=port

    @classmethod
    def singleton(cls):
        if not cls.__instance:
            obj=cls(settings.IP, settings.PORT)
            cls.__instance=obj
        return cls.__instance

obj1=MySQL('1.1.1.2',3306)
obj2=MySQL('1.1.1.3',3307)
obj3=MySQL('1.1.1.4',3308)


class MyClass:
    ''' A minimal example class

    :param value: value to set as the ``attribute`` attribute 
    :ivar attribute: contins the contents of ``value`` passed in init 
    '''
    def __init__(self, value ):
        self.attribute = value 


class Document:
    def __init__(self,text):
        self.text = text
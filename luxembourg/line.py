class Line:
    """
    Representing Line for drawing a line to the board
    """

    def __init__(self, start, end):
        if start.get_x() > end.get_x() or start.get_y() > end.get_y():
            print(str(start) + ' -> ' + str(end))
            raise RuntimeError('from position must be smaller than to position')
        self.__start = start
        self.__end   = end

    def __str__(self):
        return str(self.__start) + ' -> ' + str(self.__end)

    __repr__ = __str__

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def to_dict(self):
        return {
            start: self.__start.to_dict(),
            end:   self.__end.to_dict()
        }
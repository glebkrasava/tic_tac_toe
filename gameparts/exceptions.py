class FieldIndexError(IndexError):

    def __str__(self):
        return 'Введено значение за границами игрового поля'


class CellOccupiedError(IndexError):
    def __str__(self):
        return 'Попытка заменить занятую ячейку'

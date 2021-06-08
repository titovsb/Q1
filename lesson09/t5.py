'''
Stationary class (Канцелярия)
'''

class Stationary:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationary):
    def draw(self):
        print('Рисуем ручкой', self.title)

class Pencil(Stationary):
    def draw(self):
        print('Рисуем карандашом', self.title)

class Handle(Stationary):
    def draw(self):
        print('Рисуем маркером', self.title)

if __name__ == '__main__':

    pn = Pen('Bic')
    pl = Pencil('Сакко и Ванцетти')
    hl = Handle('Flip Chart')

    pn.draw()
    pl.draw()
    hl.draw()


'''
Рисуем ручкой Bic
Рисуем карандашом Сакко и Ванцетти
Рисуем маркером Flip Chart
'''

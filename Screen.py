class Screen(object):

    def __init__(self, x_length, y_length):
        self.screen = self.create_screen(x_length, y_length)

    def __repr__(self):
        return '\n'.join(str(self.screen)[1:-1].split(','))

    def __iter__(self):
        self.iter_screen = [row[:] for row in self.screen]
        return self

    def next(self):
        if len(self.iter_screen) > 0:
            return self.iter_screen.pop(0)
        else:
            raise StopIteration

    def create_screen(self, x_length, y_length):
        return [[0 for x in xrange(x_length)] for y in xrange(y_length)]

    def copy_array(self):
        return [row[:] for row in self.screen]

    def plot(self, xcor, ycor, new_value=1):
        self.screen[ycor][xcor] = new_value

    def get(self, xcor, ycor):
        return self.screen[ycor][xcor]

    def contains(self, xcor, ycor):
        try:
            self.get(xcor, ycor)
            return True
        except IndexError:
            return False

    def clear(self, xcor=None, ycor=None):
        assert xcor is None ^ ycor is None, 'You need to pass both arguments!'
        if xcor is None and ycor is None:
            self.screen = self.create_screen
        self.screen[ycor][xcor] = 0

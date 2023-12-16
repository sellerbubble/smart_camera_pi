from getpic import get_pic

class servo():
    def __init__(self, outputs, shape):
        self.message = get_pic(t=1)
        for value in list(outputs):
            x1, y1, x2, y2, track_id = value
        height = shape[0]
        weight = shape[1]
        middle_height = height * 0.5
        middle_weight = weight * 0.5
        middle_output_height = (y1 + y2) * 0.5
        middle_output_weight = (x1 + x2) * 0.5
        left_line = weight * 0.4
        right_line = weight * 0.6
        if middle_output_weight < left_line:
            self.turn('right')
        if middle_output_weight > right_line:
            self.turn('left')

    def turn(self, action):
        if action == 'right':
            print('1')
            self.message.footage_socket.send_string(action)
        if action == 'left':
            print(2)
            self.message.footage_socket.send_string(action)

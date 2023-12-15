import cv2
import zmq
import base64
import numpy as np


class get_pic():
    def __init__(self):

        self.footage_socket = None
        self.open_tcp()
        self.window = 0



    def open_tcp(self):
        context = zmq.Context()
        self.footage_socket = context.socket(zmq.PAIR)
        self.footage_socket.bind('tcp://*:5000')

    def show_window(self):
        if self.window == 0:
            cv2.namedWindow('Stream2', flags=cv2.WINDOW_NORMAL | cv2.WINDOW_KEEPRATIO)
            self.window = 1

    def get_pic(self):
        frame = self.footage_socket.recv()  # 接收TCP传输过来的一帧视频图像数据
        img = base64.b64decode(frame)  # 把数据进行base64解码后储存到内存img变量中
        npimg = np.frombuffer(img, dtype=np.uint8)  # 把这段缓存解码成一维数组
        self.source = cv2.imdecode(npimg, 1)  # 将一维数组解码为图像source

    def show_pic(self):
        if self.source is not None:
            cv2.imshow("Stream2", self.source)  # 把图像显示在窗口中
            cv2.waitKey(5)
    def send_str(self,action):
        self.footage_socket.send_string(action)

if __name__ == '__main__':
    '''
    程序入口
    '''
    pic = get_pic()
    pic.show_window()
    while True:
        pic.get_pic()
        st = pic.footage_socket.recv_string()


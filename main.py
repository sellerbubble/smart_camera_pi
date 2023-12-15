from AIDetector_pytorch import Detector
import imutils
import cv2
from getpic import get_pic

def main():
    func_status = {}
    func_status['headpose'] = None

    name = 'demo'

    det = Detector()
    # cap = cv2.VideoCapture('C:\\Users\\23686\\Desktop\\yolov5old\\Yolov5-deepsort-inference\\test5.mp4')
    # fps = int(cap.get(5))
    # print('fps:', fps)
    # t = int(1000 / fps)

    # size = None
    # videoWriter = None
    pic = get_pic()

    k = 0
    while True:
        k += 1

        pic.get_pic()
        print(1)
        result = pic.source

        # try:
        # _, im = cap.read()
        if k % 10 != 0:
            continue

        if result is None:
            break

        result = det.feedCap(result, func_status)
        result = result['frame']
        result = imutils.resize(result, height=500)
        # if videoWriter is None:
        #     fourcc = cv2.VideoWriter_fourcc(
        #         'm', 'p', '4', 'v')  # opencv3.0
        #     videoWriter = cv2.VideoWriter(
        #         'result.mp4', fourcc, fps, (result.shape[1], result.shape[0]))
        #
        # videoWriter.write(result)
        cv2.imshow(name, result)
        cv2.waitKey(5)
        pic.send_str('1')
        # if cv2.getWindowProperty(name, cv2.WND_PROP_AUTOSIZE) < 1:
        #     点x退出
            # break
        # except Exception as e:
        #     print(e)
        #     break

    # cap.release()
    # videoWriter.release()
    # cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
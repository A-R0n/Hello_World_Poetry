import cv2
import time

def main():
    Main()

class Main:

    def __init__(self):
        self.cam = cv2.VideoCapture(0)
        self._main()

    def _space_key_pressed(self) -> bool:
        if self.k%256 == 32:
            return True
        return False
    
    def _esc_key_pressed(self) -> bool:
        if self.k%256 == 27:
            return True
        return False
    
    def _capture_img(self):
        cv2.imwrite(self.img_name, self.frame)

    def _pause_video(self):
        cv2.waitKey(-1)

    def _get_epoch_nano(self):
        return time.time_ns()

    def _main(self):
        cv2.namedWindow("test")
        while True:
            self.ret, self.frame = self.cam.read()
            if not self.ret:
                print("failed to grab frame")
                break
            cv2.imshow("test", self.frame)
            self.k = cv2.waitKey(1)
            if self._esc_key_pressed():
                break
            elif self._space_key_pressed():
                self.epoch_nano = self._get_epoch_nano()
                self.img_name = f'{self.epoch_nano}.jpg'
                self._capture_img()
                self._pause_video()

        self.cam.release()

        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
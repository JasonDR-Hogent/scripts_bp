import cv2
import os

class video_processor:
    def __init__(self, frame_skip, video_path):
        self.frame_skip = frame_skip
        self.video_path = video_path
        self.frame_total = 0
      
    def load_video(self):
        try:
            if os.path.exists(self.video_path):
                print(os.path.exists(self.video_path))
                return cv2.VideoCapture(self.video_path)
            raise Exception("Video not found")
        except Exception as e:
            print(e)
    
    def crop_and_save_image(self, image):
        #Voederbak VDO3
#        x=250
#        w= x + 250
#        y=325
#        h= y + 250
        # Voederbak LO VDO4
        x=350
        w=x + 250
        y= 80
        h= y + 250
        crop_image = image[x:w, y:h]
        path_out = f'../data/cropped_img/{self.video_path.replace(".mp4", "").replace("../video/","")}_{self.frame_total}.png'
        print("Writing data to ", path_out)
        cv2.imwrite(f'../data/cropped_img/{self.video_path.replace(".mp4", "").replace("../video/","")}_{self.frame_total}.png', crop_image)
    
    def workflow(self):
        video = self.load_video()
        while True:
            ret, frame=video.read()
            self.frame_total += 1
            if self.frame_total % self.frame_skip == 0:
                self.crop_and_save_image(frame)
            if not ret:
               print("End of video")
               break
        video.release()
        cv2.destroyAllWindows()
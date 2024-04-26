import time
class side_bicep_curl(object):
    def __init__(self):
        self.xShoulder = -1
        self.yShoulder = -1
        self.xElbow = -1
        self.yElbow = -1
        self.xWrist = -1
        self.yWrist = -1
        self.startPoint = None
        self.startPoint2 = None
        self.finalPoint = None
        self.progress = 0
        self.rep = 0
        self.counted = False
        self.last_keypoint_time = {
            "shoulder": time.time(),
            "wrist": time.time(),
            "elbow": time.time()
        }
        self.display_colors = ""
    def sbc(self,display_colors,midpointX,midpointY):
        current_time = time.time()
        self.display_colors = display_colors
        print(self.display_colors)
        if self.display_colors == "#32ba19":
            self.last_keypoint_time["shoulder"] = time.time()

        if self.display_colors == "#000c7c":
            self.last_keypoint_time["wrist"] = time.time()

        if self.display_colors == "#005fa3":
            self.last_keypoint_time["elbow"] = time.time()

        if current_time - self.last_keypoint_time["shoulder"] > 5  or current_time - self.last_keypoint_time["wrist"] > 5 or current_time - self.last_keypoint_time["elbow"] > 5:
            raise Exception

        if self.display_colors == "#32ba19":
            self.xShoulder,self.yShoulder = midpointX,midpointY
        #     # print( self.xShoulder, self.yShoulder,"**SHOULDER**")
        if self.display_colors == "#005fa3":
            self.xElbow, self.yElbow = midpointX,midpointY
        #     # print( self.xElbow, self.yElbow,"**ELBOW**")
        if self.display_colors == "#000c7c":
            self.xWrist, self.yWrist = midpointX,midpointY
        #     # print( self.xWrist, self.yWrist,"**Wrist**")                                      

        if abs( self.xShoulder -  self.xElbow)>8:
            print("Shoulder and elbow not aligned")
        # print(self.xShoulder-self.xWrist)
        self.finalPoint = self.yShoulder+47
        ## Start position
        if not self.startPoint:
            print("SHOULDER WRIST AND ELBOW ARE ALIGNED")
            if 40.0 <= abs(self.xShoulder - self.xWrist) <= 60.0:
                self.startPoint = self.yWrist
                
        print( "93","PROGRESSSSSSSSSS",self.finalPoint,self.startPoint,self.yWrist)

        self.progress = ( (self.startPoint-self.yWrist)/(self.startPoint-self.finalPoint))*100
                                    
        print(self.counted)
        if self.startPoint and not self.counted:
            if self.progress>95:
                self.counted = True 
        if self.progress <5 and self.counted:
            self.rep = self.rep +1
            self.counted = False
                                    
        print(self.rep)

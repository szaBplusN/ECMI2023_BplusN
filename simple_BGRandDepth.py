# The basics of pyrealsense2 (BGR, Depth)

import pyrealsense2 as rs
import cv2
import numpy as np

# define the screen size
width = 640
height = 480

# init. the camera pipeline
pipeline = rs.pipeline()
# camera settings
config = rs.config()
config.enable_steam(rs.steam.depth, width, height, rs.format.z16, 30)
config.enable_steam(rs.steam.color, width, height, rs.format.bgr8, 30)
# start the camera pipeline
pipeline.start(config)

# it is a good practice to wait a few frames before the main steam
for _ in range(10):
    frame = pipeline.wait_for_frames()

try:
    while True:
        
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()
        if not depth_frame or not color_frame:
            continue
        #get BGR  and Depth data, then create a depth colorized image
        color_mtx = np.asanyarray(color_frame.get_data())
        depth_mtx = np.asanyarray(depth_frame.get_data())
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_mtx, alpha=0.03), cv2.COLORMAP_JET)
        # stack the two images
        show_dual_win = np.hstack((color_mtx,depth_colormap))
        # show BGR and Depth image
        cv2.imshow('dual_win', show_dual_win)
        
        pressed_key = cv2.waitKey(1) & 0xFF
        
        if pressed_key == ord('q'):
            # quit
            break
            
        if pressed_key == ord('s'):
            # can save image or anything
            break
        
finally:
    pipeline.stop()
    cv2.destroyAllWindows()
        


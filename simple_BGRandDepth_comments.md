### Comment 1:

We can show mutiple windows at the same time:

        #stack the two images
        show_dual_win = np.hstack((color_mtx,depth_colormap))
        #show BGR and Depth image
        cv2.imshow('dual_win', show_dual_win)

replace it:

        cv2.imshow('BGR_win',color_mtx)
        cv2.imshow('DPT_win',depth_colormap)

### Comment 2:

The depth data has a scale factor, it can be get by:

        depth_sensor = profile.get_device().first_depth_sensor()
        depth_scale = depth_sensor.get_depth_scale()

### Comment 3:

To align the depth image with the color image:

        align_to = rs.steam.color
        align = rs.align(align_to)
        
        #then in the while loop:
        frames = pipeline.wait_for_frames()
        aligned_frames = align.process(frames)
        
then the aligned frame can be used as any other frame.

### Comment 4:

To rotate an image/matrix:

        color_mtx_T = np.rot90(color_mtx, 3)

### Comment 5:

To manipulate a numpy/MAT(in cv2) object and keep the original, you need to copy it.

        color_copy = color_mtx.copy()


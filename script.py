# Edge Impulse - OpenMV Object Detection Example

import sensor, image, time, os, tf, math, uos, gc, utime

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.

net = None
labels = None
min_confidence = 0.5

try:
    # load the model, alloc the model file on the heap if we have at least 64K free after loading
    net = tf.load("trained.tflite", load_to_fb=uos.stat('trained.tflite')[6] > (gc.mem_free() - (64*1024)))
except Exception as e:
    raise Exception('Failed to load "trained.tflite", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')

try:
    labels = [line.rstrip('\n') for line in open("labels.txt")]
except Exception as e:
    raise Exception('Failed to load "labels.txt", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')

colors = [ # Add more colors if you are detecting more than 7 types of classes at once.
    (255,   0,   0),
    (  0, 255,   0),
    (255, 255,   0),
    (  0,   0, 255),
    (255,   0, 255),
    (  0, 255, 255),
    (255, 255, 255),
]

filename = "./detections.csv"
print(line for line in open(filename))
with open(filename, "w") as f:
    f.write("timestamp, amt_detections, frequency\n")
clock = time.clock()
while(True):
    clock.tick()
    local_time = utime.localtime(utime.time())
    current_minute = local_time[4]
    dict_res = {}
    while current_minute + 1 != utime.localtime(utime.time())[4]:
            img = sensor.snapshot()

            for i, detection_list in enumerate(net.detect(img, thresholds=[(math.ceil(min_confidence * 255), 255)])):
                if (i != 1): continue # background class

                amt_detect = len(detection_list)
                if amt_detect not in dict_res.keys():
                    dict_res[amt_detect] = 1
                else:
                    dict_res[amt_detect] += 1


    # Write away data
    with open(filename, "a") as f:
        timestamp =  "{:02d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}".format(local_time[0], local_time[1], local_time[2], local_time[3], local_time[4], local_time[5])
        for key in dict_res.keys():
            f.write(f"{timestamp}, {key}, {dict_res[key]}\n")
        print(dict_res)
        print([line for line in open(filename)])
    print(clock.fps(), "fps", end="\n\n")

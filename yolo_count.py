# # # # from ultralytics import YOLO
# # # # import cv2

# # # # model = YOLO("yolov8n.pt")      

# # # # def count_people(image_path):
# # # #     results = model(image_path)
# # # #     count = 0
# # # #     for box in results[0].boxes:
# # # #         if int(box.cls[0]) == 0:   # class 0 = person
# # # #             count += 1
# # # #     return count


# # # # from ultralytics import YOLO
# # # # import cv2

# # # # # Load YOLO model
# # # # model = YOLO("yolov8n.pt")  # You can replace with your custom model

# # # # def count_people(image_path, return_boxes=False):
# # # #     results = model(image_path)
# # # #     count = 0
# # # #     detections = []

# # # #     # Loop through YOLO results and count only 'person' class
# # # #     for box in results[0].boxes:
# # # #         cls = int(box.cls[0])
# # # #         if cls == 0:  # class 0 = person
# # # #             count += 1
# # # #             # Get bounding box coordinates
# # # #             x1, y1, x2, y2 = map(int, box.xyxy[0])
# # # #             detections.append((x1, y1, x2, y2))

# # # #     # Return both the count and bounding boxes if requested
# # # #     if return_boxes:
# # # #         return count, detections
# # # #     return count



# # # from ultralytics import YOLO

# # # model = YOLO("yolov8n.pt")  # YOU CAN CHANGE MODEL

# # # def count_people(image_path, return_boxes=False):
# # #     results = model(image_path)

# # #     count = 0
# # #     detections = []

# # #     for r in results:
# # #         for box in r.boxes:
# # #             cls = int(box.cls[0])
# # #             if cls == 0:     # PERSON CLASS
# # #                 count += 1
# # #                 x1, y1, x2, y2 = map(int, box.xyxy[0])
# # #                 detections.append((x1, y1, x2, y2))

# # #     if return_boxes:
# # #         return count, detections
# # #     return count

# # from ultralytics import YOLO

# # model = YOLO("yolov8n.pt")

# # def count_people(image_path):
# #     results = model(image_path)
# #     count = 0

# #     for r in results:
# #         for box in r.boxes:
# #             if int(box.cls[0]) == 0:   # class 0 = person
# #                 count += 1

# #     return count

# from ultralytics import YOLO
# import numpy as np

# model = YOLO("yolov8n.pt")

# def count_people(image_path):
#     results = model(image_path)
#     person_scores = []

#     for result in results:
#         for box in result.boxes:
#             if int(box.cls[0]) == 0:  # class 0 = person
#                 person_scores.append(float(box.conf[0]))

#     count = len(person_scores)
#     avg_conf = np.mean(person_scores) * 100 if count > 0 else 0

#     return count, round(avg_conf, 2)


# from ultralytics import YOLO
# import numpy as np

# model = YOLO("yolov8n.pt")

# def count_people(image_path):
#     results = model(image_path)
#     person_scores = []

#     for result in results:
#         for box in result.boxes:
#             if int(box.cls[0]) == 0:  # class 0 = person
#                 person_scores.append(float(box.conf[0]))

#     count = len(person_scores)
#     avg_conf = np.mean(person_scores) * 100 if count > 0 else 0

#     return count, round(avg_conf, 2)




from ultralytics import YOLO
import numpy as np

model = YOLO("yolov8n.pt")  # Load lightweight YOLO model

def count_people(image_path):
    results = model(image_path)
    person_scores = []

    for result in results:
        for box in result.boxes:
            if int(box.cls[0]) == 0:  # class 0 = person
                person_scores.append(float(box.conf[0]))

    count = len(person_scores)
    avg_conf = np.mean(person_scores) * 100 if count > 0 else 0

    return count, round(avg_conf, 2)

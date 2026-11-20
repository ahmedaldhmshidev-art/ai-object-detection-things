import cv2
import os

# تحميل الصورة
img_path = 'img/img4.jpg'
img = cv2.imread(img_path)

# التحقق من تحميل الصورة
if img is None:
    print(f"[خطأ] لم يتم العثور على الصورة في المسار: {img_path}")
    exit()

# تحميل أسماء الكائنات
classnames = []
classfile = 'pages/nameThengs.names'

if not os.path.exists(classfile):
    print(f"[خطأ] ملف الأسماء غير موجود: {classfile}")
    exit()

with open(classfile, 'rt') as f:
    classnames = f.read().rstrip('\n').split('\n')

# تحميل ملفات النموذج
model_path = 'pages/frozen_inference_graph.pb'
config_path = 'pages/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'

if not os.path.exists(model_path) or not os.path.exists(config_path):
    print(f"[خطأ] تأكد من وجود ملفات النموذج:\n- {model_path}\n- {config_path}")
    exit()

# تحميل النموذج
net = cv2.dnn.DetectionModel(model_path, config_path)
net.setInputSize(320, 230)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# الكشف عن الكائنات
classIds, confs, bbox = net.detect(img, confThreshold=0.5)

# رسم النتائج على الصورة
for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
    cv2.rectangle(img, box, color=(0, 255, 0), thickness=3)
    label = f"{classnames[classId - 1]}: {round(confidence * 100, 2)}%"
    cv2.putText(img, label, (box[0] + 10, box[1] + 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

# عرض الصورة
cv2.imshow("الكشف عن الكائنات", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

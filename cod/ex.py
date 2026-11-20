import cv2


# تحميل الصورة
img_path = 'img/img4.jpg'
img = cv2.imread(img_path)


# التحقق من تحميل الصورة
if img is None:
    print(f"[خطأ] لم يتم العثور على الصورة في المسار: {img_path}")
    exit()

# عرض الصورة
cv2.imshow("الكشف عن الكائنات", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


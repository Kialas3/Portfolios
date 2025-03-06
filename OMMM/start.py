import cv2
import numpy as np
from mss import mss
from ultralytics import YOLO
import pyautogui
import time

model = YOLO("./runs/detect/train16/weights/best.pt")

left = 420
top = 175

# 設定擷取範圍 (x, y, width, height)
# capture_region = (left, top, 2560-left*2, 1240) # for 2K monitor
capture_region = (left, top, 1920-left*2, 1080) # for 1080p monitor
timer = time.time()
waiting = True
try:
    print("按下 'q' 鍵結束程式。")
    while True:
        # 截取當前螢幕畫面
        screenshot = pyautogui.screenshot(region=capture_region)

        # 將 PIL 圖片轉換為 NumPy 陣列 (RGB 格式)
        screenshot_np = np.array(screenshot)

        # 將圖片從 RGB 轉換為 BGR 格式 (OpenCV 預設使用 BGR)
        screenshot = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)

        # 進行物件偵測
        results = model.predict(
            source=screenshot,
            stream=True,
            imgsz=1088
        )
    
        for r in results:
            boxes = r.boxes
            
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(screenshot, (x1, y1), (x2, y2), (0, 0, 255), 5)
                
                target_position = (left+(x1 + x2) // 2, top+(y1 + y2) // 2)
                
                # if time.time() - timer > 0.1:
                pyautogui.moveTo(target_position, duration=1)
                pyautogui.click()
                waiting = True
                timer = time.time()
                # elif pyautogui.position() != (left, top) and waiting:
                #     pyautogui.moveTo((left, top), duration=0.05)
                #     waiting = False
                
            if boxes.shape[0] == 0 and time.time() - timer > 1:
                print("找不到目標，重新尋找")
                pyautogui.click()
                timer = time.time()
            
        
        resized_screenshot = cv2.resize(screenshot, (1000, 632))
        
        
        # 顯示螢幕畫面
        cv2.imshow("Live Screen", resized_screenshot)

        # 每幀延遲 30 毫秒 (約 33 FPS)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("結束顯示")
            break

except KeyboardInterrupt:
    print("程式中止")

# 釋放資源並關閉視窗
cv2.destroyAllWindows()

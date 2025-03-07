# [鷗麥麥麥](https://www.youtube.com/@Omaimaimaii)

## 鷗麥麥麥，暱稱 Maii，是台灣 YouTuber[放火](https://www.youtube.com/@fanghuo)旗下的 VTuber，形象由台灣繪師米豆綠繪製。在首次直播前，其 YouTube 頻道即已突破 10 萬訂閱 。（來源：[維基百科](https://zh.wikipedia.org/zh-tw/%E9%B7%97%E9%BA%A5%E9%BA%A5%E9%BA%A5)）

---

### 在歐麥麥麥的[官網](https://vtuber-maii.com/)中有一款考驗眼力、反應力與運氣的小遊戲 - **[看誰最會射靶拔](https://games.vtuber-maii.com/)**

透過使用 yolo 模型，針對需要射擊的目標進行偵測，找出其位置，並結合 pyautogui 自動控制滑鼠移動到該位置進行射擊。

### 影片展示

[![Demo](https://img.youtube.com/vi/vA1YSSmWciQ/0.jpg)](https://www.youtube.com/watch?v=vA1YSSmWciQ)

---

### 前置作業

1. Python 3.6+
2. 安裝 [Ultralytics](https://docs.ultralytics.com/zh/quickstart/)：包含 PyTorch
3. 下載 [YOLOv8](https://docs.ultralytics.com/zh/models/yolov8/#supported-tasks-and-modes)：我是使用 yolov8m
4. 透過 Roboflow 製作訓練資料集：[Roboflow](https://roboflow.com/)
5. 可以下載我已經訓練好的模型（在[run.zip](https://drive.google.com/file/d/10in37MpOKWeJqSwGYlRvP43Q0TKJBRLp/view?usp=drive_link)）

---

### 程式碼

1. 訓練 yolo 模型並測試能否使用：[train and test.ipynb](train%20and%20test.ipynb)
2. 開始射擊：[start.py](start.py)

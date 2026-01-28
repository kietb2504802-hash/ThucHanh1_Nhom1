 import pygame
import time
import os
import random

# Danh sách mã màu để làm hiệu ứng nháy chữ
COLORS = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
RESET = '\033[0m'

# Lyrics: (Số giây, "Lời bài hát")
# Bạn có thể chỉnh lại số giây cho khớp hoàn toàn với bản nhạc bạn có
LYRICS = [
    (1.0, "--- No Love No Life - HIEUTHUHAI ---"),
    (5.0, "Đang khởi động giai điệu..."),
    (10.0, "Check... Check..."),
    (15.0, "Ta đã đi cùng nhau một đoạn đường dài..."),
    (19.0, "Em nói em muốn dừng lại..."),
    (23.0, "No love, no life... baby i'm alright"),
    (27.0, "Những ký ức giờ đây chỉ còn là quá khứ"),
    (31.0, "Anh vẫn bước tiếp, không cần sự tha thứ..."),
    (35.0, "Và anh biết... cuộc sống vẫn cứ trôi..."),
    (40.0, "HIEUTHUHAI in the building!")
]

def play_pro():
    file_path = "nolove_nolife.mp3"
    
    if not os.path.exists(file_path):
        print(f"Lỗi: Không tìm thấy file '{file_path}'!")
        return

    # Khởi tạo âm thanh
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    
    # Hẹn giờ
    try:
        time_input = input("Nhập số phút muốn nghe (nhấn Enter để nghe hết bài): ")
        timer_seconds = float(time_input) * 60 if time_input.strip() else None
    except:
        timer_seconds = None

    print("\n" + "="*40)
    print("   BẮT ĐẦU PHÁT NHẠC CÓ LYRICS & MÀU SẮC")
    print("="*40 + "\n")
    
    pygame.mixer.music.play()
    start_time = time.time()
    lyric_idx = 0

    try:
        while pygame.mixer.music.get_busy():
            elapsed = time.time() - start_time
            
            # Kiểm tra hẹn giờ
            if timer_seconds and elapsed > timer_seconds:
                print(f"\n{COLORS[0]}--- Đã hết thời gian hẹn giờ! Dừng nhạc. ---{RESET}")
                break

            # Hiển thị lyrics với màu ngẫu nhiên
            if lyric_idx < len(LYRICS) and elapsed >= LYRICS[lyric_idx][0]:
                color = random.choice(COLORS)
                print(f"{color} >> {LYRICS[lyric_idx][1]} {RESET}")
                lyric_idx += 1
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print(f"\n{COLORS[0]}Đã dừng chương trình.{RESET}")
    finally:
        pygame.mixer.music.stop()

if __name__ == "__main__":
    play_pro()

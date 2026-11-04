import json
import re

with open('data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Tách phần export const examData = ...
prefix = 'export const examData = '
if content.startswith(prefix):
    json_str = content[len(prefix):].strip()
    if json_str.endswith(';'):
        json_str = json_str[:-1]
    
    data = json.loads(json_str)
    
    # Câu 1
    q1 = data[0]
    q1['question'] = 'Có 100 học sinh tham dự kì thi Olympic Toán - tiếng Anh (thang điểm 20). Kết quả điểm của 100 học sinh trên được ghi lại ở bảng sau:<br><br>Tìm mốt của mẫu số liệu trên.'
    q1['image'] = 'cau_1.png'
    
    # Ghi lại
    with open('data.js', 'w', encoding='utf-8') as f:
        f.write(prefix + json.dumps(data, ensure_ascii=False, indent=2) + ';\n')
    print('Updated data.js')
else:
    print('Format error')

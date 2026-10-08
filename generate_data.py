import json

answers = [
    1, 2, 1, 1, 2, 1, 3, 1, 0, 0,
    0, 1, 2, 1, 3, 2, 0, 2, 3, 0,
    2, 2, 1, 0, 2, 3, 2, 3, 1, 2,
    2, 2, 2, 0, 0,
    '3,46', '101', '0,75', '1', '0,5',
    '5', '3,83', '3003', '2', '1,5',
    '0,167', '144', '2', '7/9', '203'
]

questions = []
for i in range(50):
    q_id = f'q{i+1}'
    q_type = 'mcq' if i < 35 else 'fill'
    
    question_text = '[BẠN HÃY NHẬP NỘI DUNG CÂU HỎI VÀO ĐÂY]'
    options = ['[A]', '[B]', '[C]', '[D]']
    image = None
    
    if i == 0:
        question_text = 'Có 100 học sinh tham dự kì thi Olympic Toán - tiếng Anh (thang điểm 20). Kết quả điểm của 100 học sinh trên được ghi lại ở bảng sau: Tìm mốt của mẫu số liệu trên.'
        options = ['14.', '15.', '16.', '23.']
        image = 'cau_1.png'
    elif i == 4:
        question_text = 'Xác định chiều cao của một tháp mà không cần lên đỉnh của tháp. Đặt kế giác thẳng đứng cách chân tháp một khoảng  = 60 \\\\text{ m}$, giả sử chiều cao của giác kế là  = 1 \\\\text{ m}$. Quay thanh giác kế sao cho khi ngắm theo thanh ta nhìn thấy đỉnh $ của tháp. Đọc trên giác kế số đo của góc $\\\\widehat{AOB} = 60^\\\\circ$. Chiều cao của ngọn tháp gần nhất với giá trị nào sau đây?'
        options = [' \\\\text{ m}$.', ' \\\\text{ m}$.', ',9 \\\\text{ m}$.', ' \\\\text{ m}$.']
        image = 'cau_5.png'
    elif i == 13:
        question_text = 'Một trụ điện cao thế cao  \\\\text{ m}$ được dựng thẳng đứng trên một sườn dốc ^\\\\circ$ so với phương nằm ngang. Từ đỉnh trụ điện người ta neo một sợi dây điện xuống một điểm trên sườn dốc để sửa chữa, điểm này cách chân tháp  \\\\text{ m}$ như hình vẽ dưới đây. Tính chiều dài của sợi dây điện đó (đơn vị: $; làm tròn đến hàng phần mười).'
        options = [',2 \\\\text{ m}$.', ',9 \\\\text{ m}$.', ',1 \\\\text{ m}$.', ',7 \\\\text{ m}$.']
        image = 'cau_14.png'
    elif i == 22:
        question_text = 'Để đo chiều cao của một ngọn núi người ta đứng ở các vị trí , B$ cách nhau  \\\\text{ m}$ (như hình vẽ) và đo được các góc tại $ và $ lần lượt là ^\\\\circ$ và ^\\\\circ$. Tính chiều cao của ngọn núi (làm tròn đến chữ số thập phân thứ nhất).'
        options = [',7 \\\\text{ m}$.', ',7 \\\\text{ m}$.', ',7 \\\\text{ m}$.', ',7 \\\\text{ m}$.']
        image = 'cau_23.png'
    elif i == 48:
        question_text = 'Một ứng dụng trên điện thoại thực hiện khảo sát ý kiến người dùng về tính năng mới cập nhật. Kết quả được ghi như bảng sau: Cần chọn ngẫu nhiên một ý kiến người dùng để làm báo cáo. Xác suất để ý kiến đó đến từ người dùng nam, biết rằng đó là ý kiến hài lòng bằng bao nhiêu? (Kết quả viết dưới dạng phân số tối giản)'
        image = 'cau_49.png'
        
    ans_text = str(answers[i])
    if q_type == 'mcq':
        ans_text = ['A', 'B', 'C', 'D'][answers[i]]

    q_obj = {
        'id': q_id,
        'type': q_type,
        'question': question_text,
        'correctAnswer': answers[i],
        'explanation': f'Đáp án đúng là: {ans_text}',
        'image': image
    }
    if q_type == 'mcq':
        q_obj['options'] = options
        
    questions.append(q_obj)

with open('C:\\\\Users\\\\DELL\\\\Documents\\\\CODE\\\\WEB\\\\DU_AN\\\\de-7-hsa-dinh-luong-vnes\\\\data.js', 'w', encoding='utf-8') as f:
    f.write('export const examData = ' + json.dumps(questions, ensure_ascii=False, indent=2) + ';\n')


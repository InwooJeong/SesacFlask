# step1 모듈 가져오기
from flask import Flask

# step2 플라스크 객체 생성
app = Flask(__name__)

# step3 특정 주소 요청 -> 해석 -> 서버가 응답 => 라우팅
@app.route('/')
def home():
    return 'hello flask 1'

# step4 서버 가동
if __name__ == '__main__':  # 직접 실행한다면
    # debug = True : 수정 -> 저장 -> 자동 리로드
    app.run(debug=True)
# flask란
    - 파이썬 기반 웹 서비스를 구현하는 패키지
        - 분석 기반 서비스, AI기반 서비스 등등
            - 차트가 동반, 데이터 표현 등
            - 분석 파이썬 + 서비스(웹) 파이썬 => 동일 언어
    - 종류
        - Django
            - 프레임워크 기반, 대부분 프로젝트 구조가 자동 생성
            - 상대적으로 느림
            - 개발을 빠르게 구축 -> 국내에서 선호, 추세는 변경 중
            - 스타일이 자바 진영 spring과 유사
        - flask
            - 자유도가 높다. 처음부터 모든 것을 직접 만든다.
            - 가볍고, 빠르게 구축 가능
            - 미국에서 선호
            - ex) 주피터 노트북
            - 스타일이 JS진영 node.js와 유사
        - fastAPI
            - 모델 서빙 등 추세를 넓혀가는 중
            - 가장 빠름

# 설치
    - 가상환경 구축
         - 하나의 머신에서 여러개 프로젝트, 서비스 가동 시 특정 패키지들 버전 충돌 방지 -> 격리, 샌드박스
         - 가상환경 생성(현재 프로젝트 위치에서 수행)
            - python -m venv was
         - 활성화
            - 윈도우 기준 활성화 파일 위치
                - ~/was/Scripts/activate.bat
                - (was) 프럼프트(경로) > 
                    - (was)> pip list
        - 필요한 패키지 설치
            - 명령어로 생성(코랩에서 진행)
                - pip freeze > requirements.txt
                - 이미 깔려있는 것들 다 기록됨
                - 필요한 것 만 카피해서 로컬 requirements.txt 수정
            - (was)> pip install -r requirements.txt
                - txt 경로는 상황에 맞춰 조정
            - (was) > pip list

# 최초코드
    - f1.py 참고
    - template.py 파일을 기본형으로 사용

# 웹 서비스
    - FE(Client)
        - html5 : 콘텐츠 담당, 뼈대 => 데이터 존재
            - 데이터
            - 요소(엘리먼트) 이해
            - 구조, 속성(id, class), 입력태그(input, textarea, ...)
        - css3 : 레이아웃, 디자인, 애니메이션(키프레임), 반응형
            - css selector, xpath -> 요소를 특정하는 방법
            - bootstrap등 이미 완성된 디자인 모듈 활용
                - adminlte.io
        - js : 인터렉션, 이벤트, 통신, 동적구성
            - javascript > es next > type script
                - react, angular, vue => SPA(Single Page Application)
            - 클라이언트 - 서버로 데이터 보내는 방법
                - form 전송 -> 로그인 등 화면 깜빡임
                - ajax 통신 -> 백그라운드 통신
                - 웹소켓 -> 백그라운드 통신, 쌍방향통신, 푸시 -> 챗봇 베이스
            - 개발 생산성을 높이기 위해 라이브러리 사용 => jQuery, ...
    - BE(Server)
        - flask
            - 같은 포지션, Django, Fastapi, Springboot, node.js, .net, php, ...
    - DB
        - RDBMS
            - Mysql, MSSQL, Maria, Oracle, Aurora, PostgreSQL ...
        - No SQL
            - MongoDB, redis, ...

# 프로젝트 구조
    /
    L basic     :flask를 익히기 위한 예제
        L f1.py
        L f2.py
        L template.py
    L app.py     : 서비스 엔트리 포인트
    L static    : 정적 데이터가 위치하는 곳, 라우팅 필요 없음 
                : *.js, *.css, *.이미지파일(png,...)
    L templates : html 위치
        L index.html
    L requirements.txt : 해당 프로젝트에서 사용하는 라이브러리
    L readme.MD : 설명 파일
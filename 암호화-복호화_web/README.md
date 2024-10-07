# Encryptor Project

## 프로젝트 개요
이 프로젝트는 Django를 사용하여 단어를 암호화하고 복호화하는 웹 애플리케이션입니다. 사용자가 단어와 키를 입력하면 암호화된 결과를 출력하고, 암호화된 단어와 키를 입력하면 원래 단어를 복원할 수 있습니다.

## 기능
- **암호화**: 사용자가 입력한 단어를 키 값만큼 이동시켜 암호화된 단어를 생성합니다.
- **복호화**: 암호화된 단어와 키 값을 입력하면 원래 단어로 복원합니다.

## 기술 스택
- **프레임워크**: Django
- **언어**: Python, HTML

## 프로젝트 구조
encryptor_project/ ├── encryptor_project/ │ ├── init.py │ ├── settings.py │ ├── urls.py │ └── wsgi.py ├── encryption_app/ │ ├── migrations/ │ ├── init.py │ ├── admin.py │ ├── apps.py │ ├── models.py │ ├── urls.py │ ├── views.py │ └── templates/ │ └── encryption_app/ │ ├── index.html │ ├── encrypt.html │ ├── decrypt.html │ └── result.html └── manage.py

---

## 설치 및 실행 방법
1. 프로젝트 클론

   ```bash
   git clone https://github.com/your-username/encryptor_project.git
   cd encryptor_project
   ```

2. 가상 환경 생성 및 활성화

  ```python
  python -m venv venv
  source venv/bin/activate  # Windows에서는 venv\Scripts\activate
  ```
3. 패키지 설치

  ```python
  pip install -r requirements.txt
  ```
4. 마이그레이션 적용 및 서버 실행

  ```python
  python manage.py migrate
  python manage.py runserver
  ```

---
- 홈페이지: 암호화 및 복호화 기능을 선택할 수 있습니다.
- 암호화: 단어와 키를 입력하여 암호화된 결과를 확인할 수 있습니다.
- 복호화: 암호화된 단어와 키를 입력하여 원래 단어를 복원할 수 있습니다.

---
### 진행 과정

10/7
- 프로젝트,암호화 앱, 계정 앱 생성 / 커스텀 유저 클래스 작성.등록 완
- 앱 url 생성
- encryption_app MTV생성
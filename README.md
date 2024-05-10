## 실버링크
서울열린데이터광장 공공데이터활용 창업경진대회에 참가한 OldJeans 팀의 샘플 DB, 모델 구현 Github입니다. 

### 💻 프로젝트 소개
55세 이상 시니어의 온라인 구직 과정 보조를 위한 서비스입니다. 

### 📌 주요 기능 
(1) 산재된 일자리 정보의 통합 제공
- 공공데이터 API, 크롤링을 활용해 여러 공공/민간 사이트에 산재된 구인 정보 및 직업 교육 정보를 통합해 제공합니다.
   
(2) 이력서/자기소개서 작성 보조
- STT 기술과 생성형 AI 기술을 통합해 사용자의 음성 입력으로 형식에 맞는 이력서/자기소개서 항목 답변 작성을 보조합니다.
  
(3) 적합한 공고 추천
- 사용자가 입력한 성별/연령/거주지역/희망업종 정보와 통합 DB의 구인 공고 정보를 조합해 적합한 구인 공고를 자동 필터링, 추천합니다. 

### ✅ 자기소개서/이력서 작성 보조 모델 실행 가이드

#### Requirements

(1) required_keys에 API Key, Pwd 입력
- 본 프로젝트는 STT, 생성형 AI 기술 활용을 위해 아래와 같은 사이트에서 Open API를 사용하고 있습니다. 분당 요청 수 제한이 있으나 2024.05.10 기준 무료로 사용 가능합니다. 
  - ReturnZero 일반 STT API : https://developers.rtzr.ai/
  - Google Gemini API : https://ai.google.dev/?gad_source=1&gclid=Cj0KCQjw6PGxBhCVARIsAIumnWZEKv46BEFNdI21QKEoffuQ6zYjnK3txrfWD4hZQY3f2-8GXa4wQ-0aAl38EALw_wcB
 
- 각 사이트에서 API Key, pwd를 발급 받으신 뒤 Writing Assitant 폴더의 required_keys.txt의 해당 부분을 채워 주십시오. API key가 없으면 모델이 동작하지 않습니다. 
  - rtzr_client id (returnzero stt api key), rtzr_client_pwd (returnzero stt api pwd)
  - gemini_api_key (google gemini api key) 
  
(2) 사용자 응답 오디오 파일 생성
- 아래 질문에 대한 답변을 담은 오디오 파일 3개를 각각 생성한 뒤, Writing-Assistant 모델의 auido 폴더에 추가합니다.

[질문 목록]
1. 근무하신 기간과 직책을 포함하여 수행하신 업무에 관한 정보를 알려주세요. 업무를 수행하시는동안 달성하신 성과나 강조하고 싶은 사항이 있으시다면 구체적으로 언급해주세요.
2. 귀하의 지원 동기와 직무 적합성을 간략하게 소개해주세요.
3. 귀하의 성격과 강점을 간략하게 소개해주세요. 

#### 실행
(1) 커맨드 창에서 아래 코드를 입력합니다. 
'''
python main.py results/user.txt #results/user.txt 는 결과 저장 경로
'''
(2) 경력사항, 지원동기, 성격 및 강점 순으로 사용자 응답 오디오 경로를 입력합니다.
(3) 결과는 모델 실행 시 입력한 저장 경로에 저장됩니다. 


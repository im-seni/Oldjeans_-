## Sample Models

### Writing-Assistant Model
- 음성 활용 이력서/자기소개서 작성 보조 모델입니다.
- 현재 폴더 안에는 2가지 사용자 예시가 들어 있습니다. 사용자 1,2의 응답과 모델 출력 결과는 각각 audio, results 폴더에서 확인하실 수 있습니다. 

#### 사용 방법
(1) required_keys.txt에 returnzero stt api, google gemini api 작성
(2) 경력사항, 지원동기, 성격 및 강점 사용자 음성 응답을 audio 폴더에 저장
(3) 커맨드 창에 아래 코드 입력
```
python main.py results/result.txt (결과 저장소)
```
(4) 가이드에 따라 사용자 음성 응답 경로 입력 
(5) 커맨드 창에 입력한 결과 저장 경로에서 최종 결과 확인

### 공고 필터링
- Data_Cleaning_Filtering.ipnyb 에서 사용자 기본사항에 따른 예시 필터링 결과를 확인하실 수 있습니다. 

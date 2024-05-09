from functions.speech import *
from functions.form import *
from functions.user_input import *
from functions.questions import * 

import argparse

parser = argparse.ArgumentParser(description ='name of the final txt file')

parser.add_argument('file', help='최종 파일 이름')

args = parser.parse_args()

# API Key, Pwd 등록
credentials = parse_credentials('required_keys.txt')

client_id = credentials.get('rtzr_client_id') #returnzero stt api
client_pwd = credentials.get('rtzr_client_pwd') #returnzero stt api
api_key = credentials.get('gemini_api_key') #gemini api 

def main():
    print('''안녕하세요! 귀하의 이력서 작성을 보조할 음성 비서 __ 입니다. 지금부터 제가 드리는 질문에 답변을 주시면, 제공해주신 정보를 바탕으로 기본 이력서와 자기소개서를 작성해드릴게요!''')
    
    audio_responses = {}
    for question in questions:
        key, question = question
        audio_path = get_input(question)
        while True:
            if os.path.exists(audio_path):
                break
            else:
                print(f'파일 경로 {audio_path}가 존재하지 않습니다. 다시 시도해주세요.')
                audio_path = get_input(question)
       
        audio_text = stt(client_id, client_pwd, audio_path)
        audio_responses[key] = audio_text
       
    
    job, brief1, brief2 = prompting(api_key, audio_responses['career'], audio_responses['career2'], audio_responses['career3'])

    save_responses(job, brief1, brief2, args.file)

    

if __name__ == '__main__':
    main()
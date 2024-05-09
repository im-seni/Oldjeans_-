def parse_credentials(file_path):
    credentials = {}
    with open(file_path, 'r') as file:
        for line in file:
            
            if '=' in line:
                key, value = line.strip().split('=', 1)
                credentials[key.strip()] = value.strip()
    
    return credentials



def save_responses(job, brief1, brief2, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\n경력사항: \n')
        for item in job:
            file.write(item)
            file.write('\n')
        file.write('\n자기소개서 1: \n')
        file.write(brief1)
        file.write('\n자기소개서 2: \n')
        file.write(brief2)

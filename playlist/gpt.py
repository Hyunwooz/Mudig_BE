import openai
import json
from .prompt import prompt, event_prompt
import os

# def get_music_recommendation(situations, feature, year):
#     openai.api_key = os.environ["OPEN_API_KEY"]  # 여기에 실제 API 키를 넣어주세요

#     # 모델 - GPT 3.5 Turbo 선택
#     model = "gpt-3.5-turbo"
#     # 질문 작성하기
#     query = {
#         "role": "user",
#         "content": str({
#             "현재 기분 및 상황": situations,
#             "장르 및 특성": feature,
#             "연도": year
#         }),
#     }

#     questions = {
#         "role": "user",
#         "content": str(query),
#     }

#     prompt.append(questions)
#     # ChatGPT API 호출하기
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=prompt,
#         timeout = 600
#     )
#     answer = response['choices'][0]['message']['content']
#     # response_json = answer.replace("'", "\"")
#     response_json = answer.replace("'", "\"").replace('"', '\"')
#     print('json', response_json)
#     try:
#         print('try', response_json)
#         # response_json = json.loads(response_json.replace("n\"t", "n\'t"))
#         response_json = json.loads(response_json)
#     except json.decoder.JSONDecodeError:
#         response_json = response_json.replace("n\"t", "n\'t")
#         response_json = json.loads(response_json)
#         print('except', response_json)
#     return response_json


def get_music_recommendation(situations, feature, year):
    openai.api_key = os.environ["OPEN_API_KEY"]  # 여기에 실제 API 키를 넣어주세요

    # 모델 - GPT 3.5 Turbo 선택
    model = "gpt-3.5-turbo"
    # 질문 작성하기
    query = {
        "현재 기분 및 상황": situations,
        "장르 및 특성": feature,
        "연도": year
    },

    questions = {
        "role": "user",
        "content": str(query),
    }
    prompt.append(questions)
    # ChatGPT API 호출하기
    response = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        timeout = 600
    )
    answer = response['choices'][0]['message']['content']
    print(answer)
    response_json = answer.replace("'",'"')
    # response_json = answer.replace("'", "\"").replace('"', '\"')
    
    # res_answer = json.loads(response_json)
    print('res_answer', response_json)
    try:
        res_answer = json.loads(response_json)
        print('try', res_answer)
    except json.decoder.JSONDecodeError:
        response_json = response_json.replace("n\"t", "n\'t")
        response_json = response_json.replace("\"\"", "\"")
        print('except', response_json)
        res_answer = json.loads(response_json)

    return res_answer

def event_music_recommendation(situations, feature):
    openai.api_key = os.environ["OPEN_API_KEY"]  # 여기에 실제 API 키를 넣어주세요

    # 모델 - GPT 3.5 Turbo 선택
    model = "gpt-3.5-turbo"
    # 질문 작성하기
    query = {
        "role": "user",
        "content": str({
            "현재 기분 및 상황": situations,
            "장르 및 특성": feature,
        }),
    }

    questions = {
        "role": "user",
        "content": str(query),
    }

    event_prompt.append(questions)
    # ChatGPT API 호출하기
    response = openai.ChatCompletion.create(
        model=model,
        messages=prompt,
        timeout = 600
    )
    answer = response['choices'][0]['message']['content']
    response_json = answer.replace("'", "\"")
    print('json', response_json)
    try:
        response_json = json.loads(response_json.replace("n\"t", "n\'t"))
        print('try', response_json)
    except json.decoder.JSONDecodeError:
        response_json = json.loads(response_json)
        print('except', response_json)
    return response_json
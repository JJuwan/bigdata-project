import ollama

article = """
자율주행 기술이 모빌리티 산업의 패러다임을 바꾸고 있다. 
특히 인지 알고리즘 분야에서 자율주행 시스템은 인간 운전자의 반응 속도보다 10배 빠른 판단력을 보여주고 있다. 
테슬라는 최신 FSD(Full Self-Driving) 소프트웨어를 통해 사고 발생률을 기존 대비 20% 감소시키는 성과를 거두었다. 
또한 물류 시스템에도 자율주행이 도입되어, 운송 비용을 현재의 30% 수준으로 절감할 수 있을 것으로 기대된다. 
다만 사고 발생 시 책임 소재 문제와 해킹 위험에 대한 우려도 제기되고 있어, 관련 법규 정비가 시급한 상황이다.
"""

# 키워드 추출
print("=== 키워드 추출 ===")
response = ollama.chat(
    model="gemma3:4b",
    messages=[
        {"role": "system", "content": "주어진 텍스트에서 핵심 키워드 5개를 추출하세요. 키워드만 쉼표로 구분하여 나열하세요."},
        {"role": "user", "content": article}
    ]
)
print(response["message"]["content"])

# 요약
print("\n=== 3줄 요약 ===")
response = ollama.chat(
    model="gemma3:4b",
    messages=[
        {"role": "system", "content": "주어진 텍스트를 정확히 3줄로 요약하세요. 각 줄은 한 문장으로 작성하세요."},
        {"role": "user", "content": article}
    ]
)
print(response["message"]["content"])
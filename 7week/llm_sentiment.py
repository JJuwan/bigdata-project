import ollama

reviews = [
    "영상미는 역대급으로 아름다워요! 하지만 전개가 너무 느려서 호불호가 갈릴 것 같습니다.",
    "돈 아까운 영화네요. 개연성도 없고 지루해서 중간에 나올 뻔했습니다.",
    "킬링타임용으로는 적당해요. 딱히 기억에 남는 장면은 없지만 가볍게 보기 좋습니다.",
    "인생 영화 등극입니다! 연출도 세련됐고 여운이 길게 남아서 한 번 더 볼 예정이에요."
]

for review in reviews:
    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "system",
                "content": "당신은 감성 분석 전문가입니다. 주어진 리뷰의 감성을 '긍정', '부정', '중립' 중 하나로 분류하고, 이유를 한 문장으로 설명해주세요."
            },
            {
                "role": "user",
                "content": f"다음 리뷰를 분석해주세요: {review}"
            }
        ]
    )
    print(f"리뷰: {review[:30]}...")
    print(f"분석: {response['message']['content']}")
    print("-" * 60)
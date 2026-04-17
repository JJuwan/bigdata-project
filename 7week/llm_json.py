import ollama
import json

reviews = [
    "디자인이 화면이랑 똑같고 배송도 하루 만에 왔어요. 정말 만족합니다!",
    "가성비는 최고예요. 다만 소재가 생각보다 얇아서 한 시즌 입기 적당한 것 같아요.",
    "사이즈가 정사이즈보다 조금 작게 나온 것 같으니 구매하실 분들은 참고하세요."
]

results = []

for review in reviews:
    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "system",
                "content": """당신은 리뷰 분석 전문가입니다.
주어진 리뷰를 분석하여 반드시 아래 JSON 형식으로만 응답하세요.
다른 텍스트는 포함하지 마세요.

{"sentiment": "긍정/부정/중립", "confidence": 0.0~1.0, "keywords": ["키워드1", "키워드2"]}"""
            },
            {
                "role": "user",
                "content": review
            }
        ]
    )

    raw = response["message"]["content"]

    # JSON 파싱 시도
    try:
        # LLM이 ```json ... ``` 으로 감싸서 응답할 수 있음
        clean = raw.strip()
        if "```json" in clean:
            clean = clean.split("```json")[1].split("```")[0].strip()
        elif "```" in clean:
            clean = clean.split("```")[1].split("```")[0].strip()

        data = json.loads(clean)
        results.append(data)
        print(f"리뷰: {review[:25]}...")
        print(f"   감성: {data['sentiment']}, 확신도: {data['confidence']}")
        print(f"   키워드: {data['keywords']}")
    except json.JSONDecodeError:
        print(f"JSON 파싱 실패: {raw[:100]}")

    print("-" * 50)

print(f"\n총 {len(results)}개 리뷰 분석 완료")
import ollama

# ❌ CoT 없이 바로 답 요청
bad = "5만 원짜리 셔츠 2벌을 20% 할인받아 사고, 배송비 3천 원을 더하면 총 얼마야?"

# ✅ CoT로 단계별 사고 요청
good = """5만 원짜리 셔츠 2벌을 20% 할인받아 사고, 배송비 3천 원을 더하면 총 얼마인지 단계별로 계산해줘:

단계별로 풀어주세요:
1. 셔츠 2벌의 원래 가격 합계
2. 20% 할인된 금액 계산
3. 배송비를 포함한 최종 결제 금액
"""

# 두 방식을 비교해보자
print("❌ CoT 없이:")
print("=" * 40)
response = ollama.generate(model="gemma3:4b", prompt=bad)
print(response["response"])

print("\n✅ CoT 사용:")
print("=" * 40)
response = ollama.generate(model="gemma3:4b", prompt=good)
print(response["response"])
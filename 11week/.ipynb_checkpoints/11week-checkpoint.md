기존 
프롬프트: 'You are a web security expert. Classify each HTTP request as "Normal" or "Anomalous" and provide a brief reason.\n\nExamples:\nRequest: GET /index.jsp HTTP/1.1\nOutput: {{"label": "Normal", "reason": "Standard page request, no suspicious pattern"}}\n\nRequest: GET /search?q=\' OR \'1\'=\'1 HTTP/1.1\nOutput: {{"label": "Anomalous", "reason": "Classic SQL Injection pattern with OR 1=1"}}\n\nNow classify:\nRequest: {http_text}\nOutput:'

LLM 정확도: 0.6000
LLM F1:    0.7403
분류 실패(Unknown): 0건

              precision    recall  f1-score   support

      Normal       1.00      0.07      0.13        43
   Anomalous       0.59      1.00      0.74        57

    accuracy                           0.60       100
   macro avg       0.79      0.53      0.44       100
weighted avg       0.76      0.60      0.48       100


2번째
프롬프트: """You are a highly advanced Web Application Firewall (WAF) analyzer.
Your task is to detect malicious patterns in HTTP requests including SQL Injection, XSS, and Path Traversal.

Analysis Steps:
1. Check for special characters used in attacks (e.g., ', ", <, >, ..).
2. Look for keywords like SELECT, UNION, SCRIPT, ALERT, or shell commands.
3. Determine if the request structure is normal for a standard web user.

Request: {http_text}

Output only a JSON object:
{{"label": "Normal/Anomalous", "reason": "Brief explanation identifying the specific attack vector if anomalous"}}
"""

LLM 정확도: 0.5700
LLM F1:    0.7226
분류 실패(Unknown): 1건

              precision    recall  f1-score   support

      Normal       0.50      0.02      0.04        43
   Anomalous       0.57      0.98      0.72        57

    accuracy                           0.57       100
   macro avg       0.54      0.50      0.38       100
weighted avg       0.54      0.57      0.43       100

3번째
프롬프트 : """Classify the HTTP request based on these strict guidelines:

- Normal: Basic page navigation, standard search terms, static asset requests.
- Anomalous: Parameter manipulation, SQL syntax, Script tags, Directory jumping.

Example 1 (Normal): GET /login.php HTTP/1.1 -> {{"label": "Normal", "reason": "Standard login page access"}}
Example 2 (Anomalous): GET /etc/passwd HTTP/1.1 -> {{"label": "Anomalous", "reason": "Path traversal attempt"}}
Example 3 (Anomalous): POST /search body: <script>alert(1)</script> -> {{"label": "Anomalous", "reason": "XSS injection in body"}}

Now classify:
Request: {http_text}
Output:"""

LLM 정확도: 0.5700
LLM F1:    0.7226
분류 실패(Unknown): 0건

              precision    recall  f1-score   support

      Normal       0.50      0.02      0.04        43
   Anomalous       0.57      0.98      0.72        57

    accuracy                           0.57       100
   macro avg       0.54      0.50      0.38       100
weighted avg       0.54      0.57      0.43       100

4번째
프롬프트 : """System: Specialized Web Security Scanner.
Objective: Detect any sign of automated attack tools or manual exploitation.
Input: HTTP Request.
Constraint: Be conservative. If a parameter looks suspicious, mark as Anomalous.

Request: {http_text}
Output (JSON):"""

LLM 정확도: 0.4300
LLM F1:    0.0000
분류 실패(Unknown): 100건

              precision    recall  f1-score   support

      Normal       0.43      1.00      0.60        43
   Anomalous       0.00      0.00      0.00        57

    accuracy                           0.43       100
   macro avg       0.21      0.50      0.30       100
weighted avg       0.18      0.43      0.26       100

5번째
프롬프트 : """System: Strict Malicious Request Detector.
Your goal is 100% detection. If the request contains ANY special characters (', ", <, >, ;) in the parameters, it MUST be marked as 'Anomalous'.

Request: {http_text}

Return JSON only:
{{"label": "Anomalous", "reason": "Suspicious character detected"}} or {{"label": "Normal", "reason": "Clean request"}}"""

LLM 정확도: 0.5700
LLM F1:    0.7261
분류 실패(Unknown): 0건

              precision    recall  f1-score   support

      Normal       0.00      0.00      0.00        43
   Anomalous       0.57      1.00      0.73        57

    accuracy                           0.57       100
   macro avg       0.28      0.50      0.36       100
weighted avg       0.32      0.57      0.41       100

6번째
프롬프트 : """You are a precise security analyzer. 
Your goal is to distinguish between 'Normal' and 'Anomalous' requests accurately.

Guidelines for 'Normal':
- Simple paths like /index.jsp, /login.php, /images/logo.png
- Simple parameters like id=1, search=keyword, page=2
- No special symbols like ', --, <, >, ../

Guidelines for 'Anomalous':
- SQL syntax: OR '1'='1', UNION SELECT, --
- Script tags: <script>, alert()
- System paths: /etc/passwd, ../../

[Crucial] Do not classify everything as Anomalous. If the request looks like a standard user action, you MUST label it as 'Normal'.

Request: {http_text}
Output JSON: {{"label": "Normal/Anomalous", "reason": "why"}}"""

LLM 정확도: 0.6600
LLM F1:    0.6304
분류 실패(Unknown): 0건

              precision    recall  f1-score   support

      Normal       0.57      0.86      0.69        43
   Anomalous       0.83      0.51      0.63        57

    accuracy                           0.66       100
   macro avg       0.70      0.68      0.66       100
weighted avg       0.72      0.66      0.65       100

7번째
프롬프트 : """You are a Web Security Guard. 
Classify the Request as "Normal" or "Anomalous".

[Checklist for "Anomalous"]
- Does it have special characters like: ' (quote), -- (dash), < > (brackets), ; (semicolon)?
- Does it have attack words like: SELECT, UNION, OR 1=1, ALERT, SCRIPT, ../ ?
- Is the URL path or body looking messy with symbols?

[Rule]
- If it is clean text/numbers (like id=10, name=james): Label as "Normal".
- If it matches ANY checklist above: Label as "Anomalous".

Request: {http_text}

Output format (Strict JSON):
{{"label": "Normal/Anomalous", "reason": "reason"}}"""

LLM 정확도: 0.5800
LLM F1:    0.7308
분류 실패(Unknown): 0건

              precision    recall  f1-score   support

      Normal       1.00      0.02      0.05        43
   Anomalous       0.58      1.00      0.73        57

    accuracy                           0.58       100
   macro avg       0.79      0.51      0.39       100
weighted avg       0.76      0.58      0.44       100

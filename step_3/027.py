# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.

# >> url = "http://sharebook.kr"
# 실행 예:
# kr

url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])

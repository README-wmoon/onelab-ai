# Onelab AI Project

<h3>🖥️ AI 프로젝트 소개</h3>

- 댓글 내용 플랫폼
  > 댓글 플랫폼에서의 비속어 사용은 사용자 경험을 저해할 수 있으며, 사회적으로 부적절한 내용을 제공할 수 있습니다.
  > 이에 따라 AI 기반의 댓글 비속어 필터링 시스템을 구현하여 사용자들의 편의성과 플랫폼의 안전성을 향상시키고자 하였습니다.

<h2> ✨ 문제 정의 </h2>

#### 제가 맡은 프로젝트의 목적은 댓글 플랫폼에서의 비속어를 자동으로 감지하고 또 그것을 제거하는 AI 시스템을 개발하는 것입니다. 주요 문제는 다음과 같습니다.
- 비속어를 식별하고 이를 효율적으로 필터링하는 방법 구현
- 부적절한 콘텐츠를 제거함으로써 플랫폼의 안전성을 유지하는 것

## ✨ 목차
1. 화면
2. 데이터 수집
3. Django 구현
4. Trouble-Shooting
5. 느낀점

## ✨ 화면
- Ai를 사용해서 적용할 화면 입니다.
<img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/61067828-e150-42cb-94a3-99fb92396996">
  

## ✨ 데이터 수집
- Naive Bayes 모델로 사용하였습니다.
- 수집 데이터 세트 깃허브 주소: https://github.com/2runo/Curse-detection-data
  
  1. 데이터
  - 일반 댓글과 욕설을 합쳐서 csv파일로 통합하였습니다.
  - <details>
       <summary>보기</summary>
       <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/5ac15f5e-a2d6-4a8a-a9a1-1b66a89c9067">
    </details>

  2. 데이터 전처리
  - 특수 문자 제거, 형태소 분석, 불용어 제거 함수를 사용하여 전처리를 진행하였습니다.
  - <details>
      <summary>보기</summary>
    
    ```
        # 데이터 전처리 함수 정의
        def preprocess_text(text):
            # 특수 문자 제거
            text = re.sub(r'[^가-힣a-zA-Z0-9\s-]', '', text)
            text = re.sub(r'\s+', ' ', text).strip()
            # 형태소 분석
            words = text.split()
            # 불용어 제거
            text = ' '.join([word for word in words if word not in korean_stopwords])
            return text
     ```
    </details>  
    

  3. 데이터 언더 샘플링
  - 비속어의 개수랑 비속어가 아닌 데이터를 학습시키는 과정에서 데이터의 균형을 맞추기 위해 언더샘플링을 사용하였습니다.
  - <details>
      <summary>보기</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/6fc44236-bc44-444a-996b-e26a0ca9e734">
    </details>  
    

  4. 데이터 fit
  - GridSearchCV를 사용하여 모델의 하이퍼파라미터를 튜닝하는 과정을 통해 최적의 파라미터를 찾는 방법을 사용하였습니다.
  - CountVectorizer를 사용하여 텍스트 데이터를 수치 데이터로 변환하고, MultinomialNB 분류기를 사용하여 예측하였습니다.
  - <details>
      <summary>보기</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/b5ebce7f-807f-4eaa-b07a-48a23cb5a79b">
    </details>  

    
  5. 모델 검증 결과
  - 모델 검증 결과는 정확도, 정밀도, 재현율, f1 score로 나타내었습니다.
  - <details>
      <summary>보기</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/ecbe713a-c3b2-46a5-a4a3-86cebc04c5f1">
    </details>  
    

  6. pkl 파일로 내보내기
  - Ai를 Django에서 사용하기 위하여 pkl 파일로 내보냈습니다.
  - <details>
      <summary>보기</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/bcaa911a-a8fc-4832-b988-f45b6916e756">
    </details> 
  
## ✨ Django
1. HTML, CSS
2. JS
3. View

## ✨ HTML, CSS
- 화면에서 비속어나 비속어가 아닌 댓글을 입력을 하고 등록을 하였을때 비속어는 댓글에 포함되지 않고 비속어가 아닌것만 댓글에 표시가 되게끔 만들었습니다.
-  <details>
    <summary>화면 구현</summary>
    <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/e3b7150a-f258-4f24-b201-85ab776e0ff6">
    
    - 댓글 내용을 입력을 하고 등록 버튼을 누르면 됩니다.<br> <br>
  </details>  
 

## ✨ JS
  - 등록 버튼과 신고 버튼을 눌렀을때 비동기 방식의 JavaScript로 구성하였습니다.
  - <details>
      <summary>코드</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/eaa9726a-1137-4622-988c-e5fd45a9776a">

      - 댓글 내용 입니다.

      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/25de1085-d4cb-44a3-9ae4-e7c9c0ec0d55">
      
      - 신고 쪽 입니다.
  </details> 
 

  - AI View <br>
    - Post 방식으로 reply_content를 담아 그것이 비속어인지 아닌지 구분하였습니다.
    - 또한 check_comments에 비속어인지 아닌지 Ai훈련된 모델의 함수를 호출하여 사용하였습니다.
    - <details>
        <summary>댓글 코드 입니다.</summary>
        <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/d0a09e70-f161-41a2-a6e6-9f7de0e62556">
        <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/2f9f8c5e-282b-43e7-9d79-a8fdb1f13731"> 
      </details>
      
    - <details>
        <summary>신고 코드 입니다.</summary>
        <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/7d8e06cc-02c0-48f4-a329-6e71f7c06edb">
      </details> 
  
## ✨ TroubleShooting
1. await fetch 비동기쪽 데이터를 불러오는 중 발생한 문제
   - 문제 : 데이터를 불러오는 중에 url이 not found가 뜰때가 많았었습니다. 또한 urls에 경로를 다시 확인하고 썻는데도 문제가 있었다.
   - 해결 : 강력 새로고침과 로그아웃을 하고 다시 로그인을 하니 잘 됬습니다.

2. CSRF-Token을 찾지 못하는 에러가 있었습니다.
   - 문제 : 버튼을 클릭을 하면 token을 못찾는 에러가 떳었습니다.
   - 해결 : 강력 새로고침과 캐시 삭제를 하고 다시 로그인을 하니 해결 되었습니다.

## ✨ 느낀점
- 이론적으로 배운 AI 모델을 실제 웹 애플리케이션에 적용해 볼 수 있다는 점이 매우 흥미로웠습니다. 특히 실시간으로 사용자 댓글을 분석을 하고 그것이 비속어인지 필터링 하는 기능을 구현하면서, AI 기술의 실용성을 체감할 수 있었습니다.
- 특수 문자 제거, 불용어 제거 등 데이터 전처리 과정을 통해 데이터의 품질을 향상시키는 것이 얼마나 중요한지 배웠습니다. 이 과정이 모델의 성능에 직접적으로 영향을 미치며, 보다 정확한 예측을 가능하게 한다는 것을 알게 되었습니다.
- 프로젝트를 진행하면서 여러 가지 문제를 마주하게 되었지만 특히 CSRF 토큰 문제나 비동기 통신 중 발생한 오류 등을 해결하면서 웹 개발의 깊이를 더 이해할 수 있었습니다.
- JavaScript를 사용한 비동기 통신을 통해, 사용자 경험을 개선하고, 서버와의 데이터 교환을 효율적으로 관리하는 방법을 배웠습니다. 이는 웹 애플리케이션의 성능과 응답성을 높이는 데 중요한 역할을 했습니다.
- 이번 경험을 통해 새로운 기술을 배우고 적용하는 것이 얼마나 흥미롭고 가치 있는 일인지 깨달았습니다. 앞으로도 지속적으로 학습하고 발전해 나가야겠다는 동기부여가 되었습니다.


  
  

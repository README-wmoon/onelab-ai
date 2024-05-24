# Onelab AI Project

<h3>🖥️ AI 프로젝트 소개</h3>

- 댓글 내용 플랫폼
  > 댓글 플랫폼에서의 비속어 사용은 사용자 경험을 저해할 수 있으며, 사회적으로 부적절한 내용을 제공할 수 있습니다.
  > 이에 따라 AI 기반의 댓글 비속어 필터링 시스템을 구현하여 사용자들의 편의성과 플랫폼의 안전성을 향상시키고자 하였습니다.

### ✨ 문제 정의
이 연구의 목적은 댓글 플랫폼에서의 비속어를 자동으로 감지하고 또 그것을 제거하는 AI 시스템을 개발하는 것입니다. 주요 문제는 다음과 같습니다.
- 비속어를 식별하고 이를 효율적으로 필터링하는 방법 구현
- 사용자의 댓글 경험을 향상시키고 부적절한 콘텐츠를 제거함으로써 플랫폼의 안전성을 유지하는 것

### ✨ 목차
- 화면
- 데이터 수집
- Django 구현
- Trouble-Shooting
- 느낀점

### ✨ 화면
- Ai를 사용해서 적용할 화면 입니다.
- <details>
     <summary>보기</summary>
     <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/52323e32-fe97-415d-b75b-6d9c06cdc498">
  </details>
  

### ✨ 데이터 수집
- 댓글 플랫폼에서 수집된 데이터를 기반으로 AI 모델을 훈련시켰습니다.
- 데이터의 전처리 단계에서는 토큰화, 정제, 및 벡터화 과정을 거쳤으며, 머신러닝 및 딥러닝 모델을 사용하여 비속어를 식별하고 필터링했습니다.
- smailgate 회사 비속어랑 유튜브 리뷰 비속어로 이용하여 데이터를 수집하였습니다.
- 작업 환경은 jupyter notebook으로 환경해서 진행하였습니다.
- 사용한 방법은 Naive Bays로 하였으며 그것은 다음과 같습니다.
  1. 데이터
  - 데이터 모델을 csv로 하여 처리하였습니다.
    <details>
       <summary>보기</summary>
       <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/5ac15f5e-a2d6-4a8a-a9a1-1b66a89c9067">
    </details>

  2. 데이터 전처리
  - 데이터 모델의 함수를 정의했으며, 데이터 모델을 전처리 했습니다.
  - <details>
      <summary>보기</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/3015ae85-f7be-4536-88e2-3cc2735ce798">
    </details>  
    

  3. 데이터 언더 샘플링
  - 데이터를 언더 샘플링을 하여서 처리하였습니다.
  - <details>
      <summary>보기</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/6fc44236-bc44-444a-996b-e26a0ca9e734">
    </details>  
    

  4. 데이터 fit
  - 비속어와 비속어 아닌 데이터들을 훈련시켰습니다.
  - <details>
      <summary>보기</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/b5ebce7f-807f-4eaa-b07a-48a23cb5a79b">
    </details>  

    
  5. 실험 결과
  - 실험 결과는 정확도, 정밀도, 재현율, f1 score로 나타내었습니다.
  - <details>
      <summary>보기</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/ecbe713a-c3b2-46a5-a4a3-86cebc04c5f1">
    </details>  
    

  6. pkl 파일로 내보내기
  - 훈련된 데이터들을 Django로 보내기 위해서 pkl 파일로 내보냈습니다.
  - <details>
      <summary>보기</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/bcaa911a-a8fc-4832-b988-f45b6916e756">
    </details> 
  
### ✨ Django로 구현
1. HTML, CSS
2. JS
3. View

### ✨ HTML, CSS
- 화면에서 비속어나 비속어가 아닌 댓글을 입력을 하고 등록을 하였을때 비속어는 댓글에 포함되지 않고 비속어가 아닌것만 댓글에 표시가 되게끔 만들었습니다.
-  <details>
    <summary>화면 구현</summary>
    <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/600d7ce2-e6bb-4bf2-a15e-abb902a843db">
    
    - 댓글 내용을 입력을 하고 등록 버튼을 누르면 됩니다.<br> <br>
  </details>  
 

### ✨ JS
  - 등록 버튼과 신고 버튼을 눌렀을때 비동기 방식의 JavaScript로 구성하였습니다.
  - <details>
      <summary>코드</summary>
      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/eaa9726a-1137-4622-988c-e5fd45a9776a">

      - 댓글 내용 입니다.

      <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/25de1085-d4cb-44a3-9ae4-e7c9c0ec0d55">
      
      - 신고 쪽 입니다.
  </details> 
 
  
  - 파이썬의 코드는 이렇습니다.
  - AI View <br>
    - Post 방식으로 reply_content를 담아 그것이 비속어인지 아닌지 구분하였습니다.
    - 또한 check_comments에 비속어인지 아닌지 Ai훈련된 모델의 함수를 호출하여 사용하였습니다.
    - <details>
        <summary>댓글 등록쪽 입니다.</summary>
        <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/d0a09e70-f161-41a2-a6e6-9f7de0e62556">
        <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/2f9f8c5e-282b-43e7-9d79-a8fdb1f13731"> 
      </details>
      
    - <details>
        <summary>신고 버튼 쪽 API 입니다.</summary>
        <img src="https://github.com/onelab-server-ai/onelab-ai/assets/129862668/7d8e06cc-02c0-48f4-a329-6e71f7c06edb">
      </details> 
  
### ✨ TroubleShooting
1. await fetch 비동기쪽 데이터를 불러오는 중 발생한 문제
2. CSRF-Token을 찾지 못하는 에러가 있었습니다.

1. await fetch 비동기쪽 데이터를 불러오는 중 발생한 문제
   - 문제 : 데이터를 불러오는 중에 url이 not found가 뜰때가 많았었습니다. 또한 urls에 경로를 다시 확인하고 썻는데도 문제가 있었다.
   - 해결 : 강력 새로고침과 로그아웃을 하고 다시 로그인을 하니 잘 됬습니다.

2. CSRF-Token을 찾지 못하는 에러가 있었습니다.
   - 문제 : 버튼을 클릭을 하면 token을 못찾는 에러가 떳었습니다.
   - 해결 : 강력 새로고침과 캐시 삭제를 하고 다시 로그인을 하니 해결 되었습니다.

### ✨ 느낀점
- 이번 AI 프로젝트에서는 저에 대한 부족한 점이 많았습니다.
- 프로젝트 진행 중에도 팀원들이 모델의 학습과 평가, 그리고 성능 최적화에 대해 많은 노력을 기울이는 것을 보며 배울 점이 많았습니다.
- 향후에는 더 적극적으로 참여하여 프로젝트에 기여하고 싶습니다.

### ✨ 개선사항
- 프로젝트를 하며 몇가지 개선사항이 필요하다고 생각합니다
1. 모델의 실시간 처리 능력: 댓글이 작성될 떄 실시간으로 비속어를 감지하고 경고하는 시스템이 필요하다고 생각했다.
2. 사용자 피드백: 팀원들이랑 사람들의 피드백을 적극적으로 수용하여 더 나은 성과를 얻을 수 있을것이라고 생각했다.
  
  

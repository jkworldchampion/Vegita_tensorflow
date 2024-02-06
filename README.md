# Vegita_tensorflow
나동빈 님의 배추가격 예측 프로젝트를 현재 tensorflow2 version으로 수정하였다


<img width="1470" alt="스크린샷 2024-02-06 오후 3 38 01" src="https://github.com/jkworldchampion/Vegita_tensorflow/assets/83493949/285a9b5f-e89b-4bc6-b098-2ed9a9172a19">
기본 페이지는 다음과 같다.  
기본적인 Template은 강의에서와 같이 Bootstrap에서 쉽게 받을 수 있다.
받은 index.html을 수정한 파일은 동빈나님의 [깃허브 레퍼지토리](https://github.com/ndb796/Vegita/)에 가면 받을 수 있다.

<img width="1470" alt="스크린샷 2024-02-06 오후 3 38 16" src="https://github.com/jkworldchampion/Vegita_tensorflow/assets/83493949/0b513341-0a78-4ae1-869e-36a16d10df48">
<img width="1470" alt="스크린샷 2024-02-06 오후 3 38 28" src="https://github.com/jkworldchampion/Vegita_tensorflow/assets/83493949/91f07cb9-6fb5-4f36-9852-ec984abde20e">
<img width="1470" alt="스크린샷 2024-02-06 오후 3 38 39" src="https://github.com/jkworldchampion/Vegita_tensorflow/assets/83493949/e76b0104-e966-41f7-aae7-c17c12376511">
다음과 같은 웹 페이지 flask 프로젝트를 받을 수 있고, 해당 flask폴더로 가서 python server.py명령어로 서버를 실행 시킬 수 있다.

이 때 내장된 코드가 tensorflow version_1이기 때문에, 이부분을 임의로 회귀예측 모델을 구축하고 결과를 도출하는 tensorflow version_2 코드로 바꾸었다.

결과적으로 다음과 같이 예측된 결과를 내는 것을 알 수 있다.
<img width="1190" alt="스크린샷 2024-02-06 오후 3 38 57" src="https://github.com/jkworldchampion/Vegita_tensorflow/assets/83493949/4657b162-acc3-4cdf-a04f-9c36e356bb2d">

<img width="1176" alt="스크린샷 2024-02-06 오후 3 39 05" src="https://github.com/jkworldchampion/Vegita_tensorflow/assets/83493949/08c832d1-de45-4a77-a2e6-e8d11c197df6">

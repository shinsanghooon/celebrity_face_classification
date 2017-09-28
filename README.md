# celebrity_face_classification

CNN을 통해 연예인 얼굴 사진을 이용한 classification 모델을 만들고 마지막 레이어에 softmax layer를 추가해 확률을 output으로 출력하게 만든다. 그리고 연예인이 아닌 일반인의 사진을 입력으로 하여 어느 연예인과 가장 닮았는지 출력된 확률을 확인한다. 

30명 / 각 200장 / 73% 
30명 / 각 400장 / 84%
30명 / 각 650장 / 94% 

### further study
- face landmark estimation ( 얼굴의 핵심적인 랜드마크 68개 지점을 뽑아냄 )
- openCV ( affine transformation ) 
- DNN (이미지를 128차원 데이터로 변환)
- classification algorithm 사용 
- 지인 얼굴 입력 -> 가장 닮은 연예인 확률 출력 

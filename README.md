# KLipNet
LipNet : 엔드 투 엔드 문장 수준의 리딩
Yannis M. Assael, Brendan Shillingford, Shimon Whiteson 및 Nando de Freitas의 논문 'LipNet : End-to-End 문장 수준의 Lipreading'에 설명 된 방법의 Keras 구현 ( https://arxiv.org/abs/1611.01599 ).

LipNet 예측 수행 (시각화 전용 자막 정렬)

결과
대본	시대	CER	베르	블루
보이지 않는 스피커 [C]	해당 없음	해당 없음	해당 없음	해당 없음
보이지 않는 스피커	178	6.19 %	14.19 %	88.21 %
겹친 스피커 [C]	해당 없음	해당 없음	해당 없음	해당 없음
겹친 스피커	368	1.56 %	3.38 %	96.93 %
참고 사항 :

[C]는 커리큘럼 학습을 사용하는 것을 의미합니다.
N / A는 훈련이 진행 중이거나 수행되지 않았 음을 의미합니다.
이 모델의 결과 공유에 대한 귀하의 기여는 높이 평가됩니다. :)
의존성
케 라스 2.0+
텐서 플로우 1.0+
PIP (패키지 설치용)
위에 나열된 다른 여러 라이브러리 setup.py

용법
모델을 사용하려면 먼저 저장소를 복제해야합니다.

git clone https://github.com/rizkiarm/LipNet
그런 다음 패키지를 설치할 수 있습니다.

cd LipNet/
pip install -e .
참고 : 당신이 CUDA를 사용하지 않으려면, 당신은 편집해야 setup.py하고 변화 tensorflow-gpu에tensorflow

끝났습니다!

다음에 수행 할 수있는 작업에 대한 몇 가지 아이디어가 있습니다.

패키지를 수정하고 개선하십시오.
사전 정의 된 훈련 시나리오를 사용하여 모델을 훈련시킵니다.
자신의 훈련 시나리오를 만드십시오.
미리 훈련 된 분동 을 사용 하여 립 리딩을하십시오.
미쳐 가서 다른 데이터 세트를 실험 해보세요! 일부 하이퍼 파라미터를 변경하거나 모델을 수정하여
데이터 세트
이 모델은 GRID 모음을 사용합니다 ( http://spandh.dcs.shef.ac.uk/gridcorpus/ )

사전 훈련 된 가중치
모델 교육에 어려움을 겪고 있거나 최종 결과를보고 싶을 경우 여기에 제공된 가중치를 다운로드하여 사용할 수 있습니다 : https://github.com/rizkiarm/LipNet/tree/master/evaluation / 모델 .

무게 저장 및 적재에 대한 자세한 내용은 Keras FAQ를 참조하십시오 .

훈련
사용 가능한 5 가지 교육 시나리오가 있습니다.

전제 조건
모든 비디오를 다운로드하고 (일반) GRID Corpus 웹 사이트에서 정렬하십시오.
모든 비디오를 추출하고 정렬합니다.
datasets각 교육 시나리오 폴더에 폴더를 만듭니다 .
align폴더 안에 폴더를 만듭니다 datasets.
현재 모든 train.py비디오는 100x50px 마우스 자르기 이미지 프레임 형태 일 것으로 예상합니다. 내부의 인스턴스화 에서 vtype = "face"및 face_predictor_path(에서 찾을 수 있음) 을 추가하여이를 변경할 수 있습니다 .evaluation/modelsGeneratortrain.py
다른 방법은 scripts/extract_mouth_batch.py스크립트를 사용 하여 마우스 작물 이미지를 추출하는 것 입니다.
각각 training/*/datasets/align에서 정렬 폴더로 심볼릭 링크를 만듭니다 .
train.py각 시나리오 내부 에서 수정하여 교육 매개 변수를 변경할 수 있습니다 .
무작위 분할 (유지되지 않음)
training/random_split/datasets/video비디오 데이터 세트 폴더 ( s*디렉토리 포함 ) 와의 심볼릭 링크를 만듭니다 .

다음 명령을 사용하여 모델을 학습하십시오.

./train random_split [GPUs (optional)]
참고 :의val_split 내부 인수 를 수정하여 유효성 검사 분할 값을 변경할 수 있습니다 train.py.

보이지 않는 스피커
다음 폴더를 작성하십시오.

training/unseen_speakers/datasets/train
training/unseen_speakers/datasets/val
그런 다음 비디오 데이터 세트 폴더 내부에서 training/unseen_speakers/datasets/[train|val]/s*선택한 심볼릭 링크를 만듭니다 s*.

사용 된 종이 s1, s2, s20, 및 s22평가와 교육에 대한 나머지.

다음 명령을 사용하여 모델을 학습하십시오.

./train unseen_speakers [GPUs (optional)]
커리큘럼 학습이없는 보이지 않는 스피커
보이지 않는 스피커와 같은 방식으로.

참고 :curriculum_rules 내부의 방법 을 수정하여 커리큘럼을 변경할 수 있습니다 .train.py

./train unseen_speakers_curriculum [GPUs (optional)]
겹친 스피커
준비 스크립트를 실행하십시오.

python prepare.py [Path to video dataset] [Path to align dataset] [Number of samples]
노트:

[Path to video dataset] 구조가있는 폴더 여야합니다. /s{i}/[video]
[Path to align dataset] 구조가있는 폴더 여야합니다. /[align].align
[Number of samples] 이하 여야합니다 min(len(ls '/s{i}/*'))
그런 다음 각 스피커에 대해 교육을 실행하십시오.

python training/overlapped_speakers/train.py s{i}
커리큘럼 학습이있는 겹친 스피커
복사 prepare.py에서 overlapped_speakers에 폴더 overlapped_speakers_curriculum폴더, 이전에 설명을 훈련 중복 스피커에 설명 된대로 실행합니다.

그런 다음 각 스피커에 대해 교육을 실행하십시오.

python training/overlapped_speakers_curriculum/train.py s{i}
참고 : 항상 그렇듯이 curriculum_rules내부의 방법 을 수정하여 커리큘럼을 변경할 수 있습니다train.py

평가
단일 비디오 / 이미지 프레임에서 학습 된 모델을 평가하고 시각화하려면 다음 명령을 실행할 수 있습니다.

./predict [path to weight] [path to video]
예:

./predict evaluation/models/overlapped-weights368.h5 evaluation/samples/id2_vcd_swwp2s.mpg
진행중인 작업
현재 진행중인 작업입니다. 오류가 예상됩니다. 구현 측면에서 오류가 발견되면 문제를 제출하거나 PR을 작성하여 오류를보고하십시오. 감사!

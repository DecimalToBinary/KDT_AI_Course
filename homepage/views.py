from django.shortcuts import HttpResponse, render
from django.views import View

# Create your views here.

class IntroView(View):
    
    def get(self, request, *args, **kwargs):
        info = {
            'name': '송승헌',
            'age': 26,
            'height': '179.5 cm',
            'hobby': ['영화보기', '아카이빙'],
            'stack': ['Python', 'Javascript', 'Django', 'MySQL', 'Spark'],
            'description':  """안녕하세요, 송승헌입니다. 스파크 등 데이터 처리기술을 활용한 분산처리, AI 모델 서빙하는 백엔드 개발을 주로 삼는 개발자 취업을 희망합니다. """
        }
        
        return render(request, 'intro.html', {'info': info})

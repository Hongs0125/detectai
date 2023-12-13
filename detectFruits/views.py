import shutil

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ultralytics import YOLO
import os
import base64

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@api_view(['POST'])
def detectFruits(request):
    image_file = request.FILES.get('image_file')
    result_file_path = os.path.join(BASE_DIR, 'results')
    if not image_file:
        return Response({"massege": "이미지 파일을 첨부해주세요."}, status=400)

    image_path = os.path.join(BASE_DIR, 'saveImage', 'input.jpg')
    with open(image_path, 'wb+') as destination:
        for chunk in image_file.chunks():
            destination.write(chunk)

    ref_result = []
    counts = {}

    model = YOLO(os.path.join(BASE_DIR, 'fruitsModel.pt'))
    results = model(image_path, save=True, imgsz=640, conf=0.5,
                    project=os.path.join(result_file_path))
    names = model.names

    for r in results:
        for c in r.boxes.cls:
            name = names[int(c)]
            if name in counts:
                counts[name] += 1
            else:
                counts[name] = 1

    for name, quantity in counts.items():
        ref_result.append({"name": name, "quantity": quantity})

    os.rename(os.path.join(result_file_path, 'predict', 'input.jpg'), os.path.join(result_file_path, 'result.jpg'))
    shutil.rmtree(os.path.join(result_file_path, 'predict'))

    with open(os.path.join(result_file_path, 'result.jpg'), 'rb') as f:
        encoded_file = base64.b64encode(f.read()).decode('utf-8')

    os.remove(image_path)
    os.remove(os.path.join(result_file_path, 'result.jpg'))

    print(ref_result)
    return JsonResponse({'results': ref_result, 'image': encoded_file})
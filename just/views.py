from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render


from just.models import Details, Form
from .serializers import JustSerializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def home(request):
    details = Details.objects.all()
    print(details)
    param = {'details': details}
    if request.method == 'POST':
        name = request.POST.get('name', "")
        phone = request.POST.get('phone', "")
        job = request.POST.get('job', "")
        desc = request.POST.get('desc', "")
        address = request.POST.get('address', "")
        form = Form(name=name, phone=phone, job=job,
                    desc=desc, address=address)
        form.save()
    return render(request, 'index.html', param)


def about(request):
    return render(request, 'about.html')


def price(request):
    return render(request, 'price.html')


# extra
@csrf_exempt
def get_details(request):
    if request.method == 'GET':
        detail = Details.objects.all()
        detailserializer = JustSerializer(detail, many=True)
        return JsonResponse(detailserializer.data, safe=False)
    elif request.method == 'POST':
        detailserializer_data = JSONParser().parse(request)
        detailserializer = JustSerializer(data=detailserializer_data)
        if detailserializer.is_valid:
            detailserializer.save()
            return JsonResponse('added sucessfully', safe=False)
        return JsonResponse('failed to add', safe=False)

    # elif request.method == 'PUT':
    #     detailserializer = JSONParser().parse(request)
    #     detail = Details.objects.all(ToDoId=detailserializer['ToDoId'])
    #     detailserializer_data = JustSerializer(detail, data=detailserializer)
    #     if detailserializer_data.is_valid:
    #         detailserializer.save()
    #         return JsonResponse('Updated sucessfully', safe=False)
    #     return JsonResponse('failed to add', safe=False)

    # elif request.method == 'DELETE':
    #     detail = Details.objects.all(ToDoId=id)
    #     detail.delete()
    #     return JsonResponse('DElete successfully', safe=False)


# added for test
def home_view(request):
    print(request.GET)
    return render(request, "index.html")

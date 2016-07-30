#coding:utf-8
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import StreamingHttpResponse
from django.conf import settings
from .forms import UploadForm
import os,time,json
from datastruct.CalculateExcel import func1_calculate
from datastruct import GetData
# Create your views here.

@permission_required('solvedata.solve_data',raise_exception=True)
def index(request):
	return render(request,'solvedata/main.html')

@permission_required('solvedata.solve_data',raise_exception=True)
def user(request):
	return render(request,'solvedata/user.html')

#func1
@permission_required('solvedata.solve_data',raise_exception=True)
def func1_1(request):
	filenames = os.listdir(settings.MEDIA_ROOT+'common/func1/')
	results = []
	for filename in filenames:
		file_path = settings.MEDIA_ROOT+'common/func1/'+filename
		mtime = time.localtime(os.path.getmtime(file_path))
		mtime = time.strftime('%Y-%m-%d',mtime)
		filesize = os.path.getsize(file_path)
		md5 = "12345678123456781234567812345678"
		description = "nothing"
		results.append((filename,description,md5,mtime,filesize))
	results.sort(key=lambda x:x[2])
	return render(request,'solvedata/func1_1.html',{'results':results})

@permission_required('solvedata.solve_data',raise_exception=True)
def func1_result(request):
	current_user = request.user.username
	filenames = os.listdir(settings.MEDIA_ROOT+current_user+'/func1/result')
	results = []
	for filename in filenames:
		file_path = settings.MEDIA_ROOT+current_user+'/func1/result/'+filename
		mtime = time.localtime(os.path.getmtime(file_path))
		mtime = time.strftime('%Y-%m-%d',mtime)
		filesize = os.path.getsize(file_path)
		results.append((filename,mtime,filesize))
	results.sort(key=lambda x:x[2])
	return render(request,'solvedata/func1_result.html',{'results':results})

@permission_required('solvedata.solve_data',raise_exception=True)
def func1_result_view(request):
	table,graph = GetData.func1_get(request.user.username,'result.xls')
	table = json.dumps(table)
	graph = json.dumps(graph)
	return render(request,'solvedata/func1_result_view.html',{'table':table,'graph':graph})

@permission_required('solvedata.solve_data',raise_exception=True)
def download(request,file_owner,func,file_name):
	if (not file_owner=='common') and file_owner!=request.user.username:
		return HttpResponse("<script>alert('只能下载自己的文件！')</script>")
	def file_iterator(filename, chunk_size=512):
		with open(filename,'rb') as f:
			while True:
				c = f.read(chunk_size)
				if c:
					yield c
				else:
					break
	file_path = os.path.join(settings.MEDIA_ROOT+file_owner+'/'+func,file_name)
	response = StreamingHttpResponse(file_iterator(file_path))
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_name.split('/')[-1])
	return response

def handle_uploaded_file(path,f):
	try:
		file_path = os.path.join(path,f.name)
		with open(file_path, 'wb+') as destination:
			for chunk in f.chunks():
				destination.write(chunk)
	except:
		pass


@permission_required('solvedata.solve_data',raise_exception=True)
def upload(request):
	if request.method == 'POST':
		form = UploadForm(request.POST, request.FILES)
		if form.is_valid():
			current_user = request.user.username
			handle_uploaded_file(settings.MEDIA_ROOT+current_user,request.FILES['file'])
			func1_calculate(current_user,request.FILES['file'].name)
			return HttpResponse("上传成功")
	return HttpResponse("上传失败")

@permission_required('solvedata.solve_data',raise_exception=True)
def delete(request,file_owner,func,file_name):
	file_path = os.path.join(settings.MEDIA_ROOT+file_owner+"/"+func,file_name)
	print(next)
	try:
		os.remove(file_path)
		return HttpResponseRedirect("/data/"+func+"/result")
	except:
		return HttpResponse("删除失败")

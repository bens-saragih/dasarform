from django.shortcuts import render

def index(request):
	context = {
		'judul':'Home',
	}
	
	if request.method == 'POST':
		print(request.POST['nickname'])# nickname adalah name yang ada di file html nya nya yang akan di gunakan untuk identitas di database
		print(request.POST['alamat'])

	return render(request,'index.html',context)
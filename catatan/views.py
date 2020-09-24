from django.shortcuts import render, redirect
from . import models, forms

def index(req):
    tasks = models.Catatan.objects.all()
    return render(req, 'catatan/index.html',{
        'data': tasks,
    })
    
def new(req, *args, **kwargs):
    form_catatan = forms.CatatanForm()
    form_gambar = forms.GambarForm()
    if req.method == 'POST':
        form_catatan = forms.CatatanForm(req.POST)
        if form_catatan.is_valid():
            form_catatan.save()
        images = []
        files = req.FILES.getlist('gambar')
        for file in files:
            images.append(models.Gambar.objects.create(gambar=file,catatan=form_catatan.instance))
        return redirect('/catatan/')
    return render(req, 'catatan/new.html',{
        'form_catatan' : form_catatan,
        'form_gambar' : form_gambar,
    })

def detail(req, id):
    task = models.Catatan.objects.filter(pk=id).first()
    return render(req, 'catatan/detail.html', {
        'data': task,
    })

def delete(req, id):
    models.Catatan.objects.filter(pk=id).delete()
    return redirect('/catatan/')

def update(req, id):
    if req.POST:
        task = models.Catatan.objects.filter(pk=id).update(
            tgl_kegiatan=req.POST['tgl_kegiatan'], 
            judul=req.POST['judul'], 
            ket=req.POST['ket'],
            gambar=req.POST['gambar'])
        return redirect('/catatan/')

    task = models.Catatan.objects.filter(pk=id).first()
    return render(req, 'catatan/update.html', {
        'data': task,
    })
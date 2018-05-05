################
#巡检记事
################


#与数据库模型绑定的表单（巡检记事）
class Bjs_base_other_situation_ModelForm(forms.ModelForm):
    class Meta:
        model = Bjs_base_other_situation
        fields = '__all__'


#巡检记事（添加）
@login_required(login_url='/account/')
@permission_required(
    perm='home.add_bjs_base_other_situation', login_url='/home/')
def add_bjs_base_other_situation(request):
    if request.method == 'GET':
        BBOSMF = Bjs_base_other_situation_ModelForm()
        return render(request, 'add_bjs_base_other_situation.html',
                      locals())
    else:
        BBOSMF = Bjs_base_other_situation_ModelForm(request.POST)
        if BBOSMF.is_valid():
            BBOSMF.save()
        return HttpResponse('add post')


#巡检记事（编辑）
@login_required(login_url='/account/')
@permission_required(
    perm='home.change_bjs_base_other_situation', login_url='/home/')
def change_bjs_base_other_situation(request):
    id = request.GET.get('id')
    obj = Bjs_base_other_situation.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('edit post not have obj')
    if request.method == 'GET':
        BBOSMF = Bjs_base_other_situation_ModelForm(instance=obj, )
        return render(request, 'change_bjs_base_other_situation.html',
                      locals())
    else:
        BBOSMF = Bjs_base_other_situation_ModelForm(
            request.POST,
            instance=obj,
        )
        if BBOSMF.is_valid():
            BBOSMF.save()
        return HttpResponse('edit post')


#巡检记事（删除）
@login_required(login_url='/account/')
@permission_required(
    perm='home.delete_bjs_base_other_situation', login_url='/home/')
def delete_bjs_base_other_situation(request):
    id = request.GET.get('id')
    obj = Bjs_base_other_situation.objects.filter(id=id).first()
    if not obj:
        return HttpResponse('delete post not have obj')
    if request.method == 'GET':
        BBOSMF = Bjs_base_other_situation_ModelForm(instance=obj, )
        return render(request, 'delete_bjs_base_other_situation.html',
                      locals())
    else:
        Bjs_base_other_situation.objects.filter(id=id).delete()
        return HttpResponse('delete post')
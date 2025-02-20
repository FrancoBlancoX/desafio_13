from django import forms
from .models import Post,Comentario
from datetime import date
from django.forms import ModelForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
        "fechaCreado": forms.SelectDateWidget()
         } 
           
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['fechaCreado'].initial = date.today()

       

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'email', 'contenido', 'activo')
        widgets = {
            'activo': forms.CheckboxInput(attrs={'placeholder': 'Activo'}),
        }

    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.fields['activo'].required = False

class PostFormEdit(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        widgets = {
            "fechaCreado": forms.SelectDateWidget()
        }
           
    def __init__(self, *args, **kwargs):
        super(PostFormEdit, self).__init__(*args, **kwargs)
        
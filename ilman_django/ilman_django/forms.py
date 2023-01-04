from django import forms
from blog.models import Post

class classform(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'email',
        ]

    widget={
        'title': forms.TextInput(
            attrs = {
                'class' : 'form',
                'placeholder' : 'Masukan Judul',
            }
        )
    }

    def clean_title(self):
        ji = self.cleaned_data.get('title')

        if ji == "Rasis":
            raise forms.ValidationError("Cant post Rasis")
    
        return ji

# class nameclass(forms.Form):
#     nama = forms.CharField()

# class classforms(forms.Form):
#     namac = forms.CharField()
#     alamatc = forms.CharField()
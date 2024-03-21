from django.forms import ModelForm
from .models import * 
class Personalinfoform(ModelForm):
    class Meta:

        model = User
        fields = ['email','profile_pic','about_me','address','contact','facebook','instagram']

class Skillform(ModelForm):
    class Meta:

        model = Skill
        fields = ['title','description','icon']

class Projectform(ModelForm):
    class Meta:

        model = Project
        fields = ['image']
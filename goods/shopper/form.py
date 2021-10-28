from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# class loginForm(forms.Form):
#     username=forms.CharField(max_length=11,label='输入手机号',widget=forms.TextInput(attrs={'class':'layui-input','placeholder':'输入手机号','lay-verify':'required|phone','id':'username'}),)
#     password=forms.CharField(max_length=11,label='输入密码',widget=forms.PasswordInput(attrs={'class':'layui-input','placeholder':'输入密码','lay-verify':'required|password','id':'password'}),show_hidden_initial=True)
#     def clean_username(self):
#         if len(self.cleaned_data['username'])==11:
#             return  self.cleaned_data['username']
#         else:
#             raise ValidationError('输入用户手机号')



#不能用is_vaild
class loginmodelform(forms.ModelForm):
    class Meta:
        model=User
        fields=('username','password')
        labels={
            'username':'请输入手机号',
            'password':'请输入密码',
        }
        error_messages={
            '__all__':{'required':'请输入内容',
                       'invalid':'检查输入内容'},
        }
        widgets={
            'username':forms.TextInput(attrs={'class':'layui-input','placeholder':'输入手机号','lay-verify':'required|phone','id':'username'}),
            'password':forms.TextInput(attrs={'type':'password','class':'layui-input','placeholder':'输入密码','lay-verify':'required|password','id':'password'}),
        }

    def clean_username(self):
        if len(self.cleaned_data['username']) == 11:
            return self.cleaned_data['username']
        else:
            raise ValidationError('输入用户手机号')

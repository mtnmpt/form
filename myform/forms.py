from django import forms

class MyForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")  # ✅ Lấy giá trị nhập từ form
        print(username)
        if len(username) < 2:  # ✅ So sánh đúng kiểu dữ liệu
            raise forms.ValidationError("Lỗi: Username không được là '1'")  # ✅ Dùng ValidationError
        return username  # ✅ Phải return giá trị sau khi kiểm tra

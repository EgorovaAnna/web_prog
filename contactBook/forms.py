from django import forms

class ContactForm(forms.Form):
	surname = forms.CharField(label = 'surname', max_length = 30)
	name = forms.CharField(label = 'name', max_length = 30)
	patronymic = forms.CharField(label = 'patronymic', max_length = 30)
	CHOICE = (('M', 'man'), ('W', 'woman'))
	gender = forms.ChoiceField(label = 'gender', choices = CHOICE, required = False)
	birthday = forms.DateField(label = 'birthday', required = False)
	job = forms.CharField(label = 'job', required = False, max_length = 30)
	post = forms.CharField(label = 'post', required = False, max_length = 30)
	telephone = forms.CharField(label = 'telephone', max_length = 30)
	email = forms.EmailField(label = 'E-mail', required = False)
	city = forms.CharField(label = 'city', required = False)
	street = forms.CharField(label = 'street', required = False)
	building = forms.CharField(label = 'building', max_length = 5, required = False)
	apartment = forms.IntegerField(label = 'apartment', required = False)
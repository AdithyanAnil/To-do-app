from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from.models import Create
class CreateForm(ModelForm):
    
    class Meta:
        model =Create
        fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super(Create, self).__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))
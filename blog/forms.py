from django import forms
from .models import Code
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class CodeForm(forms.ModelForm):
  class Meta:
    model = Code
    fields = ('title', 'content',)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.layout = Layout(
      Row(
        Column('title', css_class='form-group col-md-6 mb-0'),
        css_class='form-row'
      ),
      Row(
        Column('content', css_class='form-group col-md-6 mb-0'),
        css_class='form-row'
      ),
      Submit('submit', 'Save')
    )

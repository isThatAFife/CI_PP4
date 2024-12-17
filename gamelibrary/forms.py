from .models import Comment, Game
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ["name", "metascore", "console", "userscore", "date", "cover_url"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "name",
            "metascore",
            "console",
            "userscore",
            "date",
            "cover_url",
            Submit("submit", "Save Game", css_class="btn btn-primary"),
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)

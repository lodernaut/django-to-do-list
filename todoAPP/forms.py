from typing import Any

from django import forms

from todoAPP.models import ToDoItem


class CustomDateTimeInput(forms.DateTimeInput):
    input_type = "text"

    def __init__(self, *args, **kwargs):
        kwargs["format"] = "%d/%m/%Y - %H:%M"
        super().__init__(*args, **kwargs)

    def format_value(self, value):
        if value is None:
            return ""
        return value.strftime("%d/%m/%Y - %H:%M")


class ToDoItemForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = [
            "title",
            "description",
            "due_date",
            "todo_list",
        ]

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "css-class-edit",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "css-class-edit",
                }
            ),
            "created_date": forms.DateTimeInput(
                attrs={
                    "class": "css-class-edit",
                    "type": "datetime-local",
                }
            ),
            "due_date": CustomDateTimeInput(
                attrs={
                    "class": "css-class-edit",
                    "type": "datetime-local",
                }
            ),
            "todo_list": forms.Select(
                attrs={
                    "class": "css-class-edit",
                }
            ),
        }

    def clean(self, *args, **kwargs):
        return super().clean()

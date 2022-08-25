from dataclasses import field
from django import forms
from .models import Room, Message


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('body',)

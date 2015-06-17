
from django import forms
from django.forms import ModelForm
from question.models import Question, Reply, ReplyList, Tag, UserTag, QuestionTag
from accounts.models import User, UserProfile

class CustomChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        """
        タグ名をプルダウンリストに表示をするために、このメソッドをオーバーライドする。
        """
        return obj.name

class CustomMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        """
        タグ名をプルダウンリストに表示をするために、このメソッドをオーバーライドする。
        """
        return obj.name

class QuestionEditForm(ModelForm):
    """
    質問フォーム
    """
    # タグを一つのみ選ばせる場合
    #tag = CustomChoiceField(label='タグ', queryset=Tag.objects.all(), required=False,
    #                             to_field_name='name')
    # タグを複数選ばせる場合
    tag = CustomMultipleChoiceField(label='タグ', queryset=Tag.objects.all(), required=False)
    tag_added = forms.CharField(label='追加タグ', max_length=512, required=False)

    class Meta:
        model = Question
        fields = ('destination_div', 'title', 'date', 'time_limit', 'text', 'draft')
        widgets = {
          'title': forms.TextInput(attrs={'size': '100'}),
          'text': forms.Textarea(attrs={'rows':20, 'cols':100}),
        }

class ReplyEditForm(ModelForm):
    """
    回答フォーム
    """
    class Meta:
        model = Reply
        fields = ('date', 'text', 'draft')
        widgets = {
          'text': forms.Textarea(attrs={'rows':20, 'cols':100}),
        }

class UserProfileEditForm(ModelForm):
    """
    ユーザプロファイル編集フォーム
    """

    # タグを一つのみ選ばせる場合
    #tag = CustomChoiceField(label='タグ', queryset=Tag.objects.all(), required=False,
    #                             to_field_name='name')
    # タグを複数選ばせる場合
    tag = CustomMultipleChoiceField(label='タグ', queryset=Tag.objects.all(), required=False)
    tag_added = forms.CharField(label='追加タグ', max_length=512, required=False)

    class Meta:
        model = UserProfile
        fields = ('user', 'work_place', 'work_status', 'division', 'accept_question')
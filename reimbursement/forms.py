from django import forms
from django.conf import settings
from django.forms import ModelForm
from django.template.defaultfilters import filesizeformat

from app.mixins import BootstrapFormMixin
from reimbursement.models import Reimbursement, check_friend_emails


class ReceiptSubmissionReceipt(BootstrapFormMixin, ModelForm):
    bootstrap_field_info = {
        'Upload your receipt': {
            'fields': [{'name': 'receipt', 'space': 12}, {'name': 'multiple_hackers', 'space': 12},
                       {'name': 'friend_emails', 'space': 12}, ],
        },
        'Where should we send you the monies?': {
            'fields': [{'name': 'paypal_email', 'space': 12}, ],
        },
        'Where are you joining us from?': {
            'fields': [{'name': 'origin', 'space': 12}, ],
        }
    }

    def __init__(self, *args, **kwargs):
        super(ReceiptSubmissionReceipt, self).__init__(*args, **kwargs)
        self.fields['receipt'].required = True

    def clean_friend_emails(self):
        multipl_hacks = self.cleaned_data.get('friend_emails', '')
        if multipl_hacks:
            try:
                check_friend_emails(multipl_hacks, self.instance.hacker.email)
            except Exception as e:
                raise forms.ValidationError(str(e))
        return multipl_hacks

    def clean_paypal_email(self):
        paypal = self.cleaned_data.get('paypal_email', '')
        if not paypal:
            raise forms.ValidationError("Please add PayPal so we can send you reimbursement")
        return paypal

    def clean_receipt(self):
        receipt = self.cleaned_data['receipt']
        size = getattr(receipt, '_size', 0)
        if size > settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError("Please keep resume under %s. Current filesize %s" % (
                filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(size)))
        return receipt

    def save(self, commit=True):
        reimb = super(ReceiptSubmissionReceipt, self).save(commit=False)
        reimb.submit_receipt()
        if commit:
            reimb.save()
        return reimb

    class Meta:
        model = Reimbursement
        fields = (
            'paypal_email', 'receipt', 'multiple_hackers', 'friend_emails', 'origin',)
        widgets = {
            'origin': forms.TextInput(attrs={'autocomplete': 'off'}),
        }

        labels = {
            'multiple_hackers': 'This receipt covers multiple hackers',
            'friend_emails': 'Hackers emails',
            'paypal_email': 'PayPal email'
        }

        help_texts = {
            'friend_emails': 'Comma separated, use emails your friends used to register'
        }


class RejectReceiptForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RejectReceiptForm, self).__init__(*args, **kwargs)
        self.fields['public_comment'].required = True

    class Meta:
        model = Reimbursement
        fields = (
            'public_comment',
        )
        labels = {
            'public_comment': 'Why is this receipt being rejected?'
        }


class AcceptReceiptForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(AcceptReceiptForm, self).__init__(*args, **kwargs)
        self.fields['reimbursement_money'].required = True

    class Meta:
        model = Reimbursement
        fields = (
            'reimbursement_money', 'origin',)
        labels = {
            'reimbursement_money': 'Total cost in receipt'
        }

        widgets = {
            'origin': forms.TextInput(attrs={'autocomplete': 'off'}),
        }


class EditReimbursementForm(ModelForm):
    def __getitem__(self, item):
        item = super(EditReimbursementForm, self).__getitem__(item)
        # Hide reimbursement money if it has not been approved yet!
        if not self.instance.is_accepted() and item.name == 'reimbursement_money':
            item.field.widget = forms.HiddenInput()
        else:
            item.field.required = True
        return item

    class Meta:
        model = Reimbursement
        fields = ('reimbursement_money', 'expiration_time',)
        labels = {
            'reimbursement_money': 'Amount to be reimbursed',
            'expiration_time': 'When is the reimbursement expiring?'
        }

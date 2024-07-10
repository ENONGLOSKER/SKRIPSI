from django import forms
from .models import CustomUser, Alternatif, Kriteria, SubKriteria, Bobot, Jadwal, AbstractUser, Penilaian

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'jk', 'alamat', 'nim','prodi','semester','nomor_hp']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
# Perbaikan pada form AlternatifForm berdasarkan model Alternatif


class JadwalForm(forms.ModelForm):
    class Meta:
        model = Jadwal
        fields = ['tanggal', 'waktu','link_tes','status']

        widgets = {
            'tanggal': forms.DateInput(attrs={'class': 'form-control','type':'date'}),
            'waktu': forms.TimeInput(attrs={'class': 'form-control','type':'time'}),
            'link_tes': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'jk', 'alamat', 'nim','prodi','semester','nomor_hp']


        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type':'email'}),
            'jk': forms.Select(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], attrs={'class': 'form-control'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control'}),
            'nim': forms.NumberInput(attrs={'class': 'form-control','type':'number'}),
            'prodi': forms.Select(choices=[('Teknik Informatika', 'Teknik Informatika'), ('Sistem Informasi', 'Sistem Informasi')], attrs={'class': 'form-control'}),
            'semester': forms.TextInput(attrs={'class': 'form-control'}),
            'nomor_hp': forms.NumberInput(attrs={'class': 'form-control','type':'number'}),
        }
        
class AlternatifForm(forms.ModelForm):
    class Meta:
        model = Alternatif
        fields = ['simbol', 'nama']

        widgets = {
            'nama': forms.Select(attrs={'class': 'form-control'}),
            'simbol': forms.TextInput(attrs={'class': 'form-control'}),
        }

class KriteriaForm(forms.ModelForm):
    class Meta:
        model = Kriteria
        fields = ['nama', 'gap','factor','persentase']

        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'gap': forms.TextInput(attrs={'class': 'form-control'}),
            'factor': forms.TextInput(attrs={'class': 'form-control'}),
            'persentase': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SubKriteriaForm(forms.ModelForm):
    class Meta:
        model = SubKriteria
        fields = ['kriteria', 'nama_sub','nilai']

        widgets = {
            'kriteria': forms.Select(attrs={'class': 'form-control'}),
            'nama_sub': forms.TextInput(attrs={'class': 'form-control'}),
            'nilai': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BobotForm(forms.ModelForm):
    class Meta:
        model = Bobot
        fields = "__all__"

        widgets = {
            'selisih': forms.TextInput(attrs={'class': 'form-control'}),
            'bobot': forms.TextInput(attrs={'class': 'form-control'}),
            'nilai': forms.TextInput(attrs={'class': 'form-control'}),
            'keterangan': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PenilaianForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PenilaianForm, self).__init__(*args, **kwargs)
        
        if Kriteria.objects.count() >= 1:
            self.fields['kriteria1'].queryset = SubKriteria.objects.filter(kriteria=Kriteria.objects.all()[0])
        if Kriteria.objects.count() >= 2:
            self.fields['kriteria2'].queryset = SubKriteria.objects.filter(kriteria=Kriteria.objects.all()[1])
        if Kriteria.objects.count() >= 3:
            self.fields['kriteria3'].queryset = SubKriteria.objects.filter(kriteria=Kriteria.objects.all()[2])
        if Kriteria.objects.count() >= 4:
            self.fields['kriteria4'].queryset = SubKriteria.objects.filter(kriteria=Kriteria.objects.all()[3])

        self.fields['kriteria1'].label_from_instance = lambda obj: f"{obj.kriteria.nama} | {obj.nama_sub}"
        self.fields['kriteria2'].label_from_instance = lambda obj: f"{obj.kriteria.nama} | {obj.nama_sub}"
        self.fields['kriteria3'].label_from_instance = lambda obj: f"{obj.kriteria.nama} | {obj.nama_sub}"
        self.fields['kriteria4'].label_from_instance = lambda obj: f"{obj.kriteria.nama} | {obj.nama_sub}"

    class Meta:
        model = Penilaian
        fields = "__all__"

        widgets = {
            'alternatif': forms.Select(attrs={'class': 'form-control'}),
            'kriteria1': forms.Select(attrs={'class': 'form-control'}),
            'kriteria2': forms.Select(attrs={'class': 'form-control'}),
            'kriteria3': forms.Select(attrs={'class': 'form-control'}),
            'kriteria4': forms.Select(attrs={'class': 'form-control'}),
        }


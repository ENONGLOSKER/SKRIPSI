from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

from .models import CustomUser, Jadwal, Alternatif, Kriteria, SubKriteria, Bobot, Penilaian, PenilaianGap, PenilaianRangking, PenilaianHasil
from .forms import CustomUserCreationForm, AlternatifForm, KriteriaForm, SubKriteriaForm, BobotForm, PenilaianForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

# USER -----------------------------------
@login_required
def detail_user(request):
    user = request.user
    jadwal = Jadwal.objects.all()

    try:
        alternatif = Alternatif.objects.get(nama=user)
        nilai = PenilaianHasil.objects.get(alternatif=alternatif)
    except ObjectDoesNotExist:
        nilai = None

    context = {
        'user': user, 
        'jadwal': jadwal,
        'nilai': nilai
    }
    return render(request, 'detail_user.html', context)

@login_required
def dashboard_admin(request):
    jumlah_user = CustomUser.objects.count()
    jumlah_alternatif = Alternatif.objects.count()
    jumlah_kriteria = Kriteria.objects.count()
    jumlah_subkriteria = SubKriteria.objects.count()
    jumlah_bobot = Bobot.objects.count()
    persentase_penilaian = (jumlah_user / jumlah_alternatif)

    penilaianhasil_list = PenilaianHasil.objects.all().order_by('alternatif__simbol')

    context = {
        'jumlah_user': jumlah_user,
        'jumlah_alternatif': jumlah_alternatif,
        'jumlah_kriteria': jumlah_kriteria,
        'jumlah_subkriteria': jumlah_subkriteria,
        'jumlah_bobot': jumlah_bobot,
        'persentase_penilaian': persentase_penilaian,
        'penilaianhasil_list': penilaianhasil_list,
        'alternatif_list': Alternatif.objects.all()  # tambahkan ini untuk nama alternatif di x-axis
    }

    return render(request, 'dashboard.html', context)


# ALTERNATIF
@login_required
def dashboard_alternatif(request):
    # Mengambil data Alternatif dengan menghubungkan ke CustomUser
    data_alternatif = Alternatif.objects.all().select_related('nama')

    # Pencarian
    cari = request.GET.get('cari')
    if cari:
        data_alternatif = data_alternatif.filter(nama__username__icontains=cari)

    # Pagination
    paginator = Paginator(data_alternatif, 5)  # Tampilkan 1 item per halaman
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'datas': page_obj,
        'cari': cari,
    }
    return render(request, 'dashboard_alternatif.html', context)
@login_required
def tambah_alternatif(request):
    if request.method == 'POST':
        form = AlternatifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alternatif')  
    else:
        form = AlternatifForm()
    
    context = {'form': form}
    return render(request, 'dashboard_form.html', context)
@login_required
def edit_alternatif(request, id):
    alternatif = Alternatif.objects.get(id=id)
    
    if request.method == 'POST':
        form = AlternatifForm(request.POST, instance=alternatif)
        if form.is_valid():
            form.save()
            return redirect('alternatif')  
    else:
        form = AlternatifForm(instance=alternatif)
    
    context = {'form': form}
    return render(request, 'dashboard_form.html', context)
@login_required
def hapus_alternatif(request, id):
    alternatif = Alternatif.objects.get(id=id)
    alternatif.delete()
    return redirect('alternatif')

# KRITERIA
@login_required
def dashboard_kriteria(request):
    data_kriteria = Kriteria.objects.all()
    cari = request.GET.get('cari')
    if cari:
        data_kriteria = data_kriteria.filter(nama__icontains=cari)
    paginator = Paginator(data_kriteria,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'datas':page_obj,
        'cari':cari,
    }
    return render(request, 'dashboard_kriteria.html', context)
@login_required
def tambah_kriteria(request):
    if request.method == 'POST':
        form = KriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kriteria')  
    else:
        form = KriteriaForm()
    
    context = {'form': form}
    return render(request, 'dashboard_form.html', context)
@login_required
def edit_kriteria(request, id):
    kriteria = Kriteria.objects.get(id=id)
    
    if request.method == 'POST':
        form = KriteriaForm(request.POST, instance=kriteria)
        if form.is_valid():
            form.save()
            return redirect('kriteria')  
    else:
        form = KriteriaForm(instance=kriteria)
    
    context = {'form': form}
    return render(request, 'dashboard_form.html', context)
@login_required
def hapus_kriteria(request, id):
    kriteria = Kriteria.objects.get(id=id)
    kriteria.delete()
    return redirect('kriteria')

# SUB KRITERIA
@login_required
def dashboard_subkriteria(request, id):
    kriteria =  get_object_or_404(Kriteria, id=id)
    data_sub_kriteria = kriteria.subkriteria.all()

    cari = request.GET.get('cari')
    if cari:
        data_sub_kriteria = data_sub_kriteria.filter(nilai__icontains=cari)

    paginator = Paginator(data_sub_kriteria,4)
    page_number =request.GET.get('page')
    page_obj =paginator.get_page(page_number)

    context = {
        'kriteria':kriteria,
        'datas': page_obj,
        'cari':cari,
    }
    return render(request, 'dashboard_subkriteria.html', context)
@login_required
def tambah_subkriteria(request):
    if request.method == 'POST':
        form = SubKriteriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kriteria')  
    else:
        form = SubKriteriaForm()
    
    context = {'form': form}
    return render(request, 'dashboard_form.html', context)
@login_required
def edit_subkriteria(request, id):
    sub_kriteria = SubKriteria.objects.get(id=id)
    
    if request.method == 'POST':
        form = SubKriteriaForm(request.POST, instance=sub_kriteria)
        if form.is_valid():
            form.save()
            return redirect('kriteria')  
    else:
        form = SubKriteriaForm(instance=sub_kriteria)
    
    context = {'form': form}
    return render(request, 'dashboard_form.html', context)
@login_required
def hapus_subkriteria(request, id):
    sub_kriteria = SubKriteria.objects.get(id=id)
    sub_kriteria.delete()
    return redirect('kriteria')

# BOBOT
@login_required
def dashboard_bobot(request):
    data_bobot = Bobot.objects.all()
    context = {
        'datas':data_bobot,
    }
    return render(request, 'dashboard_bobot.html', context)
@login_required
def tambah_bobot(request):
    if request.method == 'POST':
        form = BobotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bobot')  
    else:
        form = BobotForm()
    
    context = {'form': form}
    return render(request, 'dashboard_form.html', context)
@login_required
def edit_bobot(request, id):
    bobot = Bobot.objects.get(id=id)
    
    if request.method == 'POST':
        form = BobotForm(request.POST, instance=bobot)
        if form.is_valid():
            form.save()
            return redirect('bobot')  
    else:
        form = BobotForm(instance=bobot)
    
    context = {'form': form}
    return render(request, 'dashboard_form.html', context)
@login_required
def hapus_bobot(request, id):
    bobot = Bobot.objects.get(id=id)
    bobot.delete()
    return redirect('bobot')

# PENILAIAN
@login_required
def dashboard_penilaian(request):
    datas = Penilaian.objects.all()
    penilaian_gap = PenilaianGap.objects.all()
    penilaian_rengking = PenilaianRangking.objects.all()
    penilaian_hasil = PenilaianHasil.objects.all()
    # Mengambil data GAP dari model Kriteria
    gap_kriteria = Kriteria.objects.all()

    context={
        'datas':datas,
        'gap_kriteria': gap_kriteria,
        'penilaian_gap': penilaian_gap,
        'penilaian_rengking': penilaian_rengking,
        'penilaian_hasil': penilaian_hasil,
    }

    return render(request, 'dashboard_penilaian.html', context)
@login_required
def tambah_penilaian(request):
    if request.method == 'POST':
        form = PenilaianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('penilaian')  
    else:
        form = PenilaianForm()
    
    context = {'form': form}
    return render(request, 'dashboard_form_penilaian.html', context)
@login_required
def edit_penilaian(request, id):
    penilaian = Penilaian.objects.get(id=id)
    
    if request.method == 'POST':
        form = PenilaianForm(request.POST, instance=penilaian)
        if form.is_valid():
            form.save()
            return redirect('penilaian')  
    else:
        form = PenilaianForm(instance=penilaian)
    
    context = {'form': form}
    return render(request, 'dashboard_form.html', context)
@login_required
def hapus_penilaian(request, id):
    penilaian = Penilaian.objects.get(id=id)
    penilaian.delete()
    return redirect('penilaian')

#PERENGKINGAN
def dashboard_rengking(request):
    datas = PenilaianHasil.objects.all().order_by('-hasil')
    context ={
        'penilaian_hasil':datas
    }
    return render(request, 'dashboard_perengkingan.html', context)

# penilaian ------------------------------
def penilaian_gap(request):
    if request.method == 'POST':
        # Ambil semua objek Penilaian
        penilaian_list = Penilaian.objects.all()

        # Loop melalui setiap objek Penilaian
        for penilaian in penilaian_list:
            gap_kriteria = PenilaianGap(
                alternatif=penilaian.alternatif,
                kriteria1=penilaian.kriteria1.nilai - penilaian.kriteria1.kriteria.gap,
                kriteria2=penilaian.kriteria2.nilai - penilaian.kriteria2.kriteria.gap,
                kriteria3=penilaian.kriteria3.nilai - penilaian.kriteria3.kriteria.gap,
                kriteria4=penilaian.kriteria4.nilai - penilaian.kriteria4.kriteria.gap
            )
            gap_kriteria.save()
        return redirect('penilaian')

    return render(request, 'dashboard_penilaian.html') 

def hitung_rengking(request):
# Ambil semua objek PenilaianGap
    penilaian_gap_list = PenilaianGap.objects.all()

    # Loop melalui setiap objek PenilaianGap
    for penilaian_gap in penilaian_gap_list:
        # Inisialisasi nilai awal untuk setiap kriteria
        nilai_kriteria1 = 0
        nilai_kriteria2 = 0
        nilai_kriteria3 = 0
        nilai_kriteria4 = 0

        # Cek bobot untuk kriteria pertama
        bobot_pertama = Bobot.objects.filter(bobot=penilaian_gap.kriteria1).first()
        if bobot_pertama:
            nilai_kriteria1 = bobot_pertama.nilai

        # Cek bobot untuk kriteria kedua
        bobot_kedua = Bobot.objects.filter(bobot=penilaian_gap.kriteria2).first()
        if bobot_kedua:
            nilai_kriteria2 = bobot_kedua.nilai

        # Cek bobot untuk kriteria ketiga
        bobot_ketiga = Bobot.objects.filter(bobot=penilaian_gap.kriteria3).first()
        if bobot_ketiga:
            nilai_kriteria3 = bobot_ketiga.nilai

        # Cek bobot untuk kriteria keempat
        bobot_keempat = Bobot.objects.filter(bobot=penilaian_gap.kriteria4).first()
        if bobot_keempat:
            nilai_kriteria4 = bobot_keempat.nilai

        # Simpan hasil konversi ke tabel PenilaianRangking
        rangking = PenilaianRangking(
            alternatif=penilaian_gap.alternatif,
            kriteria1=nilai_kriteria1,
            kriteria2=nilai_kriteria2,
            kriteria3=nilai_kriteria3,
            kriteria4=nilai_kriteria4
        )
        rangking.save()
    return redirect('penilaian')

def hitung_hasil(request):
    if request.method == 'POST':
       # Hitung jumlah kriteria berdasarkan factor
        kriteria_cf = len(Kriteria.objects.filter(factor='CF'))
        kriteria_sf = len(Kriteria.objects.filter(factor='SF'))

        # Ambil semua alternatif berdasarkan data pada PenilaianRangking
        alternatif_list = PenilaianRangking.objects.values_list('alternatif', flat=True).distinct()

        for alternatif_id in alternatif_list:
            alternatif = Alternatif.objects.get(id=alternatif_id)
            
            # Inisialisasi total nilai untuk setiap factor
            total_nilai_cf = 0
            total_nilai_sf = 0
            
            # Ambil data penilaian untuk alternatif saat ini
            penilaian = PenilaianRangking.objects.filter(alternatif=alternatif).first()

            if penilaian:
                # Cek dan jumlahkan nilai kriteria berdasarkan factor
                kriteria_list = [penilaian.kriteria1, penilaian.kriteria2, penilaian.kriteria3, penilaian.kriteria4]
                for idx, nilai in enumerate(kriteria_list, start=1):
                    kriteria = Kriteria.objects.get(pk=idx)
                    if kriteria.factor == 'CF':
                        total_nilai_cf += nilai
                    elif kriteria.factor == 'SF':
                        total_nilai_sf += nilai

            # Hitung nilai rata-rata berdasarkan factor
            ncf = total_nilai_cf / kriteria_cf if kriteria_cf else 0
            nsf = total_nilai_sf / kriteria_sf if kriteria_sf else 0

            # Hitung nilai 'hasil' berdasarkan persentase CF dan SF
            kriteria_cf_obj = Kriteria.objects.filter(factor='CF').first()
            kriteria_sf_obj = Kriteria.objects.filter(factor='SF').first()
            
            hasil_value = (kriteria_cf_obj.persentase * ncf) + (kriteria_sf_obj.persentase * nsf)


           # Simpan atau update hasil konversi ke tabel PenilaianHasil
            hasil, created = PenilaianHasil.objects.get_or_create(
                alternatif=alternatif,
                defaults={'ncf': ncf, 'nsf': nsf, 'hasil': hasil_value}
            )

            if not created:
                hasil.ncf = ncf
                hasil.nsf = nsf
                hasil.hasil = hasil_value
                hasil.save()

        return redirect('penilaian')

# reset penilaian
def penilaian_gap_reset(request):
    PenilaianGap.objects.all().delete()
    return redirect('penilaian')

def penilaian_rengking_reset(request):
    PenilaianRangking.objects.all().delete()
    return redirect('penilaian')

def penilaian_hasil_reset(request):
    PenilaianHasil.objects.all().delete()
    return redirect('penilaian')


# AUTH ----------------------------------
def signout_user(request):
    logout(request)
    return redirect('index')

def singin_user(request):
    if request.method == 'POST':
        username = request.POST.get('username').replace(' ', '_')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Sign in Berhasil, Selamat Datang {user.username}!")
            if user.is_superuser:
                # return redirect('admin:index')
                return redirect('dashboard')
            else:
                return redirect('detail')
        else:
            messages.error(request, "Sign in Gagal, Silahkan Coba Kembali!")
            return render(request, 'signin.html')
    elif request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('dashboard')
        else:
            return redirect('detail')
    else:
        return render(request, 'signin.html')

def create_custom_user(request):
    if request.method == 'POST':
        username = request.POST.get('username').replace(' ', '_')
        nim = request.POST.get('nim')
        prodi = request.POST.get('prodi')
        semester = request.POST.get('semester')
        alamat = request.POST.get('alamat')
        jk = request.POST.get('jk')
        nomor_hp = request.POST.get('nomor_hp')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Password tidak sama!")
            return redirect('signup')
        
        else:
            my_user = CustomUser.objects.create_user(username=username, email=email, password=password1, nim=nim, prodi=prodi, semester=semester, alamat=alamat, jk=jk, nomor_hp=nomor_hp)

            # Menambahkan pengguna ke grup 'anggota' atau mendapatkan grup jika belum ada
            group, created = Group.objects.get_or_create(name='anggota')
            my_user.groups.add(group)

            my_user.save()
            messages.success(request, "Selamat, Register Berhasil!")
            return redirect('signin')
    else:
        form = CustomUserCreationForm()  # Display an empty form for GET requests

    return render(request, 'signup.html', {'form': form})
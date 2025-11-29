from django.shortcuts import render, get_object_or_404, redirect
from .models import University, Group, Student
from .forms import StudentForm

def universities_list(request):
    # Avtomatik 3 ta universitet qo'shish (agar yo'q bo'lsa)
    if University.objects.count() == 0:
        University.objects.create(
            name="Buxoro Davlat Universiteti",
            description="Buxoro shahridagi yetakchi universitet",
            image="universities/buxoro.jpg"
        )
        University.objects.create(
            name="TATU",
            description="Toshkent Axborot Texnologiyalari Universiteti",
            image="universities/tatu.jpg"
        )
        University.objects.create(
            name="Toshkent Davlat Milliy Universiteti",
            description="Toshkentdagi nufuzli universitet",
            image="universities/tdmu.jpg"
        )

    universities = University.objects.all()
    return render(request, 'universities_list.html', {'universities': universities})

def groups_list(request, university_id):
    university = get_object_or_404(University, id=university_id)

    # Agar guruhlar yo'q bo'lsa, 3 ta avtomatik qo'shamiz
    if university.groups.count() == 0:
        Group.objects.create(university=university, name="1-guruh")
        Group.objects.create(university=university, name="2-guruh")
        Group.objects.create(university=university, name="3-guruh")

    groups = university.groups.all()
    return render(request, 'group_list.html', {'university': university, 'groups': groups})

def students_list(request, group_id):
    group = get_object_or_404(Group, id=group_id)


    if group.students.count() == 0:
        auto_students = [
            ("Ali", "Valiyev"),
            ("Zara", "Karimova"),
            ("Jasur", "Toshmatov"),
            ("Diyor", "Sodiqov"),
            ("Nilufar", "Qodirova"),
            ("Bekzod", "Xolboyev"),
            ("Madina", "Rasulova"),
            ("Sardor", "Eshmatov"),
            ("Laylo", "Abdullayeva"),
            ("Jahon", "Yoqubov")
        ]

        for first_name, last_name in auto_students:
            Student.objects.create(group=group, first_name=first_name, last_name=last_name)

    students = Student.objects.filter(group=group)

    return render(request, 'students_list.html', {
        'group': group,
        'students': students
    })


def add_student(request, group_id):
    group = get_object_or_404(Group, id=group_id)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.group = group
            # Agar rasm yuklanmagan bo'lsa, default rasm bilan ishlash
            if not student.photo:
                from django.core.files.base import ContentFile
                from django.templatetags.static import static
                import os
                default_path = os.path.join('static', 'default_student.jpg')
                student.photo.save('default_student.jpg', ContentFile(open(default_path, 'rb').read()), save=False)
            student.save()
            return redirect('students_list', group_id=group.id)
        else:
            print(form.errors)  # form valid bo'lmasa xatolarni konsolga chiqaradi
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form, 'group': group})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    group_id = student.group.id
    student.delete()
    return redirect('students_list', group_id=group_id)

from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Bagas",
        "npm": "2506656551",
        "study_program": "S1 Sistem Informasi, University of Indonesia",
        "bio": (
            "A student of Information Systems at the University of Indonesia " 
            "with a strong passion for graphic design and social media. "
            "I am a creative, proactive individual with a high level of adaptability. "
            "My experience as a Creative Division Volunteer at a school art performance event " 
            "has trained me in project management, teamwork, and effective communication, "
            "while also honing my skills in using design tools such as Canva, Adobe Photoshop, "
            "Marvelous Designer, Figma, and Procreate. I am enthusiastic about continuing "
            "to learn and make a meaningful contribution within the campus environment."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Bagas",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)
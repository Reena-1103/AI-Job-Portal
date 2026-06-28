from django.shortcuts import render, redirect
from .models import Register, Job, ApplyJob, Recommendation

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def home(request):
    return render(request, 'index.html')


def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:

            user = Register.objects.get(email=email)

            if user.password == password:

                request.session["full_name"] = user.full_name
                request.session["email"] = user.email

                return redirect("/")

            else:

                return render(request, "login.html", {
                    "error": "Invalid Password"
                })

        except Register.DoesNotExist:

            return render(request, "login.html", {
                "error": "Email does not exist"
            })

    return render(request, "login.html")


def register(request):

    if request.method == "POST":

        fullname = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if Register.objects.filter(email=email).exists():

            return render(request, "register.html", {
                "error": "Email already exists"
            })

        if password == confirm_password:

            register = Register(
                full_name=fullname,
                email=email,
                password=password
            )

            register.save()

            return render(request, "login.html")

        else:

            return render(request, "register.html", {
                "error": "Passwords do not match"
            })

    return render(request, "register.html")


def jobs(request):

    search = request.GET.get("search")

    if search:

        jobs = Job.objects.filter(job_title__icontains=search)

    else:

        jobs = Job.objects.all()

    return render(request, "jobs.html", {
        "jobs": jobs
    })


def apply_job(request, job_id):

    job = Job.objects.get(id=job_id)

    full_name = request.session.get("full_name")
    email = request.session.get("email")

    ApplyJob.objects.create(
        full_name=full_name,
        email=email,
        job_title=job.job_title,
        company=job.company
    )

    return redirect("/jobs/")


def my_applications(request):

    if "email" not in request.session:
        return redirect("/login/")

    email = request.session.get("email")

    applications = ApplyJob.objects.filter(email=email)

    return render(request, "my_applications.html", {
        "applications": applications
    })

def dashboard(request):

    if "email" not in request.session:
        return redirect("/login/")

    full_name = request.session.get("full_name")
    email = request.session.get("email")

    total_applications = ApplyJob.objects.filter(email=email).count()

    return render(request, "dashboard.html", {
        "full_name": full_name,
        "email": email,
        "total_applications": total_applications
    })

def recommendation(request):

    if "email" not in request.session:
        return redirect("/login/")

    if request.method == "POST":

        skills = request.POST.get("skills")

        full_name = request.session.get("full_name")
        email = request.session.get("email")

        skills_lower = skills.lower()

        if "python" in skills_lower:
            job = "Python Developer"

        elif "machine learning" in skills_lower:
            job = "AI Engineer"

        elif "sql" in skills_lower:
            job = "Data Analyst"

        else:
            job = "Software Developer"

        Recommendation.objects.create(
            full_name=full_name,
            email=email,
            skills=skills,
            recommended_job=job
        )

        return render(request, "recommendation.html", {
            "job": job
        })

    return render(request, "recommendation.html")

def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def logout(request):

    request.session.flush()

    return redirect("/login/")
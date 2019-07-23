from backend.users.models import UserProfile, Organization
from django.contrib.auth.models import User


def create_user(username,
                password='12345',
                cname='无名氏',
                ename='Unknown',
                company_id='12345',
                position='tester',
                email='unknown@bysoft.com',
                phone='110',
                department='test centre',
                org='beijing'
                ):
    u = User.objects.create_user(username=username, password=password, email=email)
    p = UserProfile(
        chinese_name=cname,
        english_name=ename,
        company_id=company_id,
        position=position,
        email=email,
        phone=phone,
        department=department,
        organization=Organization.objects.get(name=org),
        user=u
    )
    p.save()


def create_org(name='beijing'):
    from backend.users.models import Organization
    org = Organization(name=name)
    org.save()


def create_orgs():
    create_org('beijing')
    create_org('chengdu')
    create_org('guangzhou')
    create_org('shanghai')
    create_org('wuhan')
import random 

from django.contrib.auth.models import User
from faker import Faker

#from backend.users.models import UserProfile, Organization
from ..users.models import UserProfile, Organization




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

def create_faker_user(num=1):
    fc = Faker(locale='zh_CN')
    fe = Faker()
    profiles = UserProfile.objects.all()
    company_ids = [p.company_id for p in profiles]
    for _ in range(num):
        first_eng_name = fe.first_name()
        last_eng_name = fe.last_name()
        full_eng_name = ' '.join((first_eng_name, last_eng_name))
        email = '_'.join((first_eng_name, last_eng_name)) + '@bysoft.com'
        password = '12345'
        gender = random.choice(('male', 'female'))
        dep = ['ISV', 'Test Centre', 'Admin', 'HR']
        orgs = Organization.objects.order_by('name')[:]
        org = orgs[random.randint(0,len(orgs) - 1)]
        unique_cid = False
        while not unique_cid:
            company_id = random.randint(0,99999)
            if company_id not in company_ids:
                unique_cid = True
                company_ids.append(company_id)

        u = User.objects.create_user(username='_'.join((first_eng_name, last_eng_name)), password=password, email=email)
        p = UserProfile(
            chinese_name=fc.name(),
            english_name=full_eng_name,
            gender=gender,
            company_id=company_id,
            position=fc.job(),
            email=email,
            phone=fc.phone_number(),
            department=dep[random.randint(0,3)],
            organization=org,
            user=u
        )
        p.save()

def create_org(name='beijing'):
    org = Organization(name=name)
    org.save()

def create_orgs():
    for org in ['Beijing','Chengdu','Shanghai','Boise','San Davis','Guangzhou','Wuhan']:
        create_org(org)

def create_random_org():
    f = Faker()
    org = Organization(name=f.city())
    org.save()
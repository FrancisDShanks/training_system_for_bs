import random
from faker import Faker
from backend.projects.models import (
    Project, Activity, Material
)
from backend.users.models import (
    UserProfile, Organization
)

def create_projects(num=1):
    fc = Faker(locale='zh_CN')
    fe = Faker()
    project_name = fc.sentence()

    orgs = Organization.objects.order_by('name')[:]
    user_profiles = UserProfile.objects.all()
    
    for _ in range(num):
        project_name = fc.sentence()
        org = orgs[random.randint(0,len(orgs) - 1)]
        end_time = fc.future_datetime()
        start_time = fc.date_time_this_year()
        introduction = fc.text()
        cost_budget = fc.pyint()
        cost = fc.random_int()
        price = fc.random_int(max=cost//100)

        project_manager = user_profiles[random.randint(0,len(user_profiles) - 1)]
        project_creator = user_profiles[random.randint(0,len(user_profiles) - 1)]

        p = Project(
            name=project_name,
            start_time=start_time,
            end_time=end_time,
            organization=org,
            location=fc.street_address(),
            introduction=introduction,
            cost_budget=cost_budget,
            cost=cost,
            price=price,
            project_manager=project_manager,
            project_creator=project_creator
        )
        p.save()




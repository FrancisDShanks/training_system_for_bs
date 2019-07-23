def create_user(cname='无名氏',
                ename='Unknown',
                CompanyID='12345',
                Position='tester',
                Email='unknown@bysoft.com',
                phone='110',
                Department='test centre',
                Organization=1
                ):
    from backend.users.models import UserProfile
    u = UserProfile(
        ChineseName=cname,
        EnglishName=ename,
        CompanyID=CompanyID,
        Position=Position,
        EMAIL=Email,
        Phone=phone,
        Department=Department,
        organization=Organization
    )
    u.save()


def create_org(name='beijing'):
    from backend.users.models import Organization
    org = Organization(Name=name)
    org.save()

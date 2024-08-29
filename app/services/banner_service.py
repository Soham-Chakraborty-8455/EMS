from ..core_services.banners import banner1, banner2, banner3

def create_banner(template, orgname, eventname, venue, startdate, starttime):
    if template == "1":
        banner1.make_banners1(orgname, eventname, venue, startdate, starttime)
    elif template == "2":
        banner2.make_banners2(orgname, eventname, venue, startdate, starttime)
    elif template == "3":
        banner3.make_banners3(orgname, eventname, venue, startdate, starttime)

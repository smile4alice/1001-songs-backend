from .payment import PaymentAdmin
from .our_team import OurTeamAdmin
from .footer import FooterAdmin
from .education import EducationAdmin
from .about import AboutAdmin
from .location import CountryAdmin, RegionAdmin, CityAdmin

__all__ = [
    EducationAdmin,
    AboutAdmin,
    OurTeamAdmin,
    FooterAdmin,
    PaymentAdmin,
    CountryAdmin,
    RegionAdmin,
    CityAdmin,
]

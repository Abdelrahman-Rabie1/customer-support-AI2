from app.models.home import UniversityOverview

faculties_list_en = [
    "Faculty of Medicine", "Faculty of Dentistry", "Faculty of Physical Therapy", "Faculty of Engineering",
    "Faculty of Applied Health Sciences Technology", "Faculty of Economics and Business Administration",
    "Faculty of Computer Science", "Faculty of Visual Arts", "Faculty of Veterinary Medicine", "Faculty of Energy Sciences"
]

university_info_en = UniversityOverview(
    name="Banha National University",
    description="A non-profit smart university (...) consisting of 10 faculties.",
    image_url="https://bnu.edu.eg/files/26859_1659649382.jpg",
    established="Presidential Decree No. 369 of 2022",
    faculties=faculties_list_en,
    programs_count=25,
    campus="Covers 40 acres with advanced facilities",
    buildings=[
        "Administrative Building", "6 Academic Buildings", "Central Laboratories Building",
        "2 Workshop Buildings", "Recreational Area", "Theater", "Comprehensive Library"
    ],
    vision="Adopts modern educational technologies, competes globally while preserving Egyptian identity."
)
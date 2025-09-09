from typing import Dict
from app.models.colleges import College, Grant

grants_list = [
    Grant(
        title="Excellence Grants",
        details="Full scholarships for top students + discounts (25%, 20%, 15%, 10%) according to rank. Conditions apply."
    ),
    Grant(
        title="Sports Excellence Grants",
        details="Discounts for medal winners: International (70%, 50%, 25%), Arab/African (30%, 20%, 10%)."
    ),
    Grant(
        title="Creative & Research Grants",
        details="Special discounts for distinguished students in research and innovation as approved by the university council."
    ),
    Grant(
        title="Tuition Fee Reductions",
        details="50% for sons of martyrs, 20% for staff children, 10% siblings, disability-based discounts."
    ),
    Grant(
        title="Social Support",
        details="5%–25% tuition fee reduction for students facing sudden financial hardships."
    )
]

general_rules = [
    "Grants and discounts apply only to Egyptian students.",
    "Discounts apply only to tuition fees and not to administrative fees.",
    "Excellence grants apply in the following year.",
    "It is not permissible to combine more than one grant; only the highest applies.",
    "Grants or discounts are not applied retroactively."
]

colleges_data: Dict[str, College] = {
    "medicine": College(
        name="College of Medicine",
        programs=["General Medicine"],
        tuition_fee=155000
    ),
    "dentistry": College(
        name="College of Dentistry",
        programs=["General Dentistry"],
        tuition_fee=125000
    ),
    "physical_therapy": College(
        name="College of Physical Therapy",
        programs=["Physical Therapy"],
        tuition_fee=110000
    ),
    "veterinary": College(
        name="College of Veterinary Medicine",
        programs=["Veterinary Medicine"],
        tuition_fee=80000
    ),
    "engineering": College(
        name="College of Engineering",
        programs=[
            "Engineering of Communication Systems",
            "Mechatronics Engineering",
            "Housing and Community Design",
            "Construction Engineering",
            "Medical Engineering",
            "Manufacturing & Materials Engineering"
        ],
        tuition_fee=75000
    ),
    "computer_science": College(
        name="College of Computer Sciences",
        programs=[
            "Artificial Intelligence & Machine Learning",
            "Computational Linguistics",
            "Data Science",
            "Program Development & Applications",
            "Virtual Reality & Augmented Reality"
        ],
        tuition_fee=75000
    ),
    "visual_arts": College(
        name="College of Visual Arts & Design",
        programs=["Interior design and furniture", "Media and advertising"],
        tuition_fee=60000
    ),
    "business": College(
        name="College of Business and Economics",
        programs=[
            "International Business & Relations Management",
            "International Economics & Finance",
            "Accounting and Business Informatics",
            "Digital Marketing and E-Business",
            "Insurance and statistics"
        ],
        tuition_fee=50000
    ),
    "energy": College(
        name="College of Energy Sciences",
        programs=["Fossil Fuel Energy", "Renewable Energy", "Nuclear Energy"],
        tuition_fee=45000
    ),
}

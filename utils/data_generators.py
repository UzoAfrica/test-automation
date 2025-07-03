from faker import Faker
import random

fake = Faker()

def generate_fake_user():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "department": random.choice(["QA", "DevOps", "IT", "Support"]),
        "title": random.choice(["Engineer", "Analyst", "Manager"])
    }

def generate_fake_ticket():
    return {
        "title": fake.sentence(nb_words=6),
        "description": fake.paragraph(nb_sentences=2),
        "priority": random.choice(["low", "medium", "high"]),
        "category": random.choice(["Bug", "Support", "Security"])
    }

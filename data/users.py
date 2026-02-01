from faker import Faker

faker = Faker()

registered_user = {
    'first_name': 'Joe',
    'last_name': 'Peach',
    'email': faker.email(),
    'company_name': 'test',
    'phone': '555-0199',
    'password': 'test123456',
    'confirm_password': 'test123456'
}

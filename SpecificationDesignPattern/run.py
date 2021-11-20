from user import *

if __name__ == "__main__":
    tim = User()
    jim = User(super_user=True)

    root_specification = UserSpecification().and_(SuperUserSpecification())

    print(root_specification.is_satisfied(tim))
    print(root_specification.is_satisfied(jim))

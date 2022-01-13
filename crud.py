"""CRUD operations."""

from model import db, Participant, Study, Investigator, Result_Plan, connect_to_db

# CREATIONS

def create_participant(email, fname, lname, dob, phone, study_id):
    """Create and return a new user."""

    participant = Participant(email=email, fname=fname, lname=lname, dob=dob, phone=phone, study_id=study_id)

    db.session.add(participant)
    db.session.commit()

    return participant

def create_investigator(fname, lname, phone, email):
    """Create and return a new user."""

    investigator = Investigator(fname=fname, lname=lname, email=email, phone=phone)

    db.session.add(investigator)
    db.session.commit()

    return investigator

def create_study(investigator_id, study_name, investigational_product, status_code):
    """Create and return a new study."""

    study = Study(
        investigator_id=investigator_id,
        study_name=study_name,
        investigational_product=investigational_product,
        status_code=status_code
        )

    db.session.add(study)
    db.session.commit()

    return study

def create_result_plan(study_id, result_category, visit, urgency_potential, return_plan, test_name, return_timing):
    """Create and return a new study."""

    result_plan = Result_Plan(
        study_id=study_id,
        result_category=result_category,
        visit=visit,
        urgency_potential=urgency_potential,
        return_plan=return_plan,
        test_name=test_name,
        return_timing=return_timing
        )

    db.session.add(result_plan)
    db.session.commit()

    return result_plan

# RETURN ALLS

def return_all_studies():
    """Return all studies"""
    return Study.query.all()

def return_all_investigators():
    """Return all studies"""
    return Investigator.query.all()

def return_all_participants():
    """Return all participants"""
    return Participant.query.all()

# GET ITEMS

def get_study_by_id(study_id):
    """Return study based on study id"""

    return Study.query.get(study_id)

def get_participant_by_id(participant_id):
    """Return participant from participant id"""

    return Participant.query.get(participant_id)



# def get_rating_by_movie_by_user(movie, user):
#     """Return a ratings for a movie by a user"""
#     return Rating.query.filter_by(movie=movie, user=user).all()


if __name__ == '__main__':
    from server import app
    connect_to_db(app)
from flask import Blueprint, request, abort, jsonify

from app.auth.helper import token_required
from app.models import UserProfile

profile = Blueprint('profile', __name__)


@profile.route('/profile', methods=['POST'])
@token_required
def create_profile(current_user):
    if request.content_type == 'application/json':
        data = request.get_json()
        emp_id = current_user.id
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        designation = data.get('designation')
        experience = data.get('experience')
        gender = data.get('gender')
        skills = data.get('skills')
        client = data.get('client')
        location = data.get('location')
        address = data.get('address')
        mobile = data.get('mobile')
        image_url = data.get('image_url')
        linked_in = data.get('linked_in')
        github = data.get('github')
        slack = data.get('slack')
        joining_date = data.get('joining_date')
        dob = data.get('dob')

        if emp_id:
            user_profile = UserProfile(emp_id, first_name, last_name, designation, experience, gender, skills, client,
                                       location, address, mobile, image_url, linked_in, github, slack, joining_date,
                                       dob)
        else:
            return {"message": "unprocessible entity"}, 422

        try:
            user_profile.save()
            return {
                       "message": "Profile added successfully"
                   }, 200
        except:
            return {"message": "unable to add profile"}, 500

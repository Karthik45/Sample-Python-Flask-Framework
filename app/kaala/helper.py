from flask import make_response, jsonify
from app.models import LeaveTypes


def response_for_created_leave_type(leave_type, status_code):
    """
    Method returning the response when a Leave_Type has been successfully created.
    :param status_code:
    :param leave_type: Leave_Type
    :return: Http Response
    """
    return make_response(jsonify({
        'status': 'success',
        'id': leave_type.id,
        'leave_type': leave_type.leaveType,
        'description': leave_type.description,
        'num_of_days': leave_type.num_of_days,
        'validity': leave_type.validity
    })), status_code


def response_for_user_leave_type(leaveT):
    """
    Return the response for when a single Leave_Type when requested by the user.
    :param leave_type:
    :return:
    """
    return make_response(jsonify({
        'status': 'success',
        'leave_type': leaveT.leaveType,
        'description': leaveT.description,
        'num_of_days': leaveT.num_of_days,
        'validity': leaveT.validity,
        'carry_forward': leaveT.carry_forward
    }))


def get_leaves_types_list(leave_types):
    leaveT = []
    for leave_type in leave_types:
        leaveT.append(leave_type)
    return leaveT


def response_for_all_leave_types(leaveTypes):
    return make_response(jsonify({
        'status': 'success',
        'types': leaveTypes
    })), 200


def response(status, message, code):
    """
    Helper method to make a http response
    :param status: Status message
    :param message: Response message
    :param code: Response status code
    :return: Http Response
    """
    return make_response(jsonify({
        'status': status,
        'message': message
    })), code


def response_for_created_leave(leave, status_code):
    leave_type = LeaveTypes.query.filter_by(id=leave.leaveType).first()

    return make_response(jsonify({
        'status': 'success',
        'id': leave.id,
        'leave_type': leave_type.__getattribute__('leaveType'),
        'description': leave.description,
        'from_date': leave.from_date,
        'to_date': leave.to_date,
        'num_of_days': leave.num_of_days,
        'leave_status': leave.status,
        'employee_id': leave.employee_id
    })), status_code

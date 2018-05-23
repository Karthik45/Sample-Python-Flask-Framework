from flask import Blueprint, request, abort, jsonify

from app.auth.helper import token_required
from app.kaala.helper import response, response_for_created_leave_type, response_for_user_leave_type, \
    response_for_created_leave
from app.models import LeaveTypes, Leaves

# Initialize blueprint
leaveType = Blueprint('leaveTypes', __name__)
leaves = Blueprint('leaves', __name__)


@leaveType.route('/leaveTypes/', methods=['POST'])
@token_required
def create_leave_type(current_user):
    """
    Create a Leave_Type from the sent json data.
    :param current_user: Current User
    :return:
    """
    if request.content_type == 'application/json':
        data = request.get_json()
        leaveType_name = data.get('leaveType')
        description = data.get('description')
        num_of_days = data.get('num_of_days')
        validity = data.get('validity')
        carry_forward = data.get('carry_forward')
        employee_id = current_user.id
        if leaveType_name:
            leaveType = LeaveTypes(leaveType_name, description, num_of_days, validity, carry_forward, employee_id)
            leaveType.save()
            return response_for_created_leave_type(leaveType, 201)
        return response('failed', 'Missing leaveType name attribute', 400)
    return response('failed', 'Content-type must be json', 202)


@leaveType.route('/leaveTypes/<leave_type_id>', methods=['GET'])
@token_required
def get_leave_type(current_user, leave_type_id):
    """
    Return a user Leave_Type with the supplied user Id.
    :param current_user: User
    :param Leave_Type_id: Leave_Type Id
    :return:
    """
    try:
        int(leave_type_id)
    except ValueError:
        return response('failed', 'Please provide a valid Leave_Type Id', 400)
    else:
        leave_type = LeaveTypes.query.filter_by(id=leave_type_id).first()
        if leave_type:
            return response_for_user_leave_type(leave_type)
        return response('failed', "leave_type not found", 404)


@leaveType.route('/leaveTypes/', methods=['GET'])
@token_required
def get_all_leave_types(current_user):
    """
    Return a user Leave_Type with the supplied user Id.
    :param current_user: User
    :param Leave_Type_id: Leave_Type Id
    :return:
    """

    return jsonify(LeaveTypes.return_all())


@leaveType.route('/leaveTypes/<leave_type_id>', methods=['PUT'])
@token_required
def edit_leave_type(current_user, leave_type_id):
    if request.content_type == 'application/json':
        data = request.get_json()
        try:
            int(leave_type_id)
        except:
            return response('failed', 'Please provide a valid leave type Id', 400)

        leave_type = LeaveTypes.query.filter_by(id=leave_type_id).first()
        if leave_type:
            leave_type.leaveType = data.get('leaveType')
            leave_type.description = data.get('description')
            leave_type.num_of_days = data.get('num_of_days')
            leave_type.validity = data.get('validity')
            leave_type.carry_forward = data.get('carry_forward')
            leave_type.employee_id = current_user.id
            leave_type.update()
            return response_for_created_leave_type(leave_type, 201)
        return response('failed', 'The leaveType with Id ' + leave_type_id + ' does not exist', 404)
    return response('failed', 'Content-type must be json', 202)


@leaveType.route('/leaveTypes/<leave_type_id>', methods=['DELETE'])
@token_required
def delete_leave_type(current_user, leave_type_id):
    try:
        int(leave_type_id)
    except:
        return response('failed', 'Please provide a valid leave type Id', 400)

    leave_type = LeaveTypes.query.filter_by(id=leave_type_id).first()

    if not leave_type:
        abort(404)
    leave_type.delete()
    return response('success', 'LeaveType Deleted successfully', 200)


@leaves.route('/leaves/', methods=['POST'])
@token_required
def create_leave(current_user):
    """
    Create a Leave from the sent json data.
    :param current_user: Current User
    :return:
    """
    if request.content_type == 'application/json':
        data = request.get_json()
        leaveType = data.get('leaveType')
        description = data.get('description')
        from_date = data.get('from_date')
        to_date = data.get('to_date')
        num_of_days = data.get('num_of_days')
        employee_id = current_user.id
        leave_status = data.get('leave_status')

        if leaveType:
            leave = Leaves(leaveType, description, from_date, to_date, num_of_days, employee_id, leave_status)
            leave.save()
            return response_for_created_leave(leave, 201)
        return response('failed', 'Missing leaveType attribute', 400)
    return response('failed', 'Content-type must be json', 202)


@leaves.route('/leaves/<leave_id>', methods=['GET'])
@token_required
def get_leave(current_user, leave_id):
    """
    Return a user Leave_Type with the supplied user Id.
    :param current_user: User
    :param Leave_Type_id: Leave_Type Id
    :return:
    """
    try:
        int(leave_id)
    except ValueError:
        return response('failed', 'Please provide a valid Leave_Type Id', 400)
    else:
        leave = Leaves.query.filter_by(id=leave_id).first()
        if leave:
            return response_for_created_leave(leave, 200)
        return response('failed', "leave_type not found", 404)


@leaves.route('/leaves/', methods=['GET'])
@token_required
def get_all_leave(current_user):
    return jsonify(Leaves.return_all_leaves())


@leaveType.route('/leaves/<leave_id>', methods=['PUT'])
@token_required
def edit_leaves(current_user, leave_id):
    if request.content_type == 'application/json':
        data = request.get_json()
        try:
            int(leave_id)
        except:
            return response("failed", "leave id need to be integer", 404)

        leave = Leaves.query.filter_by(id=leave_id).first()

        if leave.leave_status is 0:
            if leave:
                leave.leaveType = data['leaveType']
                leave.description = data['description']
                leave.from_date = data['from_date']
                leave.to_date = data['to_date']
                leave.num_of_days = data['num_of_days']
                leave.leave_status = data['leave_status']
                leave.update()
                return response_for_created_leave(leave, 201)
            return response('failed', 'Missing leave attribute', 400)
        return response('failed', 'Unable to edit leave because already submitted. please contact admin', 400)
    return response('failed', 'Content-type must be json', 202)


@leaveType.route('/leaves/<leave_id>', methods=['DELETE'])
@token_required
def delete_leaves(current_user, leave_id):
    try:
        int(leave_id)
    except:
        return response("failed", "leave id need to be integer", 404)

    leave = Leaves.query.filter_by(id=leave_id).first()

    if leave.leave_status is 0:
        if leave:
            abort(404)
        leave.delete()
        return response('success', 'Leave Deleted successfully', 200)
    return response('failed', 'Unable to delete leave because already submitted. Please contact admin', 400)

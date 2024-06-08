from flask import Blueprint, render_template

bp = Blueprint('map', __name__)

@bp.route('/plan_route')
def plan_route():
    return render_template('plan_route.html')

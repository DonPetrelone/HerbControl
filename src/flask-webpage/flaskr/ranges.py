from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('ranges', __name__)

@bp.route('/')
@login_required
def index():
	values = get_values()
	return render_template('ranges/index.html', values=values)


def get_values():
	vals = get_db().execute('SELECT * FROM ranges').fetchone()	
	return vals

@bp.route('/update')
def update(athd, athw, atg, atlw, atld, ahhd, ahhw, ahg, ahlw, ahld, smhd, smhw, smg, smlw, smld):
	db = get_values()
	db.execute('UPDATE ranges SET airTempHighDanger = ?, airTempHighWarning = ?, airTempGood = ?, airTempLowWarning = ?, airTempLowDanger = ?, airHumHighDanger = ?,airHumHighWarning = ?, airHumGood = ?, airHumLowWarning = ?, airHumLowDanger = ?, soilMoistHighDanger = ?, soilMoistHighWarning = ?, soilMoistGood = ?, soilMoistLowWarning = ?, soilMoistLowDanger = ? ',
	(athd, athw, atg, atlw, atld, ahhd, ahhw, ahg, ahlw, ahld, smhd, smhw, smg, smlw, smld)
	)
	db.commit()

	return render_template('ranges/index.html')

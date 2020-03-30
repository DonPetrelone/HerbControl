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

@bp.route('/update', methods = ['POST', 'GET'])
@login_required
def update():
	
	if request.method == 'POST':
		try:
			athd = request.form['airTempHighDanger']
			athw = request.form['airTempHighWarning']
			atg = request.form['airTempGood']
			atlw = request.form['airTempLowWarning']
			atld = request.form['airTempLowDanger']
			ahhd = request.form['airHumHighDanger']
			ahhw = request.form['airHumHighWarning']
			ahg = request.form['airHumGood']
			ahlw = request.form['airHumLowWarning']
			ahld = request.form['airHumLowDanger']
			smhd = request.form['soilMoistHighDanger']
			smhw = request.form['soilMoistHighWarning']
			smg = request.form['soilMoistGood']
			smlw = request.form['soilMoistLowWarning']
			smld = request.form['soilMoistLowDanger']
			db = get_db()
			db.execute('UPDATE ranges SET airTempHighDanger = ?, airTempHighWarning = ?, airTempGood = ?, airTempLowWarning = ?, airTempLowDanger = ?, airHumHighDanger = ?,airHumHighWarning = ?, airHumGood = ?, airHumLowWarning = ?, airHumLowDanger = ?, soilMoistHighDanger = ?, soilMoistHighWarning = ?, soilMoistGood = ?, soilMoistLowWarning = ?, soilMoistLowDanger = ? ',
			(athd, athw, atg, atlw, atld, ahhd, ahhw, ahg, ahlw, ahld, smhd, smhw, smg, smlw, smld)
			)
			db.commit()
		except:
			db.rollback()

		finally:
			return redirect(url_for('index'))
			db.close()
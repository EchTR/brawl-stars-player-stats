# Github: EchTR
import requests
from flask import Flask,render_template,request
import os

def get_data(user_id):
	header = {
		"Accept":"application/json",
		"authorization":"Bearer <token>" 
	}
	bs = requests.get("https://api.brawlstars.com/v1/players/%{}".format(user_id),headers=header)
	data = bs.json()
	return {"user_tag":data["tag"],
			"user_name":data["name"],
			"user_club":data["club"],
			"user_color":data["nameColor"],
			"user_trophies":data["trophies"],
			"user_highest_trophies":data["highestTrophies"],
			"user_level":data["expLevel"],
			"user_s_victories":data["soloVictories"],
			"user_d_victories":data["duoVictories"],
			"user_3_victories":data["3vs3Victories"]

			}
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
@app.route("/user_information",methods=["GET","POST"])
def user_information():
	if request.method == "POST":
		u_id = request.form.get("post_id")
		try:
			if len(get_data(u_id)["user_club"]) == 0:
				k_c = "None"
			else:
				k_c = get_data(u_id)["user_club"]
				print(str(k_c))
			return render_template("user_information.html",
				k_tag = get_data(u_id)["user_tag"][1:],
				k_name = get_data(u_id)["user_name"],
				k_color = get_data(u_id)["user_color"],
				k_club = k_c,
				k_trophies = get_data(u_id)["user_trophies"],
				k_highest = get_data(u_id)["user_highest_trophies"],
				k_level = get_data(u_id)["user_level"],
				k_solo = get_data(u_id)["user_s_victories"],
				k_duo = get_data(u_id)["user_d_victories"],
				k_3 = get_data(u_id)["user_3_victories"]
			)
		except:
			return render_template("404.html")
	else:
		return render_template("503.html")
@app.errorhandler(404)
def ce404(e):
	return render_template("404page.html")
if __name__ == "__main__":
	app.run()
	
"""
1/k_tag = get_data(u_id)["user_tag"][:]
2/k_tag = get_data(u_id)["user_tag"][1:],
				k_name = get_data(u_id)["user_name"],
				k_color = get_data(u_id)["user_color"],
				1/k_club = get_data(u_id)["user_club"],
				2/k_club = k_c,
				k_trophies = get_data(u_id)["user_trophies"],
				k_highest = get_data(u_id)["user_highest_trophies"],
				k_level = get_data(u_id)["user_level"],
				k_solo = get_data(u_id)["user_s_victories"],
				k_duo = get_data(u_id)["user_d_victories"],
				k_3 = get_data(u_id)["user_3_victories"]
"""

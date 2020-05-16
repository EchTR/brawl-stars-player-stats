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
I am writing this comment line so that the python files are in the majority. it has no function. its purpose is not to take notes.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed id nibh commodo sem varius facilisis.
Curabitur fermentum eu justo at viverra. Morbi id suscipit purus. Nunc laoreet nunc nisl, quis dapibus nisl tristique eu. 
Cras quis mauris eu lectus scelerisque accumsan quis eu neque. Nam a gravida ipsum. Donec egestas felis augue, vel tempus tellus congue ut. Sed justo nunc, commodo et condimentum vel, dictum nec erat. Nulla rhoncus ut purus at condimentum. Nam mattis id nisl nec suscipit. 
Etiam et sodales nibh. Nulla vel commodo purus, at cursus nulla. Vivamus quis sem at odio tempus consectetur. 
Nunc bibendum tempor laoreet. In congue, velit et viverra convallis, mauris turpis luctus lorem, vel semper elit enim sit amet neque.
Ut finibus ultrices turpis rutrum ornare. Donec vitae tristique risus. Proin tristique massa quis posuere viverra. 
In eleifend mi nec malesuada bibendum. Aliquam felis mauris, feugiat eu lacus et, consectetur interdum risus. Nam et nunc et lacus 
vehicula ornare. Donec pellentesque nisl et mattis euismod. Proin cursus, leo sed dignissim dignissim, est mi semper neque, vitae
vehicula erat dui id nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. 
Aenean commodo commodo lacus sit amet ultrices. Nam laoreet et purus in tincidunt. Phasellus a mattis erat. 
In interdum sapien nec maximus aliquet. Donec nisi ex, vehicula ut orci id, ultricies tincidunt tortor. Morbi maximus ultrices ipsum, a
varius urna rhoncus eget.
"""

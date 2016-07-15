from flask import Flask
from flask import render_template 
app= Flask("test App")
   
import urllib.request as request
import json

@app.route('/')
def safety(): 
  dictionary={}

  key = "f739f2d3948eea92"
  fileName = "http://api.wunderground.com/api/f739f2d3948eea92/geolookup/conditions/q/NC/Cary.json"
  f = request.urlopen(fileName)
  json_string = f.read().decode('utf-8')
  print(json_string)
  parsed_json = json.loads(json_string)
  dictionary['location'] = parsed_json['location']['city']
  dictionary['temp'] = parsed_json['current_observation']['temp_f']
  dictionary['hum']= parsed_json['current_observation']['relative_humidity']
  dictionary['wind']= parsed_json['current_observation']['wind_mph']
  temp=dictionary['temp']
  hum_num=int(dictionary['hum'].strip('%'))
  wind=dictionary['wind']
  temp=80
  if temp>40:
    if temp> 100 or (temp> 90 and hum_num>55):
      dictionary['message'] = "TOO HOT DO NOT GO OUTSIDE!!!!"
    elif 40< temp<= 84 or (84 <= temp <90 and hum_num<65.1):
       dictionary['message'] ="Have fun outside!!"
       dictionary['image']="play.png"  
    else: 
      dictionary['message'] ="Caution only go outside for 10 minutes"
      dictionary['image']="hotdog.jpg"  
  else:
    if temp< 10 or (10<=temp<= 20 and wind>5):
       dictionary['message'] = "TOO COLD DO NOT GO OUTSIDE!!!!"
      
    elif 40<=temp<45 and wind<=15:
       dictionary['message'] ="Have fun outside!!"
    else: 
       dictionary['message'] = "Caution only go outside for 10 minutes"  
  return render_template("weather.html", weather=dictionary) 
if __name__=="__main__":
   app.run(debug=True)
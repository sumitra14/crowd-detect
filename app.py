from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, request, jsonify, url_for, redirect
from find import findpath,find_object_path,find_airport_size,find_parking_size
from predict import prediction
from object import object_detect
from database import connect_to_database
import datetime
app = Flask(__name__)
run_with_ngrok(app)


@app.route('/',methods=['GET','POST'])
def home():
   if request.method=='POST':
      airport=request.form.get('input')
      return redirect(url_for('result',airport=airport))
   return render_template('index.html')
@app.route('/result')
def result():
   airport=request.args.get('airport',None)
   terminal,pic=findpath(airport)
   d={}
   for i,j in zip(terminal,pic):
      count=prediction(j)
      d[i]=count
   final=[]
   int_to_week_day={0:'monday',1:'tuesday',2:'wednesday',3:'thrusday',4:'friday',5:'saturday',6:'sunday'}
   ct=datetime.datetime.now().strftime("%H:%M")
   ct1=datetime.datetime.strptime(ct,"%H:%M")
   t2 = datetime.datetime.strptime('05:30', '%H:%M')
   time_zero = datetime.datetime.strptime('00:00', '%H:%M')
   current_time=str((ct1 - time_zero + t2).time().strftime("%H:%M"))
   current_day_int=datetime.datetime.today().weekday()
   current_day=int_to_week_day[current_day_int]
   expected_increase=connect_to_database(airport.lower(),current_time,current_day)
   dic_terminal={}
   for i in expected_increase:
      dic_terminal[i[1]]=i[0]
   print(dic_terminal)
   for i,j in d.items():
      message=''
      message1=''
      message2=''
      size=find_airport_size(i)
      get_expected_count=0
      if i in dic_terminal.keys():
         get_expected_count=dic_terminal[i]
      if((size-j)<=50):
         message+="{} predicted count = {}".format(i,str(j))
         message1+="So,according to our calculation if you want to board flight from this terminal, you will have to arrive early because crowd is at its peak and it is also suggested to avoid bringing visitors"
      elif((size-j)>50 and (size-j)<100):
         message+="{} predicted count ={}".format(i,str(j))
         message1+="So,according to our calculation if you want to board flight from this terminal,you will not find much trouble but still it is suggested to avoid bringing visitors" 
      else:
         message+="{} predicted count ={}".format(i,str(j))
         message1+="So,according to our calculation if you want to board flight from this terminal, you would not find any issue regarding waiting time and check-in"
      if get_expected_count==0:
         message2+='There is only a little chance of increase in crowd in the next 2-3 hours'   
      elif get_expected_count<=2:
         message2+='PRECAUTION:the crowd is expected to increase slightly in the next 2-3 hours'
      else:
         message2+='PRECAUTION:the crowd is expected to increase in the next 2-3 hours due to scheduling of of more than 2 flights during the hours'
      final.append([message,message1,message2])
   return render_template('result.html',airport=airport.upper(),pic=pic,dic=final)
@app.route('/result1')
def result1():
   airport=request.args.get('airport',None)
   terminal,pic=find_object_path(airport.lower())
   d={}
   for i,j in zip(terminal,pic):
      count=object_detect(j)
      d[i]=count
   final=[]
   for i,j in d.items():
      message=''
      message1=''
      message2=''
      size=find_parking_size(i)
      if((size-j)<=50):
         message+="{} predicted count = {}".format(i,str(j))
         message1+="So,according to our calculation if you want to board flight from this terminal,you might not find slots for parking,So it is suggested that you should try some other means of transport in order to avoid delay"
      elif((size-j)>50 and (size-j)<100):
         message+="{} predicted count = {}".format(i,str(j))
         message1+="So,according to our calculation if you want to board flight from this terminal,there are chances to get parking slots if you arrive early"
      else:
         message+="{} predicted count = {}".format(i,str(j))
         message1+="So,according to our calculation if you want to board flight from this terminal,you will easily get parking slots"
      final.append([message,message1])
   return render_template('result1.html',airport=airport,pic=pic,dic=final)

if __name__ == '__main__':
   app.run()

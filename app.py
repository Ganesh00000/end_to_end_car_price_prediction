from flask import Flask,render_template,request
import pickle as pk
from datetime import date
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)


@app.route("/")
def start():
    return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/predict",methods=["POST","GET"])
def predict():
    if request.method=="POST":
        lists=[]
        for x in range(48):
            lists.append(0)
        dates=date.today()
        mileage=float(request.form["mileage"])
        engine=float(request.form["engine"])
        power=float(request.form["power"])
        brand=int(request.form["Brand"])
        fuel=int(request.form["fuel"])
        transmission=int(request.form["transmission"])
        owner=int(request.form["owner type"])
        use=int(request.form["use"])
    
        lists[0]=mileage
        lists[1]=engine
        lists[2]=power

        for i in range(1,33):
            if brand==i:
                lists[i+2]=1
        if fuel==1:
            lists[36]=1
        elif fuel==2:
            lists[37]=1
        elif fuel==3:
            lists[38]=1
        elif fuel==4:
            lists[39]=1
        else:
            lists[40]=1
            
            
        if transmission==1:
            lists[41]=1
        else:
            lists[42]=1
            
        if owner==1:
            lists[43]=1
        elif owner==2:
            lists[45]=1
        elif owner==3:
            lists[46]=1
        else:
            lists[44]=1
        
        
        lists[47]=use
        
            
        with open("my_model","rb") as file:
            model=pk.load(file)
            
        scaler=StandardScaler()
        x=[lists]
        x=scaler.fit_transform(x)
        
        
        predict=model.predict(x)
        print(predict)
        
        
        return render_template("/home.html",data=predict[0])
        
        
        
        
        
        
    else:
        return ("something went wrong")
    
    
    
    
    
if __name__=="__main__":
    app.run("localhost",4060,use_reloader=False,debug=True)
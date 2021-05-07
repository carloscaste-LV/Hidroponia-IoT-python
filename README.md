# Hidroponia-IoT
 Python-Micropython-Flask-Arduino
<!DOCTYPE html>
<html>
<head>

<script>
function setURL(url){
    document.getElementById('cam').src = url;
}
</script>

<style>


.button {
  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;
}

.button1 {
  background-color: white; 
  color: black; 
  border: 2px solid #4CAF50;
}

.button1:hover {
  background-color: #4CAF50;
  color: white;
}

.button2 {
  background-color: white; 
  color: black; 
  border: 2px solid #4CAF50;
}

.button2:hover {
  background-color: #4CAF50;
  color: white;
}

.button3 {
  background-color: white; 
  color: black; 
  border: 2px solid #4CAF50;
}

.button3:hover {
  background-color: #4CAF50;
  color: white;
}

.button4 {
  background-color: white; 
  color: black; 
  border: 2px solid #4CAF50;
  padding: 16px 41px;
}

.button4:hover {
  background-color: #4CAF50;
  color: white;  
}

.button5 {
  background-color: white; 
  color: black; 
  border: 2px solid #00E665;
  padding: 16px 75px;
}

.button5:hover {
  background-color: #00E665;
  color: white;  
  
}

</style>

<head>
  <style>
    div {
      background-color: #DAF7A6;
    }
  </style>
</head>
<body>
  <div>

  </div>
</body>

<font color="#D5DBDB">
<h1 >Proyecto final - IoT</h1>
</font>
<body style="background-color:#212F3C;">
</body>
 

<div style="float: left;">
<p></p>
&nbsp;&nbsp;<button class="button button3" onclick="setURL('https://www.controlmaquinas.com/ph')" >pH</button>
<button class="button button2" onclick="setURL('https://www.controlmaquinas.com/temperatura_agua')">Temperatura</button>
</p>

<p>
&nbsp;&nbsp;<button class="button button1" onclick="setURL('https://www.controlmaquinas.com/distancia')">Distancia</button>

<button class="button button4" onclick="setURL('https://www.controlmaquinas.com/tds')">Tds</button>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>
&nbsp;&nbsp;<button class="button button5" onclick="setURL('https://www.controlmaquinas.com/ph')" >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;On/Off&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</button>
 
 </div>
<div clear="right">
 <div  style="float: left;" >
 <p></p>
 <iframe width="410px" height="217px" src="https://www.controlmaquinas.com/slides" width="100%" height="86%" style="border:none;" frameborder="0"  scrolling="no"></iframe>
 </div>





<iframe id="cam" src="https://www.controlmaquinas.com/distancia" width="100%" height="86%" style="border:none;"  scrolling="no">
</iframe>

</head>

</html>

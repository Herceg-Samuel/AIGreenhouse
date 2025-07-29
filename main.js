const temp = Temperature;
const hum = Humidity;
const light = LightIntensity;
const moisture = SoilMoisture;
const CO = CarbonDioxideLevel;


const WateringControl = (moisture, hum, temp) => {
    if(moisture > 0.7){
        console.log("Skip Watering");
    }elseif((moisture >= 0.35 && moisture <= 0.5) && temp > 35){
        console.log("Light watering");
    } elseif((moisture < 0.35) || (hum < 0.4 || temp > 30)){
        console.log("Watering");
};    

switch (expression) {
  case value1:
    // code to be executed if expression matches value1
    break;
  case value2:
    // code to be executed if expression matches value2
    break;
  // ... more cases
  default:
    // code to be executed if no case matches the expression
}




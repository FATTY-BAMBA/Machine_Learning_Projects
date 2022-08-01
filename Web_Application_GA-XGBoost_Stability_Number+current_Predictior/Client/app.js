function onClickedStabilityNumber() {
    console.log("Stability Number button Clicked");
    var D = document.getElementById('uiD');
    var GSI = document.getElementById('uiGSI');
    var mi= document.getElementById('uimi');
    var beta = document.getElementById('uibeta');
    var kh = document.getElementById('uikh');
    var estPrice = document.getElementById('uiStabilityNumber');

//var url = "http://127.0.0.1:5000/predict_stability_number"; //Use this if you are NOT using nginx which is first 7 tutorials

var url = "/api/predict_stability_number"; // Use this if  you are using nginx. i.e tutorial 8 and onwards

 $.post(url, {
    D: parseFloat(D.value),
    GSI: parseFloat(GSI.value),
    mi: parseFloat(mi.value),
    beta : parseFloat(beta.value),
    kh : parseFloat(kh.value)
},function(data, status) {
    console.log(data.estimated_stability_number);
    estPrice.innerHTML = "<h2>" + data.estimated_stability_number.toString() ;
    console.log(status);
});
}

var btn_patient = document.querySelector('#show-or-patient')
var btn_requests = document.querySelector('#show-or-requests')
var btn_offers = document.querySelector('#show-or-offers')
var patient = document.querySelector('#patients')
var requests = document.querySelector('#requests')
var offers = document.querySelector('#offers')


btn_patient.addEventListener('click', function(){

    if(patient.style.display === 'block'){
        patient.style.display = 'none';
    }else{
        patient.style.display = 'block';
    }
})

btn_requests.addEventListener('click', function() {

    if(requests.style.display === 'block'){
        requests.style.display = 'none';
    }else{
        requests.style.display = 'block';
    }
})

btn_offers.addEventListener('click', function() {

    if(offers.style.display === 'block'){
        offers.style.display = 'none';
    }else{
        offers.style.display = 'block';
    }
})
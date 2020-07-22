window.onload = function(){
getCovidStat();
}

function getCovidStat(){
  fetch('https://coronavirus-tracker-api.herokuapp.com/v2/locations/163')
  .then(function(resp){
    return resp.json()
  })
  .then(function(data){
    console.log(data);
    let morts=data.location.latest.deaths;
    let confirmed=data.location.latest.confirmed;
    let update=data.location.last_updated;

    document.getElementById('confirmed').innerHTML=confirmed;
    document.getElementById('morts').innerHTML=morts;
    document.getElementById('MiseJour').innerHTML=update.substr(0,19);
  })
}

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
function populate() {
	function reqListener() {
		if (this.readyState == 4 && this.status == 200) {
			let obj = JSON.parse(this.responseText);
			document.getElementById('stop').innerHTML = obj.ride.destination
			document.getElementById('departure').innerHTML = obj.ride.departure
			document.getElementById('date').innerHTML = obj.ride.date
			document.getElementById('charges').innerHTML = obj.ride.charges
			document.getElementById('meet').innerHTML = obj.ride.meetpoint

		};

	}

	var oReq = new XMLHttpRequest();
	oReq.addEventListener("load", reqListener);
	oReq.open("GET", "https://mighty-beach-21248.herokuapp.com/api/v1/rides/1", true);
	oReq.send();
}




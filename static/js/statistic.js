function updateField(a, b) {
    const margin_value_obj = document.getElementById("id_margin_value");
    margin_value_obj.value = a-b;
}

function removeLinkFromTitle() {
	const titles = document.getElementsByClassName("field-title");
	for(let i =0;i<titles.length;i++) {
		const hrefLink = titles[i].getElementsByTagName("a");
		if(hrefLink.length>0){
			const value = hrefLink[0].innerHTML;
			titles[i].innerHTML = value;
		}
	}
}

function calculatePercentage(a, b) {
    const total_value_obj = document.getElementById("id_total_value");

    if(b!=0) {
        total_value_obj.value = (a/b * 100).toFixed(2);
    } else {
        total_value_obj.value = 0;
    }
}


//function url_uncheck() {
//    const url_class = document.getElementByClassName("field-title");
//    console.log(url_class, "Testing .........")
//    if (url_class.length > 0)
//        url_class[0].insertAdjacentHTML("");
//}



document.addEventListener("DOMContentLoaded", function(event) {

    console.log("test?")

    const total_values = document.getElementsByClassName("field-total_value");
    for(let i = 0;i<total_values.length;i++) {
        total_values[i].innerHTML = total_values[i].innerHTML.split(".")[0] + " %";
    }
    removeLinkFromTitle();

    revue_value = 0;
    total_cost = 0;

    const revue_value_obj = document.getElementById("id_revue_value");
    const total_cost_obj = document.getElementById("id_total_cost_value");
    revue_value_obj.addEventListener('input', function (evt) {
        revue_value = evt.target.value;
        updateField(revue_value, total_cost);
    });

    total_cost_obj.addEventListener('input', function (evt) {
        total_cost = evt.target.value;
        updateField(revue_value, total_cost);
    });



    initial_value = 0;
    final_value = 0;

    const initial_value_obj = document.getElementById("id_initial_value");
    const final_value_obj = document.getElementById("id_final_value");
    initial_value_obj.addEventListener('input', function (evt) {
        initial_value = evt.target.value;
        calculatePercentage(final_value, initial_value);
    });

    final_value_obj.addEventListener('input', function (evt) {
        final_value = evt.target.value;
        calculatePercentage(final_value, initial_value);
    });

});

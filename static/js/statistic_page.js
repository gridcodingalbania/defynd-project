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


function addPercent(field) {
    const elements = document.getElementsByClassName(field);
    for(let i = 0;i<elements.length;i++) {
        elements[i].innerHTML = elements[i].innerHTML.split(".")[0] + " %";
    }
}

function addCommaAndSign(field, sign) {
    const elements = document.getElementsByClassName(field);
    for(let i = 0;i<elements.length;i++) {
        elements[i].innerHTML = addCommas(elements[i].innerHTML.split(".")[0]) + " " + sign;
    }
}

function reverse(str) {
  if (str === '')
    return '';
  else
    return reverse(str.substring(1)) + str.charAt(0);
}

function addCommas(value) {
    let input = value.split(".")[0]
    if(input.length <= 3) {
        return value
    }
    else {
        let response = "";
        const reversedString = reverse(input);
        for(let i = 0;i<reversedString.length;i++) {
            response = reversedString[i] + response;
            if (response.split(",").join("").length % 3 == 0) {
                response = "," + response;
            }
        }
        if (response.charAt(0) == ","){
            response = response.substring(1);
        }

        return response;
    }
}

function finalValueCommaAndSign() {
    const elems = document.getElementsByClassName("field-title");
    let foundIndex = -1;
    for(let i =0;i<elems.length;i++) {
        const innerElement = elems[i].getElementsByTagName("a")[0];
        if(innerElement.innerHTML == "Contenzioni chiusi con contratto" || innerElement.innerHTML == "English--versiob") {
            foundIndex = i;
            break;
        }
    }

    console.log(foundIndex);

    const elements = document.getElementsByClassName("field-final_value");
    for(let i = 0;i<elements.length;i++) {
        if(i == foundIndex) {

            elements[i].innerHTML = addCommas(elements[i].innerHTML.split(".")[0]) + " " + "€";
        } else {
            elements[i].innerHTML = "-";
        }
    }

}

document.addEventListener("DOMContentLoaded", function(event) {

    addPercent("field-total_value");
    addCommaAndSign("field-initial_value", "€");
    addCommaAndSign("field-objective_value", "€");
    addCommaAndSign("field-revue_value", "€");
    addCommaAndSign("field-total_cost_value", "€");
    addCommaAndSign("field-ebit", "€");
    addCommaAndSign("field-ebit_percent", "%");
    finalValueCommaAndSign();
    removeLinkFromTitle();

    revue_value = 0;
    total_cost = 0;

    const revue_value_obj = document.getElementById("id_revue_value");
    const total_cost_obj = document.getElementById("id_total_cost_value");
    if(revue_value_obj && total_cost_obj) {
        revue_value_obj.addEventListener('input', function (evt) {
            revue_value = evt.target.value;
            updateField(revue_value, total_cost);
        });

        total_cost_obj.addEventListener('input', function (evt) {
            total_cost = evt.target.value;
            updateField(revue_value, total_cost);
        });
    }

    initial_value = 0;
    final_value = 0;

    const initial_value_obj = document.getElementById("id_initial_value");
    const final_value_obj = document.getElementById("id_final_value");

    if(initial_value_obj && final_value_obj) {
        initial_value_obj.addEventListener('input', function (evt) {
            initial_value = evt.target.value;
            calculatePercentage(final_value, initial_value);
        });

        final_value_obj.addEventListener('input', function (evt) {
            final_value = evt.target.value;
            calculatePercentage(final_value, initial_value);
        });
    }


});

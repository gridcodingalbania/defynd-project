function updateField(a, b) {
    const turnover_margin_obj = document.getElementById("id_turnover_margin");
    turnover_margin_obj.value = a-b;
}

function updateField2(c, d) {
    const residual_surface_obj = document.getElementById("id_residual_surface");
    residual_surface_obj.value = c-d;
}

function addMeterSymbol(className, number) {
    const elem = document.getElementsByClassName(className)
    if(elem.length > 0)
        elem[0].insertAdjacentHTML('beforeend', "<span>m<sup>"+number+"</sup></span>");
}


function hideDiv() {
    const radio = document.getElementById("id_total_demolition_0");
    const partial_demolition = document.getElementsByClassName("fieldBox field-partial_demolition");
    if (radio && radio.checked) {
        console.log("Yes")
        partial_demolition[0].style.display = 'none';
    } else if(radio){
        console.log("No")
        partial_demolition[0].style.display = 'block';
    }
}

function listenForRadioChange() {
    const yes_option = document.querySelectorAll('[for="id_total_demolition_0"]')[1];
    const no_option = document.querySelectorAll('[for="id_total_demolition_1"]')[0];
    const partial_demolition = document.getElementsByClassName("fieldBox field-partial_demolition");
    if(yes_option) {
        yes_option.addEventListener('click', function() {
            partial_demolition[0].style.display = 'none';
        });
    }

    if(no_option) {
        no_option.addEventListener('click', function() {
            partial_demolition[0].style.display = 'block';
        });
    }
}

document.addEventListener("DOMContentLoaded", function(event) {
    hideDiv();
    listenForRadioChange();
    revue_value = 0;
    total_cost = 0;
    surface_directly_concerned = 0;
    occupied_area = 0;

    const revue_value_obj = document.getElementById("id_revenue");
    const total_cost_obj = document.getElementById("id_total_cost");
    if(revue_value_obj) {
        revue_value_obj.addEventListener('input', function (evt) {
            revue_value = evt.target.value;
            updateField(revue_value, total_cost);
        });
    }

    if(total_cost_obj) {
        total_cost_obj.addEventListener('input', function (evt) {
            total_cost = evt.target.value;
            updateField(revue_value, total_cost);
        });
    }






    const surface_directly_concerned_obj = document.getElementById("id_surface_directly_concerned");
    const occupied_area_obj = document.getElementById("id_occupied_area");

    if(surface_directly_concerned_obj) {
        surface_directly_concerned_obj.addEventListener('input', function (evt) {
            surface_directly_concerned = evt.target.value;
            updateField2(surface_directly_concerned, occupied_area);
        });
    }

    if(occupied_area_obj) {
        occupied_area_obj.addEventListener('input', function (evt) {
            occupied_area = evt.target.value;
            updateField2(surface_directly_concerned, occupied_area);
        });
    }



    addMeterSymbol("fieldBox field-surface_directly_concerned", 2);
    addMeterSymbol("fieldBox field-occupied_area", 2);
    addMeterSymbol("fieldBox field-residual_surface", 2);
    addMeterSymbol("fieldBox field-transformation_coefficient", 3);
    addMeterSymbol("fieldBox field-extension_MQ", 2);
    addMeterSymbol("fieldBox field-MC_residui", 3);

});











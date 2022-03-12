function updateField(a, b) {
    const turnover_margin_obj = document.getElementById("id_turnover_margin");
    let valA = 0;
    let valB = 0;
    if(a!=0 && a.includes(",")) {
        valA = +a.split(",").join("")
    } else {
        valA = +a;
    }
    if(b!=0 && b.includes(",")) {
        valB = +b.split(",").join("")
    } else {
        valB = +b;
    }
    turnover_margin_obj.value = valA-valB;
}

function updateField2(c, d) {
    const residual_surface_obj = document.getElementById("id_residual_surface");
    residual_surface_obj.value = c-d;
}

function addMeterSymbol(className, number) {
    const elem = document.getElementsByClassName(className)
    if(elem.length > 0)
        elem[0].insertAdjacentHTML('beforeend', "<span style='position: absolute;top: 34px;right: 13px;'>m<sup>"+number+"</sup></span>");
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

function hideDiv3() {
    const batch = document.getElementById("id_batch_disfiguration_0");
    const batch_disfiguration = document.getElementsByClassName("form-row field-description");
    if (batch && batch.checked) {
        console.log("Yes")
        batch_disfiguration[0].style.display = 'none';
    } else if(batch){
        console.log("No")
        batch_disfiguration[0].style.display = 'block';
    }
}

function hideDiv4() {
    const batch = document.getElementById("id_residual_airspace_0");
    const batch_disfiguration = document.getElementsByClassName("fieldBox field-MC_residui");
    if (batch && batch.checked) {
        console.log("Yes")
        batch_disfiguration[0].style.display = 'block';
    } else if(batch){
        console.log("No")
        batch_disfiguration[0].style.display = 'none';
    }
}

// TODO in feature........................................
function hideDiv2() {
    const lease = document.getElementById("id_lease_agreement_1");
    const contract_duration = document.getElementsByClassName("fieldBox field-contract_duration");
    const contract_duration_1 = document.getElementsByClassName("fieldBox field-residual_rent");
    const contract_duration_2 = document.getElementsByClassName("fieldBox field-contract_fee");
    if (lease && lease.checked) {
        contract_duration[0].style.display = 'none';
        contract_duration_1[0].style.display = 'none';
        contract_duration_2[0].style.display = 'none';
    } else if (lease) {
        contract_duration[0].style.display = 'block';
        contract_duration_1[0].style.display = 'block';
        contract_duration_2[0].style.display = 'block';
    }
}



function listenForRadioChange(yesId, noId, classNames, reversed) {
    const yes_option = document.querySelectorAll("[for=" + yesId + "]")[1];
    const no_option = document.querySelectorAll("[for=" + noId + "]")[0];

    if(yes_option) {
        yes_option.addEventListener('click', function() {

            console.log("test")
            for(let i = 0;i<classNames.length;i++) {
                const partial_demolition = document.getElementsByClassName(classNames[i]);
                const batch_disfiguration = document.getElementsByClassName(classNames[i]);
                console.log(reversed);
                partial_demolition[0].style.display = reversed ? 'block' : 'none';
                batch_disfiguration[0].style.display = reversed ? 'none' : 'block';
            }
        });
    }

    if(no_option) {
        no_option.addEventListener('click', function() {
            for(let i = 0;i<classNames.length;i++) {
                const partial_demolition = document.getElementsByClassName(classNames[i]);
                const batch_disfiguration = document.getElementsByClassName(classNames[i]);
                partial_demolition[0].style.display = reversed ? 'none' : 'block';
                batch_disfiguration[0].style.display = reversed ? 'block' : 'none';
            }

        });
    }
}

function targetBlank(className) {
    const class_divs = document.getElementsByClassName(className);
    if (class_divs.length > 0) {
        const a_div = class_divs[0];
        const a_links = a_div.getElementsByTagName("a");
        if (a_links.length > 0) {
            a_links[0].target = "_blank";
        }
    }

}

function formatInputToTakeCommas(inputId) {
        $(function() {
            $(`input[id=${inputId}]`).on('input', function(e) {
                $(this).val($(this).val().replace(/[^0-9]/g, ''));
            });
        });

        $(document).ready(function(){
            $(`input[id=${inputId}]`).keyup(function(event){
                // skip for arrow keys
                if(event.which >= 37 && event.which <= 40){
                    event.preventDefault();
                }
                var $this = $(this);
                var num = $this.val().replace(/,/gi, "").split("").reverse().join("");
                var num2 = RemoveRougeChar(num.replace(/(.{3})/g,"$1,").split("").reverse().join(""));
                // the following line has been simplified. Revision history contains original.
                $this.val(num2);
            });
            $(`input[id=${inputId}]`).keyup();
        });
    }

    function RemoveRougeChar(convertString){
        if(convertString.substring(0,1) == ","){
            return convertString.substring(1, convertString.length)
        }
        return convertString;
    }

document.addEventListener("DOMContentLoaded", function(event) {
    targetBlank("form-row field-upload_pdf");
    targetBlank("form-row field-hyperlink");
    hideDiv();
    hideDiv2();
    hideDiv3();
    hideDiv4();
    listenForRadioChange("id_total_demolition_0", "id_total_demolition_1", ["fieldBox field-partial_demolition"], true);
    listenForRadioChange("id_batch_disfiguration_0", "id_batch_disfiguration_1", ["form-row field-description"], false);
    listenForRadioChange("id_lease_agreement_0", "id_lease_agreement_1", ["fieldBox field-contract_duration", "fieldBox field-contract_fee", "fieldBox field-residual_rent"], false);
    listenForRadioChange("id_residual_airspace_0", "id_residual_airspace_1", ["fieldBox field-MC_residui"], false);
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

    formatInputToTakeCommas("id_initial_estimation_value");
    formatInputToTakeCommas("id_target_value");
    formatInputToTakeCommas("id_final_value");
    formatInputToTakeCommas("id_revenue");
    formatInputToTakeCommas("id_total_cost");
    formatInputToTakeCommas("id_enrollment_amount");
    formatInputToTakeCommas("id_turnover_margin");
    formatInputToTakeCommas("id_reclamation_cost");

    formatInputToTakeCommas("id_residual_rent");
    formatInputToTakeCommas("id_contract_fee");


});











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
    elem[0].insertAdjacentHTML('beforeend', "<span>m<sup>"+number+"</sup></span>");
}

document.addEventListener("DOMContentLoaded", function(event) {

    revue_value = 0;
    total_cost = 0;
    surface_directly_concerned = 0;
    occupied_area = 0;

    const revue_value_obj = document.getElementById("id_revenue");
    const total_cost_obj = document.getElementById("id_total_cost");
    revue_value_obj.addEventListener('input', function (evt) {
        revue_value = evt.target.value;
        updateField(revue_value, total_cost);
    });

    total_cost_obj.addEventListener('input', function (evt) {
        total_cost = evt.target.value;
        updateField(revue_value, total_cost);
    });



    const surface_directly_concerned_obj = document.getElementById("id_surface_directly_concerned");
    const occupied_area_obj = document.getElementById("id_occupied_area");
    surface_directly_concerned_obj.addEventListener('input', function (evt) {
        surface_directly_concerned = evt.target.value;
        updateField2(surface_directly_concerned, occupied_area);
    });

    occupied_area_obj.addEventListener('input', function (evt) {
        occupied_area = evt.target.value;
        updateField2(surface_directly_concerned, occupied_area);
    });

    addMeterSymbol("fieldBox field-surface_directly_concerned", 2);
    addMeterSymbol("fieldBox field-occupied_area", 2);
    addMeterSymbol("fieldBox field-residual_surface", 2);
    addMeterSymbol("fieldBox field-transformation_coefficient", 3);
    addMeterSymbol("fieldBox field-extension_MQ", 2);
    addMeterSymbol("fieldBox field-MC_residui", 3);

});








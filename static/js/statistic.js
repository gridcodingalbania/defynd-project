function updateField(a, b) {
    const margin_value_obj = document.getElementById("id_margin_value");
    margin_value_obj.value = a-b;
}

function calculatePercentage(a, b) {
    const total_value_obj = document.getElementById("id_total_value");

    if(b!=0) {
        total_value_obj.value = (a/b * 100).toFixed(2);
    } else {
        total_value_obj.value = 0;
    }
}


document.addEventListener("DOMContentLoaded", function(event) {

    console.log("test?")

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

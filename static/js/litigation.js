function updateField(a, b) {
    const turnover_margin_obj = document.getElementById("id_turnover_margin");
    turnover_margin_obj.value = a-b;
}

document.addEventListener("DOMContentLoaded", function(event) {

    revue_value = 0;
    total_cost = 0;

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
});
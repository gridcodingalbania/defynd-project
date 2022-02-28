console.log("customers...")



document.addEventListener("DOMContentLoaded", function(event) {
    const selectBox = document.getElementById("id_customer_type");
    const comp = document.getElementsByClassName("form-row field-company_name")[0];
    const fsc_code = document.getElementsByClassName("form-row field-fiscal_code")[0];
    const vat_number = document.getElementsByClassName("form-row field-vat_number")[0];

    if(selectBox.value=='individual') {
        comp.style.display='none';
        fsc_code.style.display='none';
        vat_number.style.display='none';
    }

    selectBox.onchange = function(event){
        const val = event.target.value;
       if(val=="company") {
            comp.style.display='block';
            fsc_code.style.display='block';
            vat_number.style.display='block';
        }
        else {
            comp.style.display='none';
            fsc_code.style.display='none';
            vat_number.style.display='none';
        }
    };

});
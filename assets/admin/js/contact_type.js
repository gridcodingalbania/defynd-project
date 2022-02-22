(function($) {
    'use strict';

    function makeInputUpperCase(inputId) {
        const jQueryInput = $(inputId);
        if(jQueryInput) {
            const input = jQueryInput[0];
            if(input) {
                input.style.textTransform = "uppercase";
            }
        }
    }

    function formatDate(id) {
        const input = document.getElementById(id);
        if(input) {
           input.size=10;input.maxLength=10;
           $(document).ready(function(){
                $(`input[id=${id}]`).keyup(function(event){
                    $(this).val($(this).val().replace(/^(\d\d)(\d)$/g,'$1/$2').replace(/^(\d\d\/\d\d)(\d+)$/g,'$1/$2').replace(/[^\d\/]/g,''));
                });
            });
        }
    }

//  formatDate("id_birthday_container");

    $(function() {
        // TODO: add css class to group of fields per :individual - company & use only 2 vars
        
        // hide origin from form
        $('#id_origin_container').hide();


        
        var selectField = $('#id_customer_type'), // #id_field_name
            company_name = $('#id_company_name_container'),
            first_name = $('#id_first_name_container'),
            last_name = $('#id_last_name_container'),
            fiscal_code = $('#id_fiscal_code_container'),
            vat_number = $('#id_vat_number_container'),
            birthplace = $('#id_birthplace_container'),
            contact_person = $('#id_contact_person_container'),
            role = $('#id_role_container'),
            individual = $('.individual'),
            company = $('.company');

        makeInputUpperCase("#id_fiscal_code");
        makeInputUpperCase("#id_vat_number");

        var gender_container = $('.radio-field'),
            birthday_container = $('#id_birthday_container');

        // onchange contact type
        function checkContactType(contact_type) {
            console.log(contact_type);

            // Individual
            if (contact_type === 'individual') {
                individual.show();
                gender_container.show();
                birthday_container.show();
                first_name.show();
                last_name.show();
                birthplace.show();
                company.hide();
                company_name.hide();
                contact_person.hide();
                role.hide();
                fiscal_code.hide();
                vat_number.hide();
            }

            // Company
            if (contact_type === 'company') {
                company.show();
                company_name.show();
                contact_person.show();
                role.show();
                fiscal_code.show();
                vat_number.show();
                individual.hide();
                gender_container.hide();
                birthday_container.hide();
                birthplace.hide();
                first_name.hide();
                last_name.hide();
            }
        }

        // show/hide on load based on pervious value of selectField
        checkContactType(selectField.val());

        // show/hide on change
        selectField.change(function() {
            checkContactType($(this).val());
        });
        formatDate("id_birthday");
    });
})(django.jQuery);
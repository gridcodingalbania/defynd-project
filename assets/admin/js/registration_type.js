(function($) {
    'use strict';
    var interestedAreaValue = 0;
    var targetAreaValue = 0;
    $(document).ready(() => {
        initFormFields();
    });
    // When the document if fully loaded.


    function initFormFields() {
        const surfaceDirectlyConcernedInput = document.getElementById("id_surface_directly_concerned");
        const targetAreaInput = document.getElementById("id_occupied_area");
        if(surfaceDirectlyConcernedInput && targetAreaInput) {
            if(surfaceDirectlyConcernedInput.value && targetAreaInput.value) {
                console.log("test", surfaceDirectlyConcernedInput.value, targetAreaInput.value)
                interestedAreaValue = +surfaceDirectlyConcernedInput.value;
                targetAreaValue = +targetAreaInput.value;
                console.log("aa", interestedAreaValue, targetAreaValue);
                setTimeout(() => {
                    updateResidualSurface();
                }, 100);
            }
        }
        
    }



    function addErrorStyle(id) {
        const container = document.getElementById(id + "_container");
        if(container) {
            const input = container.children[0];
            const helpText = container.children[2];
            input.style.color = "#dc3545";
            helpText.style.color = "#dc3545";
            helpText.innerHTML = "Occupied Area can't be bigger than Concerned Area";
            input.style.borderBottom = "1px solid #dc3545";
        }
    }


    function removeErrorStyle(id) {
        const container = document.getElementById(id + "_container");
        if(container) {
            const input = container.children[0];
            const helpText = container.children[2];
            input.style.color = "#9e9e9e";
            helpText.style.color = "rgba(0, 0, 0, 0.6)";
            helpText.innerHTML = "Superficie Residua";
            input.style.borderBottom = "1px solid #9e9e9e";
        }
    }


    function listenForAreaChange(id) {
        const interestedArea = document.getElementById(id);
        if(interestedArea) {
            interestedArea.addEventListener('keyup', (event) => {
                console.log(event.target.value);
                if(event.target.value && event.target.value > 0) {
                    if(id == "id_surface_directly_concerned") {
                        // if writing on first input.
                        interestedAreaValue = +event.target.value;
                    } else {
                        // if writing on second input.
                        targetAreaValue = +event.target.value;
                    }
                } else {
                    // if one of input values is incorrect like minus sign or 'e' symbol
                    if(id == "id_surface_directly_concerned") {
                        interestedAreaValue = 0;
                    } else {
                        targetAreaValue = 0;
                    }
                }
                updateResidualSurface();
            });
        }
    }

    function updateResidualSurface() {
        const input = document.getElementById("id_residual_surface");
        if(input) {
            console.log(interestedAreaValue, targetAreaValue);
            input.value = interestedAreaValue - targetAreaValue;
            if(input.value >= 0) {
                removeErrorStyle("id_residual_surface");
            } else {
                addErrorStyle("id_residual_surface");
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

    function disableInput(id) {
        const inputContainer = document.getElementById(id);
        if(inputContainer) {
            const inputTags = inputContainer.getElementsByTagName("input");
            const labelTags = inputContainer.getElementsByTagName("label");
            const help_texts = inputContainer.getElementsByClassName("help-block");
            if(inputTags && labelTags) {
                const input = inputTags[0];
                input.value = 0;
                input.disabled = true;
                const label = labelTags[0];
                label.style.cursor = "default";
                if(help_texts) {
                    help_texts[0].style.top = "-5px";
                }
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

    function addSignToTemplate(container, sign, disabled = false) {
        if(container) {
            var element = container[0];
            if(element) {
                var inputSign = document.createElement('div');
                inputSign.style.cssText = 'position: absolute;right: 17px;top: 40%;font-size: 16px;font-weight: 400;transform: translateY(-50%);';
                if(disabled) {
                    inputSign.style.color = "#9e9e9e";
                    inputSign.style.cursor = "default";
                }
                inputSign.innerHTML = sign;
                element.appendChild(inputSign);
            }
        }
    }

    function onlyNumberKey(evt) {
        // Only ASCII character in that range allowed
        var ASCIICode = (evt.which) ? evt.which : evt.keyCode
        if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57))
            return false;
        return true;
    }


    $(function() {
        console.log("litigation form loaded");
        listenForAreaChange("id_surface_directly_concerned");
        listenForAreaChange("id_occupied_area");
        // hide origin from form
        $('#id_origin_container').hide();

        var selectField = $('#id_registration_type'),
            target_value_container = $('#id_target_value_container'),
            initial_estimation_value_container = $('#id_initial_estimation_value_container'),
            residual_surface_container = $("#id_residual_surface_container"),
            enrollment_amount_container = $('#id_enrollment_amount_container'),
            occupied_area_container = $("#id_occupied_area_container"),
            surface_directly_concerned_container = $("#id_surface_directly_concerned_container"),
            esproprio_agricolo = $('.esproprio_agricolo'),
            esproprio_residenziale = $('.esproprio_residenziale'),
            esproprio_fabbricato = $('.esproprio_fabbricato');

        // TODO: add css class for group of fields in form
        // show on form if esproprio_agricolo
        var area_type = $('#id_area_type_container'),
            culture_type = $('#id_culture_type_container'),
            aboveground_quantification = $('#id_aboveground_quantification_container'),
            fruit_pendants = $('#id_fruit_pendants_container'),
            fruit_pendants_label = $('label[for="id_fruit_pendants_0"]'),
            cultivator_type = $('#id_cultivator_type_container'),
            cultivator_type_0 = $('label[for="id_cultivator_type_0"]'),
            batch_disfiguration = $('#id_batch_disfiguration_container'),
            batch_disfiguration_0 = $('label[for="id_batch_disfiguration_0"]'),
            description = $('#id_description_container'),
            enrollment_amount = $('#id_enrollment_amount'),
            IMU_final_declaration = $('#id_IMU_final_declaration'),
            contract_fee = $('#id_contract_fee'),
            residual_rent = $('#id_residual_rent'),
            reclamation_cost = $('#id_reclamation_cost');
            
        // show on form if esproprio_residenziale
        var social_economic_reform = $('#id_social_economic_reform_container'),
            social_economic_reform_label = $('label[for="id_social_economic_reform_0"]'),   
            urban_destination = $('#id_urban_destination_container'),
            transformation_coefficient = $('#id_transformation_coefficient_container'),
            IMU_final_declaration = $('#id_IMU_final_declaration_container');

        // show on form if esproprio_fabbricato
        var epoch_construction = $('#id_epoch_construction_container'),
            building_titles = $('#id_building_titles_container'),
            extension_MQ = $('#id_extension_MQ_container'),
            MC_residui = $('#id_MC_residui_container'),
            partial_demolition = $('#id_partial_demolition_container'),
            total_demolition = $('#id_total_demolition_container'),
            residual_airspace = $('#id_residual_airspace_container'),
            storage_state = $('#id_storage_state_container'),
            lease_agreement = $('#id_lease_agreement_container'),
            productive_activities = $('#id_productive_activities_container'),
            contract_duration = $('#id_contract_duration_container'),
            contract_fee = $('#id_contract_fee_container'),
            residual_rent = $('#id_residual_rent_container'),
            need_transfer_user = $('#id_need_transfer_user_container'),
            reclamation_activities = $('#id_reclamation_activities_container'),
            reclamation_intervention_type = $('#id_reclamation_intervention_type_container'),
            reclamation_cost = $('#id_reclamation_cost_container'),
            id_contract_date = $('#id_contract_date');


        var lease_agreement_label = $('label[for="id_lease_agreement_0"]'),   
            need_transfer_user_label = $('label[for="id_need_transfer_user_0"]'),
            total_demolition_label = $('label[for="id_total_demolition_0"]'),
            residual_airspace_label = $('label[for="id_residual_airspace_0"]'),
            productive_activities_label = $('label[for="id_productive_activities_0"]'),
            reclamation_activities_label = $('label[for="id_reclamation_activities_0"]'),
            storage_state_label = $('label[for="id_storage_state_0"]');

        addSignToTemplate(initial_estimation_value_container, "€");
        addSignToTemplate(contract_fee, "€");
        addSignToTemplate(residual_rent, "€");
        addSignToTemplate(reclamation_cost, "€");
        addSignToTemplate(target_value_container, "€");
        addSignToTemplate(enrollment_amount_container, "€");
        addSignToTemplate(IMU_final_declaration, "€");
        addSignToTemplate(aboveground_quantification, "€");
        addSignToTemplate(transformation_coefficient, "m<sup>3</sup>");
        addSignToTemplate(extension_MQ, "m<sup>2</sup>");
        addSignToTemplate(residual_surface_container, "m<sup>2</sup>", true);
        addSignToTemplate(occupied_area_container, "m<sup>2</sup>");
        addSignToTemplate(surface_directly_concerned_container, "m<sup>2</sup>");
        addSignToTemplate(MC_residui, "m<sup>3</sup>");
        disableInput("id_residual_surface_container");

        formatInputToTakeCommas("id_initial_estimation_value");
        formatInputToTakeCommas("id_target_value");
        formatInputToTakeCommas("id_aboveground_quantification");
        formatInputToTakeCommas("id_enrollment_amount");
        formatInputToTakeCommas("id_IMU_final_declaration");
        formatInputToTakeCommas("id_contract_fee");
        formatInputToTakeCommas("id_residual_rent");
        formatInputToTakeCommas("id_reclamation_cost");


        var h5 = $("h5"),
            h5_esproprio_agricolo = '',
            h5_esproprio_libera = '',
            h5_esproprio_fabbricato = '';
        for (var i = 0; i < h5.length; i++) {
        console.log(h5[i].innerHTML)
            if (h5[i].innerHTML == "Esproprio Agricolo" || h5[i].innerHTML == "Agricultural expropriation") {
                h5_esproprio_agricolo = h5[i];
            }
            if (h5[i].innerHTML == "Esproprio Residenziale/Industriale Libera" || h5[i].innerHTML == "Free Residential / Industrial Expropriation") {
            console.log("TEST", h5[i].innerHTML)
                h5_esproprio_libera = h5[i];
            }
            if (h5[i].innerHTML == "Esproprio Fabbricato Residenziale/ Industriale" || h5[i].innerHTML == "Expropriation of a Residential / Industrial Building") {
                h5_esproprio_fabbricato = h5[i];
            }
        }
        console.log("h5_esproprio_libera", h5_esproprio_libera)

        // onchange registration type
        function toggleVerified(registration_type) {
            console.log(registration_type);

            // Esproprio Agricolo
            if (registration_type === 'Esproprio Agricolo') {
                esproprio_agricolo.show();
                area_type.show();
                culture_type.show();
                aboveground_quantification.show();
                fruit_pendants.show();
                fruit_pendants_label.show();

                cultivator_type.show();
                cultivator_type_0.show();
                batch_disfiguration.show();
                batch_disfiguration_0.show();
                description.show();

                if (h5_esproprio_agricolo) {
                    h5_esproprio_agricolo.style.display = "block";
                }


            } else {
                esproprio_agricolo.hide();
                
                area_type.hide();
                culture_type.hide();
                aboveground_quantification.hide();
                fruit_pendants.hide();
                fruit_pendants_label.hide();
                
                cultivator_type.hide();
                cultivator_type_0.hide();
                batch_disfiguration.hide();
                batch_disfiguration_0.hide();
                description.hide();
                if (h5_esproprio_agricolo) {
                    h5_esproprio_agricolo.style.display = "none";
                }
            }

            // Esproprio Residenziale Libera | Esproprio Industriale Libera
            if (['Esproprio Residenziale Libera', 'Esproprio Industriale Libera'].includes(registration_type)) {
                esproprio_residenziale.show();
                
                social_economic_reform.show();
                social_economic_reform_label.show();
                urban_destination.show();
                transformation_coefficient.show();
                IMU_final_declaration.show();

                if (h5_esproprio_libera) {
                    h5_esproprio_libera.style.display = "block";
                }
            
            } else {
                esproprio_residenziale.hide();

                social_economic_reform.hide();
                social_economic_reform_label.hide();
                urban_destination.hide();
                transformation_coefficient.hide();
                IMU_final_declaration.hide();

                if (h5_esproprio_libera) {
                    h5_esproprio_libera.style.display = "none";
                }
            }

            // Esproprio Fabbricato Residenziale | Esproprio Fabbricato Industriale
            if (['Esproprio Fabbricato Residenziale', 'Esproprio Fabbricato Industriale'].includes(registration_type)) {
                esproprio_fabbricato.show();

                epoch_construction.show();
                building_titles.show();
                extension_MQ.show();
                MC_residui.show();
                partial_demolition.show();
                total_demolition.show();
                residual_airspace.show();
                storage_state.show();
                lease_agreement.show();
                productive_activities.show();
                contract_duration.show();
                contract_fee.show();
                residual_rent.show();
                need_transfer_user.show();
                reclamation_activities.show();
                reclamation_intervention_type.show();
                reclamation_cost.show();
                lease_agreement_label.show();
                need_transfer_user_label.show();
                total_demolition_label.show();
                residual_airspace_label.show();
                productive_activities_label.show();
                reclamation_activities_label.show();
                storage_state_label.show();

                if (h5_esproprio_fabbricato) {
                    h5_esproprio_fabbricato.style.display = "block";
                }

            } else {
                esproprio_fabbricato.hide();

                epoch_construction.hide();
                building_titles.hide();
                extension_MQ.hide();
                MC_residui.hide();
                partial_demolition.hide();
                total_demolition.hide();
                residual_airspace.hide();
                storage_state.hide();
                lease_agreement.hide();
                productive_activities.hide();
                contract_duration.hide();
                contract_fee.hide();
                residual_rent.hide();
                need_transfer_user.hide();
                reclamation_activities.hide();
                reclamation_intervention_type.hide();
                reclamation_cost.hide();
                lease_agreement_label.hide();
                need_transfer_user_label.hide();
                total_demolition_label.hide();
                residual_airspace_label.hide();
                productive_activities_label.hide();
                reclamation_activities_label.hide();
                storage_state_label.hide();

                if (h5_esproprio_fabbricato) {
                    h5_esproprio_fabbricato.style.display = "none";
                }
            }
        }

        // show/hide on load based on pervious value of selectField
        toggleVerified(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleVerified($(this).val());
        });

        formatDate("id_contract_date");
        formatDate("id_date_receipt_act");

    });
})(django.jQuery);
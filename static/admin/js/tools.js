export function formatDate(id) {
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
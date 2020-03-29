function form_show() {
    form = $("#ApplicationForm");
    form.css("opacity", 1);
    $('#form-show').hide();
};

$(document).ready(

    function() {
        $("#id_country").change(function(){
            country_id = $(this).val();
            var url = $("#ApplicationForm").attr("data-states-url");
            var countryId = country_id
            $.ajax({
                    url: url,
                    data: {'country': countryId},
                    success: function (data) {
                            $("#id_state").html(data);
                            }
            });

        });

        $("#id_state").change(function(){
            state_id = $(this).val();
            var url2 = $("#ApplicationForm").attr("data-cities-url");
            var stateId = state_id
            $.ajax({
                url: url2,
                data: {'state': stateId},
                success: function (data) {
                    $("#id_city").html(data);
                    }
            });
        });

});

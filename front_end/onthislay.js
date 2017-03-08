function submitNewDate(){
    var inputDate = $("#dob-year").val() + '-' + $("#dob-month").val() + '-' + $("#dob-day").val()
    $.get("https://api.tuchfarber.com/api/onthislay/" + inputDate, function(data){
        console.log(data.data.detail);
        if(data.data.detail != ''){
            $("#parents").html("While your parent were busy shagging,");
            $("#events").html(data.data.detail)
        }else{
            $("#parents").html("Your parents' coitus was not inspired by any important event.")
        }
    },"json");
}
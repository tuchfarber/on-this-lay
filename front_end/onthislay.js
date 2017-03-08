var euphs = [
    "banging","doing it","bumping uglies","taking a trip to pound town", "knocking boots",
    "doing the no pants dance", "sliming the banana","filling the cream donut", "boning",
    "stuffing the taco","riding the skin bus into tuna town","spearing the bearded clam",
    "boinking","playing hide the canoli","parking the beef bus in tuna town","humping",
    "fornicating","shagging","fucking","putting sour cream in the burrito",
    "putting ranch dressing in the hidden valley"
]
function submitNewDate(){
    var inputDate = $("#dob-year").val() + '-' + $("#dob-month").val() + '-' + $("#dob-day").val()
    $.get("https://api.tuchfarber.com/api/onthislay/" + inputDate, function(data){
        console.log(data.data.detail);
        if(data.data.detail != ''){
            $("#parents").html("While your parent were busy " + euphs[Math.floor(Math.random() * euphs.length)] + ",");
            $("#events").html(data.data.detail)
        }else{
            $("#parents").html("Your parents' coitus was not inspired by any important event.")
        }
    },"json");
}
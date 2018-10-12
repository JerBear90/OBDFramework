function rotate(value) {
  document.getElementById('div1').style.transform="rotate(" + value + "deg)";
  document.getElementById('span1').innerHTML=value + "deg";
}

$( document ).ready(function() {
    var counttx = 0, countup = true;

    function timerr()
    {
      if (countup)
      {
        ++counttx;
        if (counttx >= 50)
          countup = false;
      }
      else
      {
        --counttx;
        if (counttx <= 3)
          countup = true;
      }
      
      document.getElementById('counter').value = counttx;
      rotate(counttx)
    }

    setInterval(timerr, 50);
});


// // alert('w')
//     function rpm() {
//             $.ajax({
//                 url: '/',
//                 type: 'get',
//                 success: function(data) {

//                     console.log('reloaded');

//                     function getValues(){

//                         // RPM VALUE
//                         var rpmValue = $('#rpm').html();
//                         // rpmValue * 10
//                         $("#rpm").load(location.href, "");
//                         $('#rpm').css({'transform' : 'rotate('+ rpmValue +'deg)'});

//                         // SPEED / MPH VALUE
//                         var spdValue = $('#speed').html();

//                         // SPEED / MPH VALUE
//                         var fuel_status = $('#fuel_status').html();

//                         // SPEED / MPH VALUE
//                         var fuel_level = $('#fuel_level').html();

//                         console.log(rpmValue + ' ' + 'the value of #rpm');
//                         console.log(spdValue + ' ' + 'the value of #speed');
//                         console.log(fuel_status + ' ' + 'the value of #fuel_status');
//                         console.log(fuel_level + ' ' + 'the value of #fuel_level');
//                     }
//                     getValues();
//                 },
//                 failure: function(data) {
//                     alert('Got an error dude');
//                 }
//             });
//         }
//     rpm();


//     // Fail safe if the page doesn't trigger ajax
//     $('#reload-page').click(function(){
//         location.reload();
//         alert('clicked');
//     })


let amount = document.getElementById('amount').innerHTML;
    let timerInSeconds = 0
    const refreshTimer = document.getElementById('refresh-timer');

    setInterval(() => {
    timerInSeconds += 1;
    refreshTimer.innerHTML = ` ${timerInSeconds} `;
}, 1000);


    setInterval(() => {
      let x= Math.floor((Math.random() * 100) + (-50))

      document.getElementById('inputtime').value = refreshTimer.innerHTML
    
      amount= amount - x;
      document.getElementById('amount').innerHTML = amount
      document.getElementById('inputamount').value = amount

      if(amount > 100){
        21
        
        document.getElementById('result').innerHTML= 'Gain'
      }
      else{
        document.getElementById('result').innerHTML= 'Loss'
      }

      document.getElementById("submit").click();

   
    }, 60*1000);

<script>
    import { SendIcon } from 'svelte-feather-icons'

    import Animate from "./Animate.svelte";
    import { onMount } from "svelte";

    let message;
    let email;

  const sendEmail=async () => {
    const response = await fetch("http://127.0.0.1:8000/send_email/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ message, email }),
    });

    if (!response.ok) {
      console.error("Error enviando correo");
    } else {
      console.log("Correo enviado correctamente");
    }
  };




  let recaptchaResponse = null;

function onRecaptcha(response) {
  recaptchaResponse = response;
}


</script>

<Animate >
  <section class="hero is-fullheight custom-component  " >
    <div class="columns is-multiline m-4">
      <div class="column"></div>
      <div class="column is-one-third m-6">
        <div class="container">
          <h4 class="title custom-text">Contact Me</h4>
          <p class="custom-text">Lorem ipsum dolor sit amet consectetur adipisicing elit. Doloribus illum fuga, aspernatur beatae consectetur eligendi sapiente aperiam consequuntur cupiditate est quas, eius provident debitis! Ipsam aliquid fugit deserunt sit mollitia!</p>
        </div>
        <form class="mt-6" action="">
        <div class="field">
          <label class="label custom-label">Email</label>
          <div class="control has-icons-left has-icons-right">
            <input class="input custom-input " type="email" bind:value={email} placeholder="Email input">
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>
            <span class="icon is-small is-right">
              <i class="fas fa-exclamation-triangle"></i>
            </span>
          </div>
        </div>
      

        <div class="field">
          <label class="label custom-label">Message</label>
          <div class="control">
            <textarea class="textarea custom-input" bind:value={message}  placeholder="Message"></textarea>
          </div>
        </div>
        
    
     
        
        <div class="field is-grouped is-justify-content-center">
          <div class="control btn-cv  ">
            <button class="button custom-button  is-normal is-rounded " on:click={sendEmail}>
              <span>
              <SendIcon size="24" />
            </span>
              Send</button>
          </div>
<!-- 
          <div class="field">
            <label class="label custom-label">reCAPTCHA</label>
            <div class="control">
              <div class="g-recaptcha" data-sitekey="TU_SITE_KEY" data-callback="onRecaptcha"></div>
              <input type="hidden" name="recaptcha_response" bind:value={recaptchaResponse} />
            </div>
          </div> -->
          
         
         
        </div>
        
      </form>
      <div class="g-recaptcha" data-sitekey="6Ld7NskkAAAAAJKzdpVtsTXKBUdX_TT3dizQHxA8"></div>

      <script src="https://www.google.com/recaptcha/api.js" async defer></script>

      </div>
      
      <div class="column"></div>

    </div>
  </section>
</Animate>







  <style>


  
.label__contact{
  color: #fffffe;

}



.title {
    font-family: "Karla", sans-serif;
    text-align: center;
    color: #fffffe;
  }

  .subtitle{
    text-align: center;
    color: #a7a9be;
  }




  .btn-contact{
    height: auto;
    width: auto;
    margin: 36px;
  }

  


  .custom-component {
        background-color: #fffffe;
    }

  :global(body.dark-mode) .custom-component {
        background-color: #0f0e17;
        color: #fffffe;
    }

    .custom-text {
        color: #1f1235;
}

:global(body.dark-mode) .custom-text {
        color: #f0f0f0;
        text-align: center;
}




.custom-form {
        color: #1f1235;
}

:global(body.dark-mode) .custom-text {
        color: #f0f0f0;
        text-align: center;
}


.custom-button{
  background-color: #ff6e6c;
    border: none;
    color: #fffffe;
    width: 115px;

}



:global(body.dark-mode) .custom-button {

  background-color: #ff8906;
    border: none;
    color: #fffffe;
    width: 115px;
}


.custom-input{
border-color:#1f1235 ;
}

:global(body.dark-mode) .custom-input {


}

.custom-label{
  color: #1f1235;
  

}

:global(body.dark-mode) .custom-label {

color: white;
}

.custom-text{
  text-align: center;
  color: #1f1235;
  font-family: "Inconsolata", monospace;
  line-height: 1.70rem;
}

  </style>
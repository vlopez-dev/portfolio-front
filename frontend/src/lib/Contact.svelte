<script>
    import { SendIcon } from 'svelte-feather-icons'

    import Animate from "./Animate.svelte";
    import { onMount } from "svelte";





    

    let message;
    let email;
    let contacts = [];
    const csrfCookie = getCookie("csrftoken");

  onMount(async () => {
    fetch("http://127.0.0.1:8000/contact/")
      .then((response) => response.json())
      .then((data) => {
        contacts = data;
        console.log(contacts);
        console.log(data);
      })
      .catch((error) => {
        console.log(error);
        return [];
      });
  });

  
  function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  // console.log(cookieValue)
  return cookieValue;

}




  const sendEmail=async () => {

    const csrfCookie = getCookie("csrftoken");

    const recaptchaResponse = grecaptcha.getResponse();

    const response = await fetch("http://127.0.0.1:8000/send_email/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfCookie,
      },
      body: JSON.stringify({ message, email,recaptchaResponse }),
      credentials: 'include',
    });

    if (!response.ok) {
      console.log(response)
      const data = await response.json();
      // console.error("Error enviando correo",data);
      document.getElementById("message").textContent = "Error al enviar e mensaje, intentelo nuevamente";

    } else {
      // console.log(response)

      // const data = await response.json();
      document.getElementById("message").textContent = "Mensaje enviado con exito";

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
    <div class="columns is-multiline mx-2 my-6">
      <div class="column"></div>
      <div class="column is-one-third">
        <div class="container">
          {#each contacts as contact}

          <h4 class="title custom-title">{contact.title}</h4>
          <p class="custom-text">{contact.description}</p>
          {/each}
          <div class="custom-message" id="message"></div>

        </div>
        <form class="mt-6" action="" on:submit|preventDefault={sendEmail}>
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
            <button class="button custom-button  is-normal is-rounded ">
              <span>
              <SendIcon size="24" />
            </span>
              Send</button>
          </div>

        </div>

      </form>
      <div class="column">
      <div class="container">
        <div class="g-recaptcha " data-sitekey="6Ld7NskkAAAAAJKzdpVtsTXKBUdX_TT3dizQHxA8"></div>

      <script src="https://www.google.com/recaptcha/api.js" async defer></script>
    </div>
  </div>
      </div>

      <div class="column"></div>

    </div>
    <script src="https://www.google.com/recaptcha/api.js" async defer></script>

  </section>
</Animate>







  <style>


  


.title {
    font-family: "Karla", sans-serif;
    text-align: center;
    color: #fffffe;
  }

 





   */


  .custom-component {
        background-color: #fffffe;
    }

  :global(body.dark-mode) .custom-component {
        background-color: #0f0e17;
        color: #fffffe;
    }

.custom-title{
  color:#0f0e17;
  text-align: center;
}

:global(body.dark-mode) .custom-title {
        background-color: #0f0e17;
        text-align: center;
        color: #fffffe;
    }





.custom-button{
  background-color: #ff6e6c;
    border: none;
    color: #fffffe;
    width: 105px;
    margin-bottom: 15px;

}



:global(body.dark-mode) .custom-button {

  background-color: #ff8906;
    border: none;
    color: #fffffe;
    width: 105px;
    margin-bottom: 15px;

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

:global(body.dark-mode) .custom-text {
        color: #f0f0f0;
        text-align: justify;
}
.custom-text{
  text-align: justify;
  color: #1f1235;
  font-family: "Inconsolata", monospace;
  line-height: 1.70rem;
}


.custom-message{
  color: green;
  text-align: center;
}


:global(body.dark-mode) .custom-message {
        color: #f0f0f0;
        text-align: center;
}





.g-recaptcha{
  margin: 0 auto;
  width: 304px;
}
  </style>
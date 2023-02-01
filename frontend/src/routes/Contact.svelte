<script>
    import Animate from "./Animate.svelte";


</script>




<Animate>
  <section class="hero is-fullheight  " >
    <div class="columns is-multiline m-4">
      <div class="column"></div>
      <div class="column is-one-third m-6">
        <div class="container">
          <h4 class="title">Contact Me</h4>
        </div>
        <form class="mt-6" action="">
        <div class="field">
          <label class="label label__contact">Email</label>
          <div class="control has-icons-left has-icons-right">
            <input class="input" type="email" placeholder="Email input" value="hello@">
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>
            <span class="icon is-small is-right">
              <i class="fas fa-exclamation-triangle"></i>
            </span>
          </div>
        </div>
        <div class="field">
          <label class="label label__contact">Message</label>
          <div class="control">
            <textarea class="textarea" placeholder="Textarea"></textarea>
          </div>
        </div>
        
    
     
        
        <div class="field is-grouped">
          <div class="control">
            <button class="button btn-contact">Send</button>
          </div>
         
        </div>
      </form>
      </div>
      
      <div class="column"></div>

    </div>
  </section>
</Animate>







  <style>
   
   section{
    background-color: #0f0e17;
   }

   .title{
    font-family: 'Karla', sans-serif;

   }
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

  .btn-contact button{
    background-color: #ff8906;
    border: none;
    color: #fffffe;
    width: 90px;
    box-shadow: -8px 0px 20px rgba(255, 146, 26, 0.3), 0px 0px 20px rgba(255, 146, 26, 0.3), 8px 0px 20px rgb(255 146 26 / 30%);

  }




  </style>